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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-10](#source-log-2026-04-10) | 1711-1773 | Semantic Router 接入与延迟口径 |

<a id="source-log-2026-04-10"></a>
### Source Log: 2026-04-10

Source lines: `Renyuan_Log.md:1711-1773`

<pre class="tech-log-source"><code>
1711 |# 2026-04-10
1712 |
1713 |## 尝试更多的开源策略
1714 |
1715 |#### 现有Pipeline
1716 |
1717 |- `llmrouter` 当前主链路是：
1718 |  数据合并与切分 -&gt; 全模型 benchmark -&gt; 自动打 tier 标签 -&gt; 训练 classifier / 调 cascade 阈值 -&gt; test 集统一评测 -&gt; 出图。
1719 |- benchmark 阶段才会真实调用各模型；训练和评测阶段主要基于已保存结果做监督训练或离线模拟。
1720 |- 因此当前 accuracy / cost 基本可直接比较，但 flat router 自身的 routing latency 并没有被完整计入。
1721 |- 当前主评测策略包括：
1722 |  `baseline-32b / 14b / 7b / 3b / 1.5b`、
1723 |  `random`、
1724 |  `oracle`、
1725 |  `cascade-default`、
1726 |  `cascade-optimized`、
1727 |  `classifier`、
1728 |  `binary-gate-logprobs`
1729 |
1730 |#### [Semantic-router](https://github.com/aurelio-labs/semantic-router)
1731 |- 我把 `semantic-router` 理解成“检索式分类器”，它更适合先以 `query -&gt; predicted_label` 的形式接入 Phase 3 evaluation，而不是直接改 benchmark 主干。
1732 |- 接入思路被收敛为：
1733 |  - 用 `unified/train` + `routing_labels` 构建 5 路 semantic routes
1734 |  - 对 `unified/test` 做 semantic routing
1735 |  - 输出 `predicted_label`
1736 |  - 复用现有 `simulate_strategy` 和 metrics
1737 |- 需要提前注意的风险：
1738 |  - 路径硬编码较多
1739 |  - 需要可用的 encoder backend
1740 |  - Python 3.13 对部分本地 encoder 兼容性一般
1741 |  - 当前延迟口径仍不是端到端 latency
1742 |- 已完成远程单独评测：
1743 |  - Accuracy: 68.18%
1744 |  - Cost Ratio: 25.9%
1745 |  - Avg Latency: 857ms
1746 |  - P99 Latency: 8308ms
1747 |- 相对位置：
1748 |  - 比 `classifier` 更准，但成本更高
1749 |  - 略低于 `cascade-optimized` 的准确率，但延迟明显更好
1750 |- 远程结果和对比文件都已经单独保存，后续可以直接回看 summary / comparison 产物。
1751 |
1752 |#### Router Latency
1753 |
1754 |- 我专门确认了一个问题：论文和综述通常会提到 latency / overhead，但很少把 `router decision latency` 单独定义为最终实验指标。
1755 |- 更常见的口径仍然是端到端响应时间，因此 router 本身的额外决策开销在很多对比里其实是模糊的。
1756 |
1757 |- 当前诊断已经比较明确：
1758 |  - route 分布严重不平衡，32B route 太小
1759 |  - hardest 样本识别不足
1760 |  - 排除 `all_wrong` 样本会进一步削弱 hardest route
1761 |- 后续调参顺序也已经确定：
1762 |  1. 先加 `all_wrong`
1763 |  2. 再做 per-route cap，处理类不平衡
1764 |  3. 最后再调 `top-k` 和 aggregation
1765 |- 已跑出的关键实验结果：
1766 |  - `semantic_router_gpu`: 68.18% / 25.9%
1767 |  - `include_all_wrong`: 68.91% / 33.2%
1768 |  - `include_all_wrong + cap2000`: 70.29% / 36.7%
1769 |  - `include_all_wrong + top5 + max`: 62.94% / 20.6%
1770 |  - `bge-m3 + include_all_wrong`: 68.72% / 31.8%
1771 |  - `bge-m3 + include_all_wrong + cap2000`: 69.34% / 33.7%
1772 |- 这一轮最重要的结论是：真正决定效果的不是“semantic-router”这个名字，而是 route 形态、数据分布和 threshold 策略。
1773 |
</code></pre>

<!-- source-log-coverage:end -->
