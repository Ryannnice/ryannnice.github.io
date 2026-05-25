---
layout: single
title: "从 CS336 作业理解 Transformer 训练基本功"
date: 2026-04-13
categories:
  - tech-blog
  - transformer-foundations
series: "Transformer Foundations"
priority: P2
tags:
  - CS336
  - Transformer
  - BF16
  - einsum
excerpt: "把 activation checkpointing、Linear/einsum、权重矩阵布局和 BF16 串成训练系统基础。"
source_log:
  - "Renyuan_Log.md:1850-1869"
  - "Renyuan_Log.md:1875-1898"
  - "Renyuan_Log.md:1967-2001"
---

训练系统的基础不是某个单独概念，而是一组张量形状、内存和数值表示之间的约定。

## Activation checkpointing

Checkpointing 常被概括为“时间换空间”。前向时不保存所有中间激活，反向时重新计算一部分，从而减少显存占用。

它不是保存参数矩阵的 checkpoint，而是保存计算图中必要的边界状态。

## Linear 与 einsum

线性层可以写成：

```text
... d_in, d_out d_in -> ... d_out
```

这说明输入最后一维是 `d_in`，权重提供 `d_out` 个输出方向，结果最后一维变成 `d_out`。

理解这个 einsum，比记住某个框架 API 更可靠。

## 权重布局

PyTorch 的 Linear 权重常按 `(out_features, in_features)` 存。这会让初学者觉得和数学里的 `xW` 方向相反。

实际实现会根据内存布局和 GEMM 调用做选择。重要的是知道每一维代表输入还是输出，而不是死记矩阵在纸面上的方向。

## BF16

BF16 适合 LLM 的关键原因是指数位和 FP32 一样多，动态范围大，但尾数更短。它牺牲精度，保留范围，因此比 FP16 更不容易溢出。

训练基础最终都要回到三个问题：张量形状是什么、内存保存什么、数值格式能不能承受当前计算。

## 知识补全：形状推理是训练系统的地基

Transformer 训练里的很多 bug 都不是公式错，而是形状理解错。batch、sequence、head、hidden、vocab、expert 这些维度在不同模块中不断重排。

例如 attention 常见形状是：

```text
(batch, seq, hidden)
-> (batch, heads, seq, head_dim)
```

MLP 则常在 hidden 和 intermediate hidden 之间变换。MoE 又会多出 expert 维度和 token dispatch。

掌握形状推理后，einsum、reshape、transpose、contiguous、shard 都会更容易理解。

## 数值格式的直觉

FP16 尾数更多但指数范围小，容易溢出。BF16 尾数更少但范围大，因此在大模型中更稳。FP32 通常用于累加、优化器状态或敏感计算。

混合精度训练的核心不是“全都用低精度”，而是把不同计算放在合适精度上。

## 学习检查清单

读训练代码时，可以逐步标注：

1. 每个张量的 shape。
2. 每次 matmul 的输入输出维度。
3. 哪些激活会被保存到反向。
4. 哪些地方用了 checkpointing。
5. 参数、梯度、优化器状态分别是什么 dtype。
6. 是否存在隐式转置或 contiguous 拷贝。

这比单独背 Transformer 结构更接近工程实践。
