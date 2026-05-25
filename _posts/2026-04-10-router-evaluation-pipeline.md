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
