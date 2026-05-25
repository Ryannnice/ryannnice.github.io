---
layout: single
title: "Semantic Router 实验：为什么 Override 形态优于五路 Tiered 路由"
date: 2026-04-11
categories:
  - tech-blog
  - llm-routing
series: "LLM Routing"
priority: P0
featured: true
tags:
  - semantic-router
  - MPNet
  - Threshold
  - Cost-Accuracy
excerpt: "实验显示，真正决定效果的不是工具名，而是 route 形态、数据分布、metadata 和 threshold。"
source_log:
  - "Renyuan_Log.md:1730-1772"
  - "Renyuan_Log.md:1780-1846"
  - "Renyuan_Log.md:1904-1963"
---

semantic-router 最开始可以被理解为一个检索式分类器：把 query 映射到 route，再由 route 对应模型。问题是，五路 tiered 路由在实验中并不天然有效。

## Tiered 的问题

五路 tiered 试图直接把样本分到 32B、14B、7B、3B、1.5B。这个形态的问题是 route 分布容易失衡，hardest 样本识别不稳定，threshold 调整后成本和准确率都可能大幅波动。

实验里，加入 `all_wrong`、per-route cap、top-k aggregation 都会改变结果，但最关键的突破不在这些局部调参。

## Override 形态

更有效的形态是：

```text
default strong model + semantic override to smaller model
```

也就是默认走一个较强基线，只在语义上足够确定时降到更小模型。这样 router 不是承担“从零选择五个模型”的压力，而是承担“哪些样本可以安全降级”的任务。

## 关键结果

两个结果最值得保留：

- `32B 默认 + 14B override + MPNet + metadata`：`79.61% / 97.2%`
- `14B 默认 + 7B override + MPNet + metadata`：`76.28% / 38.6%`

前者证明语义 override 可以几乎不掉准确率。后者在 cost <= 40% 的约束下更实用：相比 Always 14B 只小幅降低准确率，却进一步降低成本。

## 实验结论

semantic-router 的收益不是来自“用了 embedding”这个事实，而是来自更合适的路由任务定义。

相比五路 tiered，override 让问题变得更简单：不是判断所有模型谁最好，而是判断某些请求是否可以安全用低一级模型处理。

## 知识补全：为什么 override 更稳

五路分类的难点在于类别边界复杂。一个样本到底应该走 14B 还是 7B，可能取决于题型、难度、候选模型能力和数据分布。embedding 相似并不必然等于能力需求相同。

Override 把问题改写成二元判断：

```text
默认强模型是否可以安全降级？
```

这个问题更容易通过 threshold 控制风险。阈值高一点，降级更保守；阈值低一点，成本更低但风险更高。它把复杂多分类变成了可解释的风险控制问题。

## Metadata 的作用

只用 query embedding 时，router 看到的是文本语义。加入 `dataset`、`subject`、`difficulty` 等 metadata 后，router 能获得任务背景。

这很像人类做题：同一句话如果来自数学竞赛、日常问答或代码调试，所需模型能力并不一样。metadata 可以给 embedding 补上上下文。

## 实验检查清单

继续做 semantic-router 实验时，应记录：

1. route 形态：tiered 还是 override。
2. encoder：MiniLM、MPNet、BGE 等。
3. 是否包含 metadata。
4. threshold 如何调。
5. routing distribution 是否失衡。
6. cost constraint 是多少。
7. 相比 Always 14B / 32B 的真实收益。

这能让实验结论从“某个方案有效”变成“为什么有效”。
