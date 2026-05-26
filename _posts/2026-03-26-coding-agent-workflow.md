---
layout: single
title: "Coding Agent 不是一个接口：分层、RunStore、工作流与自动修复闭环"
date: 2026-03-26
categories:
  - tech-blog
  - agent-engineering
series: "Agent Engineering"
priority: P0
featured: true
tags:
  - Coding Agent
  - Workflow
  - RunStore
  - FastAPI
  - Auto Fix
excerpt: "从一次性生成接口升级为生成、验证、读错误、打补丁、再验证的工程闭环。"
source_log:
  - "Renyuan_Log.md:914-1091"
---

最早的生成接口只是把用户需求交给模型，让模型一次性吐出完整文件。这个形态适合 demo，但不适合工程系统：模型输出可能缺文件、脚本可能不能启动、依赖可能冲突，直到上传 OSS 或部署到 FC 以后才暴露问题。

更稳的形态是把 Coding Agent 看成一个运行系统，而不是一个接口。一次请求进入后，它应该创建一个 run，记录状态、事件和产物，然后按工作流推进。

## 三层边界

第一层是 API 层。它只负责参数校验、创建任务、返回 `run_id`、暴露查询和取消接口，不写生成逻辑。

第二层是 Agent 编排层。它维护状态机和工作流，决定什么时候生成、什么时候验证、什么时候修复、什么时候停止。

第三层是工具与基础设施层。LLM 调用、文件系统、命令执行、OSS、FC、HTTP 探测都应该封成工具，Agent 只通过工具产生副作用。

这样的边界让后续扩展变成“增加 step 和 workflow”，而不是把所有逻辑堆进一个 `/generate`。

## Run / Event / Artifact

核心数据模型可以压缩成三个对象。

`Run` 记录任务本身：`run_id`、状态、配置、创建时间、更新时间。

`RunEvent` 按时间追加：step start、step end、tool call、tool result、log、error。它是前端展示和后端排错的共同事实来源。

`Artifact` 记录生成物：workspace、文件集、打包结果、OSS key、预览 URL、验证报告。

这三个对象让一次生成变得可观察、可恢复、可审计。

## 工作流闭环

最小工作流是：

```text
generate -> normalize -> materialize -> validate -> patch -> validate
```

生成阶段让模型输出文件。规范化阶段补齐项目约束，例如脚本、依赖版本、入口位置。落盘阶段写入 run workspace。验证阶段执行 prepare/build/start，并用 HTTP probe 检查服务是否真的起来。失败时进入 patch 回路，只把失败日志摘要和少量相关文件交给模型，让它返回小范围补丁，再次验证。

这个闭环的关键不是“模型更聪明”，而是把错误暴露在本地验证阶段，并给模型一个受控修复面。

## 复杂方案到 `/runs`

最初可以设计很多 workflow：只生成、生成并验证、生成并上传 OSS、生成并部署 FC。但第一版不需要一次做完全部。更现实的落点是 `/runs`：先把任务状态、事件和结果稳定下来，再叠加上传和部署。

结论是：Coding Agent 的核心不是一个更大的 prompt，而是一个带状态、工具边界和验证闭环的运行系统。

## 知识补全：为什么 Agent 需要状态机

很多人第一次做 Coding Agent 时，会把它理解成“LLM + 文件写入工具”。这只覆盖了单步生成，却没有覆盖工程系统最重要的部分：任务会失败、会重试、会被取消、会超时、会产生中间产物。

状态机的价值是把这些不确定性变成可枚举状态。一个最小状态集可以是：

```text
queued -> running -> validating -> fixing -> succeeded
                         └──────-> failed / canceled
```

有了状态机，前端可以知道任务是否还在推进，后端可以知道失败发生在哪一阶段，日志也能按照阶段归档。没有状态机时，系统只剩下一段长日志，任何错误都要人工猜。

另一个关键概念是幂等性。`GET /runs/{run_id}` 应该只是读取状态，不改变任务；取消接口应该能重复调用；结果接口在成功后应该稳定返回同一份产物。这样 Agent 才像一个服务，而不是一次临时脚本执行。

## 实践检查清单

设计自己的 Coding Agent 时，可以逐项检查：

1. 每个 run 是否有唯一 ID。
2. 每个 step 是否有开始、结束、错误事件。
3. 文件写入是否限制在 workspace 内。
4. 执行命令是否有超时、输出长度限制和进程回收。
5. 自动修复是否只接收必要上下文，而不是把整个项目重新喂给模型。
6. 最终结果是否包含验证报告，而不仅是文件列表。

如果这些问题都有答案，Agent 才具备从 demo 走向工程系统的基础。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2025-03-25](#source-log-2025-03-25) | 694-964 | Coding Agent 工作流与沙箱安全 |
| [2026-03-26](#source-log-2026-03-26) | 965-1092 | 复杂 Agent 流程落地与 Docker 打包 |
| [2026-03-27](#source-log-2026-03-27) | 1093-1143 | 从 Agent 能力优先到格式化输出 |

<a id="source-log-2025-03-25"></a>
### Source Log: 2025-03-25

Source lines: `Renyuan_Log.md:694-964`

<pre class="tech-log-source"><code>
0694 |# 2025-03-25
0695 |
0696 |## 知识学习
0697 |
0698 |#### 更全面的Coding agent
0699 |
0700 |                Workshop UI
0701 |                     │
0702 |                     ▼
0703 |            FastAPI Agent Orchestrator
0704 |                     │
0705 |        ┌────────────┼────────────┐
0706 |        ▼            ▼            ▼
0707 |     Planner       Coder       Debugger
0708 |        │            │            │
0709 |        ▼            ▼            ▼
0710 |     spec.md      code tree      patch
0711 |        │            │            │
0712 |        └──────► OSS Storage ◄───┘
0713 |                      │
0714 |                      ▼
0715 |                FC Container
0716 |                      │
0717 |                      ▼
0718 |                Dev Server
0719 |                      │
0720 |                      ▼
0721 |                   iframe
0722 |
0723 |## 实践
0724 |
0725 |Multi-Agent的使用！震撼！
0726 |
0727 |#### OpenAI Codex, WSL2 CLI 模式运行
0728 |
0729 |Claude的API实在不稳定，50%时间403/503 error，换用Codex分组：
0730 |
0731 |VS Code的json配置openai codex默认不读取，所以需配置文件：
0732 |
0733 |我使用终端模式在WSL2，配置两个文件后成功运行gpt 5.4 model（默认的gpt 5 拥挤，不行）：
0734 |
0735 |**GNU nano 7.2    /home/ryan/.codex/auth.json**
0736 |```
0737 |{
0738 |  &quot;auth_mode&quot;: &quot;apikey&quot;,
0739 |  &quot;OPENAI_API_KEY&quot;: &quot;&lt;REDACTED&gt;&quot;
0740 |}
0741 |```
0742 |
0743 |**GNU nano 7.2    /home/ryan/.config/openai/config.toml**
0744 |```
0745 |disable_response_storage = true
0746 |model = &quot;gpt-5-codex&quot;
0747 |model_provider = &quot;custom&quot;
0748 |model_reasoning_effort = &quot;high&quot;
0749 |windows_wsl_setup_acknowledged = true
0750 |
0751 |[model_providers.custom]
0752 |base_url = &quot;https://hone.vvvv.ee/v1&quot;
0753 |name = &quot;custom&quot;
0754 |requires_openai_auth = true
0755 |wire_api = &quot;responses&quot;
0756 |
0757 |[notice]
0758 |hide_full_access_warning = true
0759 |```
0760 |
0761 |#### 优化LLM-CLI
0762 |
0763 |整个调用流程已换成阿里千问百炼
0764 |
0765 |#### 沙箱
0766 |
0767 |容器实例已经被创建并注册成功，现在要让容器运行起来
0768 |核心思想：AI 不直接运行代码，而是在 sandbox container 里运行。
0769 |
0770 |常规的AI Coding 沙箱架构：
0771 |User
0772 |  │
0773 |  ▼
0774 |Workshop UI (Web IDE)
0775 |  │
0776 |  ▼
0777 |Agent Service
0778 |  │
0779 |  ▼
0780 |Task Queue
0781 |  │
0782 |  ▼
0783 |Sandbox Manager
0784 |  │
0785 |  ▼
0786 |Container Runtime
0787 |  │
0788 |  ▼
0789 |Dev Server
0790 |  │
0791 |  ▼
0792 |Preview Router
0793 |  │
0794 |  ▼
0795 |Preview URL
0796 |
0797 |流程：
0798 |create container
0799 |      ↓
0800 |git clone / oss pull
0801 |      ↓
0802 |npm install
0803 |      ↓
0804 |start dev server
0805 |      ↓
0806 |expose preview url
0807 |
0808 |Response body
0809 |Download
0810 |{
0811 |  &quot;project_ids&quot;: [
0812 |    &quot;proj-1774117999499&quot;,
0813 |    &quot;proj-1774118618839&quot;,
0814 |    &quot;proj-1774118736018&quot;,
0815 |    &quot;proj-1774118993314&quot;,
0816 |    &quot;proj-1774119281456&quot;,
0817 |    &quot;proj-1774119530520&quot;,
0818 |    &quot;proj-1774261757601&quot;,
0819 |    &quot;proj-1774334030907&quot;,
0820 |    &quot;proj-1774336370281&quot;,
0821 |    &quot;proj-1774345523559&quot;,
0822 |    &quot;proj-1774365171381&quot;,
0823 |    &quot;proj-1774365451436&quot;,
0824 |    &quot;proj-1774365898657&quot;,
0825 |    &quot;proj-1774366108059&quot;,
0826 |    &quot;proj-1774366895437&quot;,
0827 |    &quot;proj-1774367246631&quot;,
0828 |    &quot;proj-1774402506350&quot;,
0829 |    &quot;proj-1774403324560&quot;,
0830 |    &quot;proj-1774424651687&quot;,
0831 |    &quot;string&quot;
0832 |  ]
0833 |}
0834 |
0835 |已经添加排查各个项目信息的接口：**GET /projects/summary**
0836 |**接口返回：**
0837 |```
0838 |{
0839 |  &quot;projects&quot;: [
0840 |    {
0841 |      &quot;project_id&quot;: &quot;proj-1774117999499&quot;,
0842 |      &quot;manifest_exists&quot;: true,
0843 |      &quot;template&quot;: &quot;base-node18&quot;,
0844 |      &quot;created_at&quot;: &quot;2026-03-21T18:33:20Z&quot;,
0845 |      &quot;preview_url&quot;: &quot;http://snake.fortuneai.cc/projects/proj-1774117999499/index.html&quot;,
0846 |      &quot;file_count&quot;: 12,
0847 |      &quot;has_fc&quot;: false,
0848 |      &quot;fc_status&quot;: &quot;NotFound&quot;,
0849 |      &quot;fc_preview_url&quot;: null,
0850 |      &quot;manifest_error&quot;: null,
0851 |      &quot;fc_error&quot;: null
0852 |    },
0853 |```
0854 |排查之后，已经逐一删除现存的FC
0855 |
0856 |现在，添加删除某项目的功能
0857 |
0858 |已经全部删除！现在有很多新接口，皆可使用：
0859 |
0860 |**目前的 FastAPI 接口：**
0861 |```
0862 |
0863 |POST
0864 |/generate
0865 |Generate With Openai
0866 |
0867 |POST
0868 |/upload
0869 |Upload
0870 |
0871 |POST
0872 |/save-project
0873 |Save Project
0874 |
0875 |GET
0876 |/projects
0877 |Get Projects
0878 |
0879 |GET
0880 |/projects/summary
0881 |Get Projects Summary
0882 |
0883 |GET
0884 |/projects/{project_id}
0885 |Get Project
0886 |
0887 |DELETE
0888 |/projects/{project_id}
0889 |Delete Project
0890 |
0891 |GET
0892 |/projects/{project_id}/tree
0893 |Get Project Tree
0894 |
0895 |GET
0896 |/projects/{project_id}/file
0897 |Get Project File
0898 |
0899 |***container***
0900 |
0901 |POST
0902 |/containers/{project_id}/start
0903 |Start Container
0904 |
0905 |GET
0906 |/containers/{project_id}/status
0907 |Get Container Status
0908 |
0909 |DELETE
0910 |/containers/{project_id}
0911 |Delete Container
0912 |```
0913 |
0914 |#### 实现较复杂的 Coding Agent（方案2）
0915 |
0916 |**Coding Agent方案2：** ***/generate/agent***
0917 |
0918 |把现在的“一次 LLM 调用吐全量文件”升级成
0919 |“多轮：生成 -&gt; 本地验证 -&gt; 读错误 -&gt; 修复 -&gt; 再验证”
0920 |的闭环，让产物在上传 OSS/跑 FC 前就尽量稳定
0921 |
0922 |架构规划：
0923 |把它从“一个接口里把所有事做完”拆成三层，并且用“可组合的工作流 + 可插拔的工具”承载未来功能增长。
0924 |
0925 |  1) 分层与边界（关键）
0926 |  - API 层（routers/*）：只负责参数校验、创建任务、返回 run_id/结果，不写业务逻辑。
0927 |  - Agent 编排层（agent/*）：状态机 + 工作流引擎。负责多轮循环、停止条件、重试、取消、超时、产物汇总。
0928 |  - 工具与基础设施层（tools/* + services/*）：把所有副作用封装成工具接口（LLM、文件系统、命令执行、HTTP 探测、OSS、FC），Agent 只能通过工具做
0929 |    事。
0930 |
0931 |  2) 推荐目录结构（可扩展）
0932 |  - Reference-framework/routers/agent.py：/generate/agent、/runs/{run_id}、/runs/{run_id}/events、/runs/{run_id}/cancel
0933 |  - Reference-framework/agent/core.py：Run 状态机、Step 约定、上下文（Context）
0934 |  - Reference-framework/agent/workflows/*.py：工作流定义（生成-only、生成+验证、生成+上传OSS、生成+上传+部署FC…）
0935 |  - Reference-framework/agent/steps/*.py：原子步骤（generate_draft、normalize、write_workspace、validate、llm_patch、package、upload_oss、
0936 |    deploy_fc…）
0937 |  - Reference-framework/agent/tools/*.py：工具接口与实现适配（llm_tool、exec_tool、fs_tool、oss_tool、fc_tool、http_probe_tool）
0938 |  - Reference-framework/agent/store/*.py：RunStore/EventStore/ArtifactStore（先本地文件或内存，后续可换 Redis/DB，不影响上层）
0939 |
0940 |  3) 核心数据模型（未来加功能不乱）
0941 |  - Run：run_id、status(queued/running/succeeded/failed/canceled)、workflow_name、config、created_at、updated_at
0942 |  - RunEvent：按时间追加（step_start/step_end/tool_call/tool_result/log/error），用于调试和前端展示
0943 |  - Artifact：生成文件集、workspace 路径、打包产物、OSS key、FC 预览 URL 等（都挂在 run 上）
0944 |
0945 |  4) 工作流设计（把“越来越多功能”变成组合）
0946 |  - 每个 workflow 只是一个 step 列表 + 分支条件，例如：
0947 |      - generate_only: LLM生成 -&gt; 规范化 -&gt; 返回文件
0948 |      - generate_validate: LLM生成 -&gt; 规范化 -&gt; 落盘 -&gt; prepare/build/start -&gt; 健康检查 -&gt; (失败则 patch 循环N次) -&gt; 返回文件+报告
0949 |      - generate_save_oss: 在通过验证后追加 upload_oss -&gt; 写manifest
0950 |      - generate_save_deploy_fc: 再追加 deploy_fc -&gt; 探测预览URL
0951 |  - 每个 step 输入/输出都只读写 Context，不直接互相调用；这样加新能力只要“加 step + 改 workflow 配置”，不会把代码越堆越硬。
0952 |
0953 |  5) LLM 交互规范（降低一次性大生成的 bug）
0954 |  - 修复轮：强制返回“补丁格式”，只允许改动少量文件（例如 {patches:[{path,content,op}]}），避免模型每轮重写全仓导致漂移。
0955 |  - 观察输入：只喂“失败日志摘要 + 相关文件（有限数量/有限字节）+ 明确目标”，并设置 max_iters、timeout、stop_condition。
0956 |
0957 |  6) 执行与安全（必须提前规划）
0958 |  - exec_tool 统一加：工作目录隔离、命令白名单/模板、CPU/时间/输出大小上限、端口占用检查、进程回收。
0959 |  - fs_tool 统一加：路径穿越防护、只允许写入 run 的 workspace。
0960 |  - 日志与密钥脱敏：event 里禁止落 API_KEY/AK/SK 原文。
0961 |
0962 |  这个结构最小闭环：/generate/agent + RunStore(EventStore) + generate_validate 工作流（多轮 patch 修
0963 |  复），其余 workflow（上传 OSS、部署 FC）用同一套 step 机制往后叠加
0964 |
</code></pre>


<a id="source-log-2026-03-26"></a>
### Source Log: 2026-03-26

Source lines: `Renyuan_Log.md:965-1092`

<pre class="tech-log-source"><code>
0965 |# 2026-03-26
0966 |
0967 |## 实践
0968 |
0969 |#### Coding Agent的较复杂实现与调用
0970 |
0971 |**Coding Agent方案2：** ***/generate/agent***
0972 |
0973 |方案2**函数调用流程图：**
0974 |```
0975 |  POST /generate/agent
0976 |  -&gt; routers/agent.generate_with_agent()
0977 |  -&gt; RunStore.create_run()
0978 |  -&gt; run_generate_validate()
0979 |  -&gt; build_enhanced_prompt()
0980 |  -&gt; OpenAI-compatible /chat/completions 生成 files[]
0981 |  -&gt; normalize_generated_files()
0982 |  -&gt; materialize_files() 写入 run workspace
0983 |  -&gt; _validate_workspace()
0984 |     -&gt; prepare.sh
0985 |     -&gt; build.sh
0986 |     -&gt; start.sh / dev.sh
0987 |     -&gt; HTTP probe
0988 |  -&gt; 如果失败且 auto_fix=true
0989 |     -&gt; pick_context_files()
0990 |     -&gt; OpenAI-compatible /chat/completions 生成 patches[]
0991 |     -&gt; apply_patches()
0992 |     -&gt; normalize_generated_files()
0993 |     -&gt; materialize_files()
0994 |     -&gt; 再次验证
0995 |  -&gt; RunStore.set_result() / set_status()
0996 |  -&gt; GET /runs/{run_id} 轮询结果
0997 |```
0998 |
0999 |方案2，根据大型agent框架构建的**数据流向：**
1000 |```
1001 |  1. 请求进入 generate_with_agent()。它把 prompt/template/model/max_iters/... 组装进 config，创建一个 run_id。见 Reference-framework/routers/
1002 |     agent.py:61、Reference-framework/routers/agent.py:78。
1003 |  2. RunStore.create_run() 会在本地创建目录：
1004 |     /tmp/reference-agent-runs/{run_id}/
1005 |     里面至少有：
1006 |  - run.json
1007 |  - events.jsonl
1008 |  - workspace/
1009 |    见 Reference-framework/agent/store.py:57、Reference-framework/agent/store.py:45。
1010 |  3. 如果 wait=false，路由只是 asyncio.create_task(coro) 把 workflow 丢到后台；如果 wait=true，当前请求会一直等到 workflow 结束。见 Reference-
1011 |     framework/routers/agent.py:95。
1012 |  4. workflow 入口是 run_generate_validate()。它先把 run 状态改成 running，然后调用 build_enhanced_prompt() 拼模板约束，再调用
1013 |     generate_project_with_openai()。见 Reference-framework/agent/workflows/generate_validate.py:230、Reference-framework/agent/workflows/
1014 |     generate_validate.py:252、Reference-framework/services/generation_rules.py:481。
1015 |  5. LLM 层当前不是 Responses API，也不是 Codex CLI 配置链路，而是后端自己读取 .env，直接请求 OPENAI_BASE_URL/chat/completions，并要求返回严格
1016 |     JSON schema。见 Reference-framework/services/openai_service.py:18、Reference-framework/services/openai_service.py:162、Reference-
1017 |     framework/services/openai_service.py:226。
1018 |  6. 生成结果被规范成 List[SaveFileItem]，也就是最核心的内部文件格式：
1019 |  - path
1020 |  - content
1021 |    见 Reference-framework/models.py:140。
1022 |  7. 生成完以后，会执行 normalize_generated_files()。这一步会强改模板相关内容，比如 Node18 依赖版本、补齐 scripts/*.sh、补 vite.config.js、修
1023 |     index.html 位置。见 Reference-framework/services/generation_rules.py:538。
1024 |  8. 然后 materialize_files() 把内存里的 files[] 写进 workspace/。注意这里是“覆盖同名文件”，不是“同步整个目录”。旧文件不会被删。见 Reference-
1025 |     framework/agent/tools/fs_tool.py:34。
1026 |  9. 如果 run_validation=false，workflow 到这里就结束，直接把 files[] 写入 run.result。见 Reference-framework/agent/workflows/
1027 |     generate_validate.py:264。
1028 |  10. 如果开启验证，会进入 _validate_workspace()：
1029 |  - 找一个空闲本地端口
1030 |  - 注入环境变量 WORKSPACE/HOST/PORT
1031 |  - 顺序跑 prepare.sh、build.sh
1032 |  - 再启动 start.sh，没有就退回 dev.sh
1033 |  - 用 HTTP 探测本地地址
1034 |    见 Reference-framework/agent/workflows/generate_validate.py:62、Reference-framework/agent/workflows/generate_validate.py:75、Reference-
1035 |    framework/agent/workflows/generate_validate.py:143。
1036 |  11. 验证时实际执行 shell 的地方在 exec_tool.py：
1037 |  - run_bash_script() 跑 prepare/build
1038 |  - start_bash_script() 起长跑进程
1039 |  - wait_http_ready() 轮询页面
1040 |  - 成功后马上 terminate_process()
1041 |    见 Reference-framework/agent/tools/exec_tool.py:37、Reference-framework/agent/tools/exec_tool.py:98、Reference-framework/agent/tools/
1042 |    exec_tool.py:191。
1043 |  12. 如果验证失败且 auto_fix=true，才会进入 patch 回路：
1044 |  - pick_context_files() 选少量关键文件
1045 |  - _build_fix_prompt() 拼失败日志和上下文
1046 |  - generate_project_patches_with_openai() 让模型返回 patches[]
1047 |  - apply_patches() 应用补丁
1048 |  - 再次 normalize_generated_files()
1049 |  - 再次 materialize_files()
1050 |  - 再验证
1051 |    见 Reference-framework/agent/workflows/generate_validate.py:323、Reference-framework/agent/tools/fs_tool.py:80、Reference-framework/
1052 |    services/openai_service.py:254。
1053 |  13. 当前 patch 的语义只有“按 path 覆盖/新增”，没有 delete，没有 rename，也没有“按最终 files 全量同步 workspace”。这正是你说要先修的 4。见
1054 |     Reference-framework/agent/tools/fs_tool.py:60。
1055 |  14. 成功或失败后，workflow 会把结果写回 run.json。result 里会直接带完整文件内容和 validation report。见 Reference-framework/agent/workflows/
1056 |     generate_validate.py:297、Reference-framework/agent/store.py:123。
1057 |  run 的状态和文件
1058 |  当前 run 的生命周期基本是：
1059 |  - queued
1060 |  - running
1061 |  - succeeded / failed / canceled
1062 |  状态变化和关键动作都会追加到 events.jsonl。见 Reference-framework/agent/store.py:119。
1063 |```
1064 |
1065 |现在简化Agent流程：
1066 |
1067 |**Coding Agent 方案3：** ***/runs***
1068 |
1069 |舍弃了大型agent的流程（）简化为简单的workflow。
1070 |**完整链路成功：**
1071 |  - 生成成功
1072 |  - 本机 prepare/build/start 全部成功
1073 |  - 发布成功
1074 |  - 已创建 OSS 项目和 FC
1075 |关键结果是：
1076 |  - run_id: run-1774496744666-42124bb9
1077 |  - project_id: proj-1774496798261
1078 |  - 最终状态：succeeded
1079 |
1080 |简化成功debug成功。
1081 |
1082 |### Docker打包成功
1083 |
1084 |(base) ryan@ENVYKatana:/mnt/c/Desktop/generate/Reference-framework$ curl --noproxy &#x27;*&#x27; -i http://127.0.0.1:9000/healthz
1085 |HTTP/1.1 200 OK
1086 |date: Thu, 26 Mar 2026 07:33:08 GMT
1087 |server: uvicorn
1088 |content-length: 166
1089 |content-type: application/json
1090 |
1091 |{&quot;ok&quot;:true,&quot;service&quot;:&quot;reference-framework&quot;,&quot;runs_dir&quot;:&quot;/data/reference-agent-runs&quot;,&quot;checks&quot;:{&quot;runs_dir_writable&quot;:true,&quot;openai_configured&quot;:true,&quot;oss_configured&quot;:true}}(base)
1092 |
</code></pre>


<a id="source-log-2026-03-27"></a>
### Source Log: 2026-03-27

Source lines: `Renyuan_Log.md:1093-1143`

<pre class="tech-log-source"><code>
1093 |# 2026-03-27
1094 |
1095 |## 知识学习
1096 |
1097 |### 探讨Coding Agent架构
1098 |
1099 |最终我们决定先完成强大的agent，再通过微调workflow的结构，格式化输出内容，以对接OSS/FC
1100 |
1101 |而不是一开始根据OSS/FC的结构化需求设计Agent
1102 |
1103 |逻辑关系是本末倒置的
1104 |
1105 |### TypeScript
1106 |
1107 |[TypeScript教程](https://www.runoob.com/typescript/ts-tutorial.html)
1108 |
1109 |非常多的开源项目用 TS 写成！
1110 |
1111 |## 实践
1112 |
1113 |### 设计能够格式化输出的Coding Agent
1114 |
1115 |按现在这个目标，不需要把主流程改成“先输出 {&quot;files&quot;:[...]} 再落盘”，具体而言：
1116 |
1117 |现有 coding agent 的主链路：
1118 |1. 用户输入进入 SessionPrompt.prompt()
1119 |2. 主 agent 开始推理
1120 |3. agent 在过程中调用 write / edit / apply_patch
1121 |4. 文件直接写到当前工作目录，比如你指定的 TEST/
1122 |
1123 |所以要加的，其实只是前置的一层：
1124 |1. 检测是否是“生成项目”意图
1125 |2. 如果不是，原样走现有聊天/分析流程
1126 |3. 如果是，先把简单 prompt 例如“生成贪吃蛇游戏”增强成一条完整、规范、工程化的 prompt
1127 |4. 然后把这条增强后的 prompt 继续交给现有 coding agent
1128 |5. 后面的文件创建仍然由现有 agent 正常完成
1129 |
1130 |落实到改动操作：
1131 |1. IntentDetector
1132 |   输入简单 prompt，比如“生成贪吃蛇游戏”。
1133 |   输出结构化判断：intent=generate_project | normal_chat，以及 template=base-node18 | base-python39。
1134 |2. ProjectPromptEnhancer
1135 |   只在 intent=generate_project 时运行。
1136 |   用专门的 enhancer agent 深度理解、补全约束、规划输出。
1137 |   输出结构化结果建议是：
1138 |   template
1139 |   enhancedPrompt
1140 |   constraints
1141 |3. 把 enhancedPrompt 覆盖原始 text part，再把这条增强后的 user message 交给现有主生成链路。
1142 |   后面的文件生成仍然由 write/edit/apply_patch 完成，直接落到 TEST/
1143 |
</code></pre>

<!-- source-log-coverage:end -->
