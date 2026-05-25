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
