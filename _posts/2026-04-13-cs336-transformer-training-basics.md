---
layout: single
title: "从 CS336 作业理解 Transformer 训练基本功"
date: 2026-04-13
categories:
  - tech-blog
  - transformer-foundations
series: "Transformer Foundations"
priority: P2
tags:
  - CS336
  - Transformer
  - BF16
  - einsum
excerpt: "把 activation checkpointing、Linear/einsum、权重矩阵布局和 BF16 串成训练系统基础。"
source_log:
  - "Renyuan_Log.md:1850-1869"
  - "Renyuan_Log.md:1875-1898"
  - "Renyuan_Log.md:1967-2001"
---

训练系统的基础不是某个单独概念，而是一组张量形状、内存和数值表示之间的约定。

## Activation checkpointing

Checkpointing 常被概括为“时间换空间”。前向时不保存所有中间激活，反向时重新计算一部分，从而减少显存占用。

它不是保存参数矩阵的 checkpoint，而是保存计算图中必要的边界状态。

## Linear 与 einsum

线性层可以写成：

```text
... d_in, d_out d_in -> ... d_out
```

这说明输入最后一维是 `d_in`，权重提供 `d_out` 个输出方向，结果最后一维变成 `d_out`。

理解这个 einsum，比记住某个框架 API 更可靠。

## 权重布局

PyTorch 的 Linear 权重常按 `(out_features, in_features)` 存。这会让初学者觉得和数学里的 `xW` 方向相反。

实际实现会根据内存布局和 GEMM 调用做选择。重要的是知道每一维代表输入还是输出，而不是死记矩阵在纸面上的方向。

## BF16

BF16 适合 LLM 的关键原因是指数位和 FP32 一样多，动态范围大，但尾数更短。它牺牲精度，保留范围，因此比 FP16 更不容易溢出。

训练基础最终都要回到三个问题：张量形状是什么、内存保存什么、数值格式能不能承受当前计算。

## 知识补全：形状推理是训练系统的地基

Transformer 训练里的很多 bug 都不是公式错，而是形状理解错。batch、sequence、head、hidden、vocab、expert 这些维度在不同模块中不断重排。

例如 attention 常见形状是：

```text
(batch, seq, hidden)
-> (batch, heads, seq, head_dim)
```

MLP 则常在 hidden 和 intermediate hidden 之间变换。MoE 又会多出 expert 维度和 token dispatch。

掌握形状推理后，einsum、reshape、transpose、contiguous、shard 都会更容易理解。

## 数值格式的直觉

FP16 尾数更多但指数范围小，容易溢出。BF16 尾数更少但范围大，因此在大模型中更稳。FP32 通常用于累加、优化器状态或敏感计算。

混合精度训练的核心不是“全都用低精度”，而是把不同计算放在合适精度上。

## 学习检查清单

读训练代码时，可以逐步标注：

1. 每个张量的 shape。
2. 每次 matmul 的输入输出维度。
3. 哪些激活会被保存到反向。
4. 哪些地方用了 checkpointing。
5. 参数、梯度、优化器状态分别是什么 dtype。
6. 是否存在隐式转置或 contiguous 拷贝。

这比单独背 Transformer 结构更接近工程实践。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-05](#source-log-2026-04-05) | 1551-1554 | 毕业设计推进 |
| [2026-04-06](#source-log-2026-04-06) | 1555-1561 | 非技术休整 |
| [2026-04-12](#source-log-2026-04-12) | 1871-1899 | CS336、MoE 与训练系统概念 |
| [2026-04-13](#source-log-2026-04-13) | 1900-2002 | Checkpoint、BF16 与 Linear 权重布局 |

<a id="source-log-2026-04-05"></a>
### Source Log: 2026-04-05

Source lines: `Renyuan_Log.md:1551-1554`

<pre class="tech-log-source"><code>
1551 |# 2026-04-05
1552 |
1553 |## 毕设毕设！
1554 |
</code></pre>


<a id="source-log-2026-04-06"></a>
### Source Log: 2026-04-06

Source lines: `Renyuan_Log.md:1555-1561`

<pre class="tech-log-source"><code>
1555 |# 2026-04-06
1556 |
1557 |## 拯救计划很好看
1558 |我觉得可以和星际穿越媲美。
1559 |太空的浪漫很纯粹。
1560 |[Bilibili细节解析](https://www.bilibili.com/video/BV1oSQZBRE8j/?spm_id_from=333.337.search-card.all.click)
1561 |
</code></pre>


<a id="source-log-2026-04-12"></a>
### Source Log: 2026-04-12

Source lines: `Renyuan_Log.md:1871-1899`

<pre class="tech-log-source"><code>
1871 |# 2026-04-12
1872 |
1873 |## 知识学习
1874 |
1875 |#### assignment1-basics/cs336_basics/trainer/utils.py
1876 |
1877 |#### assignment1-basics/cs336_basics/model/modules.py
1878 |
1879 |#### einsum()
1880 |
1881 |#### 常见显卡
1882 |
1883 |#### LLM参数量估算
1884 |
1885 |#### MoE模型
1886 |
1887 |#### PPO/GRPO/DPO
1888 |
1889 |```
1890 |# 定义前向传播：给定输入 x，输出线性变换后的结果。
1891 |def forward(self, x: torch.Tensor) -&gt; torch.Tensor:
1892 |    # 用 einsum 实现矩阵乘法。
1893 |    # 这里的含义是：
1894 |    # 输入 x 的最后一维是 d_in，
1895 |    # 权重 weight 的形状是 (d_out, d_in)，
1896 |    # 输出的最后一维就变成 d_out。
1897 |    return einsum(x, self.weight, &#x27;... d_in,  d_out d_in -&gt; ... d_out&#x27;)
1898 |```
1899 |
</code></pre>


<a id="source-log-2026-04-13"></a>
### Source Log: 2026-04-13

Source lines: `Renyuan_Log.md:1900-2002`

<pre class="tech-log-source"><code>
1900 |# 2026-04-13
1901 |
1902 |## 实践
1903 |
1904 |1. Semantic Router 的流程
1905 |
1906 |这版实现入口在 llmrouter/src/router/semantic_router_strategy.py 和 llmrouter/src/evaluate/run_evaluation.py。
1907 |
1908 |**完整流程**
1909 |```
1910 |1. 从训练集读取已标注样本。
1911 |   代码会把 /tangboyan/llmrouter/data/unified/train.jsonl 和 /tangboyan/llmrouter/results/labels/routing_labels.jsonl 对齐，只保留 unified train 里的 query。对应 load_train_labeled_queries()。
1912 |2. 把每条训练样本变成 semantic text。
1913 |   默认就是 query 本身；如果开了 semantic-text-fields，会把 dataset/subject/difficulty 这类 metadata 也拼进去。对应 build_semantic_text()。
1914 |3. 按路由目标组织成 route。
1915 |   当前支持两种模式：
1916 |    - tiered：5 路分类，直接建 1.5b / 3b / 7b / 14b / 32b 五个 route。
1917 |    - 32b-override：不是五路平权，而是“默认强模型 + 若干小模型 override”。例如 14B 默认，7B override。对应 prepare_route_training_records()。
1918 |4. 用预训练 encoder 建索引。
1919 |   每个 route 里放一批 utterances，semantic-router 用 HuggingFaceEncoder 编码后建立向量索引。对应 build_routes() 和 build_semantic_router_from_train_records()。
1920 |5. 推理时对测试 query 编码并检索。
1921 |   对测试 query 用同一个 encoder 编码，检索 top-k 相似 utterances，然后按 route 聚合分数。对应 score_routes_for_vector()。
1922 |6. 决策。
1923 |    - 如果是普通 tiered 且没调阈值：直接取 router 返回的最佳 route。
1924 |    - 如果开了 threshold tuning：按阈值判断，没过阈值就 fallback 到默认大模型。
1925 |    - 如果是 32b-override：必须走 threshold 逻辑，否则代码直接报错。对应 choose_route_with_thresholds() 和 run_semantic_router_inference()。
1926 |7. 评测。
1927 |   路由结果不会真实再调模型，而是去查已经离线跑好的 benchmark 结果，看被路由到的模型在该题上是否答对，然后统计 accuracy / cost / latency。对应 simulate_strategy() 和 compute_all_metrics()。
1928 |```
1929 |
1930 |2. 测试用了什么数据集？
1931 |测试集是 unified_test，入口写在 llmrouter/src/evaluate/run_evaluation.py。
1932 |具体是：
1933 |- 测试切分文件：/tangboyan/llmrouter/data/unified/test.jsonl
1934 |- 训练切分文件：/tangboyan/llmrouter/data/unified/train.jsonl
1935 |- 评测时会读取 5 个模型在各数据集上的 benchmark 结果，再筛出 unified_test 里的 query
1936 |- 当前这套 v2_5tier 评测覆盖的数据集，从结果里看是：
1937 |    - agieval
1938 |    - ceval
1939 |    - cmath
1940 |    - cmmlu
1941 |    - gsm8k
1942 |    - logiqa2
1943 |当前统一测试集规模是 6449 条。
1944 |
1945 |3. Semantic Router 需要训练吗？
1946 |结论：不需要像 classifier 那样做参数训练。
1947 |- classifier：要训练一个新模型
1948 |- semantic-router：不训练新分类器参数，只是“拿预训练 embedding 模型 + 训练集样本建语义路由索引”
1949 |
1950 |**semantic-router**
1951 |```
1952 |- 需要一套已标注的训练样本，用来构建 route utterances
1953 |- 需要一个预训练 encoder，例如你现在用过的：
1954 |    - sentence-transformers/all-MiniLM-L6-v2
1955 |    - sentence-transformers/all-mpnet-base-v2
1956 |- 可选地需要做一次阈值调优，但这不是模型训练，只是用训练集里再切一小块验证集做搜索
1957 |```
1958 |
1959 |现在这版代码里，threshold tuning 也只是：
1960 |- 切一部分 unified_train
1961 |- 搜索阈值
1962 |- 选 accuracy/cost 最优点
1963 |不是 gradient finetune。
1964 |
1965 |## 知识学习
1966 |
1967 |#### 为什么不直接存“参数矩阵的转置”？
1968 |
1969 |Y = X x W^T
1970 |
1971 |你可能会问：既然都要转置，为什么不直接把 self.weight 定义成 (in_features, out_features)？
1972 |
1973 |答案是：为了计算效率（和历史习惯）。
1974 |逻辑直观：在 (out, in) 的存储方式下，weight[0]（矩阵的第一行）直接对应于第一个输出神经元的所有权重。这在逻辑上非常清晰。
1975 |算子优化：底层硬件（如 NVIDIA GPU）在执行 Linear 算子时，针对这种存储方式做了深度优化。
1976 |
1977 |#### 常见数据类型详解
1978 |
1979 |通过浮点数的三个组成部分来理解它们：
1980 |符号位（Sign）、指数位（Exponent，决定范围）和尾数位（Fraction/Mantissa，决定精度）。
1981 |
1982 |#### FP32 (Full Precision / Single Precision)
1983 |结构： 1位符号，8位指数，23位尾数。
1984 |特点： 精度极高，数值范围广。
1985 |LLM 中的角色： 曾经是标准。但在如今的 LLM 训练中，它通常只作为“主权重（Master Weights）”存在，用来在优化器更新时保持微小的梯度变化。
1986 |
1987 |#### FP16 (Half Precision)
1988 |结构： 1位符号，5位指数，10位尾数。
1989 |优点： 内存占用减半，计算速度极快。
1990 |缺点： 数值范围窄（最大约 65504）。在训练 LLM 时，极易产生“梯度溢出（Overflow）”或“下溢（Underflow）”，导致训练崩溃。
1991 |对策： 需要使用混合精度训练（Mixed Precision Training）和损失缩放（Loss Scaling）。
1992 |
1993 |#### BF16 (Brain Floating Point 16) —— LLM 的宠儿
1994 |结构： **1**位符号，**8**位指数，**7**位尾数。
1995 |特点： 它是 Google 为了深度学习专门设计的。它的指数位与 FP32 一样长。
1996 |为什么好用： 它的精度（尾数）虽然不如 FP16，但它的数值范围（Range）和 FP32 完全一样。
1997 |意义： 在训练 LLM 时，你不需要担心梯度溢出，不需要搞复杂的 Loss Scaling。目前主流的大模型（Llama 3, GPT-4 等）基本都采用 BF16 进行预训练。
1998 |
1999 |#### einsum()
2000 |通过 einsum，即使输入是一个高维张量（例如 x 的形状是 (batch_size, L, d_model)），我们仍然可以通过 广播 规则来进行矩阵乘法（在这种情况下，广播会自动应用到批次维度和其他维度）。
2001 |所以，即使 x 不是二维矩阵，einsum 也能处理高维张量并正确地进行矩阵运算，保证维度匹配。
2002 |
</code></pre>

<!-- source-log-coverage:end -->
