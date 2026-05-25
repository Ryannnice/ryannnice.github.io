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
