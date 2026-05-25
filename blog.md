# 技术博客页面规划

本文档规划如何把 `Renyuan_Log.md` 中的学习日志整理成个人技术博客页面，并在当前 Jekyll 站点导航栏新增博客入口。

## 0. 当前结论

- 新增导航项：`Tech Blog`，链接到 `/tech-blog/`。
- 新增博客索引页：`tech-blog.md`，负责展示精选文章、系列分类、时间线和标签入口。
- 新增文章目录：`_posts/`，把日志按主题重组为正式博客文章。
- 保留 `Renyuan_Log.md` 作为原始素材，不直接破坏、不直接迁移全部内容。
- 第一版不要追求“所有日志都上线”，而是先发布 8-12 篇高质量主题文章。
- 公开发布前必须做脱敏：内部 IP、任务号、队列名、会议链接、密码、私有路径、API/密钥相关内容不能原样进入博客。

## 1. 站点现状

### 1.1 当前技术栈

当前仓库是 Jekyll 静态站点，结构接近 Minimal Mistakes 风格：

- `_config.yml` 控制站点基础配置和导航。
- `_includes/masthead.html` 遍历 `site.navigation.main` 渲染导航栏。
- `_layouts/single.html` 是普通页面布局。
- `assets/css/main.scss` 汇总导入 `_sass/` 下的样式。
- 首页内容在 `about.md`，并通过锚点导航到 Experience / Publications / Awards 等章节。

### 1.2 导航策略

当前导航项大多是首页锚点，例如 `#experience-renyuan`。技术博客应作为独立页面，而不是首页某个锚点。

推荐在 `_config.yml` 的 `navigation.main` 中新增：

```yml
- title: "Tech Blog"
  url: "/tech-blog/"
```

备选命名：

- `Tech Blog`：与当前英文导航一致，推荐。
- `Notes`：更轻，更像学习笔记。
- `技术博客`：中文直观，但和当前英文导航风格不完全一致。

## 2. 参考风格

用户指定参考页面：`https://fywc.github.io/pages/`。

当前环境未能成功联网抓取该页面，因此本规划先基于“技术博客页”的常见信息架构和当前站点结构设计。后续如果可以提供截图或重新联网确认，应补充一次视觉对齐。

参考方向暂定为：

- 页面以文章列表为第一主体，而不是营销首页。
- 内容按主题系列组织，而不是逐日流水账。
- 列表项包含标题、日期、摘要、标签、系列归属。
- 首页保留简洁学术站点气质，不做过重装饰。
- 支持深浅色主题，不破坏当前站点的 theme toggle。

## 3. 内容整理原则

### 3.1 从“日期日志”变成“主题文章”

`Renyuan_Log.md` 当前按日期组织，但博客应按主题组织。

转换规则：

1. 一个日期可以贡献给多篇文章。
2. 多个日期可以融合成一篇主题文章。
3. 只记录事件、链接、占位、生活碎片的内容进入 timeline，不进入正式文章。
4. 技术文章必须有清楚主线：问题、背景、方案、实验、结论、复盘。
5. 如果原文存在阶段性误判，正式文章要保留演化过程，但明确最终结论。

### 3.2 正式文章的最低标准

一篇文章应该至少满足以下条件之一：

- 有完整工程链路，例如从请求进入到部署完成。
- 有实验数据或对比表，例如准确率、成本、延迟。
- 有可复用架构抽象，例如 RunStore、workflow、router pipeline。
- 有技术解释价值，例如 RoPE、CUDA reduction、LayerNorm vs RMSNorm。
- 有真实踩坑矩阵，例如 DeepSeek V4 Flash 部署复盘。

### 3.3 不适合直接发布的内容

以下内容应只放 timeline，或脱敏后作为附录材料：

- 单纯教程链接。
- 空日期或占位内容。
- 个人状态、会议安排、生活记录。
- 内部会议链接、会议密码。
- 内部服务器 IP、队列名、任务号、私有路径。
- API key、代理配置、账号信息、密钥路径。
- 未整理的命令流水账。

## 4. 博客页面信息架构

### 4.1 `/tech-blog/` 首屏

目标：让访问者一眼知道这是“系统实现、LLM 推理、Agent 工程、GPU/NPU 学习”的技术博客。

建议内容：

- 页面标题：`Tech Blog`
- 简短副标题：`Engineering notes on coding agents, LLM routing, serving systems, and GPU/NPU kernels.`
- 四个主题入口：
  - `Agent Engineering`
  - `LLM Routing`
  - `Serving & Deployment`
  - `CUDA / Triton / NPU`

不建议做大 hero。当前个人主页是学术简洁风格，博客页面也应保持紧凑。

### 4.2 Featured Posts

第一屏下方放 4-6 篇精选文章。

推荐第一版精选：

1. `Coding Agent 不是一个接口：分层、RunStore、工作流与自动修复闭环`
2. `vLLM Semantic Router 架构拆解：从分类器到 LLM 流量控制平面`
3. `DeepSeek V4 Flash on Ascend：一次 vLLM-Ascend 部署复盘`
4. `Semantic Router 实验：为什么 Override 形态优于五路 Tiered 路由`
5. `从写循环到写映射：CUDA kernel 如何接上 LLM 优化`
6. `LayerNorm vs RMSNorm：从几何自由度到 Triton kernel 成本`

### 4.3 Series

博客应优先按系列组织，而不是只按时间排序。

建议系列：

#### Series A: Agent Engineering

定位：Coding Agent、Workshop、OnlySpecs、opencode、Agent-Do、FastAPI、SSE、部署闭环。

核心问题：

- 如何把一次性 LLM 生成升级为可验证、可修复、可部署的工程系统？
- 如何把 Agent 的内部过程展示给用户？
- 如何把开源项目拆解后接入自己的系统？

#### Series B: LLM Routing

定位：LLM Router、RouteLLM、semantic-router、evaluation pipeline、vLLM Semantic Router。

核心问题：

- 多模型系统如何在准确率、成本、延迟之间做权衡？
- 路由策略到底是分类器、级联系统、语义检索，还是控制平面？
- 实验中哪些设计真的带来收益？

#### Series C: LLM Serving & Deployment

定位：vLLM、vLLM-Ascend、DeepSeek V4 Flash、NPU 集群、Kubernetes/Volcano/ktp。

核心问题：

- 一条请求如何从 API 进入 serving runtime？
- KV cache、scheduler、tensor parallel、data parallel 对部署有什么影响？
- 大模型在 Ascend/NPU 集群上启动失败时，如何定位问题？

#### Series D: CUDA / Triton / Kernel Notes

定位：CUDA 基础、reduction、shared memory、operator fusion、LayerNorm/RMSNorm、Triton。

核心问题：

- GPU kernel 的执行模型是什么？
- 算子优化为什么常常是减少 global memory 读写？
- 归一化、softmax、规约这些基础算子如何映射到 kernel 实现？

#### Series E: Transformer Foundations

定位：RoPE、Encoder/KV、CS336、BF16、einsum、训练基础。

核心问题：

- Transformer 的抽象如何落实到张量形状和代码？
- RoPE、KV、checkpointing、BF16 这些概念如何从数学直觉过渡到实现？

### 4.4 All Posts

索引页底部展示全部文章，按时间倒序。

每个条目建议字段：

- 标题
- 日期
- 系列
- 标签
- 120 字以内摘要
- 原始日志来源日期

### 4.5 Timeline

Timeline 不等于正式文章列表。

用途：

- 保留学习轨迹。
- 放置短进展和 milestone。
- 显示哪些内容已经整理成文章，哪些仍是原始笔记。

Timeline 条目字段：

- 日期
- 简短事件
- 关联主题
- 是否已整理成文章

## 5. 推荐文件结构

第一版建议使用 Jekyll 标准 `_posts/`，避免引入复杂 collection。

```text
.
├── _config.yml
├── tech-blog.md
├── _posts/
│   ├── 2026-03-26-coding-agent-workflow.md
│   ├── 2026-03-28-agent-ux-sse-jsonl.md
│   ├── 2026-04-11-semantic-router-override.md
│   ├── 2026-04-14-vllm-semantic-router-architecture.md
│   ├── 2026-05-04-vllm-request-lifecycle.md
│   ├── 2026-05-11-parallelism-tp-fsdp-zero.md
│   ├── 2026-05-16-deepseek-v4-flash-ascend.md
│   └── 2026-05-22-layernorm-rmsnorm-geometry.md
└── _sass/
    └── layout/
        └── _tech-blog.scss
```

如果后续文章数量增多，可以再升级为自定义 collection：

```yml
collections:
  blog:
    output: true
    permalink: /tech-blog/:path/
```

第一版不建议马上上 collection，因为当前站点还没有文章体系，使用 `_posts/` 更直接。

## 6. Front Matter 规范

每篇文章建议使用如下模板：

```yml
---
layout: single
title: "Coding Agent 不是一个接口：分层、RunStore、工作流与自动修复闭环"
date: 2026-03-26
categories:
  - tech-blog
  - agent-engineering
tags:
  - Coding Agent
  - Workflow
  - RunStore
  - FastAPI
excerpt: "从一次性生成接口升级为生成、验证、修复、再验证的工程闭环。"
source_log:
  - "Renyuan_Log.md:914-1091"
---
```

字段约定：

- `categories` 第一项固定为 `tech-blog`。
- 第二项为系列 slug。
- `tags` 使用 3-6 个，避免过多。
- `excerpt` 控制列表页摘要。
- `source_log` 用于追溯原始日志行号，不一定在公开页面展示。

## 7. 第一版文章清单

### 7.1 Agent Engineering 系列

#### 1. Coding Agent 不是一个接口：分层、RunStore、工作流与自动修复闭环

- 融合日期：2025-03-25、2026-03-26
- 原始依据：`Renyuan_Log.md:914-1091`
- 核心主线：从一次性 `/generate` 升级为多轮 `生成 -> 验证 -> 读错误 -> patch -> 再验证`。
- 建议结构：
  - 背景：为什么一次性 LLM 生成不稳定。
  - 三层架构：API 层、Agent 编排层、工具与基础设施层。
  - 数据模型：Run、RunEvent、Artifact。
  - 工作流：generate_only、generate_validate、generate_save_oss、generate_save_deploy_fc。
  - 自动修复回路：失败日志、上下文选择、patch、再次验证。
  - 阶段性取舍：复杂方案到 `/runs` 简化方案。
- 标签：`Coding Agent`、`Workflow`、`RunStore`、`FastAPI`、`Auto Fix`
- 发布优先级：P0

#### 2. Agent 前端如何展示过程：SSE、JSONL、文件树、代码预览与安全状态

- 融合日期：2026-03-28、2026-03-30、2026-04-02
- 原始依据：`Renyuan_Log.md:1171-1313`、`1397-1419`、`1457-1459`
- 核心主线：从“等待最终结果”改成实时可观察的 Agent 生成体验。
- 建议结构：
  - 用户体验问题：生成过程黑盒。
  - API 设计：`POST /generate/jobs`、`GET /stream`、`GET /result`。
  - SSE 事件：`job.created`、`thinking.status`、`project.tree`、`file.snapshot`、`preview.code`、`job.completed`。
  - 安全边界：不暴露原始 reasoning，只展示阶段摘要。
  - 前端状态：文件树、代码预览、任务状态。
- 标签：`SSE`、`JSONL`、`Agent UX`、`FastAPI`、`Streaming`
- 发布优先级：P0

#### 3. 把 OnlySpecs 接入 Workshop：从 Electron Coding Agent 到 Web 低代码生成器

- 融合日期：2025-03-20 至 2025-03-22
- 原始依据：`Renyuan_Log.md:59-128`、`139-313`
- 核心主线：理解 OnlySpecs 的 Electron / IPC / node-pty / Claude CLI 架构，并通过 FastAPI 做 Web 集成。
- 建议结构：
  - 原始项目结构：Electron UI、Renderer、IPC、Main Process。
  - 接入目标：让 Web 平台调用 Coding Agent。
  - 技术障碍：pty 交互、Claude CLI、SSE、ZIP。
  - 方案演化：无头 API、历史任务、下载入口。
  - 复盘：如何判断开源项目能否被改造成服务。
- 标签：`OnlySpecs`、`Claude CLI`、`FastAPI`、`SSE`、`Low Code`
- 发布优先级：P1

#### 4. Workshop 云端运行架构：OSS、FC 容器、Docker 镜像与本地验证闭环

- 融合日期：2025-03-23 至 2025-03-24、2025-03-25、2026-03-26、2026-03-30
- 原始依据：`Renyuan_Log.md:437-459`、`547-692`、`767-806`、`1348-1394`
- 核心主线：生成的项目如何从文件变成可预览服务。
- 建议结构：
  - 端到端链路：prompt -> Claude -> OSS -> scripts -> HTTP service -> iframe。
  - Docker 基础镜像：Node、Python、Fullstack。
  - FC 容器运行约束。
  - 本地验证闭环：prepare/build/start/health probe。
  - 真实问题：端口冲突、代理、workspace 路径、脚本约束。
- 标签：`Docker`、`OSS`、`Function Compute`、`Deployment`、`Sandbox`
- 发布优先级：P1

#### 5. 从 opencode 到 Agent-Do：Workshop MVP 的瘦身重构

- 融合日期：2026-04-01 至 2026-04-03
- 原始依据：`Renyuan_Log.md:1425-1439`、`1457-1484`、`1522-1539`
- 核心主线：从深度改造大项目回到更可控的 MVP。
- 建议结构：
  - 为什么直接植入 opencode 成本高。
  - Agent-Do 的 MVP 边界。
  - Docker CLI、workspace 挂载、空项目兜底。
  - 复盘：复杂系统改造时如何判断“该删掉什么”。
- 标签：`Agent-Do`、`MVP`、`Docker`、`Refactor`
- 发布优先级：P2

### 7.2 LLM Routing 系列

#### 6. LLM Router 的设计空间：从难度感知到级联系统

- 融合日期：2026-04-07、2026-04-08
- 原始依据：`Renyuan_Log.md:1570-1620`、`1631-1653`
- 核心主线：把 LLM Router 的研究路线整理成可理解的设计空间。
- 建议结构：
  - 决策时机：pre-generation、post-generation、多阶段。
  - 使用信号：query、metadata、response、logprobs、verifier。
  - 计算方式：规则、分类器、聚类、自适应策略。
  - 六类路线：difficulty-aware、preference-aligned、clustering、RL、uncertainty、cascade。
  - 复现优先级：AutoMix、FrugalGPT、BEST-Route、GraphRouter、CP-Router。
- 标签：`LLM Router`、`Survey`、`Cascade`、`Uncertainty`
- 发布优先级：P1

#### 7. RouteLLM 复现笔记：从 GSM8K 生成到评测可视化

- 融合日期：2026-04-08、2026-04-09
- 原始依据：`Renyuan_Log.md:1673-1689`、`1695-1709`
- 核心主线：RouteLLM strong/weak model 路由链路跑通，并在 GSM8K 上比较策略效果。
- 建议结构：
  - 复现目标。
  - smoke test。
  - 修复点：路径、OPENAI_API_KEY、输出目录、评测脚本。
  - 策略对比：Random、Weak、Strong、Causal_LLM、MF、BERT/SW_Ranking。
  - 成本-准确率权衡。
- 标签：`RouteLLM`、`GSM8K`、`Evaluation`、`Cost`
- 发布优先级：P1

#### 8. 如何搭建一个 Router Evaluation Pipeline

- 融合日期：2026-04-10、2026-04-13
- 原始依据：`Renyuan_Log.md:1715-1755`、`1904-1963`
- 核心主线：把 llmrouter 的离线评测链路抽象成可复用工程方法。
- 建议结构：
  - 数据合并与切分。
  - 全模型 benchmark。
  - tier 标签与监督数据。
  - classifier / cascade / semantic-router 接入。
  - metrics：accuracy、cost、latency、P99。
  - 离线模拟的优点与缺陷。
- 标签：`LLM Router`、`Benchmark`、`Offline Simulation`、`Pipeline`
- 发布优先级：P0

#### 9. Semantic Router 实验：为什么 Override 形态优于五路 Tiered 路由

- 融合日期：2026-04-10、2026-04-11、2026-04-13
- 原始依据：`Renyuan_Log.md:1730-1772`、`1780-1846`、`1904-1963`
- 核心主线：实验显示 route 形态、数据分布、threshold 比工具名更关键。
- 关键结论：
  - `32B 默认 + 14B override + MPNet + metadata` 达到 `79.61% / 97.2%`。
  - `14B 默认 + 7B override + MPNet + metadata` 达到 `76.28% / 38.6%`。
  - 旧的五路 tiered semantic-router 在同等成本下被 override 方案压制。
- 建议结构：
  - semantic-router 被理解为检索式分类器。
  - 五路 tiered 的问题。
  - override 方案的直觉。
  - metadata、MPNet、threshold 的作用。
  - 成本约束下的最优候选。
- 标签：`semantic-router`、`MPNet`、`Threshold`、`Cost-Accuracy`
- 发布优先级：P0

#### 10. vLLM Semantic Router 架构拆解：从分类器到 LLM 流量控制平面

- 融合日期：2026-04-14、2026-04-22
- 原始依据：`Renyuan_Log.md:2007-2125`、`2273-2307`
- 核心主线：vLLM Semantic Router 不是单一分类器，而是 LLM 流量控制平面。
- 建议结构：
  - 定位：多模型系统的路由与运行控制层。
  - 分层：Signals、Projections、Decisions、Algorithms、Plugins。
  - 配置：canonical YAML、listeners、providers、routing、global。
  - 运行：Envoy extproc、OpenAIRouter、request headers/body、response filters。
  - 实跑结论：当前配置能按请求类型分流，但单 `modelRef` 下还不是真正的多模型选择。
- 标签：`vLLM Semantic Router`、`Control Plane`、`Envoy`、`Model Selection`
- 发布优先级：P0

### 7.3 LLM Serving & Deployment 系列

#### 11. vLLM V1 工程边界：一条请求如何从 API 走到 PagedAttention

- 融合日期：2026-04-30、2026-05-04、2026-05-12
- 原始依据：`Renyuan_Log.md:2578-2584`、`2607-2642`、`3016-3020`
- 核心主线：读 vLLM 不应从 kernel 开始，而应先看 serving runtime 的边界。
- 建议结构：
  - 为什么选择 vLLM / vLLM-Ascend / SGLang-Ascend / xLLM 对比。
  - vLLM 目录地图。
  - LLMEngine、EngineCore、Scheduler、KVCacheManager、ModelRunner。
  - 一次请求如何被推进。
  - continuous batching、KV cache、PagedAttention。
- 标签：`vLLM`、`Serving`、`KV Cache`、`PagedAttention`
- 发布优先级：P0

#### 12. 大模型并行的最小闭环：集合通信、TP、FSDP/ZeRO-3 到权重分片

- 融合日期：2026-05-01、2026-05-05、2026-05-11
- 原始依据：`Renyuan_Log.md:2595-2604`、`2647-2814`、`2831-3011`
- 核心主线：从通信原语推到线性层切分，再区分训练和推理并行。
- 建议结构：
  - Gather、Reduce、AllReduce、Broadcast、Scatter。
  - 分层 AllReduce 与 SHARP。
  - ColumnParallelLinear 与 RowParallelLinear。
  - FSDP / ZeRO-3 vs Tensor Parallel。
  - `narrow`、`offset`、权重分片侧栏。
- 标签：`Tensor Parallel`、`FSDP`、`ZeRO-3`、`AllReduce`、`Megatron`
- 发布优先级：P1

#### 13. DeepSeek V4 Flash on Ascend：一次 vLLM-Ascend 部署复盘

- 融合日期：2026-05-13 至 2026-05-16
- 原始依据：`Renyuan_Log.md:3023-3055`、`3069-3075`、`3083-3111`、`3114-3248`
- 核心主线：按“资源评估 -> 失败路径 -> 成功配置 -> 可复用经验”组织部署复盘。
- 必须注意：
  - 2026-05-15 阶段判断需要 32 NPU。
  - 2026-05-16 最终验证单节点 16 NPU 可以跑通。
  - 正式文章中要明确这是结论修正。
  - 公开版本必须脱敏内部 IP、任务 ID、队列名、私有路径。
- 建议结构：
  - 模型版本与资源盘点。
  - W8A8 / BF16 / Pro 差异。
  - 镜像兼容问题。
  - patch、tool parser、MTP、OOM、KV cache bug。
  - 最终可用配置。
  - 可复用排障表。
- 标签：`DeepSeek V4 Flash`、`vLLM-Ascend`、`Ascend 910`、`NPU`、`Deployment`
- 发布优先级：P0

#### 14. NPU 集群调度实战：Kubernetes + Volcano + ktp 如何影响推理服务

- 融合日期：2026-05-13、2026-05-16
- 原始依据：`Renyuan_Log.md:3043-3052`、`3131-3148`、`3207-3239`、`3250-3310`
- 核心主线：模型起不来不一定是模型问题，也可能是调度、镜像、通信、共享存储问题。
- 建议结构：
  - K8s Cluster、Node、NPU、Queue。
  - Volcano 调度流程。
  - 16 NPU 节点粒度。
  - HCCL 初始化。
  - 镜像缓存与共享存储。
  - CPU/内存请求对调度的影响。
- 标签：`Kubernetes`、`Volcano`、`ktp`、`HCCL`、`NPU`
- 发布优先级：P1

### 7.4 CUDA / Triton / Kernel Notes 系列

#### 15. 从写循环到写映射：CUDA kernel 如何接上 LLM 优化

- 融合日期：2026-04-26、2026-04-28、2026-05-16、2026-05-17
- 原始依据：`Renyuan_Log.md:2310-2389`、`2411-2470`、`3312-3384`、`3386-3497`
- 核心主线：从 CUDA 执行模型建立到 shared memory / reduction 的优化直觉。
- 建议结构：
  - CPU 写循环 vs GPU 写映射。
  - Grid、Block、Warp、Thread。
  - memory hierarchy。
  - `cudaMemcpy` vs `cudaMallocManaged`。
  - shared memory 数据映射。
  - kernel vs device function。
  - warp-level / block-level reduction。
  - Grid-Stride Loop。
- 标签：`CUDA`、`Kernel`、`Shared Memory`、`Reduction`
- 发布优先级：P0

#### 16. 融合算子的学习路线：为什么 fused softmax 不是“把函数写一起”

- 融合日期：2026-05-17、2026-05-20、2026-05-21
- 原始依据：`Renyuan_Log.md:3427-3497`、`3501-3508`、`3512-3537`
- 脱敏要求：只抽取 fused softmax、算子融合、规约和内存读写主题，不保留会议链接、会议密码、课程参与者姓名或内部安排。
- 核心主线：融合算子的核心是减少中间结果写回 global memory，而不只是把表达式合并。
- 建议结构：
  - softmax 与 element-wise 的组合。
  - global memory 中间结果消除。
  - block 划分。
  - block 内规约与跨 block 规约。
  - fused-softmax、relu(softmax)、softmax dropout 的共同模式。
- 标签：`Operator Fusion`、`Softmax`、`Triton`、`Memory Bandwidth`
- 发布优先级：P2

#### 17. LayerNorm vs RMSNorm：从几何自由度到 Triton kernel 成本

- 融合日期：2026-05-22，少量连接 2026-05-21
- 原始依据：`Renyuan_Log.md:3514-3537`、`3539-3596`
- 核心主线：用几何自由度解释归一化差异，再落到 kernel 成本。
- 建议结构：
  - RMSNorm：完整超球面，自由度 `M-1`。
  - LayerNorm：超球面与过球心超平面的交集，自由度 `M-2`。
  - 三维例子。
  - 损失的信息：长度 vs 长度 + 平移基准。
  - Triton 成本：平方和累加器 vs 均值 + 方差两个累加器。
- 标签：`LayerNorm`、`RMSNorm`、`Triton`、`Geometry`
- 发布优先级：P0

### 7.5 Transformer Foundations 系列

#### 18. RoPE 的几何直觉与代码实现

- 融合日期：2026-04-17、可补 2026-04-29
- 原始依据：`Renyuan_Log.md:2137-2252`、`2475-2573`
- 核心主线：把 RoPE 从二维旋转平面讲到代码里的 `rearrange / unbind / stack`。
- 建议结构：
  - `D` 维向量拆成 `D/2` 个二维平面。
  - 高频与低频。
  - 方向编码与长度不变。
  - shape flow：`(B,H,S,64) -> (B,H,S,32,2) -> ... -> (B,H,S,64)`。
  - NTK-aware / YaRN 可作为长上下文补充。
- 标签：`RoPE`、`Position Encoding`、`Transformer`、`PyTorch`
- 发布优先级：P1

#### 19. 从 CS336 作业理解 Transformer 训练基本功

- 融合日期：2026-04-11、2026-04-12、2026-04-13
- 原始依据：`Renyuan_Log.md:1850-1869`、`1875-1898`、`1967-2001`
- 核心主线：把 activation checkpointing、Linear/einsum、权重矩阵布局、FP32/FP16/BF16 串起来。
- 注意：原文标题里的“参数矩阵 Checkpoint”更像 activation checkpointing，成文时应修正术语。
- 标签：`CS336`、`Transformer`、`BF16`、`einsum`
- 发布优先级：P2

#### 20. Encoder 输出 Z 矩阵到底去了哪里：从 Memory 到 K/V

- 融合日期：2026-04-20
- 原始依据：`Renyuan_Log.md:2258-2266`
- 核心主线：Encoder 输出作为 Decoder cross-attention 的 memory，并被投影为 K/V。
- 建议：素材较短，优先并入 Attention 基础文章或 RoPE 文章的背景部分。
- 标签：`Attention`、`Encoder`、`KV Cache`
- 发布优先级：P3

## 8. 第一版发布范围

为了尽快上线，同时保证质量，第一版建议只发布 10 篇左右。

### P0 必发

1. `Coding Agent 不是一个接口：分层、RunStore、工作流与自动修复闭环`
2. `Agent 前端如何展示过程：SSE、JSONL、文件树、代码预览与安全状态`
3. `如何搭建一个 Router Evaluation Pipeline`
4. `Semantic Router 实验：为什么 Override 形态优于五路 Tiered 路由`
5. `vLLM Semantic Router 架构拆解：从分类器到 LLM 流量控制平面`
6. `vLLM V1 工程边界：一条请求如何从 API 走到 PagedAttention`
7. `DeepSeek V4 Flash on Ascend：一次 vLLM-Ascend 部署复盘`
8. `从写循环到写映射：CUDA kernel 如何接上 LLM 优化`
9. `LayerNorm vs RMSNorm：从几何自由度到 Triton kernel 成本`

### P1 可选

1. `把 OnlySpecs 接入 Workshop：从 Electron Coding Agent 到 Web 低代码生成器`
2. `Workshop 云端运行架构：OSS、FC 容器、Docker 镜像与本地验证闭环`
3. `LLM Router 的设计空间：从难度感知到级联系统`
4. `RouteLLM 复现笔记：从 GSM8K 生成到评测可视化`
5. `大模型并行的最小闭环：集合通信、TP、FSDP/ZeRO-3 到权重分片`
6. `RoPE 的几何直觉与代码实现`

### P2/P3 暂缓

- `从 opencode 到 Agent-Do：Workshop MVP 的瘦身重构`
- `融合算子的学习路线：为什么 fused softmax 不是“把函数写一起”`
- `从 CS336 作业理解 Transformer 训练基本功`
- `Encoder 输出 Z 矩阵到底去了哪里：从 Memory 到 K/V`

## 9. 页面视觉与交互规划

### 9.1 页面风格

原则：

- 紧凑、清晰、技术博客优先。
- 不做大面积渐变、装饰图、营销 hero。
- 不使用多层嵌套卡片。
- 继承站点已有字体、颜色变量和暗色模式。
- 卡片只用于文章条目和系列条目。

### 9.2 布局

桌面端：

```text
Tech Blog 标题区
主题入口 chips / tabs
Featured Posts 2 列
Series Overview 2 列
All Posts 单列列表
Timeline 单列压缩列表
```

移动端：

```text
Tech Blog 标题区
主题入口横向换行
Featured Posts 单列
Series Overview 单列
All Posts 单列
Timeline 单列
```

### 9.3 文章列表条目

每个文章条目包含：

- 标题
- 日期
- 系列
- 摘要
- 标签
- `Read note` 链接

示例：

```html
<article class="tech-post-card">
  <p class="tech-post-card__meta">2026-04-14 · LLM Routing</p>
  <h2>vLLM Semantic Router 架构拆解</h2>
  <p>从 Signals、Projections、Decisions 到 Plugins，理解它为什么更像 LLM 流量控制平面。</p>
  <div class="tech-tags">
    <span>vLLM</span>
    <span>Router</span>
    <span>Control Plane</span>
  </div>
</article>
```

### 9.4 标签与筛选

第一版建议不要做复杂前端搜索。使用静态分组足够。

可选增强：

- 纯锚点筛选：`#agent-engineering`、`#llm-routing`。
- 标签页：`/tags/` 后续再做。
- 站内搜索不作为第一版目标。

## 10. 实施步骤

### Step 1: 新增导航入口

修改 `_config.yml`：

```yml
navigation:
  main:
    - title: "Experience"
      url: "#experience-renyuan"
    - title: "Publications"
      url: "#publications-renyuan"
    - title: "Awards"
      url: "#awards-renyuan"
    - title: "Conference"
      url: "#conference-renyuan"
    - title: "Misc."
      url: "#misc-renyuan"
    - title: "Tech Blog"
      url: "/tech-blog/"
```

如果导航栏过宽，可以考虑把 `Tech Blog` 放在 `Misc.` 前面，或把 `Conference` 缩短为 `Talks`。

### Step 2: 新建博客索引页

新建 `tech-blog.md`：

```markdown
---
permalink: /tech-blog/
title: "Tech Blog"
author_profile: true
---

页面内容使用 Liquid 遍历 `site.posts`，筛选 `categories` 包含 `tech-blog` 的文章。
```

### Step 3: 新建文章目录

创建 `_posts/`，先放 P0 文章。

文件名建议：

```text
2026-03-26-coding-agent-workflow.md
2026-03-28-agent-ux-sse-jsonl.md
2026-04-10-router-evaluation-pipeline.md
2026-04-11-semantic-router-override.md
2026-04-14-vllm-semantic-router-architecture.md
2026-05-04-vllm-request-lifecycle.md
2026-05-16-deepseek-v4-flash-ascend.md
2026-05-17-cuda-kernel-llm-optimization.md
2026-05-22-layernorm-rmsnorm-geometry.md
```

### Step 4: 添加博客样式

新增 `_sass/layout/_tech-blog.scss`，并在 `assets/css/main.scss` 中导入。

样式目标：

- `.tech-blog-hero`
- `.tech-series-grid`
- `.tech-post-grid`
- `.tech-post-card`
- `.tech-tags`
- `.tech-timeline`

### Step 5: 从日志抽取并重写文章

不要直接复制 `Renyuan_Log.md` 原文。

每篇文章处理顺序：

1. 抽取相关日期段落。
2. 删除个人碎片、内部细节、重复命令。
3. 按“问题 -> 背景 -> 方法 -> 结果 -> 复盘”重写。
4. 保留必要表格和架构图。
5. 添加摘要和标签。
6. 最后检查脱敏。

### Step 6: 本地构建验证

优先尝试：

```bash
bundle exec jekyll build
```

如果当前环境没有 Gemfile 或 bundle 环境，则尝试：

```bash
jekyll build
```

检查项：

- `/tech-blog/` 是否可访问。
- 导航链接是否正确。
- 文章 permalink 是否正确。
- 首页原锚点是否仍然正常。
- 移动端导航是否溢出。
- 暗色模式下卡片、标签、边框是否可读。

## 11. 脱敏规则

正式发布前必须执行以下检查：

### 11.1 必删或改写

- 内部 IP，例如 `10.x.x.x`。
- 任务 ID，例如具体集群任务编号。
- 队列名、用户名、项目队列。
- 私有路径，例如 `/models/share/...` 中不适合公开的部分。
- 会议链接、会议密码。
- 同事、管理员、课程参与者姓名、账号或内部组织身份。
- 任何 API key、token、AK/SK、代理地址。
- 内部服务器主机名和节点名。

### 11.2 可以保留但需抽象

- “单节点 16 NPU”
- “DP=2，TP=8”
- “vLLM-Ascend 镜像兼容问题”
- “需要 patch 注册模型架构”
- “CPU/内存请求影响调度”

### 11.3 DeepSeek 部署文章特殊处理

原始日志中包含大量真实路径和资源信息。公开版本应改成：

- `internal cluster`
- `shared model path`
- `verified vLLM-Ascend image`
- `cluster job id`
- `project queue`
- `private patch path`

同时保留技术结论，不暴露环境细节。

## 12. 日期与事实一致性

日志中存在一个需要确认的日期问题：

- 早期日志从 `2025-03-19` 到 `2025-03-25`。
- 随后跳到 `2026-03-26`。

如果前面 7 天其实是 2026 年，应在整理文章时统一修正。如果不能确认，则按原文保留，并在 `source_log` 中记录原始日期。

另外，DeepSeek 部署链路存在阶段性结论修正：

- 2026-05-15 附近曾判断需要 32 NPU。
- 2026-05-16 最终验证单节点 16 NPU 可运行。

正式文章应明确这是调试过程中的结论更新，而不是互相矛盾。

## 13. 质量验收标准

博客第一版完成时，应满足：

- 导航栏存在 `Tech Blog` 入口。
- `/tech-blog/` 有清晰文章索引。
- 至少 8 篇 P0 文章完成整理。
- 每篇文章都有 front matter、摘要、标签、来源行号。
- 内部敏感信息已脱敏。
- 页面在桌面和移动端不出现明显溢出。
- 暗色模式可读。
- Jekyll 构建通过。
- 原首页内容不受影响。

## 14. 后续扩展

第一版上线后可以继续扩展：

- 增加 `/tech-blog/agent-engineering/` 等系列页。
- 增加 `/tags/` 标签归档页。
- 增加“正在整理”的 Drafts 区域。
- 从 `Renyuan_Log.md` 自动生成 timeline 数据。
- 为架构类文章补 Mermaid 图或手绘图。
- 为 CUDA / Triton 文章补最小可运行代码片段。
- 为 Router 实验文章补结果图和表格。

## 15. 推荐执行顺序

1. 先完成博客框架：导航、索引页、样式。
2. 发布 3 篇最能代表技术方向的文章：
   - Coding Agent 工作流
   - vLLM Semantic Router 架构
   - DeepSeek V4 Flash 部署复盘
3. 再补齐 P0 文章。
4. 最后处理 P1/P2 文章和 timeline。

这样可以尽快让技术博客“可访问、可展示、可持续更新”，同时避免一次性整理全部日志导致质量下降。
