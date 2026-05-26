---
layout: single
title: "DeepSeek V4 Flash on Ascend：一次 vLLM-Ascend 部署复盘"
date: 2026-05-16
categories:
  - tech-blog
  - serving-deployment
series: "Serving & Deployment"
priority: P0
featured: true
tags:
  - DeepSeek V4 Flash
  - vLLM-Ascend
  - Ascend 910
  - NPU
  - Deployment
excerpt: "一次大模型部署排障复盘：资源评估、镜像兼容、patch、MTP、OOM、KV cache bug 和最终可用配置。"
source_log:
  - "Renyuan_Log.md:3023-3055"
  - "Renyuan_Log.md:3069-3075"
  - "Renyuan_Log.md:3083-3111"
  - "Renyuan_Log.md:3114-3248"
---

这次部署的目标是在 Ascend NPU 环境中跑通 DeepSeek V4 Flash W8A8。过程里出现过多个看似模型相关、实际分属不同层的问题：镜像、模型架构注册、工具解析器、投机解码、资源调度、KV cache。

本文只保留可公开的技术结论，内部地址、任务号、队列、私有路径均已抽象。

## 资源评估

部署前要先确认：

- 模型版本：Flash、Pro、W8A8、BF16 等差异。
- 并行方式：DP、TP、Expert Parallel。
- 单节点还是多节点。
- NPU 数量、CPU 核数、CPU 内存。
- 镜像是否包含对应模型架构和 parser。

阶段性判断曾认为需要 32 NPU，但最终验证表明：在正确镜像和 patch 下，单节点 16 NPU 可以跑通。

## 失败路径

典型问题包括：

1. 模型架构不被 transformers 识别。
2. `tool-call-parser` 不支持目标模型类型。
3. MTP speculative config 与镜像版本不匹配。
4. 单节点 OOM。
5. 双节点调度失败。
6. 跨节点 KV cache 初始化 bug。
7. 不同镜像工作目录不一致。
8. 镜像在节点上没有缓存，导致任务长时间 Pending。

这些问题分属不同层。把它们都归因于“模型起不来”会误导排查。

## 最终经验

可复用经验是：

- 使用验证过的 vLLM-Ascend 镜像。
- 启动前应用对应模型架构 patch。
- 优先复用已验证的单节点配置。
- 明确 DP、TP 和 Expert Parallel 的组合。
- CPU 内存和 CPU 核数会影响调度，不只是 NPU 数量重要。

这篇复盘的核心不是某个命令，而是排障分层：模型兼容、镜像能力、资源调度、并行配置、运行时 bug 必须分开判断。

## 知识补全：大模型部署排障的四张表

部署大模型时，建议始终维护四张表。

第一张是模型表：模型类型、参数量、量化方式、上下文长度、是否 MoE、是否需要特殊 tokenizer、是否需要自定义模型架构注册。

第二张是镜像表：transformers 版本、vLLM 版本、vLLM-Ascend 版本、tool parser、reasoning parser、speculative decoding 支持情况。

第三张是资源表：NPU 数量、每卡显存、CPU 核数、CPU 内存、单节点/多节点、队列配额。

第四张是错误表：报错、发生阶段、可能层级、尝试方案、最终结论。

这四张表能防止排障过程变成“换镜像试一下”。每次失败都应归到模型、镜像、资源、调度或运行时 bug 中的一类。

## 学习检查清单

复盘部署时，至少应回答：

1. 最终可用配置是什么。
2. 哪些失败路径被验证无效。
3. 哪些结论是阶段性误判，后续被修正。
4. 哪些环境细节不能公开。
5. 下一步性能测试应测吞吐、延迟、显存还是稳定性。

这能把一次部署经历沉淀成可复用知识，而不是只留下一组命令。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-05-13](#source-log-2026-05-13) | 3023-3068 | DeepSeek V4 Flash 资源评估 |
| [2026-05-14](#source-log-2026-05-14) | 3069-3082 | DeepSeek V4 环境手动配置 |
| [2026-05-15](#source-log-2026-05-15) | 3083-3113 | DeepSeek V4 启动阻塞定位 |
| [2026-05-16](#source-log-2026-05-16) | 3114-3385 | DeepSeek V4 Flash 单节点跑通与 NPU 调度 |

<a id="source-log-2026-05-13"></a>
### Source Log: 2026-05-13

Source lines: `Renyuan_Log.md:3023-3068`

<pre class="tech-log-source"><code>
3023 |# 2026-05-13
3024 |
3025 |## 尝试启动 DeepSeek V4 Flash 的推理服务
3026 |
3027 |
3028 |## 1. 可用模型与硬件资源
3029 |
3030 |### 可用模型版本（/models/share/）
3031 |
3032 || 模型 | 路径 | 量化/精度 | 架构 | 推理框架 | 最低 NPU 需求 | 能否直接跑 |
3033 ||------|------|----------|------|---------|-------------|-----------|
3034 || **DeepSeek-V4-Flash (W8A8)** | `DeepSeek-V4-Flash-w8a8-mtp/` | W8A8 Ascend 量化 | 43层/4096d/256专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
3035 || **DeepSeek-V4-Flash (compressed-tensors)** | `deepseek-v4-flash-mtp/` | W8A8 compressed-tensors | 同上 | vLLM-Ascend | 32 NPU (2节点x16) | 改 MODEL_PATH + quantization 参数即可 |
3036 || DeepSeek-V4-Flash (BF16) | `DeepSeek-V4-Flash-bf16/` | BF16 原始精度 | 同上 | 自研 NPU 推理脚本 | 1 NPU（单卡验证） | adaption_test/ 下有 quick_verify.py |
3037 || **DeepSeek-V4-Pro** | `DeepSeek-V4-Pro-w4a8-mtp/` | W4A8 Ascend 量化 | 61层/7168d/384专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
3038 || DeepSeek-R1-Distill-Qwen-1.5B | `DeepSeek-R1-Distill-Qwen-1.5B/` | BF16 | Qwen2 28层/1536d | vLLM-Ascend | 1 NPU | 有现成 yaml，直接跑 |
3039 || DeepSeek-V4-Flash-Base (BF16) | `DeepSeek-V4-Flash-Base-bf16/` | BF16 | 同 Flash | 无推理脚本 | — | 不适合评测（base 模型，无 instruct 对齐） |
3040 |
3041 |所有 V4 模型均为 MoE 架构，支持最大 1M token 上下文（max_position_embeddings=1048576），使用 YaRN RoPE 扩展。
3042 |
3043 |### 可用 NPU 资源
3044 |
3045 || 队列 | 类型 | 配额 (NPU) | 物理规格 | 状态 |
3046 ||------|------|-----------|---------|------|
3047 || user-1-wangakang-compute | 个人 | 8 | 8卡 x 2chip = 16 Ascend910 chip | ok |
3048 || project-ascend-fit-wangakang | 项目 | 52 | 52卡 x 2chip = 104 Ascend910 chip | ok |
3049 |
3050 |硬件说明：每张 Ascend910 物理卡包含 2 个 AI 处理器（chip），每 chip 64GB HBM。ktp 调度以&quot;NPU&quot;（物理卡）为单位。vLLM 的 `--tensor-parallel-size` 等参数也以 NPU（卡）为单位。
3051 |
3052 |总计可用：**60 NPU**（个人 8 + 项目 52）。
3053 |
3054 |尝试使用镜像启动：镜像拉取失败。&#32;&#32;
3055 |尝试手动配置。
3056 |
3057 |## 河套学院晟腾课程
3058 |
3059 |### 关于 Linux 命令操作 ...
3060 |
3061 |在我们的个人 docker 运行实验
3062 |
3063 |### Kerminal 自动适配部署大模型&#32;
3064 |
3065 |跑了90分钟，最后还是成功了！&#32;
3066 |
3067 |
3068 |
</code></pre>


<a id="source-log-2026-05-14"></a>
### Source Log: 2026-05-14

Source lines: `Renyuan_Log.md:3069-3082`

<pre class="tech-log-source"><code>
3069 |# 2026-05-14
3070 |
3071 |## 手动配置一天的 DeepSeek V4 环境
3072 |
3073 |各种包依赖、环境冲突、未更新问题&#32;&#32;
3074 |最棘手的是环境不支持&#32;&#32;
3075 |
3076 |## 结束所有 LeetGPU Easy 题目！
3077 |
3078 |感觉还行。&#32;&#32;
3079 |但是 Medium 题目一下就难起来了。&#32;&#32;
3080 |
3081 |
3082 |
</code></pre>


<a id="source-log-2026-05-15"></a>
### Source Log: 2026-05-15

Source lines: `Renyuan_Log.md:3083-3113`

<pre class="tech-log-source"><code>
3083 |# 2026-05-15
3084 |
3085 |## 河套学院晟腾课程
3086 |
3087 |使用 Kerminal 写算子。&#32;&#32;
3088 |讨论了关于文件目录。&#32;&#32;
3089 |
3090 |### 讨论了部署需求
3091 |
3092 |- **Flash (W8A8)**: 2 节点 x 16 NPU = 32 NPU（TP=8, DP=2, Expert Parallel）— **最低要求，不可降低**
3093 |- **Pro (W4A8)**: 2 节点 x 16 NPU = 32 NPU（TP=16, DP=2, Expert Parallel）
3094 |- **R1-Distill-1.5B**: 1 NPU 即可
3095 |- **Flash BF16 单卡验证**: 1 NPU（adaption_test，max_seq_len=2048）
3096 |
3097 |注意：经实测验证，Flash W8A8 模型在单节点 16 NPU 上无论 TP=8+DP=2 还是 TP=16 均会 OOM。必须使用双节点 32 NPU 部署。当集群只有一个 16-NPU 节点空闲时无法启动。
3098 |
3099 |项目队列 52 NPU 足够同时部署 Flash + 留余量做其他实验。
3100 |
3101 |
3102 |## 尝试使用现有配置启动 DS v4
3103 |
3104 |### 当前阻塞问题（2026-05-16）
3105 |
3106 |经过多轮实测，发现以下问题：
3107 |
3108 |1. **镜像兼容性**：`qwen3_5-v0-a3` 镜像的 transformers 不认识 `deepseek_v4` 架构，必须用 `deepseekv4-a3` 镜像
3109 |2. **单节点 OOM**：16 NPU 单节点无论 TP=8+DP=2 还是 TP=16 均 OOM，必须双节点
3110 |3. **vLLM-Ascend bug**：双节点 DP=2 跨节点部署时，worker 在 KV cache 初始化阶段报 `AttributeError: &#x27;list&#x27; object has no attribute &#x27;merge&#x27;`（kv_cache_spec_values 类型错误）
3111 |
3112 |
3113 |
</code></pre>


<a id="source-log-2026-05-16"></a>
### Source Log: 2026-05-16

Source lines: `Renyuan_Log.md:3114-3385`

<pre class="tech-log-source"><code>
3114 |# 2026-05-16
3115 |
3116 |## DeepSeek V4 Flash W8A8 部署总结
3117 |
3118 |### 今日结论
3119 |
3120 |- 任务 1058 已成功启动，服务地址为 `http://10.250.193.147:8005`。
3121 |- 当前唯一验证过的可用配置是 cdy 的原版配置：`/models/share/task/cdy/deepseek-v4-flash.yaml`。
3122 |- 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
3123 |- 启动前必须在 `/vllm-workspace/vllm` 中应用 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
3124 |- 单节点 16 NPU 可以跑通 DeepSeek V4 Flash W8A8，配置为 DP=2、TP=8、Expert Parallel。
3125 |- CPU 内存需要 1000Gi，CPU 需要 500 核。
3126 |
3127 |### 立即可做
3128 |
3129 |按照 `deepseek-v4-reasoning-eval.md` 中的测试矩阵，继续进行 DeepSeek V4 Flash 性能测试。
3130 |
3131 |### 后续学习任务
3132 |
3133 |1. **服务器 NPU 资源调度**
3134 |
3135 |   管理员解释：提交任务后，调度系统会分配空闲节点。每个节点有 16 张 910 显卡，不同节点已有的镜像缓存不同，这会影响是否需要重新拉镜像。
3136 |
3137 |   后续需要进一步理解服务器节点运行方式、节点间通信和并行配置。可参考：
3138 |
3139 |   - 网络基础说明：https://lqhl.github.io/scaling-book/gpus/#%E7%BD%91%E7%BB%9C
3140 |   - 配置脚本：`/models/share/task/cdy/start_dsv4.sh`
3141 |   - 本文档附录中的 NPU 集群调度方案
3142 |
3143 |2. **服务器集群镜像系统**
3144 |
3145 |   关于“镜像拉取慢”的问题，需要学习服务器集群的镜像系统：https://luoss.nilpo.app/guide/image-storage。
3146 |
3147 |   管理员建议先上传镜像到公开镜像池。上传完成后，服务器内部拉取镜像和模型权重都会明显变快：拉镜像约 10 秒，否则可能需要 10 分钟以上。
3148 |
3149 |### 后续优化方向
3150 |
3151 |1. 管理员提到自己曾跑通过 SGLang，后续可以尝试用 SGLang 启动 DeepSeek V4 Flash。
3152 |
3153 |2. 管理员提到开源项目 [DFlash: Block Diffusion for Flash Speculative Decoding](https://github.com/z-lab/dflash)。该项目能显著提高解码速度，但目前似乎只能本机运行，不一定适合直接对外提供推理服务。后续可以考虑基于它改进 vLLM / SGLang 框架。
3154 |
3155 |## 最终成功配置
3156 |
3157 |**任务 1058**：使用 cdy 的原版配置成功启动。
3158 |
3159 || 项目 | 值 |
3160 || --- | --- |
3161 || yaml | `/models/share/task/cdy/deepseek-v4-flash.yaml` |
3162 || 镜像 | `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3` |
3163 || 节点 | atlas-19（单节点 16 NPU） |
3164 || 配置 | DP=2, TP=8, Expert Parallel |
3165 || 端口 | 8005 |
3166 || 模型名 | deepseek-v4-flash |
3167 || max_model_len | 524288 |
3168 || 关键步骤 | 启动前先 `git apply` patch 到 `/vllm-workspace/vllm` |
3169 |
3170 |## 这两天遇到的问题
3171 |
3172 |### 1. 镜像不支持 `deepseek_v4` 架构
3173 |
3174 |**现象**：`The checkpoint has model type deepseek_v4 but Transformers does not recognize this architecture`
3175 |
3176 |**原因**：`qwen3_5-v0-a3` 和 `deepseekv4-a3` 镜像中的 transformers 库版本不包含 `deepseek_v4` 模型类型注册。
3177 |
3178 |**解决方案**：使用 `v0.13.0rc3-a3` 镜像 + cdy 脚本中的 `git apply` patch。patch 位于 `/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`，它会修改 vLLM 代码，注册 `deepseek_v4` 相关组件。该镜像中的 vLLM 版本（v0.13）对 `model_type` 的检查逻辑与新版不同，patch 后即可通过。
3179 |
3180 |### 2. `tool-call-parser deepseek_v4` 不支持
3181 |
3182 |**现象**：`invalid tool call parser: deepseek_v4`
3183 |
3184 |**原因**：`qwen3_5-v0-a3` 镜像的 vLLM 版本（v0.16.0rc2）不包含 `deepseek_v4` tool parser。
3185 |
3186 |**解决方案**：
3187 |
3188 |- 方案 A：使用 `v0.13.0rc3-a3` 镜像 + patch（cdy 方案，已验证）
3189 |- 方案 B：去掉 `--tool-call-parser` 和 `--reasoning-parser` 参数（性能测试不需要）
3190 |
3191 |### 3. `speculative-config deepseek_mtp` 不支持
3192 |
3193 |**现象**：`Unsupported speculative method: &#x27;mtp&#x27;`
3194 |
3195 |**原因**：`deepseekv4-a3` 镜像的 vLLM 版本不支持 MTP 投机解码。
3196 |
3197 |**解决方案**：去掉 `--speculative-config` 参数，或使用 `v0.13.0rc3-a3` 镜像（支持 MTP）。
3198 |
3199 |### 4. 单节点 16 NPU DP=2 TP=8 OOM（`deepseekv4-a3` 镜像）
3200 |
3201 |**现象**：Worker 进程被 terminated，报错 `WorkerProc was terminated`。
3202 |
3203 |**原因**：`deepseekv4-a3` 镜像的 vLLM 版本内存管理效率较低，DP=2 在单节点上 OOM。
3204 |
3205 |**解决方案**：使用 `v0.13.0rc3-a3` 镜像（vLLM v0.13 内存管理更高效），并分配 1000Gi CPU 内存。cdy 配置证明同样的 DP=2 TP=8 单节点 16 NPU 可以跑通。
3206 |
3207 |### 5. 双节点调度失败
3208 |
3209 |**现象**：Worker pod 一直 Pending，无法分配第二个 16-NPU 节点。
3210 |
3211 |**原因**：集群中空闲的 16-NPU 节点不足两个。
3212 |
3213 |**解决方案**：使用单节点配置（cdy 方案证明可行）。
3214 |
3215 |### 6. `deepseekv4-a3` 镜像双节点 KV cache bug
3216 |
3217 |**现象**：`AttributeError: &#x27;list&#x27; object has no attribute &#x27;merge&#x27;`
3218 |
3219 |**原因**：`deepseekv4-a3` 镜像中 vLLM-Ascend 的 KV cache 初始化代码在跨节点 DP 模式下有 bug。
3220 |
3221 |**解决方案**：不使用该镜像，改用 `v0.13.0rc3-a3` 镜像。跨节点 DP 模式相关配置还需要进一步学习，尤其是 `/models/share/task/cdy/start_dsv4pro-worker.sh` 中的参数。
3222 |
3223 |### 7. `cd vllm-ascend` 路径问题
3224 |
3225 |**现象**：`cd: vllm-ascend: No such file or directory`
3226 |
3227 |**原因**：不同镜像的工作目录不同。
3228 |
3229 |**解决方案**：cdy 的脚本直接 `cd &quot;$VLLM_REPO&quot;`（即 `/vllm-workspace/vllm`），不需要进入 `vllm-ascend`。
3230 |
3231 |### 8. 镜像拉取慢
3232 |
3233 |**现象**：Pod 长时间 Pending（10-20 分钟）。
3234 |
3235 |**原因**：`deepseekv4-a3` 和 `v0.13.0rc3-a3` 镜像在部分节点上没有缓存。
3236 |
3237 |**解决方案**：等待拉取完成，或多次提交，直到调度到已有缓存的节点。
3238 |
3239 |**管理员解决方案**：先上传镜像到公开镜像池，参考 https://luoss.nilpo.app/guide/image-storage。上传完成后，服务器内部拉取镜像和模型权重都会很快。
3240 |
3241 |## 关键经验
3242 |
3243 |1. 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
3244 |2. 必须先打 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
3245 |3. 单节点 16 NPU 可以跑，配置为 DP=2 TP=8，不需要双节点。
3246 |4. CPU 内存需要 1000Gi，200Gi / 800Gi 不够。参考管理员方案：`/models/share/task/cdy/deepseek-v4-flash.yaml` 第 17、18 行。
3247 |5. CPU 需要 500 核。
3248 |6. cdy 的脚本（管理员方案）是唯一验证过的可用配置，后续所有版本都应以此为基础。
3249 |
3250 |## 附录：NPU 集群现有调度方案
3251 |
3252 |本集群使用 **Kubernetes + Volcano 调度器** 管理 NPU 资源，并通过 `ktp` CLI 工具操作。
3253 |
3254 |### 层级结构
3255 |
3256 |```text
3257 |集群 (K8s Cluster)
3258 | └── 节点 (Node): atlas-1, atlas-18, atlas-19, atlas-39, atlas-40, atlas-41 ...
3259 |      └── 每个节点有 16 NPU（8 张物理卡 x 2 chip）
3260 |           └── 每张卡 64GB HBM
3261 |
3262 |用户通过 Queue（队列）获得 NPU 配额：
3263 | ├── 个人队列: user-1-wangakang-compute (8 NPU)
3264 | └── 项目队列: project-ascend-fit-wangakang (52 NPU)
3265 |```
3266 |
3267 |### 调度流程
3268 |
3269 |1. **提交任务**：执行 `ktp submit -f job.yaml`。yaml 中指定 queue、npu 数量、镜像和启动命令，任务类型为 `acjob`（Ascend Computing Job）。
3270 |2. **调度器分配节点**：Volcano 调度器根据队列配额和节点空闲情况分配资源，无法手动指定节点。请求 16 NPU 会分配一个完整节点；请求 32 NPU 需要两个空闲节点同时可用。
3271 |3. **Pod 创建**：每个 task 对应一个 Pod。Pod 运行在分配的节点上，并挂载 `/models/` 共享存储。平台会自动生成 `hccl.json`，Pod 内的 `init_env.sh` 等待该文件就绪后设置 `MASTER_IP` 等环境变量。
3272 |4. **分布式通信初始化**：单节点时，Pod 内所有 NPU 通过 HCCL（华为集合通信库）直接通信；多节点时，通过 `data-parallel-address`（`MASTER_IP`）跨节点 RPC 通信。
3273 |5. **任务生命周期**：状态流转为 Pending -&gt; Running -&gt; Succeeded / Failed。`resumable_training.enabled: true` 时，失败会自动重试（最多 `fault_retry_times` 次）；`max_runtime_minutes` 到期后自动终止。
3274 |
3275 |### yaml 配置与调度的关系
3276 |
3277 |```yaml
3278 |tasks:
3279 |  - name: master        # Pod 名称后缀
3280 |    replicas: 1         # 该角色的 Pod 数量
3281 |    cpu: &quot;500&quot;          # CPU 核数（影响调度，节点需有足够 CPU）
3282 |    memory: &quot;1000Gi&quot;    # 内存（影响调度，节点需有足够内存）
3283 |    npu: 16             # NPU 数量（决定分配几张卡/几个节点）
3284 |    command: &quot;...&quot;      # Pod 启动后执行的命令
3285 |  - name: worker        # 第二个 Pod（可选，用于多节点）
3286 |    replicas: 1
3287 |    npu: 16             # 又一个 16 NPU = 又一个完整节点
3288 |```
3289 |
3290 |### 常用操作
3291 |
3292 || 命令 | 作用 |
3293 || --- | --- |
3294 || `ktp queues` | 查看队列配额和使用情况 |
3295 || `ktp submit -f job.yaml` | 提交任务 |
3296 || `ktp list` | 列出所有任务 |
3297 || `ktp pods &lt;ID&gt;` | 查看任务的 Pod 状态和所在节点 |
3298 || `ktp logs &lt;ID&gt;` | 查看日志（默认最新 100 行） |
3299 || `ktp logs &lt;ID&gt; --follow` | 实时跟踪日志 |
3300 || `ktp stop &lt;ID&gt;` | 停止任务 |
3301 || `ktp restart &lt;ID&gt;` | 重启已停止的任务 |
3302 || `ktp watch &lt;ID&gt;` | 实时监控任务状态 |
3303 |
3304 |### 注意事项
3305 |
3306 |- 不能指定调度到哪个节点，只能靠调度器自动分配。
3307 |- 不同节点上可能缓存了不同版本的同名镜像（tag 相同但内容不同）。
3308 |- 请求的 NPU 数量决定了需要几个节点：8 NPU = 半个节点，16 NPU = 一个节点，32 NPU = 两个节点。
3309 |- 如果集群没有足够空闲节点，Pod 会一直 Pending。
3310 |- `/models/` 是所有节点共享的 NFS 存储，脚本和权重文件对所有 Pod 可见。
3311 |
3312 |## CUDA 编程实践：共享内存
3313 |
3314 |### 核心概念
3315 |
3316 |每个 Block 都有自己独立的共享内存。在 CUDA 中，下面这句声明的是块内私有共享内存：
3317 |
3318 |```cpp
3319 |extern __shared__ float sdata[];
3320 |```
3321 |
3322 |也就是说，Block 0、Block 1 和 Block 2 各自都有一份独立的 `sdata` 数组，它们互不干扰。
3323 |
3324 |在这个例子中：
3325 |
3326 |- `blockDim.x = 4`
3327 |- 每个 Block 的 `sdata` 长度都是 4
3328 |- 每个 Block 内部的索引都是 `[0, 1, 2, 3]`
3329 |
3330 |当程序执行到下面这一行时：
3331 |
3332 |```cpp
3333 |sdata[tid] = (i &lt; N) ? input[i] : 0.0f;
3334 |```
3335 |
3336 |每个线程会根据自己的局部 ID（`tid`）和全局 ID（`i`），把全局内存中的数据搬到自己 Block 的共享内存中。
3337 |
3338 |### 数据映射关系
3339 |
3340 |#### Block 0（`blockIdx.x = 0`）
3341 |
3342 || Thread | `tid` | 全局 `i` | 执行操作 |
3343 || --- | --- | --- | --- |
3344 || Thread 0 | 0 | 0 | `sdata[0] = input[0]`（1.0） |
3345 || Thread 1 | 1 | 1 | `sdata[1] = input[1]`（2.0） |
3346 || Thread 2 | 2 | 2 | `sdata[2] = input[2]`（3.0） |
3347 || Thread 3 | 3 | 3 | `sdata[3] = input[3]`（4.0） |
3348 |
3349 |此时 Block 0 的 `sdata` 为：
3350 |
3351 |```text
3352 |[1.0, 2.0, 3.0, 4.0]
3353 |```
3354 |
3355 |#### Block 1（`blockIdx.x = 1`）
3356 |
3357 || Thread | `tid` | 全局 `i` | 执行操作 |
3358 || --- | --- | --- | --- |
3359 || Thread 0 | 0 | 4 | `sdata[0] = input[4]`（5.0） |
3360 || Thread 1 | 1 | 5 | `sdata[1] = input[5]`（6.0） |
3361 || Thread 2 | 2 | 6 | `sdata[2] = input[6]`（7.0） |
3362 || Thread 3 | 3 | 7 | `sdata[3] = input[7]`（8.0） |
3363 |
3364 |此时 Block 1 的 `sdata` 为：
3365 |
3366 |```text
3367 |[5.0, 6.0, 7.0, 8.0]
3368 |```
3369 |
3370 |#### Block 2（`blockIdx.x = 2`）
3371 |
3372 || Thread | `tid` | 全局 `i` | 执行操作 |
3373 || --- | --- | --- | --- |
3374 || Thread 0 | 0 | 8 | `sdata[0] = input[8]`（9.0） |
3375 || Thread 1 | 1 | 9 | `sdata[1] = input[9]`（10.0） |
3376 || Thread 2 | 2 | 10 | `sdata[2] = input[10]`（11.0） |
3377 || Thread 3 | 3 | 11 | `sdata[3] = input[11]`（12.0） |
3378 |
3379 |此时 Block 2 的 `sdata` 为：
3380 |
3381 |```text
3382 |[9.0, 10.0, 11.0, 12.0]
3383 |```
3384 |
3385 |
</code></pre>

<!-- source-log-coverage:end -->
