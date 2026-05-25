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
