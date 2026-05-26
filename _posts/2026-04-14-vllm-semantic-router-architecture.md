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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-04-14](#source-log-2026-04-14) | 2003-2127 | vLLM Semantic Router 架构 |
| [2026-04-15](#source-log-2026-04-15) | 2128-2129 | 空白日期占位 |
| [2026-04-22](#source-log-2026-04-22) | 2271-2309 | vLLM Router 实跑与 MoM 配置 |

<a id="source-log-2026-04-14"></a>
### Source Log: 2026-04-14

Source lines: `Renyuan_Log.md:2003-2127`

<pre class="tech-log-source"><code>
2003 |# 2026-04-14
2004 |
2005 |## 知识学习
2006 |
2007 |#### vLLM Semantic Router
2008 |是一个面向 多模型系统 的“语义路由与运行控制层”，不是单纯的模型网关，也不是只做学术路由实验的分类器。
2009 |它的官方定位是：在云、数据中心、边缘侧，为 Mixture-of-Models 提供系统级智能路由。README.md
2010 |- 不同模型在能力、成本、延迟、隐私边界上差异很大，单一模型很难覆盖所有流量。
2011 |- 真实请求不仅要“选模型”，还要同时处理安全、缓存、记忆、RAG、工具调用、回放审计等系统能力。
2012 |- 路由逻辑不能只停留在一个分类器上，而要变成可配置、可验证、可部署、可观测的运行时系统。
2013 |这个项目本质上更像一个 LLM 流量控制平面。它位于客户端和后端模型之间，理解请求，再决定走哪条路、用哪个模型、是否启用插件能力、是否需要额外的安全或工具策略。README.md docs/agent/repo-map.md
2014 |
2015 |#### 系统架构
2016 |把“路由”拆成了几个清晰层次，而不是用一个黑盒分类器直接输出模型名：
2017 |- signal evaluation
2018 |- projection coordination
2019 |- decision selection
2020 |- model selection
2021 |- plugin handling
2022 |在 AMD 参考 profile 里，这条链路写得很明确：先做多种信号检测，再做投影/分区，再选路由决策，最后把请求转发到对应模型别名。deploy/amd/README.md
2023 |
2024 |- Signals：检测层。定义“识别到了什么”。支持关键词、语言、上下文长度、结构、权限、embedding、domain、complexity、fact-check、jailbreak、PII、preference、reask、user-feedback、knowledge base 等。website/docs/tutorials/signal/overview.md
2025 |- Projections：协调层。把多个弱信号合成为可复用的中间事实，比如 intent partition、difficulty band、verification_required 这类 band，而不是把数值逻辑散落在每个 route 里。website/docs/tutorials/projection/overview.md
2026 |- Decisions：策略层。用布尔规则、优先级、tier 选出一条 route。这里是“哪条策略赢”。website/docs/tutorials/decision/overview.md src/semantic-router/pkg/config/decision_config.go
2027 |- Algorithms / Model Selection：候选模型选择层。一个 decision 可以挂多个候选模型，再用静态或学习式算法选最优，包括 static、elo、router_dc、automix、hybrid、rl_driven、gmtrouter、latency_aware，以及 looper 类的 confidence、ratings、remom。config/README.md src/semantic-router/pkg/extproc/req_filter_classification_runtime.go src/semantic-router/pkg/modelselection/selector.go
2028 |- Plugins：路由后处理层。匹配到某条 route 后，可以附加 route-local 行为，比如 semantic cache、RAG、memory、router replay、tools、system prompt、request params、content safety、hallucination、response jailbreak、image generation 等。website/docs/tutorials/plugin/overview.md
2029 |
2030 |不只是“把问题分类到模型”，而是在做 信号驱动的策略编排:
2031 |比如可以先识别“这是法律高风险请求”，再叠加“需要核验来源”“上下文很长”“用户在追问纠错”，最后才决定走 premium specialist 路线，并启用相应插件。
2032 |
2033 |#### 配置与运行方式
2034 |这个项目的另一大特点是配置体系比较完整，而且是统一的。
2035 |它采用一套 canonical YAML 合同：
2036 |- version
2037 |- listeners
2038 |- providers
2039 |- routing
2040 |- global
2041 |其中：
2042 |- routing 负责语义路由本身，包括 modelCards、signals、projections、decisions
2043 |- providers 负责具体部署绑定和默认模型
2044 |- global 负责全局运行时能力，比如 observability、router replay、stores、tools、looper、modelcatalog 等。这套约定写在公开配置文档里，也被仓库测试强约束。website/docs/installation/configuration.md configREADME.md
2045 |
2046 |此外，这个项目同时支持两种配置视角：
2047 |- YAML canonical config
2048 |- DSL authoring surface
2049 |也就是说，用户既可以直接写 config.yaml，也可以用 DSL/可视化编辑器去表达路由图，然后再编译回canonical YAML。这让它既适合工程部署，也适合调参和策略设计。
2050 |website/docs/installation/configuration.md
2051 |
2052 |在部署侧，它不是单一路径，而是支持多种环境：
2053 |- 本地 CPU 开发
2054 |- 本地 AMD/ROCm 开发
2055 |- Kubernetes / Helm / Operator
2056 |- Dashboard 控制台
2057 |- E2E profile 驱动的测试环境
2058 |
2059 |仓库文档给出的本地默认流程是：
2060 |- make vllm-sr-dev
2061 |- vllm-sr serve --image-pull-policy never
2062 |对应 CPU / AMD 两套本地环境说明也很清楚。docs/agent/environments.md
2063 |
2064 |#### 仓库组成
2065 |从代码组织上看，这个仓库已经不是一个单体 router，而是一整套平台：
2066 |- src/semantic-router：Go 核心路由器，包含 config、classification、decision engine、Envoy extproc、selection、plugin runtime。
2067 |- src/vllm-sr：Python CLI，负责本地启动、配置校验、Docker 编排、开发体验。
2068 |- dashboard：前后端控制台，用于配置编辑、部署、状态查看、playground、可视化。
2069 |- deploy/operator：Kubernetes Operator 和 CRD。
2070 |- deploy/helm：Helm chart。
2071 |- src/training：模型选择与分类相关训练脚本、数据、推理服务。
2072 |- e2e：端到端测试框架，覆盖 routing、safety、cache、response-api、dashboard、authz、streaming 多 profile。
2073 |- candle-binding ml-binding nlp-binding：Rust/native bindings，用于更底层的推理或 ML 能力接入。
2074 |
2075 |**架构图**
2076 |```
2077 |  Authoring / Control Plane
2078 |    Dashboard / DSL / YAML / CLI / Helm / Operator
2079 |          |
2080 |          v
2081 |  Canonical Config v0.3
2082 |    version / listeners / providers / routing / global
2083 |          |
2084 |          v
2085 |  Runtime Plane
2086 |    Client
2087 |      -&gt; Envoy
2088 |      -&gt; semantic-router extproc (OpenAIRouter)
2089 |         -&gt; Signals
2090 |         -&gt; Projections
2091 |         -&gt; Decisions
2092 |         -&gt; Algorithms / Looper
2093 |         -&gt; Route-local Plugins
2094 |         -&gt; Provider binding / endpoint selection / alias rewrite
2095 |         -&gt; Upstream model backends
2096 |      &lt;- Response filters / replay / cache / warnings / headers
2097 |          |
2098 |          v
2099 |  Observability / Replay / Dashboard Insight
2100 |
2101 |  Validation / Support Plane
2102 |    E2E profiles / deploy recipes / training stack / Rust-native bindings
2103 |```
2104 |这张图背后的关键点是：
2105 |- 这套系统有一个统一配置合同，不是 CLI 一套、Dashboard 一套、Operator 一套。仓库明确把入口统一为 version / listeners / providers / routing / global，其中 routing 负责 `modelCards5), website/docs/tutorials/projection/overview.md:9, website/docs/tutorials/decision/overview.md:7, website/docs/tutorials/algorithm/overview.md:7, website/docs/tutorials/plugin/overview.md:5, deploy/amd/README.md:100)
2106 |- 仓库形态也说明它是平台，不是单一 router binary。src/semantic-router 是 Go 路由内核，src/vllm-sr 是 Python CLI，dashboard/ 是控制台，deploy/operator/ 和 deploy/helm/ 是 K8s 部署面，e2e/ 是验证框架，src/training/ 和 Rust bindings 是算法/模型支持层。(docs/agent/repo-map.md:3)
2107 |
2108 |所以一句话说，它更像“LLM 流量控制平面 + 运行时策略编排层”，而不是“模型网关 + 少量规则”。
2109 |
2110 |#### 一次请求怎么被路由
2111 |1. 启动阶段先由 vllm-sr serve 做 bootstrap，解析配置、选择 Docker/K8s backend、准备 runtime config，然后把本地或集群拓扑拉起来。(src/vllm-sr/cli/commands/runtime.py:57, src/vllm-sr/cli/commands/runtime.py:214)
2112 |2. 真正请求进入时，Go 侧的 OpenAIRouter 作为 Envoy extproc server 工作。它不是只处理 request body，而是完整跑四个阶段：request headers -&gt; request body -&gt; response headers -&gt; response body。(src/semantic-router/pkg/extproc/router.go:24, src/semantic-router/pkg/extproc/processor_core.go:48)
2113 |3. request headers 阶段会先抓 request_id、:path、:method、streaming 预期、looper 内部请求标记等。也就是说，这里先决定“这是普通 chat、Response API、models 接口，还是 looper 内部调用”。(src/semantic-router/pkg/extproc/processor_req_header.go:17)
2114 |4. request body 阶段先走一个快路径：如果是 Response API，就先翻译成 chat completions 形态；然后做 body 校验；再用 fast extractor 直接拿到 model / userContent / firstImageURL / stream，避免一开始就完整反序列化。(src/semantic-router/pkg/extproc/processor_req_body.go:22, /home/ryan/CUHKSZ/LLM-Router/V:61, src/semantic-router/pkg/decision/engine.go:60, src/semantic-router/pkg/decision/engine.go:199)
2115 |5. decision engine 本身是个布尔规则树求值器。叶子节点是 type + name，支持 AND / OR / NOT，命中后会得到 confidence；多个 decision 都命中时，再按 tier -&gt; confidence -&gt; priority 或 priority -&gt; confidence 选出最终 route。(src/semantic-router/pkg/config/decision_config.go:3, src/semantic-router/pkg/decision/engine.go:151, src/semantic-router/pkg/decision/engine.go:335)
2116 |6. route 选出来以后，不一定立刻等于“最终模型已定”。
2117 |如果用户显式指定模型，router 会保留原模型，但仍然保留 decision 结果给插件使用。
2118 |如果用户走的是 auto model，router 才会根据 decision.modelRefs + decision.algorithm 去做候选选择。(src/semantic-router/pkg/extproc/req_filter_classification_runtime.go:138, src/semantic-router/pkg/extproc/req_filter_classification.go:61)
2119 |7. 候选模型选择分两类。单模型选择算法走 selector registry，比如 static / elo / router_dc / automix / hybrid / rl_driven / gmtrouter / latency_aware / knn / kmeans / svm。多模型编排算法走 looper，比如 confidence / ratings / remom。(website/docs/tutorials/algorithm/overview.md:55, src/semantic-router/pkg/selection/factory.go:96, src/semantic-router/pkg/extproc/req_filter_looper.go:45)
2120 |8. 在真正发往上游前，router 还会跑一组 route-local 行为：fast_response、rate limit、semantic cache short-circuit、RAG 检索、modality 处理、memory 注入、request params、system prompt、tools 选择。然后才做 endpoint 选择、alias 到 provider-specific model id 的映射，并把修改后的 body 发给上游。(src/semantic-router/pkg/extproc/processor_req_body_prepare.go:63, src/semantic-router/pkg/extproc/req_filter_rag.go:19, src/semantic-router/pkg/extproc/processor_req_body_routing.go:28, src/semantic-router/pkg/extproc/processor_req_body_routing.go:65, /home/ryan/CUHKSZ/LLM-Router/VLLM-sem)
2121 |
2122 |把这 12 步压成一句话就是：
2123 |客户端只发出一次 OpenAI 兼容请求，但 router 在内部实际完成了:
2124 |“请求理解、信号抽取、投影协调、策略命中、候选模型选择、插件执行、后端绑定、响应审计与告警”
2125 |这整条系统链路。
2126 |
2127 |
</code></pre>


<a id="source-log-2026-04-15"></a>
### Source Log: 2026-04-15

Source lines: `Renyuan_Log.md:2128-2129`

<pre class="tech-log-source"><code>
2128 |# 2026-04-15
2129 |
</code></pre>


<a id="source-log-2026-04-22"></a>
### Source Log: 2026-04-22

Source lines: `Renyuan_Log.md:2271-2309`

<pre class="tech-log-source"><code>
2271 |# 2026-04-22
2272 |
2273 |## vLLM-Router 完整运行起来了
2274 |
2275 |这次真正跑通后，我对当前配置的理解是：
2276 |
2277 |- `model: &quot;MoM&quot;` 时，router 才会接管选模；否则就是普通模型直连。
2278 |- 现在的 `decision -&gt; route -&gt; model` 里，大多数 route 只挂了 1 个 `modelRef`，所以它本质上还是“先分类，再直接转发”，还不是“同一路由内多模型竞争”。
2279 |- 全局虽然开了 `model_selection.method: static`，但在单 `modelRef` 配置下，这一层几乎没有发挥作用。
2280 |
2281 |当前路由大致可分为两类：
2282 |
2283 |- 强制标签路由：`#flash / #plus / #max / #deepseek / #kimi / #coder` 分别固定到对应模型。
2284 |- 语义路由：
2285 |  - 代码 / 报错 / 编程类 -&gt; `qwen3-coder-plus`
2286 |  - 深度分析 / 长上下文 -&gt; `qwen3.6-max-preview`
2287 |  - 规划 / 路线图 / 分步骤执行 -&gt; `kimi-k2.5`
2288 |  - 多问题分析 -&gt; `deepseek-v3.2`
2289 |  - 简短简单问题 -&gt; `qwen3.6-flash`
2290 |  - 兜底 -&gt; `qwen3.6-plus`
2291 |
2292 |这条 pipeline 可以概括成：
2293 |
2294 |1. 客户端请求打到 `8899`，并指定 `model: &quot;MoM&quot;`。
2295 |2. Router 先根据消息内容抽取 signals。
2296 |3. Decision engine 用这些 signals 命中某条 route。
2297 |4. 当前 route 里通常只有一个 `modelRef`，所以直接选中该模型并转发到对应 provider。
2298 |
2299 |我现在的判断：
2300 |
2301 |- 这套配置已经能稳定完成“按请求类型分流”。
2302 |- 但它还不算真正的多模型选择系统，更像是“规则分类器 + 单模型映射”。
2303 |- 如果要验证 model selection 的价值，下一步必须让同一条 decision 挂多个 `modelRef`，否则 selection 层基本没有实验意义。
2304 |
2305 |补充定位：
2306 |- 路由规则主要看 `config.yaml`
2307 |- 分类入口在 `src/semantic-router/pkg/extproc/req_filter_classification*.go`
2308 |
2309 |
</code></pre>

<!-- source-log-coverage:end -->
