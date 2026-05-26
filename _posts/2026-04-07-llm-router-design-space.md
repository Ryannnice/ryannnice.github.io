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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-07](#source-log-2026-04-07) | 1562-1621 | LLM Router 设计空间 |
| [2026-04-08](#source-log-2026-04-08) | 1622-1690 | Router Pipeline 与经典论文复现顺序 |

<a id="source-log-2026-04-07"></a>
### Source Log: 2026-04-07

Source lines: `Renyuan_Log.md:1562-1621`

<pre class="tech-log-source"><code>
1562 |# 2026-04-07
1563 |
1564 |## 知识学习
1565 |
1566 |#### AI Station
1567 |
1568 |[AI Station 教程](https://xxl9u0uq9y2.feishu.cn/wiki/LVHvw3GCWiMlV4kjH25clngHnVf)
1569 |
1570 |#### LLM Router
1571 |
1572 |谕书的完整Pipeline
1573 |
1574 |#### Router 综述
1575 |
1576 |#### LLM 路由的概念设计空间
1577 |本综述涵盖的范式（参见 1.3 节）为组织和理解文献提供了基础 。
1578 |在实践中，现实世界的系统往往同时借鉴了不止一种范式 。
1579 |为了补充基于范式的组织方式，路由方法还可以从更广泛的维度进行分类 ：
1580 |
1581 |#### 决策时机 (When)：指路由决策何时做出 。
1582 |路由系统可以依赖生成前 (Pre-generation) 决策或生成后 (Post-generation) 决策，也可以采用多阶段过程 。
1583 |生成前路由在产生任何输出前选择模型，完全依赖于输入查询的属性；而生成后路由则在产生初始响应后，根据输出质量或置信度信号做出决定 。
1584 |
1585 |#### 使用信息 (What)：路由机制使用的信号丰富程度各不相同 。最简单的方法仅基于查询本身，利用词法或语义特征来刻画请求 。
1586 |更进阶的系统还会加入可用模型的元数据来指导选择，如成本、延迟或领域专长 。生成后方法则进一步引入响应级信号，如置信度得分、Token 概率或验证器输出 。
1587 |
1588 |#### 计算方式 (How)：路由决策的计算复杂度差异显著 。一端是简单的阈值规则或基于成本的启发式方法，无需训练即可直接应用 ；
1589 |另一端是基于历史表现数据训练的监督分类器，用于预测哪个模型最适合处理给定查询 。
1590 |更复杂的方法采用自适应策略，通过与环境的持续交互来更新路由行为 。
1591 |
1592 |#### 主流技术路线
1593 |1. 难度感知路由 (Difficulty-aware Routing)
1594 |  这是最直观的路线，核心是**“看题下菜”** 。
1595 |  原理：在推理前评估查询的复杂度，将简单题分给小模型，难题分给大模型 。
1596 |  评估手段：包括启发式规则（如文本长度、词汇稀缺度）、训练专门的分类器（如你计划使用的 0.5B 模型）或使用 “LLM 作为评判者” 。
1597 |  代表案例：BEST-Route（动态分配并选择采样策略）和 VLLM Semantic Router（识别是否需要开启昂贵的思维链推理） 。
1598 |2. 人类偏好对齐路由 (Human Preference-aligned Routing)
1599 |  不看“对错”，看**“好坏”** 。
1600 |  原理：模拟人类的主观评价，预测大模型生成的答案是否会比小模型显著“更好” 。
1601 |  训练数据：利用 Chatbot Arena 等人类真实偏好数据或 LLM 自动生成的对比数据 。
1602 |  代表案例：RouteLLM（预测强模型是否会胜出）和 Arch-Router（允许用户自定义不同领域的路由偏好） 。
1603 |3. 基于聚类的路由 (Clustering-based Routing)
1604 |  核心是**“找规律”** 。
1605 |  原理：利用无监督学习（如 K-means）将语义相似的查询聚类，并为每个簇分配表现最好的模型 。
1606 |  优势：具有极强的扩展性，添加新模型时无需重新训练路由器，只需测试新模型在各个簇上的表现即可 。
1607 |  代表案例：UniRoute 和 Avengers-Pro 。
1608 |4. 强化学习路由 (Reinforcement Learning Routing)
1609 |  核心是**“实战进化”** 。
1610 |  策略优化：通过多步交互（思考 -&gt; 路由 -&gt; 再思考）迭代改进答案，适合复杂推理，但延迟较高（如 Router-R1） 。
1611 |  在线老虎机 (Bandit)：在实时交互中通过用户反馈（点赞/踩）动态调整路由策略，平衡“探索新模型”与“利用已知强模型” 。
1612 |  代表案例：MixLLM（实现 97% 的 GPT-4 质量且仅需 24% 的成本） 。
1613 |5. 基于不确定性的路由 (Uncertainty-based Routing)这是你项目中 Logprobs 熵值 策略的理论依据 。
1614 |  原理：监控模型对自身回答的“信心” 。如果内部数学信号（如概率分布）显示模型在犹豫，则触发升级 。
1615 |  关键点：研究证明，模型内部的探测信号（Logits）远比模型自己口头说的“我很确定”要准得多 。
1616 |  代表案例：CP-Router（利用共形预测处理不确定性） 。
1617 |6. 级联系统 (Cascading)这是你项目中 Binary Gate 和逐级踢球架构的归属 。
1618 |  原理：顺序执行。先让小模型试，不行再给中模型，最后大模型保底 。
1619 |  核心逻辑：引入了“后悔药”机制，通过自我验证或外部评估器决定是否停止或升级 。
1620 |  代表案例：FrugalGPT（三大组件：路由器、质量评估器、停止判断器）和 AutoMix 。
1621 |
</code></pre>


<a id="source-log-2026-04-08"></a>
### Source Log: 2026-04-08

Source lines: `Renyuan_Log.md:1622-1690`

<pre class="tech-log-source"><code>
1622 |# 2026-04-08
1623 |
1624 |## 实践
1625 |
1626 |搭建了自己的完整Pipeline
1627 |质量不变的情况下，cluster方法效果最好，成本降低了 ***10%***
1628 |
1629 |## 知识学习
1630 |
1631 |#### Router 经典论文总结
1632 |本文档面向后续逐篇复现，聚焦综述 《Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey》 中以下三节的代表性工作：
1633 |
1634 |Section 2: Difficulty-aware Routing
1635 |Section 6: Uncertainty-based Routing
1636 |Section 7: Cascades
1637 |整理原则：
1638 |
1639 |只优先采用原论文、官方项目页、官方代码仓库、会议页面。
1640 |如果某些细节在摘要页看不到，我会明确标注“需要补读 PDF/附录”。
1641 |如果仓库 README 展示的是论文发布后的扩展结果，我会明确写成“仓库后续更新”，避免和论文主结果混淆。
1642 |一页结论
1643 |如果你接下来要逐一复现，我建议按这个顺序推进：
1644 |
1645 |AutoMix：代码、数据、任务说明最完整，最适合先跑通一个 cascade 基线。
1646 |FrugalGPT：工程可用性强，官方仓库完整，适合改造成商业 API 版本。
1647 |BEST-Route：代码完整，但包含 reward model、best-of-n、多阶段数据构造，工程复杂度高于前两者。
1648 |GraphRouter：官方代码已放出，但图构建与数据预处理更复杂。
1649 |EmbedLLM：数据和代码齐全，但更像“模型表示学习 + routing 下游头”，对实验环境要求更高。
1650 |CP-Router：训练自由、思路清晰，但我当前未检索到官方代码，复现需要自己补实现。
1651 |Self-REF / Learning to Route LLMs with Confidence Tokens：论文价值高，但目前未检索到官方公开代码。
1652 |Confidence-Driven LLM Router：适合后续用商业 API 重做，但目前主要能拿到论文页面信息，代码未公开。
1653 |
1654 |#### 开源Router方案总结
1655 |本文档对 4 个你点名的开源 router / router 模型做统一拆解：
1656 |
1657 |1. `RouteLLM`
1658 |2. `semantic-router`
1659 |3. `notdiamond-0001`
1660 |4. `knn-router`
1661 |整理维度尽量与 `经典论文.md` 保持一致：
1662 |- 项目定位
1663 |- 相关论文或技术来源
1664 |- 数据集
1665 |- 测试用大模型 / 候选模型池
1666 |- router 模型 / 机制
1667 |- 效果 / benchmark
1668 |- 创新点
1669 |- 实验与工程形态
1670 |- 开源代码位置
1671 |- 复现建议
1672 |
1673 |#### RouteLLM
1674 |
1675 |这一段原本保留了完整的操作指令，整理后保留关键信息：
1676 |
1677 |- `RouteLLM` 的 GSM8K 基本链路已经打通，2 题 smoke test 可以分别产出 strong / weak model 结果。
1678 |- 当时最后的阻塞点只是 `outputs/` 目录不存在，后来已经补成自动创建。
1679 |- 关键修复包括：
1680 |  - `bert` 路径不再强依赖 `OPENAI_API_KEY`
1681 |  - `openai_server.py` 不再在 import 阶段崩溃
1682 |  - `gsm8k.generate_responses` 支持自定义模型对和输出文件
1683 |  - 评测脚本可以直接读取自定义 GSM8K 响应 CSV 并做可视化
1684 |- 固定执行顺序被整理成：
1685 |  1. 保持 `routellm.openai_server` 运行
1686 |  2. 先做 5 题 smoke test
1687 |  3. 成功后再跑全量生成
1688 |  4. 最后执行 evaluate 出图
1689 |- 这一段最重要的收获不是命令本身，而是把 `RouteLLM` 的“响应生成 -&gt; 评测 -&gt; 可视化”链路真正跑通了。
1690 |
</code></pre>

<!-- source-log-coverage:end -->
