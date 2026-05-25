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
