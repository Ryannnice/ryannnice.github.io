---
layout: single
title: "vLLM V1 工程边界：一条请求如何从 API 走到 PagedAttention"
date: 2026-05-04
categories:
  - tech-blog
  - serving-deployment
series: "Serving & Deployment"
priority: P0
featured: true
tags:
  - vLLM
  - Serving
  - KV Cache
  - PagedAttention
excerpt: "读 vLLM 不要一开始盯 kernel，而要先看 serving runtime 的稳定边界和请求生命周期。"
source_log:
  - "Renyuan_Log.md:2578-2584"
  - "Renyuan_Log.md:2607-2642"
  - "Renyuan_Log.md:3016-3020"
---

理解 vLLM，最好不要从某个 kernel 开始。vLLM 的核心价值首先体现在 serving runtime：它如何接收请求、调度 batch、管理 KV cache、驱动模型执行，再把结果流式返回。

## 主要边界

一个请求进入后，大致会经过：

```text
API Server -> LLMEngine -> EngineCore -> Scheduler -> KVCacheManager -> ModelRunner -> Attention Backend
```

API Server 负责协议层。LLMEngine 是对外接口。EngineCore 维护推理主循环。Scheduler 决定哪些请求进入本轮执行。KVCacheManager 管理缓存块。ModelRunner 负责实际模型前向。Attention Backend 才会接到底层注意力实现。

## 为什么 Scheduler 重要

LLM serving 的难点不是单个请求，而是大量请求共享 GPU。continuous batching 的价值就在于不断把新请求和未完成请求合并，减少设备空转。

这也意味着 scheduler 决定了吞吐、延迟和公平性。它不是辅助模块，而是 serving 系统的核心。

## KV cache 与 PagedAttention

自回归生成会不断复用历史 token 的 K/V。KV cache 的组织方式直接影响显存利用率。PagedAttention 的直觉是把 KV cache 拆成块，像虚拟内存一样管理，减少连续大块显存分配带来的浪费。

因此，vLLM 的工程边界可以这样理解：API 层处理请求，调度层组织执行，缓存层管理历史状态，attention backend 承担高性能计算。

## 读代码顺序

推荐顺序：

1. 先看请求生命周期。
2. 再看 scheduler 和 KV cache。
3. 最后看 attention backend 和 CUDA graph。

这样更容易把 kernel 级优化放回系统上下文里。

## 知识补全：prefill 和 decode

LLM serving 里一个请求通常分成两个阶段。Prefill 阶段处理用户输入的 prompt，一次性计算上下文的 K/V。Decode 阶段每次生成一个或少量新 token，不断复用历史 KV cache。

这两个阶段的性能瓶颈不同。Prefill 更像大矩阵计算，吞吐和算力利用率重要。Decode 则更容易受 KV cache 读取、batch 调度和尾延迟影响。

Scheduler 要同时处理长 prompt、短 prompt、已经进入 decode 的请求和新来的请求。Continuous batching 的本质就是让这些请求在每一步动态组合，尽量不让 GPU 空等。

## 学习检查清单

读 vLLM 或其他 serving 框架时，可以按这条线检查：

1. 请求在哪里进入队列。
2. prefill 和 decode 是否分开调度。
3. KV cache block 如何分配和释放。
4. scheduler 如何决定本轮执行哪些 sequence。
5. attention backend 接收的张量形状是什么。
6. streaming response 如何把 token 送回客户端。

如果这些问题能串起来，就能从系统层理解 vLLM，而不是只记住 PagedAttention 这个名词。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-04](#source-log-2026-04-04) | 1541-1550 | PageAttention 与 Flash Attention 入口 |
| [2026-04-30](#source-log-2026-04-30) | 2578-2594 | 推理框架选型入口 |
| [2026-05-04](#source-log-2026-05-04) | 2607-2646 | vLLM 工程边界与请求生命周期 |
| [2026-05-12](#source-log-2026-05-12) | 3016-3022 | mini-vLLM 源码阶段完成 |

<a id="source-log-2026-04-04"></a>
### Source Log: 2026-04-04

Source lines: `Renyuan_Log.md:1541-1550`

<pre class="tech-log-source"><code>
1541 |# 2026-04-04
1542 |
1543 |## 知识学习
1544 |
1545 |#### PageAttention
1546 |[怎么加快大模型推理？10分钟学懂VLLM内部原理，KV Cache，PageAttention](https://www.bilibili.com/video/BV1kx4y1x7bu/?spm_id_from=333.1391.0.0&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1547 |
1548 |#### Flash Attention
1549 |[Flash Attention 为什么那么快？原理讲解](https://www.bilibili.com/video/BV1UT421k7rA/?spm_id_from=333.1391.0.0&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1550 |
</code></pre>


<a id="source-log-2026-04-30"></a>
### Source Log: 2026-04-30

Source lines: `Renyuan_Log.md:2578-2594`

<pre class="tech-log-source"><code>
2578 |# 2026-04-30
2579 |
2580 |## 关于推理框架
2581 |
2582 |我们两个小时的组会讨论了各个主流的推理框架&#32;&#32;
2583 |我们排除了OmniInfer、ChiTu&#32;&#32;
2584 |最终，决定在vLLM、vLLM-Ascend、SGLang-Ascend、xLLM中选取&#32;&#32;
2585 |
2586 |
2587 |## 港中深新生见面会
2588 |
2589 |七八个新的志同道合者&#32;&#32;
2590 |受益！&#32;&#32;
2591 |
2592 |
2593 |
2594 |
</code></pre>


<a id="source-log-2026-05-04"></a>
### Source Log: 2026-05-04

Source lines: `Renyuan_Log.md:2607-2646`

<pre class="tech-log-source"><code>
2607 |# 2026-05-04
2608 |
2609 |## vLLM 工程边界与目录地图
2610 |
2611 |理解 vLLM，先不要盯住某个 kernel；先看它把 serving runtime 切成了哪些稳定边界。
2612 |
2613 || 层次 | 关键文件 | 主要契约 | 为什么关键 |
2614 || --- | --- | --- | --- |
2615 || 用户入口 | [`v1/engine/llm_engine.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) | 请求规范化、输出回组装 | 把 API 面和 runtime 面隔开 |
2616 || EngineCore | [`v1/engine/core.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) | `add_request()` / `step()` 主循环 | 是 V1 runtime 总装点 |
2617 || Scheduler | [`v1/core/sched/scheduler.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) | 本轮谁前进、前进多少、是否抢占 | continuous batching 的真正核心 |
2618 || KV 系统 | [`v1/core/kv_cache_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py)、[`v1/core/block_pool.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/block_pool.py) | prefix hit、slot 分配、block 生命周期 | PagedAttention 的系统收益都在这里释放 |
2619 || 协议对象 | [`v1/request.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/request.py)、[`v1/core/sched/output.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py) | Request、SchedulerOutput、status 字段 | feature 越多，越要靠协议对象稳住边界 |
2620 || Worker / ModelRunner | [`v1/worker/gpu/model_runner.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py)、[`v1/worker/gpu/input_batch.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py) | 把 scheduler output 变成设备输入批次 | 调度和算子之间的翻译层 |
2621 || Attention backend | [`v1/attention/backend.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/backend.py)、[`v1/attention/selector.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/selector.py) | backend 选择、metadata 协议 | attention 不是单函数而是一套派发体系 |
2622 || Paged Attention 执行 | [`v1/attention/ops/paged_attn.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/ops/paged_attn.py)、[`v1/worker/gpu/block_table.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/block_table.py) | block table、slot mapping、decode 访存路径 | 把 block 化 KV 变成真实执行 |
2623 || 编译与图执行 | [`compilation/cuda_graph.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/cuda_graph.py)、[`compilation/passes/pass_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/passes/pass_manager.py) | capture/replay、pass 重写、runtime wrapper | 压低 decode 高频小步固定开销 |
2624 || 执行器与分布式 | [`v1/executor/abstract.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/executor/abstract.py)、[`distributed/parallel_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/parallel_state.py) | 单进程/多进程/Ray、TP/EP/CP 进程组 | 把单卡 runtime 拉成服务系统 |
2625 || Connector / 外部缓存 | [`distributed/kv_transfer/kv_connector/base.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/kv_transfer/kv_connector/base.py)、[`distributed/ec_transfer/ec_transfer_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/ec_transfer/ec_transfer_state.py) | KV/encoder cache 搬运协议 | disaggregated serving 的关键拼图 |
2626 |
2627 |
2628 |
2629 |## 一次请求在 vLLM 里如何被推进
2630 |
2631 |把一条请求主链拉直之后，很多“为什么快”都会落回同一条控制流。
2632 |
2633 |1. 用户请求经 [`LLMEngine`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) 标准化，形成 engine request。
2634 |2. [`EngineCore.add_request()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 把请求交给 runtime，进入 waiting queue。
2635 |3. [`EngineCore.step()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 驱动一轮 scheduler + executor 主循环。
2636 |4. [`Scheduler.schedule()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) 计算该请求本轮还能前进多少 token。
2637 |5. [`KVCacheManager.get_computed_blocks()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 查 prefix hit，再由 [`allocate_slots()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 申请 block。
2638 |6. Scheduler 产出 [`SchedulerOutput`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py)，executor 把它下发到 worker。
2639 |7. [`GPUModelRunner.prepare_inputs()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py) 构造 [`InputBatch`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py)，再由 `prepare_attn()` 拼出 block tables 和 slot mappings。
2640 |8. `model_state.prepare_attn()` 与 attention backend 生成 metadata，按 full graph / piecewise / eager 路径执行模型。
2641 |9. `sample()` 或 rejection sampler 产出 token，`postprocess()` 更新 host/device 两侧状态镜像。
2642 |10. output processor 把底层 token 流整理成用户侧可见结果。
2643 |
2644 |
2645 |
2646 |
</code></pre>


<a id="source-log-2026-05-12"></a>
### Source Log: 2026-05-12

Source lines: `Renyuan_Log.md:3016-3022`

<pre class="tech-log-source"><code>
3016 |# 2026-05-12
3017 |
3018 |## mini-vllm 源码完结！
3019 |
3020 |前海湾公园的海与落日很美 ...
3021 |
3022 |
</code></pre>

<!-- source-log-coverage:end -->
