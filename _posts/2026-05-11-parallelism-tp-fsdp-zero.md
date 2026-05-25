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

## 知识补全：训练并行和推理并行的目标不同

训练时显存压力来自参数、梯度、优化器状态和激活。FSDP / ZeRO-3 的核心价值是把这些状态分散到多张卡上，必要时再临时 gather。

推理时没有梯度和优化器状态，压力主要来自模型权重、KV cache 和单步 decode 延迟。Tensor Parallel 更常见，因为它能把单层权重和计算拆开，让单个大模型放进多张卡并并行执行。

这也是为什么同一个“并行”名词在训练和推理里含义不同。训练关心能不能省显存并保持反向传播正确；推理关心能不能降低单 token 延迟和提升吞吐。

## 通信直觉

通信不是免费的。每次 AllReduce、AllGather 都会带来同步等待。并行设计的关键是让计算节省大于通信成本。

判断一个并行方案时，可以问：

1. 切分的是参数、激活、梯度，还是计算维度。
2. 每一层需要几次通信。
3. 通信发生在前向、反向，还是 decode 每一步。
4. 是否会增加尾延迟。
5. 当前瓶颈是显存、算力还是网络带宽。

这些问题比记住 TP、DP、PP、FSDP 的缩写更重要。
