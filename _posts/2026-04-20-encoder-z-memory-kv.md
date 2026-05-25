---
layout: single
title: "Encoder 输出 Z 矩阵到底去了哪里：从 Memory 到 K/V"
date: 2026-04-20
categories:
  - tech-blog
  - transformer-foundations
series: "Transformer Foundations"
priority: P3
tags:
  - Attention
  - Encoder
  - KV Cache
excerpt: "Encoder 的最终输出不是消失了，而是作为 memory 被 Decoder cross-attention 投影成 Key 和 Value。"
source_log:
  - "Renyuan_Log.md:2258-2266"
---

Encoder 的每一层都会把输入表示更新成新的上下文表示。最后一层输出的 `Z` 矩阵可以理解为整段输入的 memory。

## 内部与外部视角

从 Encoder 内部看，`Z` 是层层加工后的中间产物。每一层 self-attention 和 FFN 都在修改它。

从 Decoder 外部看，Encoder 最终输出不再是中间变量，而是可查询的记忆库。

## K 和 V

在 cross-attention 中，Decoder 会从 Encoder 输出中生成 Key 和 Value：

- Key 像索引标签，用来匹配当前 Decoder query。
- Value 像内容载荷，被注意力权重加权读取。

因此，Encoder 输出 `Z` 的归宿就是成为 K/V 的母体。

这个理解可以帮助区分两个概念：训练和推理里常说的 KV cache 是一种运行时缓存，而 Encoder 输出作为 memory 则是注意力机制中的信息来源。

## 知识补全：self-attention 和 cross-attention 的 K/V 来源不同

在 self-attention 中，Q、K、V 都来自同一个序列。Encoder self-attention 里，它们来自源序列；Decoder self-attention 里，它们来自已经生成的目标序列。

在 cross-attention 中，Q 来自 Decoder 当前状态，K/V 来自 Encoder 输出 memory。也就是说，Decoder 用自己的 query 去检索源句子的 memory。

这个区别解释了为什么 Encoder-Decoder 模型里会有两套注意力：一套看自己已经生成了什么，一套看输入原文提供了什么。

## 和 KV cache 的关系

推理中的 KV cache 是为了避免重复计算历史 token 的 K/V。Decoder-only 模型缓存的是自回归历史。Encoder-Decoder 模型中，Encoder 的 K/V 对整段输入固定，可以预先计算并在每一步 decode 中复用。

因此：

```text
Encoder memory: 语义来源
KV cache:       运行时加速结构
```

两者相关，但不是同一个概念。

## 学习检查清单

遇到 K/V 概念时，可以问：

1. K/V 来自 Encoder 还是 Decoder。
2. 它服务 self-attention 还是 cross-attention。
3. 它是模型结构中的 memory，还是推理系统中的 cache。
4. 它是否随每个 decode step 增长。
5. 它是否可以预先计算。

这样能避免把所有 K/V 都混成同一种缓存。
