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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-05-22](#source-log-2026-05-22) | 3539-3596 | LayerNorm 与 RMSNorm 几何理解 |

<a id="source-log-2026-05-22"></a>
### Source Log: 2026-05-22

Source lines: `Renyuan_Log.md:3539-3596`

<pre class="tech-log-source"><code>
3539 |# 2026-05-22
3540 |
3541 |## LayerNorm 和 RMSNorm 的几何理解
3542 |
3543 |### 今日结论
3544 |
3545 |- RMSNorm 后的数据分布在完整的 $M$ 维超球面上，自由度为 $M-1$。
3546 |- LayerNorm 后的数据分布在被超平面切开的“大圆”上，自由度为 $M-2$。
3547 |- RMSNorm 只去掉向量长度信息；LayerNorm 同时去掉向量长度信息和平移基准（直流分量）。
3548 |- 从 Triton 算子角度看，RMSNorm 计算开销更低，因为它只需要维护平方和累加器；LayerNorm 需要同时维护均值和方差。
3549 |
3550 |### 几何直觉
3551 |
3552 |当一个超平面去切割一个超球面，并且这个平面正好穿过球心时，切出来的交集是一个大圆（Great Circle）。
3553 |
3554 |在 $M$ 维空间里，这个交集可以理解为一个 $M-2$ 维的子超球面。
3555 |
3556 |因此：
3557 |
3558 |- RMSNorm：只把数据投影到完整超球面上。
3559 |- LayerNorm：先要求数据落在超球面上，又要求数据落在过球心的超平面上。
3560 |
3561 |### 三维空间例子（$M=3$）
3562 |
3563 |假设特征维度为 3，一行数据为 $[x, y, z]$。
3564 |
3565 |RMSNorm 的约束是：
3566 |
3567 |```text
3568 |x^2 + y^2 + z^2 = 3
3569 |```
3570 |
3571 |这对应一个普通的三维球面。
3572 |
3573 |LayerNorm 的约束是：
3574 |
3575 |```text
3576 |x^2 + y^2 + z^2 = 3
3577 |x + y + z = 0
3578 |```
3579 |
3580 |也就是说，LayerNorm 不仅要求数据落在球面上，还要求数据落在过球心的平面上。最终数据只能落在球面和平面的交线上，也就是一条圆形轨道。
3581 |
3582 |### 对大模型和 Triton 算子的意义
3583 |
3584 || 归一化方式 | 几何形态 | 损失的信息 | Triton 计算开销 |
3585 || --- | --- | --- | --- |
3586 || RMSNorm | 完整的超球面 | 向量的绝对长度 | 低，只需维护 1 个平方和累加器 |
3587 || LayerNorm | 超球面上的“平切圆” | 向量的绝对长度 + 平移基准（直流分量） | 高，需要维护均值和方差 2 个累加器 |
3588 |
3589 |### 物理本质
3590 |
3591 |从几何上看：
3592 |
3593 |- RMSNorm 是“只缩放长度”，保留方向和平移基准。
3594 |- LayerNorm 是“去均值 + 缩放长度”，同时去掉平移基准和长度尺度。
3595 |
3596 |这也是为什么在大模型推理和 Triton kernel 实现中，RMSNorm 往往比 LayerNorm 更轻量。
</code></pre>

<!-- source-log-coverage:end -->
