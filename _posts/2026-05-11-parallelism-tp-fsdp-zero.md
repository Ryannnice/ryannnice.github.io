---
layout: single
title: "大模型并行的最小闭环：集合通信、TP、FSDP/ZeRO-3 到权重分片"
date: 2026-05-11
categories:
  - tech-blog
  - serving-deployment
series: "Serving & Deployment"
priority: P1
tags:
  - Tensor Parallel
  - FSDP
  - ZeRO-3
  - AllReduce
  - Megatron
excerpt: "从通信原语推到线性层切分，再区分训练省显存和推理拆单层计算的不同目标。"
source_log:
  - "Renyuan_Log.md:2595-2604"
  - "Renyuan_Log.md:2647-2814"
  - "Renyuan_Log.md:2831-3011"
---

大模型并行可以先从集合通信理解。无论是训练还是推理，多个设备之间都要交换张量，只是交换的时机和目的不同。

## 通信原语

常见原语包括：

- Gather：收集。
- Reduce：归约。
- AllReduce：所有设备都得到归约结果。
- Broadcast：广播。
- Scatter：切分发送。

这些原语是 TP、DP、FSDP、ZeRO 的共同底层语言。

## Tensor Parallel

Tensor Parallel 关注把单层计算拆到多张卡上。以线性层为例：

- ColumnParallelLinear 按输出维度切权重。
- RowParallelLinear 按输入维度切权重。

前者通常需要后续拼接或保持分片，后者通常需要对 partial output 做 AllReduce。

TP 的目标不是保存 optimizer state，而是让单层矩阵乘法跨设备执行。

## FSDP / ZeRO-3

FSDP 和 ZeRO-3 更偏训练省显存。它们把参数、梯度、优化器状态分片。计算某一层时再 gather 需要的参数，算完后释放或重新分片。

因此它们和 TP 的核心区别是：TP 拆的是计算，FSDP/ZeRO-3 拆的是训练状态。

## 权重分片直觉

代码里常见 `narrow` 和 `offset`，本质是在完整权重中取出当前 rank 负责的切片。理解这些切片，比死记并行名词更重要。

大模型并行的最小闭环是：知道张量怎么切、什么时候通信、通信后每张卡手里有什么。
