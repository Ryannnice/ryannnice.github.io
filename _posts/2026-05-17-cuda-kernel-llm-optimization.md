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
