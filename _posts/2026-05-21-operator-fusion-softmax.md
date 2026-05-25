---
layout: single
title: "融合算子的学习路线：为什么 fused softmax 不是“把函数写一起”"
date: 2026-05-21
categories:
  - tech-blog
  - kernel-notes
series: "CUDA / Triton / Kernel Notes"
priority: P2
tags:
  - Operator Fusion
  - Softmax
  - Triton
  - Memory Bandwidth
excerpt: "融合算子的核心是减少中间结果写回 global memory，而不是简单把几个函数排在一起。"
source_log:
  - "Renyuan_Log.md:3427-3497"
  - "Renyuan_Log.md:3501-3508"
  - "Renyuan_Log.md:3512-3537"
---

公开整理时，这组笔记只保留 fused softmax、算子融合、规约和内存读写主题，不保留会议链接、会议密码、课程参与者姓名或内部安排。

## 融合的核心

把 `softmax` 和 element-wise 操作写在一个函数里，不自动等于高性能 fused kernel。融合的关键是减少中间结果写回 global memory。

例如：

```text
x -> softmax(x) -> relu(softmax(x))
```

如果中间的 `softmax(x)` 被完整写回 global memory，再读回来做 relu，那融合价值就很有限。真正的 fused kernel 会尽量在寄存器或 shared memory 中完成中间计算。

## Softmax 为什么特殊

softmax 不是纯 element-wise，它需要规约：

1. 求最大值。
2. 减最大值后求 exp。
3. 求和。
4. 除以和。

这意味着 block 划分和 reduction 策略会直接影响实现。

## 学习路线

可以按三个层次学：

1. 单纯 element-wise fusion，例如 `relu`、`silu`、`x * sigmoid(x)`。
2. softmax + element-wise，例如 `relu(softmax(x))`。
3. 带 block 划分和跨 block 规约的 softmax 变体。

这条路线的核心问题始终是：哪些中间值必须写回 global memory，哪些可以留在更近的存储层。

## 知识补全：为什么 softmax 难融合

element-wise 操作天然好融合，因为每个输出只依赖对应输入元素。softmax 不一样，它的每个输出都依赖整行数据的最大值和总和。

这意味着 softmax 至少需要两类规约：max reduction 和 sum reduction。融合其他操作时，必须保证这些规约结果仍然正确。

例如 `softmax + dropout` 不能只把两段代码粘在一起，还要考虑随机 mask、缩放系数、是否需要保存 mask 给反向传播，以及中间概率是否必须写回。

## 实践检查清单

判断一个 fused kernel 是否真的有价值，可以问：

1. 少写回了哪些中间张量。
2. 多做了哪些计算或分支。
3. block 内是否能覆盖整行。
4. 如果一行太长，跨 block reduction 怎么做。
5. 反向传播是否需要保存中间值。
6. 数值稳定性是否仍然使用减最大值。

融合不是目的，减少内存流量并保持正确性才是目的。
