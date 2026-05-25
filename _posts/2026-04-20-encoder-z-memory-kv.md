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
