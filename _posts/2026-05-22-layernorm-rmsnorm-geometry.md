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

## 知识补全：为什么 RMSNorm 常见于大模型

大模型中 RMSNorm 常见，不只是因为它计算少一点，还因为它保留了均值方向的信息。LayerNorm 会去掉每个 token 表示的均值分量，RMSNorm 则只按均方根缩放。

从实现上看，RMSNorm 通常只需要：

```text
rms = sqrt(mean(x^2) + eps)
y = x / rms * weight
```

LayerNorm 需要：

```text
mean = mean(x)
var = mean((x - mean)^2)
y = (x - mean) / sqrt(var + eps) * weight + bias
```

多出来的均值和方差会增加 reduction 和中间计算。

## 学习检查清单

比较两个归一化层时，可以看：

1. 它去掉了哪些信息。
2. 它需要几个 reduction。
3. 是否有 bias。
4. 是否适合 fused residual add。
5. 推理时瓶颈是计算还是访存。
6. Triton kernel 里需要维护几个 accumulator。

这样看归一化，就能从数学定义走到实际 kernel 成本。
