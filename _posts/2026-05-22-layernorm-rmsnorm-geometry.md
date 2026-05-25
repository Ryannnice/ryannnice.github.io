---
layout: single
title: "LayerNorm vs RMSNorm：从几何自由度到 Triton kernel 成本"
date: 2026-05-22
categories:
  - tech-blog
  - kernel-notes
series: "CUDA / Triton / Kernel Notes"
priority: P0
featured: true
tags:
  - LayerNorm
  - RMSNorm
  - Triton
  - Geometry
excerpt: "RMSNorm 只去掉长度，LayerNorm 同时去掉长度和平移基准；这个几何差异会落到 kernel 成本上。"
source_log:
  - "Renyuan_Log.md:3514-3537"
  - "Renyuan_Log.md:3539-3596"
---

RMSNorm 和 LayerNorm 都是在做归一化，但它们保留和丢弃的信息不同。几何上看，这个差异非常直观。

## RMSNorm

RMSNorm 的约束可以理解为把向量缩放到一个固定半径的超球面上。

在三维例子里，它要求：

```text
x^2 + y^2 + z^2 = 3
```

它去掉的是向量长度，但保留方向和平移基准。

## LayerNorm

LayerNorm 不仅缩放长度，还会去均值。三维里可以写成：

```text
x^2 + y^2 + z^2 = 3
x + y + z = 0
```

也就是说，它要求数据同时落在球面上和过球心的平面上。两者交集是一条圆。推广到 `M` 维，RMSNorm 的自由度是 `M-1`，LayerNorm 的自由度是 `M-2`。

## Kernel 成本

这个几何差异会落到实现成本上。

RMSNorm 只需要维护平方和累加器。LayerNorm 需要维护均值和方差，通常需要更多 reduction 和中间值。

从 Triton kernel 的角度，RMSNorm 更轻，不是因为概念更简单，而是因为它少去掉一个统计量。

## 结论

RMSNorm 是“只缩放长度”。LayerNorm 是“去均值 + 缩放长度”。在大模型推理里，这种少一个统计量的差异会变成真实的 kernel 成本差异。
