---
layout: single
title: "从写循环到写映射：CUDA kernel 如何接上 LLM 优化"
date: 2026-05-17
categories:
  - tech-blog
  - kernel-notes
series: "CUDA / Triton / Kernel Notes"
priority: P0
featured: true
tags:
  - CUDA
  - Kernel
  - Shared Memory
  - Reduction
excerpt: "用学习者视角把 CUDA 从线程映射讲到 shared memory、reduction 和 LLM kernel 优化入口。"
source_log:
  - "Renyuan_Log.md:2310-2389"
  - "Renyuan_Log.md:2411-2470"
  - "Renyuan_Log.md:3312-3384"
  - "Renyuan_Log.md:3386-3497"
---

学习 CUDA 的第一个转变是：不要再把程序想成 CPU 上的一个循环，而要想成很多线程同时处理不同索引。

CPU 代码常写：

```cpp
for (int i = 0; i < N; i++) {
  out[i] = f(input[i]);
}
```

CUDA kernel 则让每个线程负责一个或多个 `i`。

## 执行层级

CUDA 的层级是：

```text
Grid -> Block -> Warp -> Thread
```

一个 warp 固定 32 个线程，一个 block 最多通常是 1024 个线程。理解这个层级后，很多 reduction 和 shared memory 设计就变得自然。

## Shared Memory

Shared memory 是 block 内共享、block 间隔离的高速存储。声明：

```cpp
extern __shared__ float sdata[];
```

表示每个 block 都有自己的一份 `sdata`。线程先把 global memory 中的数据搬到 shared memory，再在 block 内协作计算。

这能减少 global memory 访问，但也要求清楚 `threadIdx`、`blockIdx`、全局索引和局部索引的关系。

## Kernel 和 Device Function

`__global__` 函数是 kernel，可以由 CPU 用 `<<<blocks, threads>>>` 启动。

`__device__` 函数只能在 GPU 代码里被调用，是 kernel 内部的辅助函数。

这一区分很关键。`warpReduceMax`、`blockReduceMax` 这类函数不是执行入口，而是 kernel 内部的规约组件。

## Reduction 直觉

高效 reduction 通常按层次做：

```text
thread-local value -> warp reduction -> block reduction -> global reduction
```

warp 内可以用 shuffle 直接交换寄存器数据。warp 间则把 partial result 写入 shared memory，再由第一个 warp 汇总。

优化优先级可以记成：

```text
register > shuffle > shared memory > global memory
```

这也是 CUDA 如何接上 LLM 优化的入口：许多 kernel 优化本质上都在减少 global memory 读写，并尽可能在寄存器、warp 和 shared memory 层完成计算。

## 知识补全：带宽瓶颈和算力瓶颈

写 CUDA kernel 时，首先要判断瓶颈在哪里。

如果一个 kernel 做的计算很少，但需要读写大量数据，它通常是 memory-bound。优化方向是减少 global memory 访问、合并访问、复用 shared memory、融合算子。

如果一个 kernel 做大量矩阵乘法或复杂计算，可能是 compute-bound。优化方向是提升 tensor core 利用率、选择合适 tile、减少控制分支。

LLM 推理中两类都存在。GEMM 更偏算力，LayerNorm、RMSNorm、softmax、sampling 等更容易受带宽和规约影响。

## 学习检查清单

写一个 kernel 前，可以先问：

1. 每个线程负责哪些元素。
2. global memory 读写次数是多少。
3. 是否有重复读取可以放进 shared memory。
4. warp 内是否能用 shuffle 代替 shared memory。
5. block 大小是否匹配数据规模。
6. 最终瓶颈更可能是带宽还是算力。

这组问题能把 CUDA 从语法学习推进到性能推理。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-26](#source-log-2026-04-26) | 2310-2393 | CUDA 执行模型与 LLM 优化入口 |
| [2026-04-28](#source-log-2026-04-28) | 2411-2474 | CUDA 内存分配与拷贝 |
| [2026-05-17](#source-log-2026-05-17) | 3386-3500 | CUDA kernel、device function 与 reduction |

<a id="source-log-2026-04-26"></a>
### Source Log: 2026-04-26

Source lines: `Renyuan_Log.md:2310-2393`

<pre class="tech-log-source"><code>
2310 |# 2026-04-26
2311 |
2312 |## CUDA
2313 |
2314 |今天主要先把 CUDA 的整体脉络理顺了，重点不是背文档，而是搞清楚它和 LLM 优化到底怎么接上。
2315 |
2316 |### 先建立整体图景
2317 |
2318 |- CUDA 是让 CPU 发起、GPU 执行并行任务的编程模型；主机代码负责分配内存、发射 kernel、同步结果。
2319 |- GPU 追求吞吐量，适合海量并行；CPU 追求低延迟和复杂控制。
2320 |- CUDA 程序常见分层：高层框架 / 库（PyTorch、cuBLAS、cuDNN、Triton） -&gt; CUDA Runtime / Driver -&gt; PTX / cubin -&gt; GPU 硬件。
2321 |
2322 |### 我真正需要记住的执行模型
2323 |
2324 |- kernel 是站在“单个线程”的视角写的：先算出自己的全局索引，再决定自己处理哪一段数据。
2325 |- 启动方式是 `&lt;&lt;&lt;grid, block&gt;&gt;&gt;`；`blockIdx`、`blockDim`、`threadIdx` 不是函数参数，而是 CUDA 提供的内置上下文。
2326 |- `.x / .y / .z` 只是数据维度的映射方式：向量通常只用 `.x`，图像或矩阵才会自然用到 `.x + .y`。
2327 |- `grid` 负责覆盖总任务量，`block` 负责组织线程协作；简单向量加法只用 thread 视角，矩阵乘法 / attention 这类问题必须引入 block 视角。
2328 |- warp 是 32 个线程的执行单位，因此 block 大小通常尽量设成 32 的倍数，避免浪费 lane。
2329 |- 不同 block 之间默认不能相互依赖；块内协作靠 shared memory 和 `__syncthreads()`。
2330 |
2331 |### 内存与性能直觉
2332 |
2333 |- 全局内存大但慢，寄存器和 shared memory 小但快。
2334 |- 线程多不等于快，常见瓶颈反而在内存访问。
2335 |- 一个 kernel 的性能，往往取决于：
2336 |  - 是否减少了全局内存读写
2337 |  - 是否避免了 warp divergence
2338 |  - 是否让访问尽量 coalesced
2339 |  - 寄存器 / shared memory 占用是否把 occupancy 压得太低
2340 |
2341 |### 从代码层面想明白的几个点
2342 |
2343 |- `(N + threads - 1) / threads` 是为了向上取整，保证任务不漏；多开的线程再用 `if (i &lt; N)` 挡住。
2344 |- `cudaDeviceSynchronize()` 是显式同步点。调试时很好用，也能暴露前面 kernel 的错误；但在性能敏感场景里不能滥用。
2345 |- `extern &quot;C&quot;` 是为了关闭 C++ 名字修饰，方便被其他语言或动态加载逻辑找到。
2346 |- `__global__` 表示“CPU 发起、GPU 执行”的 kernel 入口，必须 `void` 返回。
2347 |
2348 |## CUDA 编程
2349 |
2350 |今天这部分最大的转变，是把“写循环”改成“做映射”。
2351 |
2352 |```cpp
2353 |__global__ void vector_add(const float* A, const float* B, float* C, int N) {
2354 |    int i = blockIdx.x * blockDim.x + threadIdx.x;
2355 |    if (i &lt; N) {
2356 |        C[i] = A[i] + B[i];
2357 |    }
2358 |}
2359 |```
2360 |
2361 |我现在的理解：
2362 |
2363 |- CPU 时代的思路是“for 循环遍历数组”。
2364 |- CUDA 的思路是“每个线程只负责自己的那个索引”。
2365 |- 所以 kernel 本质上是在写 SPMD：同一段程序，被很多线程拿去处理不同数据。
2366 |
2367 |### 和 LLM 优化怎么接上
2368 |
2369 |- Python / PyTorch 负责模型结构、调度和实验；CUDA kernel 负责真正重的并行算子。
2370 |- 真正值得自己写 kernel 的地方，通常不是标准 GEMM，而是：
2371 |  - Attention / KV Cache 这类特殊访问模式
2372 |  - 量化解码
2373 |  - 多个小算子的融合
2374 |- 如果只是标准矩阵乘法，优先用 `cuBLAS`；如果要在 GEMM 周围融合逻辑，再考虑 `CUTLASS`；如果想先快速试验，自定义 kernel 之前可以先看 `Triton`。
2375 |
2376 |### 目前的工程判断
2377 |
2378 |- 写 CUDA 的核心不是“会不会语法”，而是能不能判断瓶颈在算力还是带宽。
2379 |- 定位瓶颈不能靠猜，至少要会用：
2380 |  - `Nsight Systems` 看整体时间线
2381 |  - `Nsight Compute` 看单 kernel 的 roofline、memory throughput、occupancy
2382 |  - `torch.profiler` 把 Python 层和 CUDA kernel 对上
2383 |
2384 |### 这次学习后我给自己的路线
2385 |
2386 |1. 先把 thread / block / warp / memory hierarchy 彻底吃透。
2387 |2. 用最小例子把 kernel launch、同步、索引映射跑顺。
2388 |3. 再进入 LLM 相关的 Triton / PyTorch Extension / CUTLASS。
2389 |4. 真做优化时，先判断是 memory bound 还是 compute bound，再决定要不要手写 kernel。
2390 |
2391 |
2392 |
2393 |
</code></pre>


<a id="source-log-2026-04-28"></a>
### Source Log: 2026-04-28

Source lines: `Renyuan_Log.md:2411-2474`

<pre class="tech-log-source"><code>
2411 |# 2026-04-28
2412 |
2413 |## CUDA 编程
2414 |
2415 |### 内存分配
2416 |
2417 |#### 今日要点
2418 |
2419 |- `cudaMemcpyDefault` 的核心是让 CUDA 驱动自动判断搬运方向。
2420 |- `cudaMallocManaged` 的核心不是复制两份数据，而是统一地址空间下的按需页迁移。
2421 |- `cudaMemcpy` 更像“复制 + 粘贴”，`cudaMallocManaged` 更像“同一份逻辑数据在 CPU / GPU 之间迁移”。
2422 |
2423 |#### `cudaMemcpy` 第一个参数永远是目标地址（Destination）
2424 |
2425 |示例：
2426 |
2427 |```cpp
2428 |cudaMemcpy(devA, A, vectorLength * sizeof(float), cudaMemcpyDefault);
2429 |```
2430 |
2431 |理解：
2432 |
2433 |- `cudaMemcpyDefault` 就是让 CUDA 驱动开启“自动驾驶”模式。
2434 |- CUDA 驱动会通过 PCIe 总线自动把数据从内存搬到显存。
2435 |
2436 |常见搬运方向：
2437 |
2438 || 源地址（Source） | 目的地址（Destination） | 驱动实际执行的操作 |
2439 || --- | --- | --- |
2440 || CPU（`A`） | GPU（`devA`） | `HtoD`（上传到显卡） |
2441 || GPU（`devA`） | CPU（`A`） | `DtoH`（下载到内存） |
2442 || GPU1（`devA`） | GPU2（`devB`） | `Peer-to-Peer`（显卡间直接对传） |
2443 || GPU1（`devA`） | GPU1（`devB`） | `Device Copy`（显存内部搬运） |
2444 |
2445 |#### `cudaMallocManaged`：原来位于 CPU 的数据还在吗？
2446 |
2447 |这是一个非常深刻的问题，涉及到操作系统的虚拟内存管理和 CUDA 驱动的数据一致性策略。
2448 |
2449 |简单来说：
2450 |
2451 |- 数据依然“存在”，但在物理上它可能已经从 CPU 内存中“搬”走了。
2452 |
2453 |为了理解这一点，需要把“数据”拆分为逻辑地址和物理位置来看：
2454 |
2455 |1. 逻辑上：它一直都在&#32;&#32;
2456 |   对于你的程序代码来说，变量 `A` 指向的地址（比如 `0x7f8000`）始终有效。无论数据当前是在显存里还是在主存里，都可以通过这个指针访问它。
2457 |
2458 |2. 物理上：它是“按需移动”的&#32;&#32;
2459 |   统一内存（Unified Memory）的核心机制是页迁移（Page Migration）。它的行为非常像操作系统里的“交换文件（Swap）”：
2460 |   - GPU 访问时：如果数据在 CPU 内存中，驱动会产生一个“页错误”（Pa
2461 |  ge Fault）。此时，驱动会将这一页数据（通常是 `4KB` 或 `2MB`）通过 PCIe 总线拷贝到显存，并更新 GPU 的页表。
2462 |   - 原来在 CPU 的副本：在大多数现代系统（如 Pascal 架构及之后的 GPU）上，为了保证数据一致性，CPU 端的这一页内存会被标记为“无效”或直接被物理释放。
2463 |
2464 |#### `cudaMemcpy` 和 `cudaMallocManaged` 的本质区别
2465 |
2466 |使用 `cudaMemcpy` 时，数据是“复制 + 粘贴”：
2467 |
2468 |- 物理存在：拷贝完成后，CPU 内存（地址 `A`）和 GPU 显存（地址 `devA`）中各有一份完整的数据副本。
2469 |- 独立性：如果随后在 CPU 上修改了 `A[0]`，GPU 上的 `devA[0]` 不会跟着变。它们是两个完全独立的物理实体。
2470 |- LLM 场景应用：在加载大模型权重时，通常把权重从主存（RAM）拷贝到显存。
2471 |
2472 |
2473 |
2474 |
</code></pre>


<a id="source-log-2026-05-17"></a>
### Source Log: 2026-05-17

Source lines: `Renyuan_Log.md:3386-3500`

<pre class="tech-log-source"><code>
3386 |# 2026-05-17
3387 |
3388 |## CUDA kernel 与 device function
3389 |
3390 |### 问题
3391 |
3392 |为什么到了 `reduce_max_kernel` 才说 “kernel 1”？前面的几个函数不是 kernel 吗？
3393 |
3394 |前面的函数包括：
3395 |
3396 |- `warpReduceMax`
3397 |- `warpReduceSum`
3398 |- `blockReduceMax`
3399 |- `blockReduceSum`
3400 |
3401 |### 结论
3402 |
3403 |这些函数都不是 CUDA kernel，而是 device function（设备函数）。
3404 |
3405 |在 CUDA 中，**kernel = GPU 并行执行入口**，也就是能被 CPU 端用 `&lt;&lt;&lt;blocks, threads&gt;&gt;&gt;` 启动的函数。
3406 |
3407 |### CUDA 中三类关键函数
3408 |
3409 || 类型 | 示例 | 运行位置 | 是否 kernel | 是否能用 `&lt;&lt;&lt;&gt;&gt;&gt;` 启动 |
3410 || --- | --- | --- | --- | --- |
3411 || `__global__` | `__global__ void reduce_max_kernel(...)` | GPU | 是 | 是 |
3412 || `__device__` | `__device__ float warpReduceMax(float val)` | GPU | 否 | 否 |
3413 || 普通 CPU 函数 | `extern &quot;C&quot; void solve(...)` | CPU | 否 | 否 |
3414 |
3415 |`__global__` 函数是真正的 GPU 启动入口，例如：
3416 |
3417 |```cpp
3418 |__global__ void reduce_max_kernel(...) {
3419 |  // GPU kernel body
3420 |}
3421 |
3422 |reduce_max_kernel&lt;&lt;&lt;blocks, threads&gt;&gt;&gt;(...);
3423 |```
3424 |
3425 |`__device__` 函数只能被 GPU 代码调用，它是 GPU 内部的辅助函数，不是执行入口。
3426 |
3427 |## Reduction 规约操作
3428 |
3429 |### 执行层级
3430 |
3431 |CUDA 的执行层级是：
3432 |
3433 |```text
3434 |Grid -&gt; Block -&gt; Warp -&gt; Thread
3435 |```
3436 |
3437 |关键限制：
3438 |
3439 |- 一个 warp 固定 32 个线程。
3440 |- 一个 block 最多 1024 个线程。
3441 |- 因此一个 block 最多只有 32 个 warp。
3442 |
3443 |### Warp-level reduction
3444 |
3445 |Warp 内通信主要使用 `__shfl_down_sync`。它允许线程直接读取其他 lane 的寄存器数据，比 shared memory 更快。
3446 |
3447 |Warp reduction 的本质是：**信息向低 lane 聚合**。最终只有 `lane 0` 一定保存整个 warp 的规约结果。
3448 |
3449 |### Block-level reduction
3450 |
3451 |Block reduction 通常采用两级结构：
3452 |
3453 |1. 每个 warp 内部先做 reduction。
3454 |2. 每个 warp 把自己的结果写入 `shared[32]`。
3455 |3. 第一个 warp 继续对这些 partial results 做 reduction。
3456 |
3457 |`shared[32]` 足够的原因是：一个 block 最多只有 32 个 warp，而第一个 warp 正好有 32 个 lane，可以覆盖全部 warp partial results。
3458 |
3459 |## Grid-Stride Loop
3460 |
3461 |Grid-Stride Loop 是 CUDA 中处理超大数据的经典模式：
3462 |
3463 |```cpp
3464 |for (int i = idx; i &lt; N; i += stride) {
3465 |  // process input[i]
3466 |}
3467 |```
3468 |
3469 |其中：
3470 |
3471 |- `idx` 是当前线程的全局编号。
3472 |- `stride = blockDim.x * gridDim.x`，表示整个 grid 的线程总数。
3473 |- 一个线程会循环处理多个元素。
3474 |
3475 |### `local_max` 的含义
3476 |
3477 |`local_max` 不是全局最大值，而是当前线程负责的数据分片中的局部最大值（thread-local max）。
3478 |
3479 |完整规约路径是：
3480 |
3481 |```text
3482 |thread-local max -&gt; warpReduceMax -&gt; blockReduceMax -&gt; global reduction -&gt; final max
3483 |```
3484 |
3485 |### CUDA reduction 优化直觉
3486 |
3487 |优先级通常是：
3488 |
3489 |```text
3490 |register &gt; shuffle &gt; shared memory &gt; global memory
3491 |```
3492 |
3493 |因此优化方向是：
3494 |
3495 |- warp 内尽量使用 shuffle。
3496 |- warp 间使用 shared memory。
3497 |- 尽可能减少 global memory 访问。
3498 |
3499 |
3500 |
</code></pre>

<!-- source-log-coverage:end -->
