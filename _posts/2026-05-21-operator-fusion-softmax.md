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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-05-20](#source-log-2026-05-20) | 3501-3511 | 融合算子与 fused softmax |
| [2026-05-21](#source-log-2026-05-21) | 3512-3538 | 数值处理、softmax 融合与 block 规约 |

<a id="source-log-2026-05-20"></a>
### Source Log: 2026-05-20

Source lines: `Renyuan_Log.md:3501-3511`

<pre class="tech-log-source"><code>
3501 |# 2026-05-20
3502 |
3503 |Chapter2：简单融合算子与激活函数 (softmax, relu, silu, sigmoid)	&quot;录制: Wang Akang (SRIBD)预定的会议
3504 |日期: 2026-05-20 13:57:08
3505 |录制文件：https://meeting.tencent.com/crm/2BYebVgo61
3506 |密码：JAIW&quot;	算子学习第二节课复盘_融合算子与FusedSoftmax_整理与补充版.pdf	session5(20min)：基本融合算子：softmax	朱子为	以 fused-softmax为例，讲一下融合算子（fused softmax，不是 softmax）
3507 |			session6：融合的“模型”	杨明哲	把 fused softmax 的数据流动画出来，讲讲为什么要融合，数学本质是什么（函数复合，一次加载多次计算）
3508 |			session7（20min）：融合算子练习	占贺深	relu、gelu、x*sigmoid(x)融合与不融合的版本、x + sigmoid(x) + silu(x)（如何加载一次 x 就算 3 个值）
3509 |
3510 |
3511 |
</code></pre>


<a id="source-log-2026-05-21"></a>
### Source Log: 2026-05-21

Source lines: `Renyuan_Log.md:3512-3538`

<pre class="tech-log-source"><code>
3512 |# 2026-05-21
3513 |
3514 |## 算子学习 Chapter 3：数值处理与规约
3515 |
3516 |### 课程主题
3517 |
3518 |- `log softmax`
3519 |- `relu softmax`
3520 |- `softmax dropout`
3521 |- softmax 与 element-wise 操作的融合
3522 |- block 划分与规约
3523 |
3524 |### Session 安排
3525 |
3526 || Session | 负责人 | 主题 | 重点 |
3527 || --- | --- | --- | --- |
3528 || session8 | 刘欣 | 简单的算子优化方法 | 以 `log-softmax` 为例，展示简单算子优化方法 |
3529 || session9（20min） | 付谕书 | softmax 与 element-wise 的组合 | 以 `log-softmax + nll_loss`、`softmax + dropout` 为例，理解 softmax 与 element-wise 的融合方式 |
3530 || session10 | 崔诺拉 | 融合算子中的 block 划分与规约 | 实现 softmax 分块版本（不 fused） |
3531 || session11 | 刘稔远 | 实现 `relu(softmax(x))` | 讲解 Triton 实现代码，涉及 block 内部 program 计算和 block 之间的规约 |
3532 |
3533 |### 今日关注
3534 |
3535 |- softmax 相关算子不仅要理解数学形式，也要理解内存读写路径。
3536 |- softmax 与 element-wise 操作融合时，关键问题是哪些中间结果不需要写回 global memory。
3537 |- block 划分会直接影响规约方式，需要同时考虑 block 内 program 计算和 block 间结果合并。
3538 |
</code></pre>

<!-- source-log-coverage:end -->
