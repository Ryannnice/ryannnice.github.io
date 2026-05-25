---
layout: single
title: "LLM Router 的设计空间：从难度感知到级联系统"
date: 2026-04-07
categories:
  - tech-blog
  - llm-routing
series: "LLM Routing"
priority: P1
tags:
  - LLM Router
  - Survey
  - Cascade
  - Uncertainty
excerpt: "把模型路由拆成决策时机、使用信号、计算方式和六类主流技术路线。"
source_log:
  - "Renyuan_Log.md:1570-1620"
  - "Renyuan_Log.md:1631-1653"
---

LLM Router 的目标是在多个模型之间做选择，让系统在准确率、成本和延迟之间取得更好的平衡。它不是单一算法，而是一组设计选择。

## 三个维度

第一是决策时机。生成前路由在模型回答前根据输入选择模型；生成后路由先得到回答，再根据质量或置信度决定是否升级；多阶段路由则把这两者组合起来。

第二是使用信息。最简单的路由只看 query 本身，例如长度、关键词、语义向量。更复杂的路由会加入模型元数据、成本、延迟、领域能力、logprobs、verifier 输出或用户反馈。

第三是计算方式。规则和阈值最容易部署；监督分类器可以利用历史表现；聚类方法强调语义结构；强化学习或 bandit 方法适合在线调整。

## 六类路线

难度感知路由是最直观的一类：简单问题给小模型，复杂问题给大模型。

人类偏好路由关注“哪个回答更好”，不一定只看对错。

聚类路由把语义相似的请求归为一组，为每个簇选择表现最好的模型。

强化学习路由把路由视为长期策略，在反馈中调整。

不确定性路由关注模型是否犹豫，例如 logits、熵或置信度信号。

级联系统先让便宜模型尝试，再通过停止判断或验证器决定是否升级。

## 复现顺序

工程复现不应该从最复杂的方案开始。更现实的顺序是先跑通 AutoMix 或 FrugalGPT 这类 cascade 基线，再尝试 BEST-Route、GraphRouter、CP-Router 等复杂方案。

这个设计空间的价值在于：后续做任何 router 实验时，都能先问清楚三个问题。它在什么时候决策？它看什么信号？它用什么方式计算？

## 知识补全：路由的目标函数

LLM Router 不是单纯追求最高准确率。真实系统通常在优化一个多目标函数：

```text
utility = quality - cost_penalty - latency_penalty - risk_penalty
```

quality 可以是准确率、偏好分数、人工满意度或任务成功率。cost_penalty 来自模型价格、token 数和硬件成本。latency_penalty 关注平均延迟和尾延迟。risk_penalty 则和安全、隐私、合规、幻觉风险有关。

因此，同一个 router 在不同产品里会有不同最优解。客服系统可能优先低成本和低延迟，医疗法律系统可能优先风险控制，代码生成系统可能优先可验证正确性。

## 学习检查清单

读一篇路由论文或项目时，可以逐项拆解：

1. 它优化的是 accuracy、win-rate、cost，还是综合效用。
2. 路由发生在生成前、生成后，还是多阶段。
3. 它使用 query、response、logprobs、metadata 还是用户反馈。
4. 它是否需要训练数据。
5. 它是否能加入新模型。
6. 它报告的是 router latency 还是端到端 latency。
7. 它的失败样本是否会被强模型兜底。

这组问题能避免只记方法名字，而忽略系统适用条件。
