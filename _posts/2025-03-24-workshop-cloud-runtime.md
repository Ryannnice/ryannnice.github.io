---
layout: single
title: "Workshop 云端运行架构：OSS、FC 容器、Docker 镜像与本地验证闭环"
date: 2025-03-24
categories:
  - tech-blog
  - agent-engineering
series: "Agent Engineering"
priority: P1
tags:
  - Docker
  - OSS
  - Function Compute
  - Deployment
  - Sandbox
excerpt: "生成代码只是开始，真正要交付给用户的是能构建、能启动、能预览、能回收的运行闭环。"
source_log:
  - "Renyuan_Log.md:437-459"
  - "Renyuan_Log.md:547-692"
  - "Renyuan_Log.md:767-806"
  - "Renyuan_Log.md:1348-1394"
---

低代码平台的输出不能停留在“模型返回一堆文件”。用户真正需要的是一个可以预览、下载、部署的项目。Workshop 的云端运行架构就是为了解决这个问题。

## 端到端链路

一个完整链路可以抽象成：

```text
prompt -> Agent -> files -> workspace -> build -> run -> probe -> package -> OSS/FC -> preview
```

其中最容易被低估的是本地验证。只有在上传或部署前先跑一遍 prepare、build、start 和 HTTP probe，才能尽早暴露依赖缺失、端口冲突、入口错误和脚本问题。

## 基础镜像

生成项目通常会落到几类模板：

- Node 前端项目。
- Python / FastAPI 项目。
- Fullstack 项目。

这些模板对应不同 Docker 基础镜像和标准脚本。生成器不应自由发明启动方式，而应被约束到稳定 contract：`prepare.sh`、`build.sh`、`start.sh` 或 `dev.sh`。

## OSS 与 FC

OSS 适合保存产物、源码包和静态文件。FC 容器适合运行可预览服务。两者组合后，系统可以把生成结果从文件变成 URL。

但这也引入了工程问题：端口映射、健康检查、路径挂载、代理配置、容器内工作目录、构建缓存。它们都不是模型层问题，却会决定用户是否能打开页面。

## 验证闭环

本地验证阶段应该包含：

1. 创建隔离 workspace。
2. 写入生成文件。
3. 执行 prepare。
4. 执行 build。
5. 启动服务。
6. HTTP 探测。
7. 成功后打包或部署，失败则进入修复回路。

这样系统交付的是“可运行项目”，而不只是“看起来完整的代码”。

## 知识补全：为什么必须先本地验证再部署

云端部署失败的成本比本地验证失败高得多。上传 OSS、创建 FC、拉镜像、启动容器、等待健康检查，每一步都会消耗时间，也会把错误传播到更多系统。

本地验证的目标是把错误压缩在 workspace 内。依赖安装失败、构建失败、端口没监听、入口文件不存在，这些都应该在上传前发现。

一个可靠的验证报告至少应包含：

- 执行了哪些脚本。
- 每个脚本的退出码。
- stdout / stderr 摘要。
- 服务监听端口。
- HTTP probe 的状态码和响应摘要。
- 如果失败，下一轮 patch 应该优先查看哪些文件。

这份报告同时服务三类对象：开发者看日志、前端展示状态、LLM 进行修复。

## 部署链路的分层思维

Workshop 的部署问题可以分成四层：

1. 代码层：文件是否完整，入口是否正确。
2. 构建层：依赖是否可安装，build 是否通过。
3. 运行层：端口、环境变量、进程生命周期是否正确。
4. 云资源层：OSS、FC、镜像、权限和网络是否可用。

排障时应从下往上确认。否则很容易把代码错误误判成云平台问题，或把镜像问题误判成模型生成问题。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2025-03-23](#source-log-2025-03-23) | 415-528 | Docker、FastAPI 与 FC 容器初步架构 |
| [2025-03-24](#source-log-2025-03-24) | 529-693 | 云端运行闭环与端口、代理、镜像问题 |
| [2026-03-30](#source-log-2026-03-30) | 1319-1420 | Workshop 在线运行与架构路线收敛 |
| [2026-04-27](#source-log-2026-04-27) | 2394-2410 | Faraway 项目进展 |

<a id="source-log-2025-03-23"></a>
### Source Log: 2025-03-23

Source lines: `Renyuan_Log.md:415-528`

<pre class="tech-log-source"><code>
0415 |# 2025-03-23
0416 |
0417 |## 知识学习
0418 |
0419 |#### Docker
0420 |
0421 |```
0422 |https://www.bilibili.com/video/BV1THKyzBER6/?share_source=copy_web&amp;vd_source=035cd776909e96dadfc9bbaeb1588cd4
0423 |```
0424 |
0425 |#### FastAPI
0426 |
0427 |FastAPI配合**后端开发**：
0428 |```
0429 |https://www.bilibili.com/video/BV1eUxve7Ein/?share_source=copy_web&amp;vd_source=035cd776909e96dadfc9bbaeb1588cd4
0430 |```
0431 |```
0432 |https://fastapi.org.cn/python-types/#pydantic-models
0433 |```
0434 |
0435 |上下文工程 Context Engineering
0436 |
0437 |#### 谕书的Workshop框架和API
0438 |
0439 |项目框架采用FC容器(每个项目一个)，而不是fs操作本地文件
0440 |```
0441 |OSS+FC的架构：
0442 |┌─────────────────────────────────────────────────────┐
0443 |│                    用户浏览器                         │
0444 |│  左：对话+文件树    中：代码查看    右：预览iframe      │
0445 |└──────────┬──────────────────────────────┬───────────┘
0446 |           │              │ iframe src
0447 |           ▼                             ▼
0448 |┌─────────────────┐            ┌──────────────────────┐
0449 |│  你的FastAPI服务 │            │  FC容器(每个项目一个) │
0450 |│  (项目管理/调度) │            │   dev server:9000    │
0451 |└────────┬────────┘            └──────────┬───────────┘
0452 |         │                                │
0453 |    ┌────┴──────────────────────────┐     │
0454 |    │         阿里云基础设施         │     │
0455 |    │  OSS(代码+静态)  RDS(MySQL)    |◄───┘
0456 |    │  ACR(镜像仓库)   MNS(消息队列) │
0457 |    └───────────────────────────────┘
0458 |```
0459 |这个线上部署运行架构值得融合，今天做这件事：
0460 |
0461 |## 实践
0462 |
0463 |```
0464 |OnlySpecs 的现有架构梳理：
0465 |
0466 |  四种运行模式:
0467 |  ┌──────────────┬───────────────┬──────┬─────────────────────┐
0468 |  │     模式     │     入口      │ 端口 │        说明         │
0469 |  ├──────────────┼───────────────┼──────┼─────────────────────┤
0470 |  │ 桌面应用     │ npm run dev   │ —    │ Electron + IPC      │
0471 |  ├──────────────┼───────────────┼──────┼─────────────────────┤
0472 |  │ 无头 API     │ npm run api   │ 3580 │ Express + 子进程    │
0473 |  ├──────────────┼───────────────┼──────┼─────────────────────┤
0474 |  │ Web 界面     │ npm run web   │ 3579 │ Express + WebSocket │
0475 |  ├──────────────┼───────────────┼──────┼─────────────────────┤
0476 |  │ FastAPI 前端 │ python app.py │ 9000 │ 代理 API + SSE      │
0477 |  └──────────────┴───────────────┴──────┴─────────────────────┘
0478 |  核心数据流:
0479 |
0480 |  桌面模式：
0481 |  Renderer (Monaco/xterm) → IPC → ipc-handlers.ts → 文件系统 / node-pty / Claude SDK
0482 |
0483 |  API模式：
0484 |  HTTP POST /generate → 创建任务 → 启动 claude CLI子进程 → 写入 code_v0001/
0485 |  HTTP GET /logs/:id→ 轮询日志
0486 |
0487 |  Web 模式：
0488 |  浏览器 → WebSocket → web-server（复用 ipc-handlers 逻辑）→ 文件系统 / node-pty
0489 |  FastAPI 模式：
0490 |  Vue3 → FastAPI (9000) → HTTP → API Server (3580) → claude CLI↑ SSE 实时日志流
0491 |
0492 |  关键文件
0493 |
0494 |  ┌──────────────────────────┬─────────────────────────────────────────────┐
0495 |  │           文件           │                    作用                     │
0496 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0497 |  │ src/main/ipc-handlers.ts │ 所有 IPC 处理（编辑器、终端、文件、GitHub） │
0498 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0499 |  │ src/main/claude/sdk.ts   │ Claude Agent SDK 封装，流式输出             │
0500 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0501 |  │ src/renderer/index.ts    │ 主App 类，组装所有 UI组件                   │
0502 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0503 |  │ src/api-server/index.ts  │ 无头 API，任务管理 + 子进程调度             │
0504 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0505 |  │ src/web-server/index.ts  │ WebSocket 服务，镜像 IPC 协议               │
0506 |  ├──────────────────────────┼─────────────────────────────────────────────┤
0507 |  │ api-integration/app.py   │ FastAPI 代理 + SSE + ZIP 下载 + 项目管理    │
0508 |  └──────────────────────────┴─────────────────────────────────────────────┘
0509 |
0510 |  ---
0511 |  数据存储
0512 |
0513 |  ~/Documents/OnlySpecs/
0514 |  ├── editors/          # 编辑器内容（每个 tab 一个 JSON）
0515 |  ├── config.json       # API Key、上次项目路径
0516 |  ├── api-workspaces/   # API 模式生成的代码
0517 |  │   └── task_*/
0518 |  │├── specs_v0001.md
0519 |  │       └── code_v0001/
0520 |  └── tmp/              # GitHub import 临时克隆目录
0521 |
0522 |  两个独立的 Claude 调用路径：
0523 |  1. 桌面/Web 模式 — 通过 claude/sdk.ts 调用 @anthropic-ai/claude-agent-sdk，流式返回结果给 UI
0524 |  2. API 模式 — 直接 spawn claude CLI 子进程，用 node-pty 捕获输出，存入任务日志
0525 |
0526 |  两条路径互相独立，不共享代码。
0527 |```
0528 |
</code></pre>


<a id="source-log-2025-03-24"></a>
### Source Log: 2025-03-24

Source lines: `Renyuan_Log.md:529-693`

<pre class="tech-log-source"><code>
0529 |# 2025-03-24
0530 |
0531 |## 实践
0532 |
0533 |#### Debug 网络代理
0534 |
0535 |#### 完善数据流向
0536 |
0537 |优化prompt以暴露onlyspecs原有复杂文档生成能力
0538 |
0539 |#### FastAPI
0540 |
0541 |对接谕书的架构，我第一次跑通了FastAPI的agent接口！
0542 |
0543 |已成功完成/generate接口，成功对接、上传到OSS
0544 |
0545 |目前，需完善FC系统
0546 |
0547 |#### FC容器
0548 |
0549 |#### 方案规划
0550 |**potential solution:**
0551 |```
0552 |完成 FC 容器调度与多文件生成验证
0553 |
0554 | Context
0555 |
0556 | 当前状态：
0557 | - Claude CLI 集成完成：POST /generate → Claude CLI → 收集文件 → OSS
0558 | - 标准化 prompt 已实现：build_enhanced_prompt() 注入 scripts/ 目录要求
0559 | - FC API 调度完成：POST /containers/{project_id}/start → 创建 FC 函数 → 返回 preview_url
0560 | - OSS 存储完成：save_project() 上传文件 + manifest.json
0561 |
0562 | 核心问题：
0563 | FC 容器无法启动生成的代码，因为缺少容器内的启动逻辑：
0564 | 1. 缺少 entrypoint.sh - 容器启动脚本，负责从 OSS 下载代码并执行标准化脚本
0565 | 2. 缺少容器镜像 - base-node18/base-python39/base-fullstack 镜像不存在
0566 | 3. 无法验证多文件生成 - 没有端到端测试验证 Claude CLI 生成的复杂项目能否正常运行
0567 |
0568 | 目标：
0569 | 完成 FC 调度链路，实现：用户 prompt → Claude 生成 → OSS 存储 → FC 容器运行 → 前端 iframe 预览
0570 |
0571 | ---
0572 | 实现方案
0573 |
0574 | 方案 A：完整 FC 容器方案（生产级）
0575 |
0576 | 需要实现：
0577 | 1. 创建 3 个 Dockerfile（base-node18, base-python39, base-fullstack）
0578 | 2. 编写 entrypoint.sh 脚本（下载 OSS 代码 → 执行 prepare.sh → 执行 dev.sh）
0579 | 3. 构建镜像并推送到 ACR
0580 | 4. 验证完整链路
0581 |
0582 | 优点： 真实生产环境，完全符合 goal.md 架构
0583 | 缺点： 需要 Docker 环境、ACR 推送权限、FC 配额
0584 |
0585 | ---
0586 | 方案 B：本地验证方案（快速验证）
0587 |
0588 | 只验证文件生成和脚本执行，不依赖 FC：
0589 | 1. 调用 /generate 生成项目
0590 | 2. 从 OSS 下载生成的文件到本地临时目录
0591 | 3. 本地执行 scripts/prepare.sh 和 scripts/dev.sh
0592 | 4. 验证服务能在 9000 端口启动
0593 |
0594 | 优点： 快速验证，无需云资源
0595 | 缺点： 不是真实 FC 环境
0596 |
0597 | ---
0598 | 推荐方案：方案 B（本地验证）+ 方案 A 的容器脚本准备
0599 |
0600 | 分两步走：
0601 |
0602 | 第一步：本地验证多文件生成（立即可做）
0603 |
0604 | 创建测试脚本 test_generation.py：
0605 | - 调用 /generate API 生成简单项目（如 &quot;创建一个 Hello World 网页&quot;）
0606 | - 检查返回的 files 列表是否包含：
0607 |   - scripts/prepare.sh
0608 |   - scripts/dev.sh（包含端口 9000）
0609 |   - scripts/build.sh
0610 |   - scripts/start.sh
0611 |   - 业务代码文件（如 src/index.html）
0612 | - 从 OSS 下载所有文件到 /tmp/test-{project_id}/
0613 | - 执行 bash scripts/prepare.sh（安装依赖）
0614 | - 后台执行 bash scripts/dev.sh（启动服务）
0615 | - 验证 curl http://localhost:9000 返回 200
0616 |
0617 | 验证目标： 确认 Claude CLI 生成的项目结构正确，脚本可执行
0618 |
0619 | ---
0620 | 第二步：准备 FC 容器资源（为生产部署做准备）
0621 |
0622 | 创建 3 个容器镜像的 Dockerfile 和 entrypoint.sh：
0623 |
0624 | 文件结构：
0625 | Reference-framework/
0626 |   docker/
0627 |     base-node18/
0628 |       Dockerfile
0629 |       entrypoint.sh
0630 |     base-python39/
0631 |       Dockerfile
0632 |       entrypoint.sh
0633 |     base-fullstack/
0634 |       Dockerfile
0635 |       entrypoint.sh
0636 |```
0637 |
0638 |#### 本地运行测试
0639 |
0640 |为了验证代码树的运行可行性。之后再真正在云端FC环境运行代码
0641 |
0642 |先完成**本地测试**，之后“登录 ACR”（ACR 指的是 Alibaba Cloud Container Registry）：
0643 |
0644 |把构建的 Docker 镜像**上传到阿里云的镜像仓库**，让 **FC 容器**可以拉取运行
0645 |
0646 |排查出的三个问题:
0647 |
0648 |问题 1：系统代理拦截了 localhost 请求 → 502
0649 |
0650 |  http_proxy=http://172.26.224.1:7890
0651 |  所有 requests 发出的请求（包括 localhost）都走了代理，代理无法转发本地流量，返回 502
0652 |  解决：对 localhost 请求显式禁用代理，对公网 OSS 保留代理:
0653 |  PROXY_FOR_LOCALHOST = {&quot;http&quot;: None, &quot;https&quot;: None}
0654 |  PROXY_FOR_OSS = {&quot;http&quot;: os.environ.get(&quot;http_proxy&quot;), ...}
0655 |
0656 |问题 2：FastAPI 和生成项目端口冲突（都是 9000）
0657 |
0658 |  测试脚本发完请求后，Step 6 验证的 http://localhost:9000 其实打到了 FastAPI 自己
0659 |  解决：FastAPI 改用 9001 启动：
0660 |  uvicorn app:app --port 9001
0661 |
0662 |问题 3：prepare.sh 写死 /workspace 本地不存在
0663 |
0664 |  Claude 生成的脚本是为 FC 容器设计的（容器里代码在 /workspace），本地 /workspace 不存在
0665 |  解决：下载脚本后自动替换路径： patched = content.replace(&quot;/workspace&quot;, test_dir)
0666 |
0667 |  验证结果:
0668 |  ┌───────────────────────────┬────────────────────────────┐
0669 |  │           步骤            │            结果            │
0670 |  ├───────────────────────────┼────────────────────────────┤
0671 |  │ Claude CLI 生成文件       │  7个文件包含所有必需脚本 │
0672 |  ├───────────────────────────┼────────────────────────────┤
0673 |  │ OSS 上传/下载             │  正常                    │
0674 |  ├───────────────────────────┼────────────────────────────┤
0675 |  │ prepare.sh（npm install） │  成功                    │
0676 |  ├───────────────────────────┼────────────────────────────┤
0677 |  │ dev.sh（npx serve :9000） │  成功                    │
0678 |  ├───────────────────────────┼────────────────────────────┤
0679 |  │ HTTP 200 验证             │  返回完整 HTML           │
0680 |  └───────────────────────────┴────────────────────────────┘
0681 |  整条链路 prompt → Claude → OSS → 脚本执行 → HTTP服务 验证完毕。
0682 |
0683 |  端口分配：
0684 |  ┌────────────────────────────┬──────┬────────────────────────────┐
0685 |  │            用途             │ 端口 │            备注
0686 |  ├────────────────────────────┼──────┼────────────────────────────┤
0687 |  │ FastAPI（uvicorn app:app）  │ 9000 │ 正常启动，不变
0688 |  ├────────────────────────────┼──────┼────────────────────────────┤
0689 |  │ 本地测试生成项目            │ 8080 │ 脚本自动 patch，测完还原
0690 |  ├────────────────────────────┼──────┼────────────────────────────┤
0691 |  │ FC 容器里生成项目           │ 9000 │ 真实环境不 patch，保持原样
0692 |  └────────────────────────────┴──────┴────────────────────────────┘
0693 |
</code></pre>


<a id="source-log-2026-03-30"></a>
### Source Log: 2026-03-30

Source lines: `Renyuan_Log.md:1319-1420`

<pre class="tech-log-source"><code>
1319 |# 2026-03-30
1320 |
1321 |## 知识学习
1322 |
1323 |#### 对现有工程的思考：我们的目的是什么？
1324 |
1325 |***真正缺的，不是“再造一个能连续对话的 /generate”，而是把 /generate 里更强的那部分能力搬进 web 的标准 session 路径里***
1326 |
1327 |#### 如果是workshop，那重心在于强大的coding agent、在线运行。但“生成自己的openclaw”这样级别的要求难以实现
1328 |“贪吃蛇”是远远不够的。目前，coding agent已经足够强大，但在云端运行“用户生成的程序”仍需细致对接
1329 |
1330 |#### 如果是能解决具体需求的agent，那重心在于SKILL.md, 理解需求、细致的构造pipeline，通过多个skill真正去解决问题
1331 |
1332 |#### TODO List
1333 |
1334 |- find skills的SKILL.md, 进一步的，一堆工具skills，如何调用
1335 |
1336 |- 需求分析的SKILL.md
1337 |
1338 |- 不同应用场景，写paper，写report，上网
1339 |
1340 |- AI降重：带上自己的思想;  降重 SKILL.md
1341 |
1342 |- 让claude触手可得
1343 |
1344 |## 实践
1345 |
1346 |#### Coding Agent网页版在线运行
1347 |
1348 |在现有网页应用上加OSS/FC在线运行：
1349 |
1350 |#### 第一阶段
1351 |```
1352 |  - 从 packages/opencode/src/server/generate-project.ts 抽出“项目 contract 校验”模块。
1353 |  - 保留现有规则：模板识别、必需文件、scripts/*.sh 约束、Vite/Vue 版本约束、Python/FastAPI约束。
1354 |  - 目标文件建议新建为 packages/opencode/src/server/project-contract.ts 或相近位置。
1355 |  - /generate 和 web session 后续都复用这一个模块。
1356 |```
1357 |
1358 |#### 第二阶段
1359 |```
1360 |  - 在 web 端加“在线构建并在线运行模式”开关。
1361 |  - 入口优先放在 packages/app/src/components/prompt-input/submit.ts 所在提交链路附近。
1362 |  - 这一步只做“把模式标记传到后端 prompt 流程”，不要先做部署。
1363 |```
1364 |
1365 |#### 第三阶段
1366 |```
1367 |  - 扩展 packages/opencode/src/plugin/prompt-enhancer.ts，让它在该模式下启用更强 project contract。
1368 |  - 普通聊天不受影响。
1369 |  - 项目生成首条消息启用：固定模板规则、输出目录规则、运行脚本规则、可部署规则。
1370 |```
1371 |
1372 |#### 第四阶段
1373 |```
1374 |  - 在标准 session 流里接入“校验失败自动修复”。
1375 |  - 不再走临时 /generate session。
1376 |  - 在同一 session 内，首轮生成完成后校验；失败时自动追加 repair prompt；成功则结束。
1377 |  - 这样 web 的持续对话、流式状态、消息历史都天然保留。
1378 |```
1379 |
1380 |#### 第五阶段
1381 |```
1382 |  - 只约束部署必需接口，不先绑定具体云厂商实现细节。
1383 |  - 先稳定：
1384 |    scripts/prepare.sh
1385 |    scripts/build.sh
1386 |    scripts/start.sh
1387 |    HOST
1388 |    PORT
1389 |    WORKSPACE
1390 |```
1391 |
1392 |保留 /generate: 作为外部 API、作为 contract 回归测试入口、作为未来批量生成入口
1393 |
1394 |最值得先做的是第 1 步和第 2 步。做完这两步，主路径就从“独立 /generate”转成“web session + 强约束项目模式”。
1395 |下一步直接改两处：packages/opencode/src/server/generate-project.ts、packages/opencode/src/plugin/、prompt-enhancer.ts，然后再接 web 的模式开关。
1396 |
1397 |现在 web 版已经接上这条链路了：
1398 |新会话输入框里新增了一个持久化的 “Run Online / 在线构建运行” 开关
1399 |打开后，首条普通 prompt 会带上在线运行 mode marker；后端prompt-enhancer会据此启用之前加的“在线构建并运行”约束
1400 |相关改动在 packages/app/src/components/prompt-input.tsx
1401 |packages/app/src/components/prompt-input/submit.ts
1402 |packages/opencode/src/plugin/prompt-enhancer.ts
1403 |以及新的共享模块 packages/util/src/project-mode.ts
1404 |
1405 |## 知识学习
1406 |
1407 |#### Workshop数据流动、架构细节分析讨论
1408 |
1409 |#### Seminar: World Model
1410 |
1411 |## 实践
1412 |
1413 |#### Debug Web应用
1414 |
1415 |已添加“构建项目”模式，并在前端展示现已生成的文件
1416 |
1417 |带前端版本的完整pipeline已跑通！
1418 |
1419 |现在，对接CUHKSZ的第二前端。
1420 |
</code></pre>


<a id="source-log-2026-04-27"></a>
### Source Log: 2026-04-27

Source lines: `Renyuan_Log.md:2394-2410`

<pre class="tech-log-source"><code>
2394 |# 2026-04-27
2395 |
2396 |## 远方 faraway
2397 |
2398 |基于腾讯云对接完整的后端
2399 |
2400 |[网页版APP](https://faraway-app-d0gpvf2ko79ceaba3-1426371841.tcloudbaseapp.com/)
2401 |
2402 |### 安卓 APP 打包成功
2403 |
2404 |[目前版本 GihHub 仓库](https://github.com/Tt200411/faraway)
2405 |
2406 |待对接、开发更详细的后端功能
2407 |
2408 |
2409 |
2410 |
</code></pre>

<!-- source-log-coverage:end -->
