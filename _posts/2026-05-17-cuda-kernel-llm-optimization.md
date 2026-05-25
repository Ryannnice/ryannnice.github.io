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
