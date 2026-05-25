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

## 知识补全：Gateway、Router 和 Control Plane 的区别

模型网关通常解决协议和转发问题：统一 OpenAI 兼容接口、鉴权、限流、日志、provider 绑定。

Router 在网关基础上增加选择逻辑：根据请求内容、成本或策略选择模型。

Control Plane 更进一步，它不仅选择模型，还管理策略、插件、可观测性、回放、配置发布和运行时行为。vLLM Semantic Router 更接近这一层。

这三个概念可以这样区分：

```text
Gateway:      request -> provider
Router:       request -> decision -> provider
Control Plane request -> signals -> policy -> plugins -> provider -> observability
```

## 配置即系统边界

Canonical YAML 的价值在于让策略从代码中抽离出来。Signals、Projections、Decisions 和 Providers 都在配置中表达，系统就能做到：

- 策略变更不一定要改 Go 代码。
- Dashboard、CLI、Operator 可以共享同一份配置合同。
- E2E 测试可以直接验证配置行为。
- 路由策略能被审计和回放。

## 学习检查清单

分析一个 LLM control plane 时，可以看：

1. 请求是否仍兼容标准 OpenAI API。
2. 路由决策是否可配置。
3. 是否支持多模型候选选择，而不只是单 route 映射。
4. 插件是在路由前、路由后，还是响应后执行。
5. 是否有 replay 和 observability。
6. Dashboard / CLI / Operator 是否共享同一配置语义。

这些问题决定它是“网关工具”，还是“多模型运行时平台”。
