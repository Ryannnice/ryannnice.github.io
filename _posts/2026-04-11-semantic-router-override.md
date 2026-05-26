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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-11](#source-log-2026-04-11) | 1774-1870 | Semantic Override 实验 |

<a id="source-log-2026-04-11"></a>
### Source Log: 2026-04-11

Source lines: `Renyuan_Log.md:1774-1870`

<pre class="tech-log-source"><code>
1774 |# 2026-04-11
1775 |
1776 |## 实践
1777 |
1778 |#### 追求极致的正确率
1779 |
1780 |- 当前 best semantic-router: 79.61% / 97.2%
1781 |- 提升是 +0.08 个点 accuracy，同时成本从 100% 降到 97.2%
1782 |
1783 |最新结果：
1784 |  跑完了 4 组cost &lt;= 40% 的 semantic-router 新实验。当前最优是：
1785 |  - semantic_router_override14b_7b_meta_mpnet_cost40_fresh4xa100
1786 |  - Accuracy: 76.28%
1787 |  - Cost Ratio: 38.6%
1788 |  - Avg Latency: 1054ms
1789 |  - P99 Latency: 9744ms
1790 |
1791 |  关键配置：
1792 |  - encoder: sentence-transformers/all-mpnet-base-v2
1793 |  - routing mode: 32b-override 这一套逻辑被我用作“base model default + semantic override”，这里 base 是 qwen2.5-14b
1794 |  - override candidate: qwen2.5-7b
1795 |  - text fields: dataset,subject,difficulty
1796 |  - tuned threshold: qwen2.5-7b = 0.8628563005596404
1797 |  - routing distribution: qwen2.5-14b = 4935, qwen2.5-7b = 1514
1798 |
1799 |#### 已知方案总体对比
1800 |
1801 || 策略 | 准确率 | 相对成本 | 平均延迟 | P99 延迟 |
1802 ||------|--------|----------|----------|----------|
1803 || Always 32B | 79.53% | 100.0% | 1539ms | 18354ms |
1804 || Always 14B | 76.73% | 43.7% | 1248ms | 13021ms |
1805 || Always 7B | 72.58% | 22.1% | 659ms | 4878ms |
1806 || Always 3B | 63.92% | 9.4% | 621ms | 4673ms |
1807 || Always 1.5B | 55.93% | 4.7% | 624ms | 4280ms |
1808 || Random | 69.64% | 36.6% | 897ms | 7977ms |
1809 || Oracle | 90.80% | 20.3% | 824ms | 6848ms |
1810 || Cascade (default) | 62.35% | 10.3% | 951ms | 6759ms |
1811 || Cascade (optimized) | 68.85% | 24.7% | 2053ms | 21973ms |
1812 || Binary Gate (logprobs) | 68.85% | 24.7% | 2053ms | 21973ms |
1813 || Classifier (0.5B) | 60.89% | 12.3% | 765ms | 6386ms |
1814 || Semantic Tiered MiniLM cap2000 | 70.71% | 37.2% | 968ms | 9624ms |
1815 || Semantic Tiered MiniLM cost33 | 70.12% | 33.8% | 942ms | 9019ms |
1816 || Semantic Tiered MiniLM cost35.5 | 70.62% | 36.8% | 963ms | 9503ms |
1817 || Semantic Override 32B-&gt;14B MPNet | 79.61% | 97.2% | 1525ms | 17398ms |
1818 || Semantic Override 14B-&gt;7B MPNet | 76.28% | 38.6% | 1054ms | 9744ms |
1819 || Semantic Override 14B-&gt;3B MPNet | 74.57% | 35.7% | 1017ms | 9050ms |
1820 || Semantic Override 14B-&gt;1.5B/3B MPNet | 73.67% | 35.1% | 1023ms | 8919ms |
1821 |
1822 |#### 最新 Semantic Router 内部对比
1823 |
1824 || 方案 | Encoder | 路由形式 | 关键设置 | 准确率 | 成本 |
1825 ||------|---------|----------|----------|--------|------|
1826 || Tiered MiniLM cap2000 | all-MiniLM-L6-v2 | 五路 tiered | include_all_wrong + cap2000 | 70.71% | 37.2% |
1827 || Tiered MiniLM tuned cost33 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.33 | 70.12% | 33.8% |
1828 || Tiered MiniLM tuned cost35.5 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.355 | 70.62% | 36.8% |
1829 || Override 32B-&gt;14B MPNet | all-mpnet-base-v2 | 32B 默认，命中后降到 14B | metadata: dataset/subject/difficulty，threshold=0.9364 | 79.61% | 97.2% |
1830 || Override 14B-&gt;7B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 7B | metadata: dataset/subject/difficulty，threshold=0.8629 | 76.28% | 38.6% |
1831 || Override 14B-&gt;3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 3B | metadata: dataset/subject/difficulty，threshold=0.8585 | 74.57% | 35.7% |
1832 || Override 14B-&gt;1.5B/3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 1.5B/3B | metadata: dataset/subject/difficulty，threshold=0.8818 | 73.67% | 35.1% |
1833 |
1834 |#### 关键结论
1835 |1. **Semantic Router 的当前最高准确率方案**是 `32B 默认 + 14B override + MPNet + metadata`，达到 **79.61% / 97.2%**。相比 Always 32B，准确率仅提高 **0.08** 个百分点，成本下降 **2.8** 个百分点，收益很小，但它证明 semantic override 已经可以做到几乎不掉点。
1836 |2. **在 cost &lt;= 40% 约束下，当前最优方案**是 `14B 默认 + 7B override + MPNet + metadata`，达到 **76.28% / 38.6%**。相比 Always 14B，准确率只低 **0.45** 个百分点，但成本少 **5.1** 个百分点。
1837 |3. **旧的 tiered semantic-router 已经被 override 方案明显压制。** 最好的 tiered 版本是 `include_all_wrong + cap2000`，只有 **70.71% / 37.2%**；而 `14B-&gt;7B override` 在几乎相同成本下把准确率再拉高了 **5.57** 个百分点，成本只增加 **1.4** 个百分点。
1838 |4. **真正带来提升的不是“semantic-router”这个名字本身，而是方案形态变化。** 从五路 tiered 改成“强模型默认 + 低一级模型 override”，再叠加 `all-mpnet-base-v2` 和结构化 metadata，效果才明显跃升。
1839 |5. **如果目标是把 semantic-router 接到现有 llmrouter pipeline 做单独验证，当前最值得保留的候选只需要两条：**
1840 |   - `semantic-override32b-14b-mpnet-meta-acc`：用于验证语义路由的准确率上限。
1841 |   - `semantic-override14b-7b-mpnet-meta-cost40`：用于验证成本受限场景下的真实收益。
1842 |
1843 |#### 和已有 Router 方案的相对位置
1844 |- 相比 `classifier`，`14B-&gt;7B semantic override` 准确率从 **60.89%** 提升到 **76.28%**，但成本也从 **12.3%** 提升到 **38.6%**。
1845 |- 相比 `cascade-optimized` / `binary-gate-logprobs` 的 **68.85% / 24.7%**，`14B-&gt;7B semantic override` 在准确率上高出 **7.43** 个百分点，但成本也更高。
1846 |- 在“可直接上线的简单策略”里，Always 14B 仍然是很强的朴素基线：**76.73% / 43.7%**。Semantic override 的价值在于把这条强基线压到 40% 左右成本时，仍能尽量保留准确率。
1847 |
1848 |## 知识学习
1849 |
1850 |#### 参数矩阵 Checkpoint
1851 |参数矩阵只保存某些checkpoint：
1852 |训练时，**时间换空间**
1853 |
1854 |为什么 checkpoint 不只存第一层：
1855 |反向传播需要 每一层的输入激活值。如果只存第一层：
1856 |L1 (存)
1857 |L2
1858 |L3
1859 |L4
1860 |反向传播时会反复从 L1 重新算：
1861 |L1→L2→L3
1862 |L1→L2
1863 |...
1864 |计算量会爆炸。因此实际做法是 每隔几层存一个：
1865 |L1 (存)
1866 |L2
1867 |L3
1868 |L4 (存)
1869 |这样反向时最多只需要 重新算中间几层，计算量可控，同时减少显存。
1870 |
</code></pre>

<!-- source-log-coverage:end -->
