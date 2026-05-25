---
layout: single
title: "vLLM Semantic Router 架构拆解：从分类器到 LLM 流量控制平面"
date: 2026-04-14
categories:
  - tech-blog
  - llm-routing
series: "LLM Routing"
priority: P0
featured: true
tags:
  - vLLM Semantic Router
  - Control Plane
  - Envoy
  - Model Selection
excerpt: "vLLM Semantic Router 更像 LLM 流量控制平面：信号、投影、决策、模型选择和插件共同组成运行时策略。"
source_log:
  - "Renyuan_Log.md:2007-2125"
  - "Renyuan_Log.md:2273-2307"
---

vLLM Semantic Router 不是一个简单的“query 分类器”。它更像多模型系统的流量控制平面，位于客户端和模型后端之间，理解请求、命中策略、选择模型，并执行 route-local 插件。

## 五层抽象

第一层是 Signals，用来检测请求中出现了什么，例如语言、长度、domain、complexity、jailbreak、PII、preference。

第二层是 Projections，用来把多个弱信号合成为中间事实，例如 intent partition、difficulty band、verification required。

第三层是 Decisions，用布尔规则、优先级、tier 和 confidence 选出 route。

第四层是 Algorithms / Model Selection，在候选模型之间做选择，例如 static、elo、latency-aware、automix、router_dc。

第五层是 Plugins，在路由后执行 RAG、cache、memory、tools、system prompt、request params、content safety 等行为。

## 配置合同

它的配置不是零散参数，而是一套 canonical YAML：

- `version`
- `listeners`
- `providers`
- `routing`
- `global`

`routing` 描述信号、投影、决策和模型卡；`providers` 绑定具体后端；`global` 承载观测、replay、stores、tools 等运行能力。

## 请求路径

请求进入后，Envoy extproc 把处理交给 OpenAIRouter。router 会处理 request headers、request body、response headers、response body，而不是只在 body 上做一次分类。

在 request body 阶段，它会解析模型名、用户内容、streaming 预期和 modality，然后进行 signal extraction、decision evaluation、model selection，最后做 provider alias rewrite 并转发。

## 实跑判断

当请求指定 `model: "MoM"` 时，router 才真正接管选模。当前很多 route 只挂一个 `modelRef`，所以它本质上更像“规则分类器 + 单模型映射”。如果要验证 model selection 的价值，同一条 decision 必须挂多个候选模型，否则 selection 层没有实验空间。

这个结论很重要：系统具备多模型控制平面能力，不等于当前配置已经在做真正多模型竞争。
