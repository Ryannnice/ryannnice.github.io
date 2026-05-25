---
layout: single
title: "RouteLLM 复现笔记：从 GSM8K 生成到评测可视化"
date: 2026-04-09
categories:
  - tech-blog
  - llm-routing
series: "LLM Routing"
priority: P1
tags:
  - RouteLLM
  - GSM8K
  - Evaluation
  - Cost
excerpt: "跑通 RouteLLM 的响应生成、评测和可视化链路，并比较 strong/weak/router 的成本准确率。"
source_log:
  - "Renyuan_Log.md:1673-1689"
  - "Renyuan_Log.md:1695-1709"
---

RouteLLM 复现的核心不是安装成功，而是跑通完整链路：

```text
responses -> evaluation -> visualization
```

只有拿到可比较的准确率和成本，router 才能被评价。

## 修复点

复现过程中几个小问题会阻塞主链路：输出目录不存在、import 阶段依赖 API key、评测脚本不支持自定义响应文件、可视化读取路径固定。

这些问题本身不复杂，但它们提醒了一点：开源 router 项目往往默认作者自己的实验路径。要把它接入自己的评测体系，第一步是把输入输出变成可配置。

## 策略对比

GSM8K 上的对比包括：

- weak model：成本最低，但能力有上限。
- strong model：准确率最高，但成本明显更高。
- random：没有有效路由，只是基线。
- Causal_LLM / MF / BERT / SW_Ranking：不同 router 策略。

其中 Causal_LLM 类策略体现了路由价值：在成本低于 strong model 的情况下，保留了接近强模型的能力。

## 复现实用顺序

推荐顺序是：

1. 保持 router server 运行。
2. 先跑 5 题 smoke test。
3. 确认 strong / weak 都能产出响应。
4. 再跑全量生成。
5. 最后执行 evaluate 和可视化。

这篇复现的结论是：RouteLLM 的价值不只在算法，而在于它提供了一条能比较 cost-performance tradeoff 的实验路径。

## 知识补全：为什么 GSM8K 适合 smoke test

GSM8K 是小学数学应用题数据集，答案通常有明确数值。这让它很适合做 router 的第一轮验证：评测标准清楚，强弱模型差距明显，错误容易归因。

但 GSM8K 也有局限。它主要测数学推理，不能代表代码、长文本、事实问答、多轮对话或安全场景。一个在 GSM8K 上有效的 router，不一定能迁移到真实混合流量。

因此，GSM8K 更适合作为 smoke test 和方法调通，而不是最终证明。

## 结果如何解读

看 router 结果时，不应只看准确率。更有意义的是画出三角关系：

```text
Weak:   low cost, lower ceiling
Strong: high cost, high ceiling
Router: between them, seeking better tradeoff
```

如果 router 的准确率接近 strong，但成本明显更低，它就有价值。如果 router 的成本接近 strong，准确率却没有提升，那它只是增加复杂度。

## 复现检查清单

复现 RouteLLM 类项目时，应保留这些产物：

1. 原始响应文件。
2. 每个样本的 strong/weak 正误。
3. router 选择结果。
4. 统一评测脚本。
5. 成本计算口径。
6. 可视化图表。

这些产物能支持后续换模型、换数据、换 router，而不是只留下一次运行截图。
