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
