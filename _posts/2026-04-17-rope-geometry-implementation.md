---
layout: single
title: "RoPE 的几何直觉与代码实现"
date: 2026-04-17
categories:
  - tech-blog
  - transformer-foundations
series: "Transformer Foundations"
priority: P1
tags:
  - RoPE
  - Position Encoding
  - Transformer
  - PyTorch
excerpt: "把 RoPE 理解成 D/2 个二维平面的成对旋转，再映射到 rearrange、unbind 和 stack。"
source_log:
  - "Renyuan_Log.md:2137-2252"
  - "Renyuan_Log.md:2475-2573"
---

RoPE 的核心不是给每个维度加一个位置值，而是把隐藏维度两两成对，放进多个二维平面里旋转。

如果向量维度是 `D`，RoPE 会形成 `D/2` 个二维平面：

```text
(x0, x1), (x2, x3), ..., (xD-2, xD-1)
```

每个平面都有自己的频率。低频平面旋转慢，更适合长距离关系；高频平面旋转快，更适合近距离区分。

## 几何性质

二维旋转改变方向，但不改变长度。因此 RoPE 把位置信息写进方向关系里，同时保留幅值信息。

这也是为什么它必须成对处理维度。只缩放单个维度不是旋转，只有 `(x_even, x_odd)` 联动才构成平面上的点。

## 代码形状

实现中常见的第一步是重排：

```python
x = rearrange(x, "... (s r) -> ... s r", r=2)
```

形状从：

```text
(B, H, S, 64)
```

变成：

```text
(B, H, S, 32, 2)
```

最后的 `2` 就是每个二维平面的坐标。

接着：

```python
x_even, x_odd = x.unbind(dim=-1)
x = torch.stack((-x_odd, x_even), dim=-1)
```

这个变换把 `[a, b]` 变成 `[-b, a]`，对应二维平面中的 90 度旋转基向量。再和 `sin/cos` 组合，就得到任意角度旋转。

RoPE 的代码难点不是语法，而是始终记住：隐藏维度被组织成了很多独立的二维旋转平面。

## 知识补全：相对位置为什么会出现

RoPE 的一个重要性质是，两个 token 的 query/key 点积会自然包含相对位置差。直观地说，如果第 `m` 个位置旋转了 `m * theta`，第 `n` 个位置旋转了 `n * theta`，它们之间的角度差就是 `(m - n) * theta`。

因此模型不只是知道“我在第几个位置”，还可以通过旋转后的方向关系感知两个 token 的相对距离。

这也是 RoPE 相比绝对位置编码更适合长上下文扩展的原因之一。当然，长上下文扩展还需要处理频率外推问题，所以会出现 NTK-aware、YaRN 等方法。

## 学习检查清单

理解 RoPE 时，建议确认：

1. 最后一维是否按偶数/奇数成对。
2. 每一对是否对应一个二维平面。
3. 旋转是否保持向量长度。
4. 不同平面是否使用不同频率。
5. 点积中如何体现相对位置。
6. 长上下文扩展调的是位置、频率，还是缩放策略。

这些问题能避免把 RoPE 只记成一段 `rotate_half` 代码。
