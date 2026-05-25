---
layout: single
title: "如何搭建一个 Router Evaluation Pipeline"
date: 2026-04-10
categories:
  - tech-blog
  - llm-routing
series: "LLM Routing"
priority: P0
featured: true
tags:
  - LLM Router
  - Benchmark
  - Offline Simulation
  - Pipeline
excerpt: "把多模型 benchmark、tier 标签、classifier、cascade 和 semantic-router 放进统一离线评测链路。"
source_log:
  - "Renyuan_Log.md:1715-1755"
  - "Renyuan_Log.md:1904-1963"
---

Router 实验容易陷入一个问题：每个策略都用自己的数据、脚本和指标，最后很难比较。一个可靠的 evaluation pipeline 应该先固定数据和指标，再把不同路由策略接进去。

## 主链路

一个可复用流程可以是：

```text
data merge -> split -> all-model benchmark -> tier labels -> strategy simulation -> metrics -> plots
```

benchmark 阶段真实调用候选模型，保存每个样本在每个模型上的结果。后续训练和评测尽量复用这些结果，避免每次调整 router 都重新调用模型。

## 策略接口

所有策略最终都应该输出一个选择结果：某个样本应该走哪个模型或哪个 tier。

因此 classifier、cascade、binary gate、semantic-router 都可以接到同一个 `simulate_strategy` 接口上。

这种设计让实验关注策略本身，而不是重复写评测逻辑。

## 指标

基本指标包括：

- accuracy
- cost ratio
- average latency
- P99 latency
- routing distribution

其中 latency 要特别小心。很多论文报告的是端到端时间，而不是 router decision latency。离线模拟可以比较 accuracy 和 cost，但如果没有真实在线部署，就不能声称完整覆盖了端到端延迟。

## 为什么离线模拟有价值

离线模拟的优势是快速、稳定、可复现。只要 benchmark 结果可靠，就能大量尝试 threshold、route 形态和模型池。

缺点是它不自动覆盖真实系统开销，例如 embedding 计算、网络、batching、服务排队和 router runtime。

因此 pipeline 的定位应明确：它是策略筛选器，不是最终上线验证。

## 知识补全：Oracle 为什么重要

Router 评测里常见一个特殊基线：Oracle。Oracle 假设我们提前知道每个样本在哪个模型上答对，然后选择最便宜的正确模型。

Oracle 在真实系统中不可用，但它给出了当前模型池的理论上限。如果 Oracle 准确率很高且成本很低，说明模型之间存在互补性，router 有发挥空间。如果 Oracle 本身也不理想，继续调 router 的收益就有限。

另一个重要基线是 Always Strong 和 Always Weak。前者提供质量上限和成本上限，后者提供成本下限和质量下限。router 必须解释自己相对这两个基线的价值。

## 数据泄漏风险

离线 pipeline 最容易出现数据泄漏。比如用 test 集结果调 threshold，或让 router 训练时见到评测标签，都会让结果虚高。

一个更稳的切分是：

```text
train: 训练 classifier / routes
dev:   调 threshold / hyperparameter
test:  最终只评一次
```

如果数据量不大，也要明确哪些实验是探索，哪些结果可以作为最终报告。

## 学习检查清单

一个 router evaluation pipeline 至少应回答：

1. 每个模型的原始结果是否被保存。
2. 训练、调参、测试是否分离。
3. cost 是否按同一 token 价格表计算。
4. latency 是否来自真实调用还是离线估计。
5. Oracle、Always Strong、Always Weak 是否都存在。
6. 每个策略是否复用同一个评测函数。

缺少这些约束，router 实验很容易变成不可复现的手工调参。
