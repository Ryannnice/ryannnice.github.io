# 稔远学习日志

仅个人学习与实践记录，便于回顾与整理。

# 2025-03-19

## 知识学习

#### 图解Transformer
非常清晰的图示教程，用矩阵拆解Transformer，难度梯度很合适
[教程](https://jalammar.github.io/illustrated-transformer/)

#### TypeScript/npm包管理

#### TypeScript[(清华大学的AI教育项目)](https://github.com/Ryannnice/CUHK-LLM-Edu/edit/main/README.md)

整个项目绝大部分使用TypeScript,文件结构、调用逻辑非常复杂
TypeScript 是 JavaScript 的超集

#### npm

npm = Node Package Manager（Node.js 包管理器）

安装库和工具/管理依赖（项目里用到的第三方包）/**运行脚本**（比如启动 Vue、React 或 Node 项目）
*npm run <脚本名>: 运行 package.json 里的脚本*

#### FastAPI python框架了解
第一次实习，第一次接触偏工程的项目：不同于科研的是，可行性/整体模块的缝合、运行似乎比细致的优化更重要

清华的开源教育项目未采用前后端分离架构

使用.json格式请求体完成数据/信息传递

前端直接通过函数调用REST API:
```
 fastapi_backend/
    └── static/
        ├── index.html        # 主页（需求输入 + 设置）
        ├── generate.html     # 生成流程页（SSE 大纲流 + 进度）
        ├── classroom.html    # 课堂播放页（幻灯片/测验/聊天）
        ├── app.js            # 全局工具：API 调用、设置存储、路由
        ├── generate.js       # 生成流程逻辑
        ├── classroom.js      # 课堂播放逻辑（幻灯片渲染、测验、聊天）
        └── style.css         # 全局样式
```

## 实践

#### FastAPI
在原本的REST API接口上，建立/fastapi_backend文件夹，用FastAPI封装全部18个功能的api
原有.ts文件前端直接调用api的所有逻辑均保留，与Fast后端接口不冲突

实现后端分离之后，建立/fastapi_backend/static文件夹，仅使用js/html初步实现前端功能，以验证FastAPI后端接口可行性

# 2025-03-20

## 知识学习

#### 开源库OnlySpecs
这是自动生成软件的agent系统，可能对项目第二部分*WorkShop*有帮助
（上午团队实现workshop功能时发现直接调用LLM实现代码（软件编程）能力有限：贪吃蛇不成功，推箱子成功）
试图部署该开源项目，接入我们的项目

## 实践

#### Linux bash
上午claude api爆了，以为是网络问题重新配置安装一遍windows WSL的linux的网络环境

# 2025-03-21

## 知识学习

#### 开源库OnlySpecs

#### node-pty

pty.spawn("claude")

相当于**在程序里打开**一个**终端**窗口

#### AIEngine

一个“可以驱动 Claude CLI 干活”的执行器

```
return new Promise((resolve, reject) => {
    proc.onExit((e) => {
        if (e.exitCode === 0) resolve()
        else reject(new Error(...))
    })
})
```
```
┌─────────────┐
│ run() 调用  │
│ await engine│
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ Promise     │   <-- pending 状态
│ resolve/reject 内部管子
└─────┬───────┘
      │
      ▼
┌─────────────┐
│ proc.onExit │  <-- Claude CLI 退出触发
│ e.exitCode  │
└─────┬───────┘
      │
      ▼
if(exitCode==0) resolve()  else reject(error)
      │
      ▼
Promise 状态变更 → 外层 await/then/catch 收到结果
```

#### Shim

是一种兼容层或适配器，用于在不修改原有代码的情况下，让新旧接口或系统之间能够协同工作

这很适用于最小化更改，让该开源项目快速应用于我们的项目中，以此为起点吧

#### Node.js Web 服务器

Node.js 是一个运行环境，可以用 JavaScript 写服务端程序

"Node.js Web 服务器"就是用 Node.js 写的 HTTP 服务，比如用 Express、Fastify、Koa 等框架搭建的后端，和阿里云服务器不冲突

```
阿里云 ECS（服务器硬件/系统）
    └── Nginx（反向代理，监听 80/443 端口）
          └── Node.js 进程（监听 3000 端口）
                └── 你的业务代码
```

## 实践

#### Web版OnlySpecs功能测试

已完成在web上的部署，使用简单的html转跳

汉化前端菜单栏

#### 融入大项目的Workshop部分

**我们项目Workshop的原架构：**

```
用户 → Vue
        │
        ▼
FastAPI /generate
        │
        ▼
DeepSeek 生成 HTML
        │
        ▼
FastAPI /upload
        │
        ▼
阿里云 OSS
        │
        ▼
返回 URL
        │
        ▼
Vue 展示
```

**开源软件OnlySpecs的原架构：**
```
Electron UI
    ↓
Renderer (DOM + Monaco)
    ↓
IPC
    ↓
Main Process
    ↓
node-pty
    ↓
Claude CLI
```

**新架构融合，两种方案：**

***方案一，分离式：***
```
 大项目
 ├── Vue 仪表盘（前端）   → Docker: Nginx 静态托管，端口 80
 ├── FastAPI 后端         → Docker: Uvicorn，端口 9000
 │   ├── /generate        → DeepSeek 流式生成 HTML
 │   └── /upload          → 阿里云 OSS 上传
 └── OnlySpecs（待加入）  → Docker: Node.js，端口 3579
     └── 功能：Specs 编写、Claude AI 代码生成、终端
```

***方案二，通过FastAPI使用功能，仅替换掉LLM，使用claude agent编写软件：***
```
Vue 前端
    ↓ POST /generate-software { prompt }
  FastAPI
    ↓ 调用 OnlySpecs Node.js 服务（HTTP 或子进程）
  OnlySpecs Web Server
    ↓ 写 specs.md → 启动 Claude CLI
  Claude CLI（node-pty）
    ↓ 生成代码
  返回结果（文件路径 / OSS URL）
    ↑ 流式进度推送（SSE / WebSocket）
  Vue 前端展示


FastAPI 端点设计
  # POST /generate-software
  # 输入：用户 prompt
  # 输出：SSE 流式进度 + 最终代码 URL

  @app.post("/generate-software")
  async def generate_software(prompt: str):
      # 1. 调用 OnlySpecs API 创建 specs 文件
      # 2. 触发 Generate from Specs
      # 3. 流式返回进度
      # 4. 完成后上传到 OSS，返回 URL
```

先尝试方案二，先设计无头OnlySpecs的API

# 2025-03-22

## 实践

FastAPI 编写完成，核心是/generate 根据用户指令来交给OnlySpecs，利用其功能生成

api测试成功（文档：/home/ryan/OnlySpecs/docs/API_QUICKSTART.md，测试：终端运行 npm run test:api）

接下来对接我们的项目第二部分Workshop：
实现方式参考原框架，写出仿制的前端：/home/ryan/OnlySpecs/api-integration

整个Pipeline:

```
  📁 Project Structure

  ~/OnlySpecs/api-integration/
  ├── app.py              # FastAPI backend (API proxy + SSE streaming)
  ├── requirements.txt    # Python dependencies
  ├── .env               # Environment configuration
  ├── .env.example       # Environment template
  ├── start.sh           # Quick start script
  ├── static/
  │   └── index.html     # Vue 3 frontend (312 lines)
  └── README.md          # Complete documentation

  🎯 Key Features Implemented

  Backend (FastAPI):
  - ✅ CORS-enabled API proxy to OnlySpecs API
  - ✅ SSE streaming for real-time log updates
  - ✅ Endpoints: /api/generate, /api/status, /api/logs, /api/tasks, /api/download
  - ✅ Error handling and timeout controls

  Frontend (Vue 3 + Tailwind):
  - ✅ Clean, responsive UI with Chinese localization
  - ✅ Real-time log display with auto-scroll
  - ✅ Task status tracking (pending/running/completed/failed)
  - ✅ History task list with click-to-load
  - ✅ Download generated code as ZIP
  - ✅ EventSource for SSE log streaming

  🚀 Quick Start

  # 1. Start OnlySpecs API (in one terminal)
  cd ~/OnlySpecs
  npm run api

  # 2. Start frontend (in another terminal)
  cd ~/OnlySpecs/api-integration
  ./start.sh

  Then visit: http://localhost:9000

  📝 Usage Flow
  1. Enter software requirements in the text area
  2. Click "开始生成" (Start Generation)
  3. Watch real-time Claude CLI logs
  4. Download code when complete or open in file explorer
  5. View history tasks in the collapsible section

  The implementation follows the plan exactly, using SSE for real-time updates and providing a simple, user-friendly interface for interacting
  with OnlySpecs.
```

已经能完美运行，依靠简洁的web界面，通过FastAPI和OnlySpecs交互

***输入-->OnlySpecs-->Claude CLI-->输出***，用户只负责敲几个字：项目第二部分低代码的思想

debug修复内容：

1. claude开始但是不工作，代码写不进去项目文件夹 / claude 不动，接收不到指令：--print 标志可以完全跳过交互式 UI，直接输出结果。不需要 pty 模拟，改用子进程即可。用 spawn + --print 替换整个 pty 方案，彻底解决交互式 UI 问题。

2. 下载 ZIP之后win系统打不开：之前是把 OnlySpecs API 返回的 JSON 当 ZIP 存的，当然打不开。现在后端拿到 codePath，用 shutil.make_archive 真正打包成 ZIP，Win11 可以直接解压。

3. “在文件管理器中打开”的按钮点不动：新增了 /api/open/{task_id} 接口，调用 xdg-open 打开 Linux 文件管理器，同时在界面显示代码路径。
WSL2 里 xdg-open 无法直接打开 Windows 文件管理器。需要用 explorer.exe 来打开，但路径要转换成 Windows 格式。
转换出来是 \\wsl.localhost\Ubuntu\... 格式，Win11 的文件资源管理器可以直接打开这个 UNC 路径。
```
\\wsl.localhost\Ubuntu\home\ryan\Documents\OnlySpecs\api-workspaces\task_1774168877875_1u1yudaz6\code_v0001
```

***全部修复***

朝着更更更低代码平台进发：

📋 计划总结

核心功能： 在 Web 界面添加 4 种输出类型选择：

1. 📄 源代码 - 可编辑的源文件
2. 🌐 Web 应用 - 单文件 HTML，浏览器直接运行
3. 💻 桌面程序 - Windows .exe 可执行文件（自动打包）
4. 📱 手机应用 - PWA 渐进式 Web 应用

用户使用Pipeline:

```
用户浏览器
    │
    ▼
Vue 前端
    │
    ▼
FastAPI API
    │
    ▼
OnlySpecs AI Engine （调用Claude CLI）
    │
    ▼
生成代码
    │
    ▼
Build Worker（Docker）
    │
    ▼
编译为 .exe
    │
    ▼
上传到 OSS
    │
    ▼
用户下载
```

本地项目列表已更新：

新功能：
1. 类型标签 - 每个项目左侧显示彩色标签：
  - 📄 源代码（紫色）
  - 🌐 Web应用（靛蓝色）
  - 💻 桌面程序（橙色）
  - 📱 手机应用（粉色）
2. 对应按钮 - 根据项目类型显示不同的主功能按钮：
  - 源代码：📄 线上查看 + 📦 下载源码
  - Web应用：🌐 线上运行 + 📦 下载源码
  - 桌面程序：💻 下载 .exe + 📦 下载源码
  - 手机应用：📱 下载应用 + 📦 下载源码

```
  部署步骤：

  1. 在阿里云服务器上安装依赖：
  安装Node.js
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
  sudo apt-get install -y nodejs

  安装Python
  sudo apt-get install python3 python3-pip

  安装Docker
  curl -fsSL https://get.docker.com | sudo sh
  sudo usermod -aG docker $USER

  安装Claude CLI
  npm install -g @anthropic-ai/claude-code

  2. 配置Claude API密钥：
  export ANTHROPIC_API_KEY="your-api-key-here"

  3. 打包项目：
  cd ~/OnlySpecs
  tar -czf onlyspecs-deploy.tar.gz \
    src/ \
    api-integration/ \
    package.json\
    tsconfig.json
  4. 上传到服务器：
  scp onlyspecs-deploy.tar.gz user@your-server:/home/user/

  5. 在服务器上解压并启动：
  tar -xzf onlyspecs-deploy.tar.gz
  npm install
  docker pull cdrx/pyinstaller-windows

  启动服务
  npm run api &
  cd api-integration && python3 app.py &

  6. 配置防火墙：
  sudo ufw allow 3580
  sudo ufw allow 9000

  访问：http://your-server-ip:9000
```

# 2025-03-23

## 知识学习

#### Docker

```
https://www.bilibili.com/video/BV1THKyzBER6/?share_source=copy_web&vd_source=035cd776909e96dadfc9bbaeb1588cd4
```

#### FastAPI

FastAPI配合**后端开发**：
```
https://www.bilibili.com/video/BV1eUxve7Ein/?share_source=copy_web&vd_source=035cd776909e96dadfc9bbaeb1588cd4
```
```
https://fastapi.org.cn/python-types/#pydantic-models
```

上下文工程 Context Engineering

#### 谕书的Workshop框架和API

项目框架采用FC容器(每个项目一个)，而不是fs操作本地文件
```
OSS+FC的架构：
┌─────────────────────────────────────────────────────┐
│                    用户浏览器                         │
│  左：对话+文件树    中：代码查看    右：预览iframe      │
└──────────┬──────────────────────────────┬───────────┘
           │              │ iframe src
           ▼                             ▼
┌─────────────────┐            ┌──────────────────────┐
│  你的FastAPI服务 │            │  FC容器(每个项目一个) │
│  (项目管理/调度) │            │   dev server:9000    │
└────────┬────────┘            └──────────┬───────────┘
         │                                │
    ┌────┴──────────────────────────┐     │
    │         阿里云基础设施         │     │
    │  OSS(代码+静态)  RDS(MySQL)    |◄───┘
    │  ACR(镜像仓库)   MNS(消息队列) │
    └───────────────────────────────┘
```
这个线上部署运行架构值得融合，今天做这件事：

## 实践

```
OnlySpecs 的现有架构梳理：

  四种运行模式:
  ┌──────────────┬───────────────┬──────┬─────────────────────┐
  │     模式     │     入口      │ 端口 │        说明         │
  ├──────────────┼───────────────┼──────┼─────────────────────┤
  │ 桌面应用     │ npm run dev   │ —    │ Electron + IPC      │
  ├──────────────┼───────────────┼──────┼─────────────────────┤
  │ 无头 API     │ npm run api   │ 3580 │ Express + 子进程    │
  ├──────────────┼───────────────┼──────┼─────────────────────┤
  │ Web 界面     │ npm run web   │ 3579 │ Express + WebSocket │
  ├──────────────┼───────────────┼──────┼─────────────────────┤
  │ FastAPI 前端 │ python app.py │ 9000 │ 代理 API + SSE      │
  └──────────────┴───────────────┴──────┴─────────────────────┘
  核心数据流:

  桌面模式：
  Renderer (Monaco/xterm) → IPC → ipc-handlers.ts → 文件系统 / node-pty / Claude SDK

  API模式：
  HTTP POST /generate → 创建任务 → 启动 claude CLI子进程 → 写入 code_v0001/
  HTTP GET /logs/:id→ 轮询日志

  Web 模式：
  浏览器 → WebSocket → web-server（复用 ipc-handlers 逻辑）→ 文件系统 / node-pty
  FastAPI 模式：
  Vue3 → FastAPI (9000) → HTTP → API Server (3580) → claude CLI↑ SSE 实时日志流

  关键文件

  ┌──────────────────────────┬─────────────────────────────────────────────┐
  │           文件           │                    作用                     │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ src/main/ipc-handlers.ts │ 所有 IPC 处理（编辑器、终端、文件、GitHub） │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ src/main/claude/sdk.ts   │ Claude Agent SDK 封装，流式输出             │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ src/renderer/index.ts    │ 主App 类，组装所有 UI组件                   │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ src/api-server/index.ts  │ 无头 API，任务管理 + 子进程调度             │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ src/web-server/index.ts  │ WebSocket 服务，镜像 IPC 协议               │
  ├──────────────────────────┼─────────────────────────────────────────────┤
  │ api-integration/app.py   │ FastAPI 代理 + SSE + ZIP 下载 + 项目管理    │
  └──────────────────────────┴─────────────────────────────────────────────┘

  ---
  数据存储

  ~/Documents/OnlySpecs/
  ├── editors/          # 编辑器内容（每个 tab 一个 JSON）
  ├── config.json       # API Key、上次项目路径
  ├── api-workspaces/   # API 模式生成的代码
  │   └── task_*/
  │├── specs_v0001.md
  │       └── code_v0001/
  └── tmp/              # GitHub import 临时克隆目录

  两个独立的 Claude 调用路径：
  1. 桌面/Web 模式 — 通过 claude/sdk.ts 调用 @anthropic-ai/claude-agent-sdk，流式返回结果给 UI
  2. API 模式 — 直接 spawn claude CLI 子进程，用 node-pty 捕获输出，存入任务日志

  两条路径互相独立，不共享代码。
```

# 2025-03-24

## 实践

#### Debug 网络代理

#### 完善数据流向

优化prompt以暴露onlyspecs原有复杂文档生成能力

#### FastAPI

对接谕书的架构，我第一次跑通了FastAPI的agent接口！

已成功完成/generate接口，成功对接、上传到OSS

目前，需完善FC系统

#### FC容器

#### 方案规划
**potential solution:**
```
完成 FC 容器调度与多文件生成验证

 Context

 当前状态：
 - Claude CLI 集成完成：POST /generate → Claude CLI → 收集文件 → OSS
 - 标准化 prompt 已实现：build_enhanced_prompt() 注入 scripts/ 目录要求
 - FC API 调度完成：POST /containers/{project_id}/start → 创建 FC 函数 → 返回 preview_url
 - OSS 存储完成：save_project() 上传文件 + manifest.json

 核心问题：
 FC 容器无法启动生成的代码，因为缺少容器内的启动逻辑：
 1. 缺少 entrypoint.sh - 容器启动脚本，负责从 OSS 下载代码并执行标准化脚本
 2. 缺少容器镜像 - base-node18/base-python39/base-fullstack 镜像不存在
 3. 无法验证多文件生成 - 没有端到端测试验证 Claude CLI 生成的复杂项目能否正常运行

 目标：
 完成 FC 调度链路，实现：用户 prompt → Claude 生成 → OSS 存储 → FC 容器运行 → 前端 iframe 预览

 ---
 实现方案

 方案 A：完整 FC 容器方案（生产级）

 需要实现：
 1. 创建 3 个 Dockerfile（base-node18, base-python39, base-fullstack）
 2. 编写 entrypoint.sh 脚本（下载 OSS 代码 → 执行 prepare.sh → 执行 dev.sh）
 3. 构建镜像并推送到 ACR
 4. 验证完整链路

 优点： 真实生产环境，完全符合 goal.md 架构
 缺点： 需要 Docker 环境、ACR 推送权限、FC 配额

 ---
 方案 B：本地验证方案（快速验证）

 只验证文件生成和脚本执行，不依赖 FC：
 1. 调用 /generate 生成项目
 2. 从 OSS 下载生成的文件到本地临时目录
 3. 本地执行 scripts/prepare.sh 和 scripts/dev.sh
 4. 验证服务能在 9000 端口启动

 优点： 快速验证，无需云资源
 缺点： 不是真实 FC 环境

 ---
 推荐方案：方案 B（本地验证）+ 方案 A 的容器脚本准备

 分两步走：

 第一步：本地验证多文件生成（立即可做）

 创建测试脚本 test_generation.py：
 - 调用 /generate API 生成简单项目（如 "创建一个 Hello World 网页"）
 - 检查返回的 files 列表是否包含：
   - scripts/prepare.sh
   - scripts/dev.sh（包含端口 9000）
   - scripts/build.sh
   - scripts/start.sh
   - 业务代码文件（如 src/index.html）
 - 从 OSS 下载所有文件到 /tmp/test-{project_id}/
 - 执行 bash scripts/prepare.sh（安装依赖）
 - 后台执行 bash scripts/dev.sh（启动服务）
 - 验证 curl http://localhost:9000 返回 200

 验证目标： 确认 Claude CLI 生成的项目结构正确，脚本可执行

 ---
 第二步：准备 FC 容器资源（为生产部署做准备）

 创建 3 个容器镜像的 Dockerfile 和 entrypoint.sh：

 文件结构：
 Reference-framework/
   docker/
     base-node18/
       Dockerfile
       entrypoint.sh
     base-python39/
       Dockerfile
       entrypoint.sh
     base-fullstack/
       Dockerfile
       entrypoint.sh
```

#### 本地运行测试

为了验证代码树的运行可行性。之后再真正在云端FC环境运行代码

先完成**本地测试**，之后“登录 ACR”（ACR 指的是 Alibaba Cloud Container Registry）：

把构建的 Docker 镜像**上传到阿里云的镜像仓库**，让 **FC 容器**可以拉取运行

排查出的三个问题:

问题 1：系统代理拦截了 localhost 请求 → 502

  http_proxy=http://172.26.224.1:7890
  所有 requests 发出的请求（包括 localhost）都走了代理，代理无法转发本地流量，返回 502
  解决：对 localhost 请求显式禁用代理，对公网 OSS 保留代理:
  PROXY_FOR_LOCALHOST = {"http": None, "https": None}
  PROXY_FOR_OSS = {"http": os.environ.get("http_proxy"), ...}

问题 2：FastAPI 和生成项目端口冲突（都是 9000）

  测试脚本发完请求后，Step 6 验证的 http://localhost:9000 其实打到了 FastAPI 自己
  解决：FastAPI 改用 9001 启动：
  uvicorn app:app --port 9001

问题 3：prepare.sh 写死 /workspace 本地不存在

  Claude 生成的脚本是为 FC 容器设计的（容器里代码在 /workspace），本地 /workspace 不存在
  解决：下载脚本后自动替换路径： patched = content.replace("/workspace", test_dir)

  验证结果:
  ┌───────────────────────────┬────────────────────────────┐
  │           步骤            │            结果            │
  ├───────────────────────────┼────────────────────────────┤
  │ Claude CLI 生成文件       │  7个文件包含所有必需脚本 │
  ├───────────────────────────┼────────────────────────────┤
  │ OSS 上传/下载             │  正常                    │
  ├───────────────────────────┼────────────────────────────┤
  │ prepare.sh（npm install） │  成功                    │
  ├───────────────────────────┼────────────────────────────┤
  │ dev.sh（npx serve :9000） │  成功                    │
  ├───────────────────────────┼────────────────────────────┤
  │ HTTP 200 验证             │  返回完整 HTML           │
  └───────────────────────────┴────────────────────────────┘
  整条链路 prompt → Claude → OSS → 脚本执行 → HTTP服务 验证完毕。

  端口分配：
  ┌────────────────────────────┬──────┬────────────────────────────┐
  │            用途             │ 端口 │            备注
  ├────────────────────────────┼──────┼────────────────────────────┤
  │ FastAPI（uvicorn app:app）  │ 9000 │ 正常启动，不变
  ├────────────────────────────┼──────┼────────────────────────────┤
  │ 本地测试生成项目            │ 8080 │ 脚本自动 patch，测完还原
  ├────────────────────────────┼──────┼────────────────────────────┤
  │ FC 容器里生成项目           │ 9000 │ 真实环境不 patch，保持原样
  └────────────────────────────┴──────┴────────────────────────────┘

# 2025-03-25

## 知识学习

#### 更全面的Coding agent

                Workshop UI
                     │
                     ▼
            FastAPI Agent Orchestrator
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Planner       Coder       Debugger
        │            │            │
        ▼            ▼            ▼
     spec.md      code tree      patch
        │            │            │
        └──────► OSS Storage ◄───┘
                      │
                      ▼
                FC Container
                      │
                      ▼
                Dev Server
                      │
                      ▼
                   iframe

## 实践

Multi-Agent的使用！震撼！

#### OpenAI Codex, WSL2 CLI 模式运行

Claude的API实在不稳定，50%时间403/503 error，换用Codex分组：

VS Code的json配置openai codex默认不读取，所以需配置文件：

我使用终端模式在WSL2，配置两个文件后成功运行gpt 5.4 model（默认的gpt 5 拥挤，不行）：

**GNU nano 7.2    /home/ryan/.codex/auth.json**
```
{
  "auth_mode": "apikey",
  "OPENAI_API_KEY": "<REDACTED>"
}
```

**GNU nano 7.2    /home/ryan/.config/openai/config.toml**
```
disable_response_storage = true
model = "gpt-5-codex"
model_provider = "custom"
model_reasoning_effort = "high"
windows_wsl_setup_acknowledged = true

[model_providers.custom]
base_url = "https://hone.vvvv.ee/v1"
name = "custom"
requires_openai_auth = true
wire_api = "responses"

[notice]
hide_full_access_warning = true
```

#### 优化LLM-CLI

整个调用流程已换成阿里千问百炼

#### 沙箱

容器实例已经被创建并注册成功，现在要让容器运行起来
核心思想：AI 不直接运行代码，而是在 sandbox container 里运行。

常规的AI Coding 沙箱架构：
User
  │
  ▼
Workshop UI (Web IDE)
  │
  ▼
Agent Service
  │
  ▼
Task Queue
  │
  ▼
Sandbox Manager
  │
  ▼
Container Runtime
  │
  ▼
Dev Server
  │
  ▼
Preview Router
  │
  ▼
Preview URL

流程：
create container
      ↓
git clone / oss pull
      ↓
npm install
      ↓
start dev server
      ↓
expose preview url

Response body
Download
{
  "project_ids": [
    "proj-1774117999499",
    "proj-1774118618839",
    "proj-1774118736018",
    "proj-1774118993314",
    "proj-1774119281456",
    "proj-1774119530520",
    "proj-1774261757601",
    "proj-1774334030907",
    "proj-1774336370281",
    "proj-1774345523559",
    "proj-1774365171381",
    "proj-1774365451436",
    "proj-1774365898657",
    "proj-1774366108059",
    "proj-1774366895437",
    "proj-1774367246631",
    "proj-1774402506350",
    "proj-1774403324560",
    "proj-1774424651687",
    "string"
  ]
}

已经添加排查各个项目信息的接口：**GET /projects/summary**
**接口返回：**
```
{
  "projects": [
    {
      "project_id": "proj-1774117999499",
      "manifest_exists": true,
      "template": "base-node18",
      "created_at": "2026-03-21T18:33:20Z",
      "preview_url": "http://snake.fortuneai.cc/projects/proj-1774117999499/index.html",
      "file_count": 12,
      "has_fc": false,
      "fc_status": "NotFound",
      "fc_preview_url": null,
      "manifest_error": null,
      "fc_error": null
    },
```
排查之后，已经逐一删除现存的FC

现在，添加删除某项目的功能

已经全部删除！现在有很多新接口，皆可使用：

**目前的 FastAPI 接口：**
```

POST
/generate
Generate With Openai

POST
/upload
Upload

POST
/save-project
Save Project

GET
/projects
Get Projects

GET
/projects/summary
Get Projects Summary

GET
/projects/{project_id}
Get Project

DELETE
/projects/{project_id}
Delete Project

GET
/projects/{project_id}/tree
Get Project Tree

GET
/projects/{project_id}/file
Get Project File

***container***

POST
/containers/{project_id}/start
Start Container

GET
/containers/{project_id}/status
Get Container Status

DELETE
/containers/{project_id}
Delete Container
```

#### 实现较复杂的 Coding Agent（方案2）

**Coding Agent方案2：** ***/generate/agent***

把现在的“一次 LLM 调用吐全量文件”升级成
“多轮：生成 -> 本地验证 -> 读错误 -> 修复 -> 再验证”
的闭环，让产物在上传 OSS/跑 FC 前就尽量稳定

架构规划：
把它从“一个接口里把所有事做完”拆成三层，并且用“可组合的工作流 + 可插拔的工具”承载未来功能增长。

  1) 分层与边界（关键）
  - API 层（routers/*）：只负责参数校验、创建任务、返回 run_id/结果，不写业务逻辑。
  - Agent 编排层（agent/*）：状态机 + 工作流引擎。负责多轮循环、停止条件、重试、取消、超时、产物汇总。
  - 工具与基础设施层（tools/* + services/*）：把所有副作用封装成工具接口（LLM、文件系统、命令执行、HTTP 探测、OSS、FC），Agent 只能通过工具做
    事。

  2) 推荐目录结构（可扩展）
  - Reference-framework/routers/agent.py：/generate/agent、/runs/{run_id}、/runs/{run_id}/events、/runs/{run_id}/cancel
  - Reference-framework/agent/core.py：Run 状态机、Step 约定、上下文（Context）
  - Reference-framework/agent/workflows/*.py：工作流定义（生成-only、生成+验证、生成+上传OSS、生成+上传+部署FC…）
  - Reference-framework/agent/steps/*.py：原子步骤（generate_draft、normalize、write_workspace、validate、llm_patch、package、upload_oss、
    deploy_fc…）
  - Reference-framework/agent/tools/*.py：工具接口与实现适配（llm_tool、exec_tool、fs_tool、oss_tool、fc_tool、http_probe_tool）
  - Reference-framework/agent/store/*.py：RunStore/EventStore/ArtifactStore（先本地文件或内存，后续可换 Redis/DB，不影响上层）

  3) 核心数据模型（未来加功能不乱）
  - Run：run_id、status(queued/running/succeeded/failed/canceled)、workflow_name、config、created_at、updated_at
  - RunEvent：按时间追加（step_start/step_end/tool_call/tool_result/log/error），用于调试和前端展示
  - Artifact：生成文件集、workspace 路径、打包产物、OSS key、FC 预览 URL 等（都挂在 run 上）

  4) 工作流设计（把“越来越多功能”变成组合）
  - 每个 workflow 只是一个 step 列表 + 分支条件，例如：
      - generate_only: LLM生成 -> 规范化 -> 返回文件
      - generate_validate: LLM生成 -> 规范化 -> 落盘 -> prepare/build/start -> 健康检查 -> (失败则 patch 循环N次) -> 返回文件+报告
      - generate_save_oss: 在通过验证后追加 upload_oss -> 写manifest
      - generate_save_deploy_fc: 再追加 deploy_fc -> 探测预览URL
  - 每个 step 输入/输出都只读写 Context，不直接互相调用；这样加新能力只要“加 step + 改 workflow 配置”，不会把代码越堆越硬。

  5) LLM 交互规范（降低一次性大生成的 bug）
  - 修复轮：强制返回“补丁格式”，只允许改动少量文件（例如 {patches:[{path,content,op}]}），避免模型每轮重写全仓导致漂移。
  - 观察输入：只喂“失败日志摘要 + 相关文件（有限数量/有限字节）+ 明确目标”，并设置 max_iters、timeout、stop_condition。

  6) 执行与安全（必须提前规划）
  - exec_tool 统一加：工作目录隔离、命令白名单/模板、CPU/时间/输出大小上限、端口占用检查、进程回收。
  - fs_tool 统一加：路径穿越防护、只允许写入 run 的 workspace。
  - 日志与密钥脱敏：event 里禁止落 API_KEY/AK/SK 原文。

  这个结构最小闭环：/generate/agent + RunStore(EventStore) + generate_validate 工作流（多轮 patch 修
  复），其余 workflow（上传 OSS、部署 FC）用同一套 step 机制往后叠加

# 2026-03-26

## 实践

#### Coding Agent的较复杂实现与调用

**Coding Agent方案2：** ***/generate/agent***

方案2**函数调用流程图：**
```
  POST /generate/agent
  -> routers/agent.generate_with_agent()
  -> RunStore.create_run()
  -> run_generate_validate()
  -> build_enhanced_prompt()
  -> OpenAI-compatible /chat/completions 生成 files[]
  -> normalize_generated_files()
  -> materialize_files() 写入 run workspace
  -> _validate_workspace()
     -> prepare.sh
     -> build.sh
     -> start.sh / dev.sh
     -> HTTP probe
  -> 如果失败且 auto_fix=true
     -> pick_context_files()
     -> OpenAI-compatible /chat/completions 生成 patches[]
     -> apply_patches()
     -> normalize_generated_files()
     -> materialize_files()
     -> 再次验证
  -> RunStore.set_result() / set_status()
  -> GET /runs/{run_id} 轮询结果
```

方案2，根据大型agent框架构建的**数据流向：**
```
  1. 请求进入 generate_with_agent()。它把 prompt/template/model/max_iters/... 组装进 config，创建一个 run_id。见 Reference-framework/routers/
     agent.py:61、Reference-framework/routers/agent.py:78。
  2. RunStore.create_run() 会在本地创建目录：
     /tmp/reference-agent-runs/{run_id}/
     里面至少有：
  - run.json
  - events.jsonl
  - workspace/
    见 Reference-framework/agent/store.py:57、Reference-framework/agent/store.py:45。
  3. 如果 wait=false，路由只是 asyncio.create_task(coro) 把 workflow 丢到后台；如果 wait=true，当前请求会一直等到 workflow 结束。见 Reference-
     framework/routers/agent.py:95。
  4. workflow 入口是 run_generate_validate()。它先把 run 状态改成 running，然后调用 build_enhanced_prompt() 拼模板约束，再调用
     generate_project_with_openai()。见 Reference-framework/agent/workflows/generate_validate.py:230、Reference-framework/agent/workflows/
     generate_validate.py:252、Reference-framework/services/generation_rules.py:481。
  5. LLM 层当前不是 Responses API，也不是 Codex CLI 配置链路，而是后端自己读取 .env，直接请求 OPENAI_BASE_URL/chat/completions，并要求返回严格
     JSON schema。见 Reference-framework/services/openai_service.py:18、Reference-framework/services/openai_service.py:162、Reference-
     framework/services/openai_service.py:226。
  6. 生成结果被规范成 List[SaveFileItem]，也就是最核心的内部文件格式：
  - path
  - content
    见 Reference-framework/models.py:140。
  7. 生成完以后，会执行 normalize_generated_files()。这一步会强改模板相关内容，比如 Node18 依赖版本、补齐 scripts/*.sh、补 vite.config.js、修
     index.html 位置。见 Reference-framework/services/generation_rules.py:538。
  8. 然后 materialize_files() 把内存里的 files[] 写进 workspace/。注意这里是“覆盖同名文件”，不是“同步整个目录”。旧文件不会被删。见 Reference-
     framework/agent/tools/fs_tool.py:34。
  9. 如果 run_validation=false，workflow 到这里就结束，直接把 files[] 写入 run.result。见 Reference-framework/agent/workflows/
     generate_validate.py:264。
  10. 如果开启验证，会进入 _validate_workspace()：
  - 找一个空闲本地端口
  - 注入环境变量 WORKSPACE/HOST/PORT
  - 顺序跑 prepare.sh、build.sh
  - 再启动 start.sh，没有就退回 dev.sh
  - 用 HTTP 探测本地地址
    见 Reference-framework/agent/workflows/generate_validate.py:62、Reference-framework/agent/workflows/generate_validate.py:75、Reference-
    framework/agent/workflows/generate_validate.py:143。
  11. 验证时实际执行 shell 的地方在 exec_tool.py：
  - run_bash_script() 跑 prepare/build
  - start_bash_script() 起长跑进程
  - wait_http_ready() 轮询页面
  - 成功后马上 terminate_process()
    见 Reference-framework/agent/tools/exec_tool.py:37、Reference-framework/agent/tools/exec_tool.py:98、Reference-framework/agent/tools/
    exec_tool.py:191。
  12. 如果验证失败且 auto_fix=true，才会进入 patch 回路：
  - pick_context_files() 选少量关键文件
  - _build_fix_prompt() 拼失败日志和上下文
  - generate_project_patches_with_openai() 让模型返回 patches[]
  - apply_patches() 应用补丁
  - 再次 normalize_generated_files()
  - 再次 materialize_files()
  - 再验证
    见 Reference-framework/agent/workflows/generate_validate.py:323、Reference-framework/agent/tools/fs_tool.py:80、Reference-framework/
    services/openai_service.py:254。
  13. 当前 patch 的语义只有“按 path 覆盖/新增”，没有 delete，没有 rename，也没有“按最终 files 全量同步 workspace”。这正是你说要先修的 4。见
     Reference-framework/agent/tools/fs_tool.py:60。
  14. 成功或失败后，workflow 会把结果写回 run.json。result 里会直接带完整文件内容和 validation report。见 Reference-framework/agent/workflows/
     generate_validate.py:297、Reference-framework/agent/store.py:123。
  run 的状态和文件
  当前 run 的生命周期基本是：
  - queued
  - running
  - succeeded / failed / canceled
  状态变化和关键动作都会追加到 events.jsonl。见 Reference-framework/agent/store.py:119。
```

现在简化Agent流程：

**Coding Agent 方案3：** ***/runs***

舍弃了大型agent的流程（）简化为简单的workflow。
**完整链路成功：**
  - 生成成功
  - 本机 prepare/build/start 全部成功
  - 发布成功
  - 已创建 OSS 项目和 FC
关键结果是：
  - run_id: run-1774496744666-42124bb9
  - project_id: proj-1774496798261
  - 最终状态：succeeded

简化成功debug成功。

### Docker打包成功

(base) ryan@ENVYKatana:/mnt/c/Desktop/generate/Reference-framework$ curl --noproxy '*' -i http://127.0.0.1:9000/healthz
HTTP/1.1 200 OK
date: Thu, 26 Mar 2026 07:33:08 GMT
server: uvicorn
content-length: 166
content-type: application/json

{"ok":true,"service":"reference-framework","runs_dir":"/data/reference-agent-runs","checks":{"runs_dir_writable":true,"openai_configured":true,"oss_configured":true}}(base)

# 2026-03-27

## 知识学习

### 探讨Coding Agent架构

最终我们决定先完成强大的agent，再通过微调workflow的结构，格式化输出内容，以对接OSS/FC

而不是一开始根据OSS/FC的结构化需求设计Agent

逻辑关系是本末倒置的

### TypeScript

[TypeScript教程](https://www.runoob.com/typescript/ts-tutorial.html)

非常多的开源项目用 TS 写成！

## 实践

### 设计能够格式化输出的Coding Agent

按现在这个目标，不需要把主流程改成“先输出 {"files":[...]} 再落盘”，具体而言：

现有 coding agent 的主链路：
1. 用户输入进入 SessionPrompt.prompt()
2. 主 agent 开始推理
3. agent 在过程中调用 write / edit / apply_patch
4. 文件直接写到当前工作目录，比如你指定的 TEST/

所以要加的，其实只是前置的一层：
1. 检测是否是“生成项目”意图
2. 如果不是，原样走现有聊天/分析流程
3. 如果是，先把简单 prompt 例如“生成贪吃蛇游戏”增强成一条完整、规范、工程化的 prompt
4. 然后把这条增强后的 prompt 继续交给现有 coding agent
5. 后面的文件创建仍然由现有 agent 正常完成

落实到改动操作：
1. IntentDetector
   输入简单 prompt，比如“生成贪吃蛇游戏”。
   输出结构化判断：intent=generate_project | normal_chat，以及 template=base-node18 | base-python39。
2. ProjectPromptEnhancer
   只在 intent=generate_project 时运行。
   用专门的 enhancer agent 深度理解、补全约束、规划输出。
   输出结构化结果建议是：
   template
   enhancedPrompt
   constraints
3. 把 enhancedPrompt 覆盖原始 text part，再把这条增强后的 user message 交给现有主生成链路。
   后面的文件生成仍然由 write/edit/apply_patch 完成，直接落到 TEST/

# 2026-03-28

## 知识学习

### Opencode

Opencode 内部调用逻辑

## 实践

### Coding Agent

我通过修改opencode的工作流，实现了我们项目所需的Coding Agent!

### 封装 Coding Agent 到 FastAPI

我找到更稳的落点了：直接给 opencode 加一个正式 CLI 子命令，比如 generate-project --prompt ...
这样 FastAPI 只需要调用这个命令拿 JSON，完全绕开“内部再起一个 HTTP 服务”的不稳定链路

我已经封装成功！
现在能稳定输出.json格式的文件。

### 删改opencode大项目结构

这很像我一年前删除Colias项目文件的过程......
已完成并存档。这是目前的baseline版本。

### 流式输出架构

我的流式推送接口应能：
1.我希望前端能展示出当前项目的文件结构文件树、已有的文件。
2.我希望不仅能够展示工作状态，还要有一行或者几行，实时显示LLM正在生成的代码。
3.我希望用“思考状态”展示agent的工作状态。

**推荐接口：**
```

- POST /generate/jobs
  提交生成任务，返回 job_id
- GET /generate/jobs/{job_id}/stream
  SSE 流式输出
- GET /generate/jobs/{job_id}/result
  获取最终 { "files": [...] }
- GET /generate/jobs/{job_id}
  获取任务当前快照
- DELETE /generate/jobs/{job_id}
  可选，取消任务
```

为什么这样设计：
- 前端更容易接。POST 提交，GET 用 EventSource 收流。
- 能断线重连。
- 能同时拿“状态流”和“最终结果”。
- 不破坏现有 /generate。

**SSE 事件设计：**
```
建议统一 JSON，事件名固定。
- job.created
  {"job_id":"gen_xxx","status":"queued"}
- thinking.status
  不传原始 CoT，只传安全摘要
  {
    "job_id":"gen_xxx",
    "phase":"planning",
    "label":"正在规划项目结构",
    "detail":"分析需求，确定模板和最小文件集"
  }
- project.tree
  前端文件树用这个
  {
    "job_id":"gen_xxx",
    "paths":["package.json","scripts/start.sh","src/main.js"]
  }
- file.snapshot
  当前已有文件内容
  {
    "job_id":"gen_xxx",
    "path":"src/main.js",
    "content":"..."
  }
- file.delta
  可选，给前端展示“刚写出来的几行代码”
  {
    "job_id":"gen_xxx",
    "path":"src/main.js",
    "append":"const app = ...\n"
  }
- preview.code
  专门给你第二个需求
  {
    "job_id":"gen_xxx",
    "path":"src/main.js",
    "lines":["const app = ...","app.listen(...)"]
  }
- session.status
  忙闲状态
  {
    "job_id":"gen_xxx",
    "status":{"type":"busy"}
  }
- job.completed
  {
    "job_id":"gen_xxx",
    "file_count":9,
    "result_url":"/generate/jobs/gen_xxx/result"
  }
- job.failed
  {
    "job_id":"gen_xxx",
    "error":"..."
  }
```

**怎么满足 3 个需求：**
```

- 文件树、已有文件：
  用 project.tree + file.snapshot
- 实时显示 LLM 正在生成的代码：
  用 file.delta 或 preview.code
  这个不要依赖模型“口头输出代码”，而要监听真实文件写入
- 用“思考状态”展示 agent 状态：
  用 thinking.status内容来自阶段摘要，不直接暴露模型原始推理后端实现建议基于现有 packages/opencode/src/generate-api.ts 和 packages/opencode/src/server/generate-projectts改：
- Python FastAPI 负责：
    - 创建 job
    - 保存 job 状态
    - 返回 SSE StreamingResponse
- Bun 生成器负责：
    - 输出 JSONL 事件到 stdout
    - 最后一条输出最终 files
- 生成器内部增加 3 类 hook：
    - 阶段变化 hook：发 thinking.status
    - 文件变化 hook：发 project.tree、file.snapshot、preview.code
    - 结束 hook：发 job.completed
```

最重要的一点：thinking.status 不建议传模型原始 reasoning。
建议只传这种：
- 分析需求中
- 规划项目结构中
- 正在编写 package.json
- 正在修复启动脚本
- 正在校验最终结果
这样前端效果够好，也安全。

已实现

  改动在 app.py、packages/opencode/src/generate-api.ts、packages/opencode/src/server/generate-project.ts、packages/opencode/
  test/generate-api.test.ts。

  现在接口是：

  - POST /generate：保留原来的同步返回 { files: [...] }
  - POST /generate/jobs：创建流式生成任务
  - GET /generate/jobs/{job_id}：拿当前快照，里面有文件树、已有文件、预览代码、thinking 状态
  - GET /generate/jobs/{job_id}/stream：SSE 流
  - GET /generate/jobs/{job_id}/result：任务完成后拿最终 { files: [...] }

  流式行为现在支持：

  - 文件树：project.tree
  - 文件内容快照：file.snapshot
  - 代码预览：preview.code
  - 安全的工作状态：thinking.status
  - 任务状态：job.status
  - 最终结果：job.result

  另外，Bun 内部生成入口加了 --stream-jsonl，FastAPI 会把它解析成 job 状态并转成 SSE。同步 /generate 不受影响。reasoning 原文没
  有直接暴露给前端，只保留了状态级事件。

# 2026-03-29

## 毕设毕设！

# 2026-03-30

## 知识学习

#### 对现有工程的思考：我们的目的是什么？

***真正缺的，不是“再造一个能连续对话的 /generate”，而是把 /generate 里更强的那部分能力搬进 web 的标准 session 路径里***

#### 如果是workshop，那重心在于强大的coding agent、在线运行。但“生成自己的openclaw”这样级别的要求难以实现
“贪吃蛇”是远远不够的。目前，coding agent已经足够强大，但在云端运行“用户生成的程序”仍需细致对接

#### 如果是能解决具体需求的agent，那重心在于SKILL.md, 理解需求、细致的构造pipeline，通过多个skill真正去解决问题

#### TODO List

- find skills的SKILL.md, 进一步的，一堆工具skills，如何调用

- 需求分析的SKILL.md

- 不同应用场景，写paper，写report，上网

- AI降重：带上自己的思想;  降重 SKILL.md

- 让claude触手可得

## 实践

#### Coding Agent网页版在线运行

在现有网页应用上加OSS/FC在线运行：

#### 第一阶段
```
  - 从 packages/opencode/src/server/generate-project.ts 抽出“项目 contract 校验”模块。
  - 保留现有规则：模板识别、必需文件、scripts/*.sh 约束、Vite/Vue 版本约束、Python/FastAPI约束。
  - 目标文件建议新建为 packages/opencode/src/server/project-contract.ts 或相近位置。
  - /generate 和 web session 后续都复用这一个模块。
```

#### 第二阶段
```
  - 在 web 端加“在线构建并在线运行模式”开关。
  - 入口优先放在 packages/app/src/components/prompt-input/submit.ts 所在提交链路附近。
  - 这一步只做“把模式标记传到后端 prompt 流程”，不要先做部署。
```

#### 第三阶段
```
  - 扩展 packages/opencode/src/plugin/prompt-enhancer.ts，让它在该模式下启用更强 project contract。
  - 普通聊天不受影响。
  - 项目生成首条消息启用：固定模板规则、输出目录规则、运行脚本规则、可部署规则。
```

#### 第四阶段
```
  - 在标准 session 流里接入“校验失败自动修复”。
  - 不再走临时 /generate session。
  - 在同一 session 内，首轮生成完成后校验；失败时自动追加 repair prompt；成功则结束。
  - 这样 web 的持续对话、流式状态、消息历史都天然保留。
```

#### 第五阶段
```
  - 只约束部署必需接口，不先绑定具体云厂商实现细节。
  - 先稳定：
    scripts/prepare.sh
    scripts/build.sh
    scripts/start.sh
    HOST
    PORT
    WORKSPACE
```

保留 /generate: 作为外部 API、作为 contract 回归测试入口、作为未来批量生成入口

最值得先做的是第 1 步和第 2 步。做完这两步，主路径就从“独立 /generate”转成“web session + 强约束项目模式”。
下一步直接改两处：packages/opencode/src/server/generate-project.ts、packages/opencode/src/plugin/、prompt-enhancer.ts，然后再接 web 的模式开关。

现在 web 版已经接上这条链路了：
新会话输入框里新增了一个持久化的 “Run Online / 在线构建运行” 开关
打开后，首条普通 prompt 会带上在线运行 mode marker；后端prompt-enhancer会据此启用之前加的“在线构建并运行”约束
相关改动在 packages/app/src/components/prompt-input.tsx
packages/app/src/components/prompt-input/submit.ts
packages/opencode/src/plugin/prompt-enhancer.ts
以及新的共享模块 packages/util/src/project-mode.ts

## 知识学习

#### Workshop数据流动、架构细节分析讨论

#### Seminar: World Model

## 实践

#### Debug Web应用

已添加“构建项目”模式，并在前端展示现已生成的文件

带前端版本的完整pipeline已跑通！

现在，对接CUHKSZ的第二前端。

# 2026-04-01

## 知识学习

#### Claude Code 框架

Claude Code 源码泄露...

学一波：[Bilibili: Claude Code源码泄露！首发解读51万行代码！](https://www.bilibili.com/video/BV11zXCBFEMo/?spm_id_from=333.1387.top_right_bar_window_default_collection.content.click)

## 实践

#### [Workshop 架构重构：MVP 版本](https://github.com/Ryannnice/Agent-Do)

我们非常简洁、高效地实现了workshop。

效果很好，并且摒弃了opencode的庞大源代码植入。

优化前端，现在反应简洁迅速美观。

# 2026-04-02

## 知识学习

#### Docker

[Bilibili Docker](https://www.bilibili.com/video/BV1THKyzBER6/?spm_id_from=333.1387.favlist.content.click&vd_source=487ef5084994b81a0ec05eeffa991ed2)

#### 关于项目未来的讨论

教育平台是核心竞争力

下一阶段定位：用户每天早晨五分钟了解AI圈大事，甚至上手实践，学习一二。

## 实践

#### Workshop 架构重构：MVP 版本

Debug, 增添流式输出功能

#### Claude Code 宠物系统修复

已经成功部署运行[“开源”的Claude Code](https://github.com/Ryannnice/claude-code)!

修复了桌面宠物 /buddy 功能！

#### Git Branch

常见 type（非常重要）
```
feature	  新功能	  feature/payment-api
fix   	  修复 bug  fix/order-null-pointer
hotfix  	紧急修复	hotfix/login-crash
refactor	代码重构	refactor/cache-module
docs	    文档修改	docs/api-guide
test	    测试代码	test/user-service
chore	    杂项修改	chore/dependency-update
```

#### Workshop

尝试构建多项目运行时，并展示：

我们发现似乎并不需要FC或者公网URL。

# 2026-04-03

## 知识学习

#### git / docker

- 用 `git pull` 和 `docker compose up --build -d` 熟悉基本更新与重建流程。

这一天原本保留了整段学习对话，这里压缩为日志摘要：

- 学习对象是 `assignment1-basics`，目标是把 Transformer 训练链路真正串起来理解。
- 当天抓住的主线是：
  `文本 -> tokenizer -> token id -> embedding -> Transformer -> logits -> cross entropy -> 反向传播 -> 参数更新`
- 核心代码入口包括：
  `cs336_basics/tokenizer.py`、
  `cs336_basics/model/modules.py`、
  `cs336_basics/model/transformer.py`、
  `cs336_basics/trainer/data_loading.py`、
  `cs336_basics/trainer/utils.py`、
  `cs336_basics/train.py`
- 最重要的认识有 6 点：
  1. 语言模型训练的本质是“给定前文，预测下一个 token”。
  2. `inputs` 是当前 token 序列，`targets` 是右移一位后的监督信号。
  3. Transformer 本体负责把上下文表示加工成下一个 token 的打分 `logits`。
  4. block 的核心结构是 Pre-Norm + Attention + FFN + Residual。
  5. `Linear`、`Embedding`、`RMSNorm`、`SwiGLU`、self-attention、RoPE 是后续必须啃透的基础模块。
  6. 训练闭环可以概括为：采样 -> 前向 -> 计算 loss -> backward -> 更新参数。
- 当天的直接产出：
  - 给 `trainer/data_loading.py`
  - 给 `trainer/utils.py`
    增加了逐行中文注释，作为第一部分学习基线。
- 下一步计划：
  继续理解 `Embedding`、`Linear`、attention 与 `transformer.py` 的整体拼装。

## 实践

#### Docker构建Claude Code

遇到构建docker镜像时候地址错误问题：

- Claude 看起来执行了
- 但改动写进了错误挂载目标
- 当前 session 的真实 workspace/ 还是空的
- 然后 runtime/start 检测不到 index.html / package.json，就返回 400 当前 session 没有可在线运行的项目

问题不是 HTTP 400 本身，而是 Agent-Do 之前把 Claude 子容器的 workspace 挂到了错误的宿主机路径。
AGENT_DATA_HOST_ROOT 在 Backend/WorkShop/.env 里指向了旧机器上的 /root/internship-szdsjyjy/...，
但这台机器真实路径是 /home/ryan/CUHKSZ/Education_Platform/Backend/Agent-Do/data。

- 修正了 Agent-Do 容器内 Docker CLI 的集成，避免之前的 input/output error: 'docker'
- 修正了 Backend/WorkShop/.env 里的 AGENT_DATA_HOST_ROOT，并重启了 agent-do

当前 qwen3-coder-next 这条模型链路有时会“看起来成功，实际上没写任何文件”。
我准备从 WorkShop 侧加兜底：当第一轮生成后没有形成可预览项目时，自动发一轮更强约束的修复 prompt，而不是直接把 runtime/start 400 暴露给前端。

# 2026-04-04

## 知识学习

#### PageAttention
[怎么加快大模型推理？10分钟学懂VLLM内部原理，KV Cache，PageAttention](https://www.bilibili.com/video/BV1kx4y1x7bu/?spm_id_from=333.1391.0.0&vd_source=487ef5084994b81a0ec05eeffa991ed2)

#### Flash Attention
[Flash Attention 为什么那么快？原理讲解](https://www.bilibili.com/video/BV1UT421k7rA/?spm_id_from=333.1391.0.0&vd_source=487ef5084994b81a0ec05eeffa991ed2)

# 2026-04-05

## 毕设毕设！

# 2026-04-06

## 拯救计划很好看
我觉得可以和星际穿越媲美。
太空的浪漫很纯粹。
[Bilibili细节解析](https://www.bilibili.com/video/BV1oSQZBRE8j/?spm_id_from=333.337.search-card.all.click)

# 2026-04-07

## 知识学习

#### AI Station

[AI Station 教程](https://xxl9u0uq9y2.feishu.cn/wiki/LVHvw3GCWiMlV4kjH25clngHnVf)

#### LLM Router

谕书的完整Pipeline

#### Router 综述

#### LLM 路由的概念设计空间
本综述涵盖的范式（参见 1.3 节）为组织和理解文献提供了基础 。
在实践中，现实世界的系统往往同时借鉴了不止一种范式 。
为了补充基于范式的组织方式，路由方法还可以从更广泛的维度进行分类 ：

#### 决策时机 (When)：指路由决策何时做出 。
路由系统可以依赖生成前 (Pre-generation) 决策或生成后 (Post-generation) 决策，也可以采用多阶段过程 。
生成前路由在产生任何输出前选择模型，完全依赖于输入查询的属性；而生成后路由则在产生初始响应后，根据输出质量或置信度信号做出决定 。

#### 使用信息 (What)：路由机制使用的信号丰富程度各不相同 。最简单的方法仅基于查询本身，利用词法或语义特征来刻画请求 。
更进阶的系统还会加入可用模型的元数据来指导选择，如成本、延迟或领域专长 。生成后方法则进一步引入响应级信号，如置信度得分、Token 概率或验证器输出 。

#### 计算方式 (How)：路由决策的计算复杂度差异显著 。一端是简单的阈值规则或基于成本的启发式方法，无需训练即可直接应用 ；
另一端是基于历史表现数据训练的监督分类器，用于预测哪个模型最适合处理给定查询 。
更复杂的方法采用自适应策略，通过与环境的持续交互来更新路由行为 。

#### 主流技术路线
1. 难度感知路由 (Difficulty-aware Routing)
  这是最直观的路线，核心是**“看题下菜”** 。
  原理：在推理前评估查询的复杂度，将简单题分给小模型，难题分给大模型 。
  评估手段：包括启发式规则（如文本长度、词汇稀缺度）、训练专门的分类器（如你计划使用的 0.5B 模型）或使用 “LLM 作为评判者” 。
  代表案例：BEST-Route（动态分配并选择采样策略）和 VLLM Semantic Router（识别是否需要开启昂贵的思维链推理） 。
2. 人类偏好对齐路由 (Human Preference-aligned Routing)
  不看“对错”，看**“好坏”** 。
  原理：模拟人类的主观评价，预测大模型生成的答案是否会比小模型显著“更好” 。
  训练数据：利用 Chatbot Arena 等人类真实偏好数据或 LLM 自动生成的对比数据 。
  代表案例：RouteLLM（预测强模型是否会胜出）和 Arch-Router（允许用户自定义不同领域的路由偏好） 。
3. 基于聚类的路由 (Clustering-based Routing)
  核心是**“找规律”** 。
  原理：利用无监督学习（如 K-means）将语义相似的查询聚类，并为每个簇分配表现最好的模型 。
  优势：具有极强的扩展性，添加新模型时无需重新训练路由器，只需测试新模型在各个簇上的表现即可 。
  代表案例：UniRoute 和 Avengers-Pro 。
4. 强化学习路由 (Reinforcement Learning Routing)
  核心是**“实战进化”** 。
  策略优化：通过多步交互（思考 -> 路由 -> 再思考）迭代改进答案，适合复杂推理，但延迟较高（如 Router-R1） 。
  在线老虎机 (Bandit)：在实时交互中通过用户反馈（点赞/踩）动态调整路由策略，平衡“探索新模型”与“利用已知强模型” 。
  代表案例：MixLLM（实现 97% 的 GPT-4 质量且仅需 24% 的成本） 。
5. 基于不确定性的路由 (Uncertainty-based Routing)这是你项目中 Logprobs 熵值 策略的理论依据 。
  原理：监控模型对自身回答的“信心” 。如果内部数学信号（如概率分布）显示模型在犹豫，则触发升级 。
  关键点：研究证明，模型内部的探测信号（Logits）远比模型自己口头说的“我很确定”要准得多 。
  代表案例：CP-Router（利用共形预测处理不确定性） 。
6. 级联系统 (Cascading)这是你项目中 Binary Gate 和逐级踢球架构的归属 。
  原理：顺序执行。先让小模型试，不行再给中模型，最后大模型保底 。
  核心逻辑：引入了“后悔药”机制，通过自我验证或外部评估器决定是否停止或升级 。
  代表案例：FrugalGPT（三大组件：路由器、质量评估器、停止判断器）和 AutoMix 。

# 2026-04-08

## 实践

搭建了自己的完整Pipeline
质量不变的情况下，cluster方法效果最好，成本降低了 ***10%***

## 知识学习

#### Router 经典论文总结
本文档面向后续逐篇复现，聚焦综述 《Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey》 中以下三节的代表性工作：

Section 2: Difficulty-aware Routing
Section 6: Uncertainty-based Routing
Section 7: Cascades
整理原则：

只优先采用原论文、官方项目页、官方代码仓库、会议页面。
如果某些细节在摘要页看不到，我会明确标注“需要补读 PDF/附录”。
如果仓库 README 展示的是论文发布后的扩展结果，我会明确写成“仓库后续更新”，避免和论文主结果混淆。
一页结论
如果你接下来要逐一复现，我建议按这个顺序推进：

AutoMix：代码、数据、任务说明最完整，最适合先跑通一个 cascade 基线。
FrugalGPT：工程可用性强，官方仓库完整，适合改造成商业 API 版本。
BEST-Route：代码完整，但包含 reward model、best-of-n、多阶段数据构造，工程复杂度高于前两者。
GraphRouter：官方代码已放出，但图构建与数据预处理更复杂。
EmbedLLM：数据和代码齐全，但更像“模型表示学习 + routing 下游头”，对实验环境要求更高。
CP-Router：训练自由、思路清晰，但我当前未检索到官方代码，复现需要自己补实现。
Self-REF / Learning to Route LLMs with Confidence Tokens：论文价值高，但目前未检索到官方公开代码。
Confidence-Driven LLM Router：适合后续用商业 API 重做，但目前主要能拿到论文页面信息，代码未公开。

#### 开源Router方案总结
本文档对 4 个你点名的开源 router / router 模型做统一拆解：

1. `RouteLLM`
2. `semantic-router`
3. `notdiamond-0001`
4. `knn-router`
整理维度尽量与 `经典论文.md` 保持一致：
- 项目定位
- 相关论文或技术来源
- 数据集
- 测试用大模型 / 候选模型池
- router 模型 / 机制
- 效果 / benchmark
- 创新点
- 实验与工程形态
- 开源代码位置
- 复现建议

#### RouteLLM

这一段原本保留了完整的操作指令，整理后保留关键信息：

- `RouteLLM` 的 GSM8K 基本链路已经打通，2 题 smoke test 可以分别产出 strong / weak model 结果。
- 当时最后的阻塞点只是 `outputs/` 目录不存在，后来已经补成自动创建。
- 关键修复包括：
  - `bert` 路径不再强依赖 `OPENAI_API_KEY`
  - `openai_server.py` 不再在 import 阶段崩溃
  - `gsm8k.generate_responses` 支持自定义模型对和输出文件
  - 评测脚本可以直接读取自定义 GSM8K 响应 CSV 并做可视化
- 固定执行顺序被整理成：
  1. 保持 `routellm.openai_server` 运行
  2. 先做 5 题 smoke test
  3. 成功后再跑全量生成
  4. 最后执行 evaluate 出图
- 这一段最重要的收获不是命令本身，而是把 `RouteLLM` 的“响应生成 -> 评测 -> 可视化”链路真正跑通了。

# 2026-04-09

## 尝试更多的开源策略

#### [RouteLLM](https://github.com/aurelio-labs/semantic-router)

准确率（Accuracy）:

在 GSM8K 数据集上，不同策略的表现如下：
策略              准确率 (Accuracy)    相比 Random 的提升                     评价
Random (随机)        88.93%                  -                     基准线：无脑混合强弱模型的结果。
Causal_LLM         0.52%+1.59%           显著胜出：                成功识别了模型专长，捕获了互补性 。
MF (矩阵分解)      90.30%+1.37%           优于随机：                即使只有部分数据，也展现了预判能力。
BERT/SW_Ranking     ~88.7%             -0.2%(负优化)           低于随机：说明这些路由器在数学逻辑上出现了误判。

策略,               准确率 (Accuracy),   成本 (CNY),性能/成本效率评价
Weak (7B),          85.90%,0.58,        成本极低，但存在能力天花板
Strong (72B),       92.87%,1.77,        准确率最高，但成本是 7B 的 3.06 倍
Causal_LLM (Router),90.52%,1.20,        最优解：用 67% 的成本换取了 97.5% 的最强性能

# 2026-04-10

## 尝试更多的开源策略

#### 现有Pipeline

- `llmrouter` 当前主链路是：
  数据合并与切分 -> 全模型 benchmark -> 自动打 tier 标签 -> 训练 classifier / 调 cascade 阈值 -> test 集统一评测 -> 出图。
- benchmark 阶段才会真实调用各模型；训练和评测阶段主要基于已保存结果做监督训练或离线模拟。
- 因此当前 accuracy / cost 基本可直接比较，但 flat router 自身的 routing latency 并没有被完整计入。
- 当前主评测策略包括：
  `baseline-32b / 14b / 7b / 3b / 1.5b`、
  `random`、
  `oracle`、
  `cascade-default`、
  `cascade-optimized`、
  `classifier`、
  `binary-gate-logprobs`

#### [Semantic-router](https://github.com/aurelio-labs/semantic-router)
- 我把 `semantic-router` 理解成“检索式分类器”，它更适合先以 `query -> predicted_label` 的形式接入 Phase 3 evaluation，而不是直接改 benchmark 主干。
- 接入思路被收敛为：
  - 用 `unified/train` + `routing_labels` 构建 5 路 semantic routes
  - 对 `unified/test` 做 semantic routing
  - 输出 `predicted_label`
  - 复用现有 `simulate_strategy` 和 metrics
- 需要提前注意的风险：
  - 路径硬编码较多
  - 需要可用的 encoder backend
  - Python 3.13 对部分本地 encoder 兼容性一般
  - 当前延迟口径仍不是端到端 latency
- 已完成远程单独评测：
  - Accuracy: 68.18%
  - Cost Ratio: 25.9%
  - Avg Latency: 857ms
  - P99 Latency: 8308ms
- 相对位置：
  - 比 `classifier` 更准，但成本更高
  - 略低于 `cascade-optimized` 的准确率，但延迟明显更好
- 远程结果和对比文件都已经单独保存，后续可以直接回看 summary / comparison 产物。

#### Router Latency

- 我专门确认了一个问题：论文和综述通常会提到 latency / overhead，但很少把 `router decision latency` 单独定义为最终实验指标。
- 更常见的口径仍然是端到端响应时间，因此 router 本身的额外决策开销在很多对比里其实是模糊的。

- 当前诊断已经比较明确：
  - route 分布严重不平衡，32B route 太小
  - hardest 样本识别不足
  - 排除 `all_wrong` 样本会进一步削弱 hardest route
- 后续调参顺序也已经确定：
  1. 先加 `all_wrong`
  2. 再做 per-route cap，处理类不平衡
  3. 最后再调 `top-k` 和 aggregation
- 已跑出的关键实验结果：
  - `semantic_router_gpu`: 68.18% / 25.9%
  - `include_all_wrong`: 68.91% / 33.2%
  - `include_all_wrong + cap2000`: 70.29% / 36.7%
  - `include_all_wrong + top5 + max`: 62.94% / 20.6%
  - `bge-m3 + include_all_wrong`: 68.72% / 31.8%
  - `bge-m3 + include_all_wrong + cap2000`: 69.34% / 33.7%
- 这一轮最重要的结论是：真正决定效果的不是“semantic-router”这个名字，而是 route 形态、数据分布和 threshold 策略。

# 2026-04-11

## 实践

#### 追求极致的正确率

- 当前 best semantic-router: 79.61% / 97.2%
- 提升是 +0.08 个点 accuracy，同时成本从 100% 降到 97.2%

最新结果：
  跑完了 4 组cost <= 40% 的 semantic-router 新实验。当前最优是：
  - semantic_router_override14b_7b_meta_mpnet_cost40_fresh4xa100
  - Accuracy: 76.28%
  - Cost Ratio: 38.6%
  - Avg Latency: 1054ms
  - P99 Latency: 9744ms

  关键配置：
  - encoder: sentence-transformers/all-mpnet-base-v2
  - routing mode: 32b-override 这一套逻辑被我用作“base model default + semantic override”，这里 base 是 qwen2.5-14b
  - override candidate: qwen2.5-7b
  - text fields: dataset,subject,difficulty
  - tuned threshold: qwen2.5-7b = 0.8628563005596404
  - routing distribution: qwen2.5-14b = 4935, qwen2.5-7b = 1514

#### 已知方案总体对比

| 策略 | 准确率 | 相对成本 | 平均延迟 | P99 延迟 |
|------|--------|----------|----------|----------|
| Always 32B | 79.53% | 100.0% | 1539ms | 18354ms |
| Always 14B | 76.73% | 43.7% | 1248ms | 13021ms |
| Always 7B | 72.58% | 22.1% | 659ms | 4878ms |
| Always 3B | 63.92% | 9.4% | 621ms | 4673ms |
| Always 1.5B | 55.93% | 4.7% | 624ms | 4280ms |
| Random | 69.64% | 36.6% | 897ms | 7977ms |
| Oracle | 90.80% | 20.3% | 824ms | 6848ms |
| Cascade (default) | 62.35% | 10.3% | 951ms | 6759ms |
| Cascade (optimized) | 68.85% | 24.7% | 2053ms | 21973ms |
| Binary Gate (logprobs) | 68.85% | 24.7% | 2053ms | 21973ms |
| Classifier (0.5B) | 60.89% | 12.3% | 765ms | 6386ms |
| Semantic Tiered MiniLM cap2000 | 70.71% | 37.2% | 968ms | 9624ms |
| Semantic Tiered MiniLM cost33 | 70.12% | 33.8% | 942ms | 9019ms |
| Semantic Tiered MiniLM cost35.5 | 70.62% | 36.8% | 963ms | 9503ms |
| Semantic Override 32B->14B MPNet | 79.61% | 97.2% | 1525ms | 17398ms |
| Semantic Override 14B->7B MPNet | 76.28% | 38.6% | 1054ms | 9744ms |
| Semantic Override 14B->3B MPNet | 74.57% | 35.7% | 1017ms | 9050ms |
| Semantic Override 14B->1.5B/3B MPNet | 73.67% | 35.1% | 1023ms | 8919ms |

#### 最新 Semantic Router 内部对比

| 方案 | Encoder | 路由形式 | 关键设置 | 准确率 | 成本 |
|------|---------|----------|----------|--------|------|
| Tiered MiniLM cap2000 | all-MiniLM-L6-v2 | 五路 tiered | include_all_wrong + cap2000 | 70.71% | 37.2% |
| Tiered MiniLM tuned cost33 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.33 | 70.12% | 33.8% |
| Tiered MiniLM tuned cost35.5 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.355 | 70.62% | 36.8% |
| Override 32B->14B MPNet | all-mpnet-base-v2 | 32B 默认，命中后降到 14B | metadata: dataset/subject/difficulty，threshold=0.9364 | 79.61% | 97.2% |
| Override 14B->7B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 7B | metadata: dataset/subject/difficulty，threshold=0.8629 | 76.28% | 38.6% |
| Override 14B->3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 3B | metadata: dataset/subject/difficulty，threshold=0.8585 | 74.57% | 35.7% |
| Override 14B->1.5B/3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 1.5B/3B | metadata: dataset/subject/difficulty，threshold=0.8818 | 73.67% | 35.1% |

#### 关键结论
1. **Semantic Router 的当前最高准确率方案**是 `32B 默认 + 14B override + MPNet + metadata`，达到 **79.61% / 97.2%**。相比 Always 32B，准确率仅提高 **0.08** 个百分点，成本下降 **2.8** 个百分点，收益很小，但它证明 semantic override 已经可以做到几乎不掉点。
2. **在 cost <= 40% 约束下，当前最优方案**是 `14B 默认 + 7B override + MPNet + metadata`，达到 **76.28% / 38.6%**。相比 Always 14B，准确率只低 **0.45** 个百分点，但成本少 **5.1** 个百分点。
3. **旧的 tiered semantic-router 已经被 override 方案明显压制。** 最好的 tiered 版本是 `include_all_wrong + cap2000`，只有 **70.71% / 37.2%**；而 `14B->7B override` 在几乎相同成本下把准确率再拉高了 **5.57** 个百分点，成本只增加 **1.4** 个百分点。
4. **真正带来提升的不是“semantic-router”这个名字本身，而是方案形态变化。** 从五路 tiered 改成“强模型默认 + 低一级模型 override”，再叠加 `all-mpnet-base-v2` 和结构化 metadata，效果才明显跃升。
5. **如果目标是把 semantic-router 接到现有 llmrouter pipeline 做单独验证，当前最值得保留的候选只需要两条：**
   - `semantic-override32b-14b-mpnet-meta-acc`：用于验证语义路由的准确率上限。
   - `semantic-override14b-7b-mpnet-meta-cost40`：用于验证成本受限场景下的真实收益。

#### 和已有 Router 方案的相对位置
- 相比 `classifier`，`14B->7B semantic override` 准确率从 **60.89%** 提升到 **76.28%**，但成本也从 **12.3%** 提升到 **38.6%**。
- 相比 `cascade-optimized` / `binary-gate-logprobs` 的 **68.85% / 24.7%**，`14B->7B semantic override` 在准确率上高出 **7.43** 个百分点，但成本也更高。
- 在“可直接上线的简单策略”里，Always 14B 仍然是很强的朴素基线：**76.73% / 43.7%**。Semantic override 的价值在于把这条强基线压到 40% 左右成本时，仍能尽量保留准确率。

## 知识学习

#### 参数矩阵 Checkpoint
参数矩阵只保存某些checkpoint：
训练时，**时间换空间**

为什么 checkpoint 不只存第一层：
反向传播需要 每一层的输入激活值。如果只存第一层：
L1 (存)
L2
L3
L4
反向传播时会反复从 L1 重新算：
L1→L2→L3
L1→L2
...
计算量会爆炸。因此实际做法是 每隔几层存一个：
L1 (存)
L2
L3
L4 (存)
这样反向时最多只需要 重新算中间几层，计算量可控，同时减少显存。

# 2026-04-12

## 知识学习

#### assignment1-basics/cs336_basics/trainer/utils.py

#### assignment1-basics/cs336_basics/model/modules.py

#### einsum()

#### 常见显卡

#### LLM参数量估算

#### MoE模型

#### PPO/GRPO/DPO

```
# 定义前向传播：给定输入 x，输出线性变换后的结果。
def forward(self, x: torch.Tensor) -> torch.Tensor:
    # 用 einsum 实现矩阵乘法。
    # 这里的含义是：
    # 输入 x 的最后一维是 d_in，
    # 权重 weight 的形状是 (d_out, d_in)，
    # 输出的最后一维就变成 d_out。
    return einsum(x, self.weight, '... d_in,  d_out d_in -> ... d_out')
```

# 2026-04-13

## 实践

1. Semantic Router 的流程

这版实现入口在 llmrouter/src/router/semantic_router_strategy.py 和 llmrouter/src/evaluate/run_evaluation.py。

**完整流程**
```
1. 从训练集读取已标注样本。
   代码会把 /tangboyan/llmrouter/data/unified/train.jsonl 和 /tangboyan/llmrouter/results/labels/routing_labels.jsonl 对齐，只保留 unified train 里的 query。对应 load_train_labeled_queries()。
2. 把每条训练样本变成 semantic text。
   默认就是 query 本身；如果开了 semantic-text-fields，会把 dataset/subject/difficulty 这类 metadata 也拼进去。对应 build_semantic_text()。
3. 按路由目标组织成 route。
   当前支持两种模式：
    - tiered：5 路分类，直接建 1.5b / 3b / 7b / 14b / 32b 五个 route。
    - 32b-override：不是五路平权，而是“默认强模型 + 若干小模型 override”。例如 14B 默认，7B override。对应 prepare_route_training_records()。
4. 用预训练 encoder 建索引。
   每个 route 里放一批 utterances，semantic-router 用 HuggingFaceEncoder 编码后建立向量索引。对应 build_routes() 和 build_semantic_router_from_train_records()。
5. 推理时对测试 query 编码并检索。
   对测试 query 用同一个 encoder 编码，检索 top-k 相似 utterances，然后按 route 聚合分数。对应 score_routes_for_vector()。
6. 决策。
    - 如果是普通 tiered 且没调阈值：直接取 router 返回的最佳 route。
    - 如果开了 threshold tuning：按阈值判断，没过阈值就 fallback 到默认大模型。
    - 如果是 32b-override：必须走 threshold 逻辑，否则代码直接报错。对应 choose_route_with_thresholds() 和 run_semantic_router_inference()。
7. 评测。
   路由结果不会真实再调模型，而是去查已经离线跑好的 benchmark 结果，看被路由到的模型在该题上是否答对，然后统计 accuracy / cost / latency。对应 simulate_strategy() 和 compute_all_metrics()。
```

2. 测试用了什么数据集？
测试集是 unified_test，入口写在 llmrouter/src/evaluate/run_evaluation.py。
具体是：
- 测试切分文件：/tangboyan/llmrouter/data/unified/test.jsonl
- 训练切分文件：/tangboyan/llmrouter/data/unified/train.jsonl
- 评测时会读取 5 个模型在各数据集上的 benchmark 结果，再筛出 unified_test 里的 query
- 当前这套 v2_5tier 评测覆盖的数据集，从结果里看是：
    - agieval
    - ceval
    - cmath
    - cmmlu
    - gsm8k
    - logiqa2
当前统一测试集规模是 6449 条。

3. Semantic Router 需要训练吗？
结论：不需要像 classifier 那样做参数训练。
- classifier：要训练一个新模型
- semantic-router：不训练新分类器参数，只是“拿预训练 embedding 模型 + 训练集样本建语义路由索引”

**semantic-router**
```
- 需要一套已标注的训练样本，用来构建 route utterances
- 需要一个预训练 encoder，例如你现在用过的：
    - sentence-transformers/all-MiniLM-L6-v2
    - sentence-transformers/all-mpnet-base-v2
- 可选地需要做一次阈值调优，但这不是模型训练，只是用训练集里再切一小块验证集做搜索
```

现在这版代码里，threshold tuning 也只是：
- 切一部分 unified_train
- 搜索阈值
- 选 accuracy/cost 最优点
不是 gradient finetune。

## 知识学习

#### 为什么不直接存“参数矩阵的转置”？

Y = X x W^T

你可能会问：既然都要转置，为什么不直接把 self.weight 定义成 (in_features, out_features)？

答案是：为了计算效率（和历史习惯）。
逻辑直观：在 (out, in) 的存储方式下，weight[0]（矩阵的第一行）直接对应于第一个输出神经元的所有权重。这在逻辑上非常清晰。
算子优化：底层硬件（如 NVIDIA GPU）在执行 Linear 算子时，针对这种存储方式做了深度优化。

#### 常见数据类型详解

通过浮点数的三个组成部分来理解它们：
符号位（Sign）、指数位（Exponent，决定范围）和尾数位（Fraction/Mantissa，决定精度）。

#### FP32 (Full Precision / Single Precision)
结构： 1位符号，8位指数，23位尾数。
特点： 精度极高，数值范围广。
LLM 中的角色： 曾经是标准。但在如今的 LLM 训练中，它通常只作为“主权重（Master Weights）”存在，用来在优化器更新时保持微小的梯度变化。

#### FP16 (Half Precision)
结构： 1位符号，5位指数，10位尾数。
优点： 内存占用减半，计算速度极快。
缺点： 数值范围窄（最大约 65504）。在训练 LLM 时，极易产生“梯度溢出（Overflow）”或“下溢（Underflow）”，导致训练崩溃。
对策： 需要使用混合精度训练（Mixed Precision Training）和损失缩放（Loss Scaling）。

#### BF16 (Brain Floating Point 16) —— LLM 的宠儿
结构： **1**位符号，**8**位指数，**7**位尾数。
特点： 它是 Google 为了深度学习专门设计的。它的指数位与 FP32 一样长。
为什么好用： 它的精度（尾数）虽然不如 FP16，但它的数值范围（Range）和 FP32 完全一样。
意义： 在训练 LLM 时，你不需要担心梯度溢出，不需要搞复杂的 Loss Scaling。目前主流的大模型（Llama 3, GPT-4 等）基本都采用 BF16 进行预训练。

#### einsum()
通过 einsum，即使输入是一个高维张量（例如 x 的形状是 (batch_size, L, d_model)），我们仍然可以通过 广播 规则来进行矩阵乘法（在这种情况下，广播会自动应用到批次维度和其他维度）。
所以，即使 x 不是二维矩阵，einsum 也能处理高维张量并正确地进行矩阵运算，保证维度匹配。

# 2026-04-14

## 知识学习

#### vLLM Semantic Router
是一个面向 多模型系统 的“语义路由与运行控制层”，不是单纯的模型网关，也不是只做学术路由实验的分类器。
它的官方定位是：在云、数据中心、边缘侧，为 Mixture-of-Models 提供系统级智能路由。README.md
- 不同模型在能力、成本、延迟、隐私边界上差异很大，单一模型很难覆盖所有流量。
- 真实请求不仅要“选模型”，还要同时处理安全、缓存、记忆、RAG、工具调用、回放审计等系统能力。
- 路由逻辑不能只停留在一个分类器上，而要变成可配置、可验证、可部署、可观测的运行时系统。
这个项目本质上更像一个 LLM 流量控制平面。它位于客户端和后端模型之间，理解请求，再决定走哪条路、用哪个模型、是否启用插件能力、是否需要额外的安全或工具策略。README.md docs/agent/repo-map.md

#### 系统架构
把“路由”拆成了几个清晰层次，而不是用一个黑盒分类器直接输出模型名：
- signal evaluation
- projection coordination
- decision selection
- model selection
- plugin handling
在 AMD 参考 profile 里，这条链路写得很明确：先做多种信号检测，再做投影/分区，再选路由决策，最后把请求转发到对应模型别名。deploy/amd/README.md

- Signals：检测层。定义“识别到了什么”。支持关键词、语言、上下文长度、结构、权限、embedding、domain、complexity、fact-check、jailbreak、PII、preference、reask、user-feedback、knowledge base 等。website/docs/tutorials/signal/overview.md
- Projections：协调层。把多个弱信号合成为可复用的中间事实，比如 intent partition、difficulty band、verification_required 这类 band，而不是把数值逻辑散落在每个 route 里。website/docs/tutorials/projection/overview.md
- Decisions：策略层。用布尔规则、优先级、tier 选出一条 route。这里是“哪条策略赢”。website/docs/tutorials/decision/overview.md src/semantic-router/pkg/config/decision_config.go
- Algorithms / Model Selection：候选模型选择层。一个 decision 可以挂多个候选模型，再用静态或学习式算法选最优，包括 static、elo、router_dc、automix、hybrid、rl_driven、gmtrouter、latency_aware，以及 looper 类的 confidence、ratings、remom。config/README.md src/semantic-router/pkg/extproc/req_filter_classification_runtime.go src/semantic-router/pkg/modelselection/selector.go
- Plugins：路由后处理层。匹配到某条 route 后，可以附加 route-local 行为，比如 semantic cache、RAG、memory、router replay、tools、system prompt、request params、content safety、hallucination、response jailbreak、image generation 等。website/docs/tutorials/plugin/overview.md

不只是“把问题分类到模型”，而是在做 信号驱动的策略编排:
比如可以先识别“这是法律高风险请求”，再叠加“需要核验来源”“上下文很长”“用户在追问纠错”，最后才决定走 premium specialist 路线，并启用相应插件。

#### 配置与运行方式
这个项目的另一大特点是配置体系比较完整，而且是统一的。
它采用一套 canonical YAML 合同：
- version
- listeners
- providers
- routing
- global
其中：
- routing 负责语义路由本身，包括 modelCards、signals、projections、decisions
- providers 负责具体部署绑定和默认模型
- global 负责全局运行时能力，比如 observability、router replay、stores、tools、looper、modelcatalog 等。这套约定写在公开配置文档里，也被仓库测试强约束。website/docs/installation/configuration.md configREADME.md

此外，这个项目同时支持两种配置视角：
- YAML canonical config
- DSL authoring surface
也就是说，用户既可以直接写 config.yaml，也可以用 DSL/可视化编辑器去表达路由图，然后再编译回canonical YAML。这让它既适合工程部署，也适合调参和策略设计。
website/docs/installation/configuration.md

在部署侧，它不是单一路径，而是支持多种环境：
- 本地 CPU 开发
- 本地 AMD/ROCm 开发
- Kubernetes / Helm / Operator
- Dashboard 控制台
- E2E profile 驱动的测试环境

仓库文档给出的本地默认流程是：
- make vllm-sr-dev
- vllm-sr serve --image-pull-policy never
对应 CPU / AMD 两套本地环境说明也很清楚。docs/agent/environments.md

#### 仓库组成
从代码组织上看，这个仓库已经不是一个单体 router，而是一整套平台：
- src/semantic-router：Go 核心路由器，包含 config、classification、decision engine、Envoy extproc、selection、plugin runtime。
- src/vllm-sr：Python CLI，负责本地启动、配置校验、Docker 编排、开发体验。
- dashboard：前后端控制台，用于配置编辑、部署、状态查看、playground、可视化。
- deploy/operator：Kubernetes Operator 和 CRD。
- deploy/helm：Helm chart。
- src/training：模型选择与分类相关训练脚本、数据、推理服务。
- e2e：端到端测试框架，覆盖 routing、safety、cache、response-api、dashboard、authz、streaming 多 profile。
- candle-binding ml-binding nlp-binding：Rust/native bindings，用于更底层的推理或 ML 能力接入。

**架构图**
```
  Authoring / Control Plane
    Dashboard / DSL / YAML / CLI / Helm / Operator
          |
          v
  Canonical Config v0.3
    version / listeners / providers / routing / global
          |
          v
  Runtime Plane
    Client
      -> Envoy
      -> semantic-router extproc (OpenAIRouter)
         -> Signals
         -> Projections
         -> Decisions
         -> Algorithms / Looper
         -> Route-local Plugins
         -> Provider binding / endpoint selection / alias rewrite
         -> Upstream model backends
      <- Response filters / replay / cache / warnings / headers
          |
          v
  Observability / Replay / Dashboard Insight

  Validation / Support Plane
    E2E profiles / deploy recipes / training stack / Rust-native bindings
```
这张图背后的关键点是：
- 这套系统有一个统一配置合同，不是 CLI 一套、Dashboard 一套、Operator 一套。仓库明确把入口统一为 version / listeners / providers / routing / global，其中 routing 负责 `modelCards5), website/docs/tutorials/projection/overview.md:9, website/docs/tutorials/decision/overview.md:7, website/docs/tutorials/algorithm/overview.md:7, website/docs/tutorials/plugin/overview.md:5, deploy/amd/README.md:100)
- 仓库形态也说明它是平台，不是单一 router binary。src/semantic-router 是 Go 路由内核，src/vllm-sr 是 Python CLI，dashboard/ 是控制台，deploy/operator/ 和 deploy/helm/ 是 K8s 部署面，e2e/ 是验证框架，src/training/ 和 Rust bindings 是算法/模型支持层。(docs/agent/repo-map.md:3)

所以一句话说，它更像“LLM 流量控制平面 + 运行时策略编排层”，而不是“模型网关 + 少量规则”。

#### 一次请求怎么被路由
1. 启动阶段先由 vllm-sr serve 做 bootstrap，解析配置、选择 Docker/K8s backend、准备 runtime config，然后把本地或集群拓扑拉起来。(src/vllm-sr/cli/commands/runtime.py:57, src/vllm-sr/cli/commands/runtime.py:214)
2. 真正请求进入时，Go 侧的 OpenAIRouter 作为 Envoy extproc server 工作。它不是只处理 request body，而是完整跑四个阶段：request headers -> request body -> response headers -> response body。(src/semantic-router/pkg/extproc/router.go:24, src/semantic-router/pkg/extproc/processor_core.go:48)
3. request headers 阶段会先抓 request_id、:path、:method、streaming 预期、looper 内部请求标记等。也就是说，这里先决定“这是普通 chat、Response API、models 接口，还是 looper 内部调用”。(src/semantic-router/pkg/extproc/processor_req_header.go:17)
4. request body 阶段先走一个快路径：如果是 Response API，就先翻译成 chat completions 形态；然后做 body 校验；再用 fast extractor 直接拿到 model / userContent / firstImageURL / stream，避免一开始就完整反序列化。(src/semantic-router/pkg/extproc/processor_req_body.go:22, /home/ryan/CUHKSZ/LLM-Router/V:61, src/semantic-router/pkg/decision/engine.go:60, src/semantic-router/pkg/decision/engine.go:199)
5. decision engine 本身是个布尔规则树求值器。叶子节点是 type + name，支持 AND / OR / NOT，命中后会得到 confidence；多个 decision 都命中时，再按 tier -> confidence -> priority 或 priority -> confidence 选出最终 route。(src/semantic-router/pkg/config/decision_config.go:3, src/semantic-router/pkg/decision/engine.go:151, src/semantic-router/pkg/decision/engine.go:335)
6. route 选出来以后，不一定立刻等于“最终模型已定”。
如果用户显式指定模型，router 会保留原模型，但仍然保留 decision 结果给插件使用。
如果用户走的是 auto model，router 才会根据 decision.modelRefs + decision.algorithm 去做候选选择。(src/semantic-router/pkg/extproc/req_filter_classification_runtime.go:138, src/semantic-router/pkg/extproc/req_filter_classification.go:61)
7. 候选模型选择分两类。单模型选择算法走 selector registry，比如 static / elo / router_dc / automix / hybrid / rl_driven / gmtrouter / latency_aware / knn / kmeans / svm。多模型编排算法走 looper，比如 confidence / ratings / remom。(website/docs/tutorials/algorithm/overview.md:55, src/semantic-router/pkg/selection/factory.go:96, src/semantic-router/pkg/extproc/req_filter_looper.go:45)
8. 在真正发往上游前，router 还会跑一组 route-local 行为：fast_response、rate limit、semantic cache short-circuit、RAG 检索、modality 处理、memory 注入、request params、system prompt、tools 选择。然后才做 endpoint 选择、alias 到 provider-specific model id 的映射，并把修改后的 body 发给上游。(src/semantic-router/pkg/extproc/processor_req_body_prepare.go:63, src/semantic-router/pkg/extproc/req_filter_rag.go:19, src/semantic-router/pkg/extproc/processor_req_body_routing.go:28, src/semantic-router/pkg/extproc/processor_req_body_routing.go:65, /home/ryan/CUHKSZ/LLM-Router/VLLM-sem)

把这 12 步压成一句话就是：
客户端只发出一次 OpenAI 兼容请求，但 router 在内部实际完成了:
“请求理解、信号抽取、投影协调、策略命中、候选模型选择、插件执行、后端绑定、响应审计与告警”
这整条系统链路。


# 2026-04-15

# 2026-04-16


# 2026-04-17

## 知识学习

### RoPE

- 今天把 RoPE 的几何直觉重新想清楚了：一个 `D` 维向量会被拆成 `D/2` 个二维平面，每个平面都以原点 `(0, 0)` 为旋转中心。
- 第 `k` 个平面由 `(x_{2k}, x_{2k+1})` 组成，位置编码的本质就是把这一对坐标绕原点旋转角度 `theta_k`。
- 不同平面之间是正交、互不干涉的：
  - 平面 0 只影响 `(x0, x1)`
  - 平面 1 只影响 `(x2, x3)`
  - 各平面独立旋转，不会互相混入
- 它们唯一的系统性联系是频率分布：
  - 低频平面旋转慢，更偏向捕捉长距离关系
  - 高频平面旋转快，更偏向捕捉短距离细节

### 维度与旋转

- 另一个关键理解是：RoPE 不是“单维缩放”，而是二维成对旋转。
- 在第 `k` 个平面中：
  - `x_{2k}` 是横坐标
  - `x_{2k+1}` 是纵坐标
  - 它们共同组成平面上的点 `P`
- 当 token 位于第 `m` 个位置时，这个点会被旋转 `m * theta_k`。
- 旋转后的核心性质：
  - 方向改变
  - 向量长度不变
  - 因而保留了幅值信息，同时把位置信息写进方向关系里
- 这也解释了为什么必须“成对旋转”：
  只动一个维度会更像缩放；只有 `(x_{2k}, x_{2k+1})` 联动，才是真正的圆周旋转。

对应代码理解：

```python
x = rearrange(x, '... (s r) -> ... s r', r=2)

[
  [x0, x1],   # 第 1 个平面的坐标
  [x2, x3],   # 第 2 个平面的坐标
  ...
  [x62, x63]  # 第 32 个平面的坐标
]
```

这段代码本质上就是把一维向量按两维一组重排，显式变成“多个二维旋转平面”。



### 代码实现详解

``` RoPE
    def rotate_tensor(self, x: torch.Tensor) -> torch.Tensor:
        '''
        create a rotated tensor (x_2k, x_2k+1) -> (-x_2k+1, x_2k)
        '''
        # 先把最后一维按两两一组重排：
        # (..., Dh) -> (..., Dh/2, 2)
        # 最后那个长度为 2 的维度分别存放偶数位和奇数位。
        x = rearrange(x, '... (s r) -> ... s r', r=2)

        # 拆出每一对中的偶数位和奇数位。
        x_even, x_odd = x.unbind(dim=-1)

        # 完成二维平面旋转中的“正交向量”构造：
        # (x_even, x_odd) -> (-x_odd, x_even)
        x = torch.stack((-x_odd, x_even), dim=-1)

        # 再还原回原始最后一维的布局，方便和输入逐元素相乘。
        return rearrange(x, '... s r -> ... (s r)')
```

1. 核心算子：从“一排”到“一对” (rearrange)
在进行旋转前，必须将平铺的隐藏维度 Dh 进行两两分组。

代码：x = rearrange(x, '... (s r) -> ... s r', r=2)

形状流：(..., 64) -> (..., 32, 2)

意义：物理上确立了 32 个平面。最后一维的 2 代表每个平面内的坐标点 (x_even, x_odd)。

2. 拆解与重组：实现 90° 垂直旋转
RoPE 的旋转公式中，关键在于构造 rotate_half(x)。其内部逻辑如下：

A. 拆分 (unbind)
操作：x_even, x_odd = x.unbind(dim=-1)

维度变化：

x (原变量): 保持 (..., 32, 2) 不变。

x_even / x_odd (新变量): 变为 (..., 32)。最后那个 2 被拆掉了。

直观理解：像是把一叠双层卡片拆成了“上层”和“下层”两堆。

B. 取反与配对 (stack)
操作：x_rotated = torch.stack((-x_odd, x_even), dim=-1)

逻辑：这里的 stack 会新建一个维度，将 -x_odd 和 x_even 按位置重新配对。

变换结果：[a, b] -> [-b, a]。

几何意义：这在二维平面上对应一个标准的逆时针 90° 旋转。

3. 全程形状流动图 (Shape Flow)
这是理解 RoPE 变换最清晰的视角：

原始输入：(B, H, S, 64)
—— 64 个特征平铺。

分组 (rearrange)：(B, H, S, 32, 2)
—— 形成 32 个平面坐标系。

提取 (unbind)：x_even: (B, H, S, 32) | x_odd: (B, H, S, 32)
—— 坐标分量拆分。

旋转 (stack)：(B, H, S, 32, 2)
—— 得到 [-x_odd, x_even] 组合。

还原 (rearrange)：(B, H, S, 64)
—— 旋转后的向量重新进入后续点积计算。



# 2026-04-20

## Encoder 输出Z矩阵的归宿：KV
 
内部循环：Z 矩阵是“中间产物”，负责特征的层层叠加。  
对外接口：Encoder 整体的最终输出被视作一个 Memory（记忆库）。  

KV 的功能分工：  
Key (K)：相当于 Encoder 给每个词打的“索引标签”，供 Decoder 查找。    
Value (V)：相当于 Encoder 给每个词提取的“语义精华”，供 Decoder 提取。   
总结：Encoder 最后的 Z 矩阵就是 KV 的母体。在翻译模型中，我们常说 Encoder 将输入序列“编码成了一个 KV 缓存（KV Cache）”。  




# 2026-04-22

## vLLM-Router 完整运行起来了

这次真正跑通后，我对当前配置的理解是：

- `model: "MoM"` 时，router 才会接管选模；否则就是普通模型直连。
- 现在的 `decision -> route -> model` 里，大多数 route 只挂了 1 个 `modelRef`，所以它本质上还是“先分类，再直接转发”，还不是“同一路由内多模型竞争”。
- 全局虽然开了 `model_selection.method: static`，但在单 `modelRef` 配置下，这一层几乎没有发挥作用。

当前路由大致可分为两类：

- 强制标签路由：`#flash / #plus / #max / #deepseek / #kimi / #coder` 分别固定到对应模型。
- 语义路由：
  - 代码 / 报错 / 编程类 -> `qwen3-coder-plus`
  - 深度分析 / 长上下文 -> `qwen3.6-max-preview`
  - 规划 / 路线图 / 分步骤执行 -> `kimi-k2.5`
  - 多问题分析 -> `deepseek-v3.2`
  - 简短简单问题 -> `qwen3.6-flash`
  - 兜底 -> `qwen3.6-plus`

这条 pipeline 可以概括成：

1. 客户端请求打到 `8899`，并指定 `model: "MoM"`。
2. Router 先根据消息内容抽取 signals。
3. Decision engine 用这些 signals 命中某条 route。
4. 当前 route 里通常只有一个 `modelRef`，所以直接选中该模型并转发到对应 provider。

我现在的判断：

- 这套配置已经能稳定完成“按请求类型分流”。
- 但它还不算真正的多模型选择系统，更像是“规则分类器 + 单模型映射”。
- 如果要验证 model selection 的价值，下一步必须让同一条 decision 挂多个 `modelRef`，否则 selection 层基本没有实验意义。

补充定位：
- 路由规则主要看 `config.yaml`
- 分类入口在 `src/semantic-router/pkg/extproc/req_filter_classification*.go`


# 2026-04-26

## CUDA

今天主要先把 CUDA 的整体脉络理顺了，重点不是背文档，而是搞清楚它和 LLM 优化到底怎么接上。

### 先建立整体图景

- CUDA 是让 CPU 发起、GPU 执行并行任务的编程模型；主机代码负责分配内存、发射 kernel、同步结果。
- GPU 追求吞吐量，适合海量并行；CPU 追求低延迟和复杂控制。
- CUDA 程序常见分层：高层框架 / 库（PyTorch、cuBLAS、cuDNN、Triton） -> CUDA Runtime / Driver -> PTX / cubin -> GPU 硬件。

### 我真正需要记住的执行模型

- kernel 是站在“单个线程”的视角写的：先算出自己的全局索引，再决定自己处理哪一段数据。
- 启动方式是 `<<<grid, block>>>`；`blockIdx`、`blockDim`、`threadIdx` 不是函数参数，而是 CUDA 提供的内置上下文。
- `.x / .y / .z` 只是数据维度的映射方式：向量通常只用 `.x`，图像或矩阵才会自然用到 `.x + .y`。
- `grid` 负责覆盖总任务量，`block` 负责组织线程协作；简单向量加法只用 thread 视角，矩阵乘法 / attention 这类问题必须引入 block 视角。
- warp 是 32 个线程的执行单位，因此 block 大小通常尽量设成 32 的倍数，避免浪费 lane。
- 不同 block 之间默认不能相互依赖；块内协作靠 shared memory 和 `__syncthreads()`。

### 内存与性能直觉

- 全局内存大但慢，寄存器和 shared memory 小但快。
- 线程多不等于快，常见瓶颈反而在内存访问。
- 一个 kernel 的性能，往往取决于：
  - 是否减少了全局内存读写
  - 是否避免了 warp divergence
  - 是否让访问尽量 coalesced
  - 寄存器 / shared memory 占用是否把 occupancy 压得太低

### 从代码层面想明白的几个点

- `(N + threads - 1) / threads` 是为了向上取整，保证任务不漏；多开的线程再用 `if (i < N)` 挡住。
- `cudaDeviceSynchronize()` 是显式同步点。调试时很好用，也能暴露前面 kernel 的错误；但在性能敏感场景里不能滥用。
- `extern "C"` 是为了关闭 C++ 名字修饰，方便被其他语言或动态加载逻辑找到。
- `__global__` 表示“CPU 发起、GPU 执行”的 kernel 入口，必须 `void` 返回。

## CUDA 编程

今天这部分最大的转变，是把“写循环”改成“做映射”。

```cpp
__global__ void vector_add(const float* A, const float* B, float* C, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        C[i] = A[i] + B[i];
    }
}
```

我现在的理解：

- CPU 时代的思路是“for 循环遍历数组”。
- CUDA 的思路是“每个线程只负责自己的那个索引”。
- 所以 kernel 本质上是在写 SPMD：同一段程序，被很多线程拿去处理不同数据。

### 和 LLM 优化怎么接上

- Python / PyTorch 负责模型结构、调度和实验；CUDA kernel 负责真正重的并行算子。
- 真正值得自己写 kernel 的地方，通常不是标准 GEMM，而是：
  - Attention / KV Cache 这类特殊访问模式
  - 量化解码
  - 多个小算子的融合
- 如果只是标准矩阵乘法，优先用 `cuBLAS`；如果要在 GEMM 周围融合逻辑，再考虑 `CUTLASS`；如果想先快速试验，自定义 kernel 之前可以先看 `Triton`。

### 目前的工程判断

- 写 CUDA 的核心不是“会不会语法”，而是能不能判断瓶颈在算力还是带宽。
- 定位瓶颈不能靠猜，至少要会用：
  - `Nsight Systems` 看整体时间线
  - `Nsight Compute` 看单 kernel 的 roofline、memory throughput、occupancy
  - `torch.profiler` 把 Python 层和 CUDA kernel 对上

### 这次学习后我给自己的路线

1. 先把 thread / block / warp / memory hierarchy 彻底吃透。
2. 用最小例子把 kernel launch、同步、索引映射跑顺。
3. 再进入 LLM 相关的 Triton / PyTorch Extension / CUTLASS。
4. 真做优化时，先判断是 memory bound 还是 compute bound，再决定要不要手写 kernel。




# 2026-04-27

## 远方 faraway

基于腾讯云对接完整的后端

[网页版APP](https://faraway-app-d0gpvf2ko79ceaba3-1426371841.tcloudbaseapp.com/)

### 安卓 APP 打包成功

[目前版本 GihHub 仓库](https://github.com/Tt200411/faraway)

待对接、开发更详细的后端功能




# 2026-04-28

## CUDA 编程

### 内存分配

#### 今日要点

- `cudaMemcpyDefault` 的核心是让 CUDA 驱动自动判断搬运方向。
- `cudaMallocManaged` 的核心不是复制两份数据，而是统一地址空间下的按需页迁移。
- `cudaMemcpy` 更像“复制 + 粘贴”，`cudaMallocManaged` 更像“同一份逻辑数据在 CPU / GPU 之间迁移”。

#### `cudaMemcpy` 第一个参数永远是目标地址（Destination）

示例：

```cpp
cudaMemcpy(devA, A, vectorLength * sizeof(float), cudaMemcpyDefault);
```

理解：

- `cudaMemcpyDefault` 就是让 CUDA 驱动开启“自动驾驶”模式。
- CUDA 驱动会通过 PCIe 总线自动把数据从内存搬到显存。

常见搬运方向：

| 源地址（Source） | 目的地址（Destination） | 驱动实际执行的操作 |
| --- | --- | --- |
| CPU（`A`） | GPU（`devA`） | `HtoD`（上传到显卡） |
| GPU（`devA`） | CPU（`A`） | `DtoH`（下载到内存） |
| GPU1（`devA`） | GPU2（`devB`） | `Peer-to-Peer`（显卡间直接对传） |
| GPU1（`devA`） | GPU1（`devB`） | `Device Copy`（显存内部搬运） |

#### `cudaMallocManaged`：原来位于 CPU 的数据还在吗？

这是一个非常深刻的问题，涉及到操作系统的虚拟内存管理和 CUDA 驱动的数据一致性策略。

简单来说：

- 数据依然“存在”，但在物理上它可能已经从 CPU 内存中“搬”走了。

为了理解这一点，需要把“数据”拆分为逻辑地址和物理位置来看：

1. 逻辑上：它一直都在  
   对于你的程序代码来说，变量 `A` 指向的地址（比如 `0x7f8000`）始终有效。无论数据当前是在显存里还是在主存里，都可以通过这个指针访问它。

2. 物理上：它是“按需移动”的  
   统一内存（Unified Memory）的核心机制是页迁移（Page Migration）。它的行为非常像操作系统里的“交换文件（Swap）”：
   - GPU 访问时：如果数据在 CPU 内存中，驱动会产生一个“页错误”（Pa
  ge Fault）。此时，驱动会将这一页数据（通常是 `4KB` 或 `2MB`）通过 PCIe 总线拷贝到显存，并更新 GPU 的页表。
   - 原来在 CPU 的副本：在大多数现代系统（如 Pascal 架构及之后的 GPU）上，为了保证数据一致性，CPU 端的这一页内存会被标记为“无效”或直接被物理释放。

#### `cudaMemcpy` 和 `cudaMallocManaged` 的本质区别

使用 `cudaMemcpy` 时，数据是“复制 + 粘贴”：

- 物理存在：拷贝完成后，CPU 内存（地址 `A`）和 GPU 显存（地址 `devA`）中各有一份完整的数据副本。
- 独立性：如果随后在 CPU 上修改了 `A[0]`，GPU 上的 `devA[0]` 不会跟着变。它们是两个完全独立的物理实体。
- LLM 场景应用：在加载大模型权重时，通常把权重从主存（RAM）拷贝到显存。




# 2026-04-29

## RoPE

$n$ 是动力源： 随着 $n$ 的增加（即 Token 越来越靠后），旋转的角度 $n\theta_i$ 就会越来越大。



刚才不是说越大，频率越低，角度越小吗

这是个非常棒的观察！这里其实涉及两个不同的变量在“赛跑”，你的直觉敏锐地捕捉到了它们的矛盾点。

我们要区分 位置 n 和 频率 θ 
i
​
  对最终角度的贡献：

1. 核心公式：角度 = 位置 × 频率
旋转的角度公式是：

Angle=n×θ 
i
​
 
这里有两个变量：

n (位置索引)：指 Token 是第几个（0,1,2,…）。

θ 
i
​
  (频率)：指某个维度旋转的“步长”（由 inv_freq 决定）。

2. 回答你的疑问：为什么你觉得“矛盾”？
你说的“越大越小”是指维度 i 越大，频率 θ 
i
​
  越小：

在 高维度（i 很大时），频率 θ 
i
​
  极其微小（比如 0.0001）。

这意味着在这个维度上，位置 n 每增加 1，角度只增加一点点。

但我说的“越大越大”是指位置 n 增加时，角度会变大：

即使频率 θ 
i
​
  很小（比如 0.0001），当位置 n 从 1 变成 10000 时，角度也会从 0.0001 变成 1.0。

3. 用“时钟”类比（解决你的困惑）
想象一个时钟，里面有秒针、分针和时针。它们代表了不同的维度 i。

频率 θ 
i
​
 （由维度决定）：

秒针：频率最高（转得最快）。

时针：频率最低（转得最慢，也就是你说的“维度越大，频率越低”）。

位置 n（动力源）：

n 就是流逝的时间。

随着时间 n 的流逝，所有的针都在往前转，角度都在变大。

重点来了：

当 n 增加时（时间流逝），秒针转得飞快，很快就转满一圈回到原点（容易产生你之前担心的“碰撞”）。

当 n 增加时，时针转得极慢。虽然它的角度也在变大，但它转得很稳，能区分非常遥远的时间点。

4. 总结：到底谁大谁小？
变量增加	对频率的影响	对角度 (nθ 
i
​
 ) 的影响	物理意义
维度 i 变大	变小	变小	旋转步长变短（从秒针变成时针）
位置 n 变大	无关	变大	随着 Token 靠后，总旋转量累积
你的困惑点在于： 你把“维度带来的频率衰减”和“位置带来的角度累加”搞混了。

维度决定了这根针转得有多快。

位置决定了这根针转了多久。

所以，在同一个维度下，Token 越靠后（n 越大），角度肯定越大；但在同一个位置下，维度越高，旋转的角度反而越小。


你现在能理解为什么 NTK-aware Scaling 很有用了：
当我们想把上下文从 2k 扩展到 8k 时，如果我们直接把所有维度都“调慢”（位置内插），那么原本就很快的高频维度变慢了，会导致模型在短距离内的分辨精度下降（模型变糊了）。

所以聪明的做法是：保持高频维度不动，只把那些本来就很慢的低频维度变得更慢。 这样既保住了“近视”的清晰度，又获得了“远视”的广度。

现在的逻辑是不是彻底闭环了？低频维度在短距离确实“废”，但它们是为长跑而生的。




# 2026-04-30

## 关于推理框架

我们两个小时的组会讨论了各个主流的推理框架  
我们排除了OmniInfer、ChiTu  
最终，决定在vLLM、vLLM-Ascend、SGLang-Ascend、xLLM中选取  


## 港中深新生见面会

七八个新的志同道合者  
受益！  




# 2026-05-01

## GPU操作

Gather  
All-Gather  
Reduce  
All-Reduce  
Reduce-Scatter  
All-to-All  


# 2026-05-04

## vLLM 工程边界与目录地图

理解 vLLM，先不要盯住某个 kernel；先看它把 serving runtime 切成了哪些稳定边界。

| 层次 | 关键文件 | 主要契约 | 为什么关键 |
| --- | --- | --- | --- |
| 用户入口 | [`v1/engine/llm_engine.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) | 请求规范化、输出回组装 | 把 API 面和 runtime 面隔开 |
| EngineCore | [`v1/engine/core.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) | `add_request()` / `step()` 主循环 | 是 V1 runtime 总装点 |
| Scheduler | [`v1/core/sched/scheduler.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) | 本轮谁前进、前进多少、是否抢占 | continuous batching 的真正核心 |
| KV 系统 | [`v1/core/kv_cache_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py)、[`v1/core/block_pool.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/block_pool.py) | prefix hit、slot 分配、block 生命周期 | PagedAttention 的系统收益都在这里释放 |
| 协议对象 | [`v1/request.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/request.py)、[`v1/core/sched/output.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py) | Request、SchedulerOutput、status 字段 | feature 越多，越要靠协议对象稳住边界 |
| Worker / ModelRunner | [`v1/worker/gpu/model_runner.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py)、[`v1/worker/gpu/input_batch.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py) | 把 scheduler output 变成设备输入批次 | 调度和算子之间的翻译层 |
| Attention backend | [`v1/attention/backend.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/backend.py)、[`v1/attention/selector.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/selector.py) | backend 选择、metadata 协议 | attention 不是单函数而是一套派发体系 |
| Paged Attention 执行 | [`v1/attention/ops/paged_attn.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/ops/paged_attn.py)、[`v1/worker/gpu/block_table.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/block_table.py) | block table、slot mapping、decode 访存路径 | 把 block 化 KV 变成真实执行 |
| 编译与图执行 | [`compilation/cuda_graph.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/cuda_graph.py)、[`compilation/passes/pass_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/passes/pass_manager.py) | capture/replay、pass 重写、runtime wrapper | 压低 decode 高频小步固定开销 |
| 执行器与分布式 | [`v1/executor/abstract.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/executor/abstract.py)、[`distributed/parallel_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/parallel_state.py) | 单进程/多进程/Ray、TP/EP/CP 进程组 | 把单卡 runtime 拉成服务系统 |
| Connector / 外部缓存 | [`distributed/kv_transfer/kv_connector/base.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/kv_transfer/kv_connector/base.py)、[`distributed/ec_transfer/ec_transfer_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/ec_transfer/ec_transfer_state.py) | KV/encoder cache 搬运协议 | disaggregated serving 的关键拼图 |



## 一次请求在 vLLM 里如何被推进

把一条请求主链拉直之后，很多“为什么快”都会落回同一条控制流。

1. 用户请求经 [`LLMEngine`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) 标准化，形成 engine request。
2. [`EngineCore.add_request()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 把请求交给 runtime，进入 waiting queue。
3. [`EngineCore.step()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 驱动一轮 scheduler + executor 主循环。
4. [`Scheduler.schedule()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) 计算该请求本轮还能前进多少 token。
5. [`KVCacheManager.get_computed_blocks()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 查 prefix hit，再由 [`allocate_slots()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 申请 block。
6. Scheduler 产出 [`SchedulerOutput`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py)，executor 把它下发到 worker。
7. [`GPUModelRunner.prepare_inputs()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py) 构造 [`InputBatch`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py)，再由 `prepare_attn()` 拼出 block tables 和 slot mappings。
8. `model_state.prepare_attn()` 与 attention backend 生成 metadata，按 full graph / piecewise / eager 路径执行模型。
9. `sample()` 或 rejection sampler 产出 token，`postprocess()` 更新 host/device 两侧状态镜像。
10. output processor 把底层 token 流整理成用户侧可见结果。




# 2026-05-05  

分层 AllReduce + SHARP合在一起的真实执行路径讲清楚，并给一个具体数值例子。重点关注：哪一步在节点内做、哪一步跨节点、谁在算、谁在发。

场景设定（例子）
2 个节点（Node A / Node B）
每个节点 4 张 GPU（共 8 张）
每张 GPU 有数据大小 B = 8 MB
网络：
节点内：NVLink / NVSwitch（很快）
节点间：InfiniBand + SHARP（较慢但可做网络内归约）
总体流程（一句话）

先在节点内“压缩”（AllReduce），再把“压缩结果”交给交换机做全局归约，最后再分发回节点内。

Step 1️⃣ 节点内 AllReduce（intra-node）⚡

在 Node A 内（4 张 GPU）：

用 NCCL 做一次 AllReduce
Node B 同样做一遍

结果：

Node A 的每张 GPU 都拿到：A 节点的归约结果（8 MB）
Node B 同理

👉 这里通信量确实是 B×N = 8MB × 4 = 32MB（节点内）
但因为 NVLink 很快，这一步不是瓶颈

Step 2️⃣ 选“代表”参与跨节点 🌐

每个节点选一个“代表”（通常是一个 GPU 或 NIC）：

Node A：选 GPU0
Node B：选 GPU0

👉 注意：
不再是 4 张 GPU 都出去通信，而是每个节点只出 1 份数据

Step 3️⃣ GPU → 交换机（上行）⬆️
Node A 的代表发送 8 MB
Node B 的代表发送 8 MB

👉 跨节点总发送：

每节点只发 B = 8MB
而不是 B×N = 32MB
Step 4️⃣ 交换机内做 Reduce（SHARP 核心）🧠

在支持 SHARP 的交换机里（由 NVIDIA 网络实现）：

收到来自 Node A / B 的数据
直接在交换机 ASIC 里做：
result = A + B

👉 这一步原本是在 GPU 上做的，现在搬到网络里

Step 5️⃣ 交换机 → GPU（下行，多播）⬇️
交换机把结果（8 MB）广播回：
Node A 的代表
Node B 的代表
Step 6️⃣ 节点内广播（intra-node broadcast）🔁

在每个节点内部：

代表 GPU 把结果发给本节点其他 GPU（NVLink）

最终：

所有 8 张 GPU 都拿到全局 AllReduce 结果（8 MB）
📊 对比数据量（关键）
❌ 不用分层 + 不用 SHARP

跨节点：

4 张 GPU × 8MB = 32MB / 节点
✅ 分层 + SHARP

跨节点：

每节点只发 8MB

👉 直接减少 4 倍（= N）

🧠 直觉总结

把整个过程想成“三段式”：

① 节点内（快）

“我们自己先算好一个结果”

② 网络（SHARP）

“交换机帮我们把各节点结果再合并”

③ 节点内（快）

“把最终答案发给自己人”

🔥 为什么这是大模型训练的标配

在：

Megatron-LM
DeepSpeed
大规模 DDP

中都会这样做，因为：

NVLink 带宽 ≫ IB 带宽
跨节点才是瓶颈
SHARP 能进一步减少 GPU 参与通信
一句话总结

分层 AllReduce 负责减少“谁跨节点通信”，SHARP 负责减少“通信时谁做归约 + 几轮通信”，两者结合把跨节点流量从 B×N 降到 B，并减少一轮计算/通信。



4️⃣ 总体时间模型（关键）

可以写成：

不分层：
T = T_slow(BN)

分层 + SHARP：
T = T_fast(BN) + T_slow(B)



## 不同的并行方式

### ColumnParallelLinear: 
**按照列维度分开。 某个GPU计算完后，结果的*某个维度*是*最终结果*，但是某GPU只有这些局部维度的信息。所以最后通过通讯来收集别的GPU结果**

### RowParallelLinear:
**按照行维度分开。 某个GPU计算完后，有*每个*维度的信息，但是完整的维度上，都不是最终结果。所以最后*每个维度都*要再与来自其他GPU的中间信息进行计算，得到最终结果**


  ┌────────────────────────────┬─────────────┬──────────┬──────────────────────────┬────────────┬────────────────────┐
  │             类             │  切哪一维   │ 输入状态 │         输出状态         │    通信    │      放在哪里      │
  ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
  │ ReplicatedLinear           │ 不切        │ 完整     │ 完整                     │ 无         │ 非并行场景或小矩阵 │
  ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
  │ ColumnParallelLinear       │ out (dim 0) │ 完整     │ 切开                     │ 无         │ 一段计算的入口     │
  ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
  │ RowParallelLinear          │ in (dim 1)  │ 切开     │ 完整（需 all-reduce）    │ all-reduce │ 一段计算的出口     │
  ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
  │ MergedColumnParallelLinear │ out (dim 0) │ 完整     │ 切开（由多个子矩阵拼成） │ 无         │ gate+up 合并       │
  ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
  │ QKVColumnParallelLinear    │ out (dim 0) │ 完整     │ 切开（Q/K/V 三段）       │ 无         │ attention 的 QKV   │
  └────────────────────────────┴─────────────┴──────────┴──────────────────────────┴────────────┴────────────────────┘
```

```在 Megatron-LM / vLLM 中典型结构：
X
 │
 ├── ColumnParallel + Merged (QKV / MLP expand)
 │
 ▼
 attention / activation
 │
 ├── RowParallel
 ▼
 Y
```




# 2026-05-07
I can do this all day ...   
# 2026-05-08  
赶路到广州    
# 2026-05-09  
毕业照  
# 2026-05-10  
赶路到深圳  




# 2026-05-11

## FSDP / ZeRO-3 和张量并行 TP 的区别

  FSDP：切“模型状态”，主要为了省显存
  TP：切“单层计算”，主要为了让多卡一起算一个大矩阵

  更具体地说：

  | 对比点 | FSDP / ZeRO-3 | 张量并行 TP |
  |---|---|---|
  | 切什么 | 参数、梯度、优化器状态 | 线性层/注意力层里的大矩阵 |
  | 激活怎么切 | 通常按 batch/token 切 | 通常按 hidden dim / intermediate dim 切 |
  | 每张卡算什么 | 每张卡处理不同 batch 数据 | 多张卡一起算同一个 token 的同一层 |
  | 主要目的 | 降低显存占用 | 降低单卡计算量，并让超大层能并行计算 |
  | 通信内容 | 主要通信权重/梯度 | 主要通信激活/中间结果 |
  | 常见通信 | AllGather 参数，ReduceScatter 梯度 | AllGather 激活，ReduceScatter 或 AllReduce 输出 |
  | 对模型结构的侵入 | 相对低 | 较高，需要改 Linear/Attention 的实现 |

  举个线性层例子：

  Y = X @ W

  假设：

  X: [B, D]
  W: [D, F]
  Y: [B, F]

  FSDP 的思路

  每张卡存一部分 W，但真正算这一层时，会先把完整 W 收集回来：

  平时：
  GPU0: W 第 0 片
  GPU1: W 第 1 片
  GPU2: W 第 2 片
  GPU3: W 第 3 片

  计算前：
  AllGather -> 每张卡临时拿到完整 W

  计算时：
  GPU0 算 batch 第 0 份
  GPU1 算 batch 第 1 份
  GPU2 算 batch 第 2 份
  GPU3 算 batch 第 3 份

  所以 FSDP 本质上还是偏 数据并行：每张卡处理不同数据，只是参数平时不完整保存。

  TP 的思路

  每张卡不收集完整 W，而是真的只用自己那片 W 参与计算：

  GPU0: W[:, 0:F/4]      -> 算 Y[:, 0:F/4]
  GPU1: W[:, F/4:F/2]    -> 算 Y[:, F/4:F/2]
  GPU2: W[:, F/2:3F/4]   -> 算 Y[:, F/2:3F/4]
  GPU3: W[:, 3F/4:F]     -> 算 Y[:, 3F/4:F]

  最后再通过通信把结果拼起来或规约。

  所以 TP 是真正把 一个矩阵乘法拆开计算。

  一个简单类比：

  FSDP：
  书太大，每个人平时只背几章。
  要读某一页时，大家临时把整本书凑出来，各自读自己的题。

  TP：
  一道题太大，一个人算不完。
  大家每人算这道题的一部分，最后合并答案。


## narrow

narrow 是 PyTorch 里用来沿某一个维度取连续切片的方法。

  你的代码：

  sliced_weight = loaded_weights.narrow(0, start_index, shard_size)

  意思是：

  从 loaded_weights 的第 0 维开始切
  起点是 start_index
  长度是 shard_size

  等价于常见切片：

  sliced_weight = loaded_weights[start_index : start_index + shard_size]

  如果写完整一点：

  loaded_weights.narrow(dim, start, length)

  参数含义是：

  dim: 沿哪个维度切
  start: 从这个维度的哪个下标开始
  length: 取多少个元素


## slided_weight = loaded_weights.narrow(0, start_index, shard_size)

slided_weight 不是“纯指针”，而是一个 Tensor 视图（view）对象。

  可以粗略理解成：

  slided_weight = 指向原始数据的一张“切片窗口”

  它本身是个 Tensor，带着：

  - 数据在哪
  - 形状是多少
  - 从原始 loaded_weights 的哪一段开始看
  - 步长怎么走

  但它通常不拷贝底层数据。

  例如：

  slided_weight = loaded_weights.narrow(0, start_index, shard_size)

  这里 slided_weight 和 loaded_weights 共享同一块底层存储，只是 slided_weight 只看其中一部分。

  所以你可以把它理解成：

  - 不是新开一份完整内存
  - 也不是 C 语言里那种裸指针
  - 更像“带形状信息的视图引用”

  真正把数据写进本地参数的是：

  param_data.copy_(slided_weight)

  这一步才发生拷贝。

  一句话：

  slided_weight 不是数据副本，而是原 tensor 上的一个切片视图。


## offset：

offset = sum(self.output_sizes[:loaded_weight_id]) // self.tp_size ，// self.tp_size是什么作用

// self.tp_size 的作用是：

  把“完整大矩阵里的偏移量”换算成“当前 rank 本地分片里的偏移量”。

  ———

  假设：

  output_sizes = [4096, 4096, 4096]
  tp_size = 4

  完整合并矩阵是：

  [ q: 4096 行 ][ k: 4096 行 ][ v: 4096 行 ]

  如果现在加载 k，也就是：

  loaded_weight_id = 1

  完整矩阵里的偏移是：

  sum(output_sizes[:1]) = 4096

  也就是 k 在完整大矩阵里从第 4096 行开始。

  但是当前 rank 本地只保存每个子矩阵的 1/4：

  rank 本地矩阵:
  [ q shard: 1024 行 ][ k shard: 1024 行 ][ v shard: 1024 行 ]

  所以 k 在本地矩阵里的起点不是 4096，而是：

  4096 // 4 = 1024




  
# 2026-05-12

## mini-vllm 源码完结！

前海湾公园的海与落日很美 ...


# 2026-05-13

## 尝试启动 DeepSeek V4 Flash 的推理服务


## 1. 可用模型与硬件资源

### 可用模型版本（/models/share/）

| 模型 | 路径 | 量化/精度 | 架构 | 推理框架 | 最低 NPU 需求 | 能否直接跑 |
|------|------|----------|------|---------|-------------|-----------|
| **DeepSeek-V4-Flash (W8A8)** | `DeepSeek-V4-Flash-w8a8-mtp/` | W8A8 Ascend 量化 | 43层/4096d/256专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
| **DeepSeek-V4-Flash (compressed-tensors)** | `deepseek-v4-flash-mtp/` | W8A8 compressed-tensors | 同上 | vLLM-Ascend | 32 NPU (2节点x16) | 改 MODEL_PATH + quantization 参数即可 |
| DeepSeek-V4-Flash (BF16) | `DeepSeek-V4-Flash-bf16/` | BF16 原始精度 | 同上 | 自研 NPU 推理脚本 | 1 NPU（单卡验证） | adaption_test/ 下有 quick_verify.py |
| **DeepSeek-V4-Pro** | `DeepSeek-V4-Pro-w4a8-mtp/` | W4A8 Ascend 量化 | 61层/7168d/384专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
| DeepSeek-R1-Distill-Qwen-1.5B | `DeepSeek-R1-Distill-Qwen-1.5B/` | BF16 | Qwen2 28层/1536d | vLLM-Ascend | 1 NPU | 有现成 yaml，直接跑 |
| DeepSeek-V4-Flash-Base (BF16) | `DeepSeek-V4-Flash-Base-bf16/` | BF16 | 同 Flash | 无推理脚本 | — | 不适合评测（base 模型，无 instruct 对齐） |

所有 V4 模型均为 MoE 架构，支持最大 1M token 上下文（max_position_embeddings=1048576），使用 YaRN RoPE 扩展。

### 可用 NPU 资源

| 队列 | 类型 | 配额 (NPU) | 物理规格 | 状态 |
|------|------|-----------|---------|------|
| user-1-wangakang-compute | 个人 | 8 | 8卡 x 2chip = 16 Ascend910 chip | ok |
| project-ascend-fit-wangakang | 项目 | 52 | 52卡 x 2chip = 104 Ascend910 chip | ok |

硬件说明：每张 Ascend910 物理卡包含 2 个 AI 处理器（chip），每 chip 64GB HBM。ktp 调度以"NPU"（物理卡）为单位。vLLM 的 `--tensor-parallel-size` 等参数也以 NPU（卡）为单位。

总计可用：**60 NPU**（个人 8 + 项目 52）。

尝试使用镜像启动：镜像拉取失败。  
尝试手动配置。

## 河套学院晟腾课程

### 关于 Linux 命令操作 ...

在我们的个人 docker 运行实验

### Kerminal 自动适配部署大模型 

跑了90分钟，最后还是成功了！ 



# 2026-05-14

## 手动配置一天的 DeepSeek V4 环境

各种包依赖、环境冲突、未更新问题  
最棘手的是环境不支持  

## 结束所有 LeetGPU Easy 题目！

感觉还行。  
但是 Medium 题目一下就难起来了。  



# 2026-05-15

## 河套学院晟腾课程

使用 Kerminal 写算子。  
讨论了关于文件目录。  

### 讨论了部署需求

- **Flash (W8A8)**: 2 节点 x 16 NPU = 32 NPU（TP=8, DP=2, Expert Parallel）— **最低要求，不可降低**
- **Pro (W4A8)**: 2 节点 x 16 NPU = 32 NPU（TP=16, DP=2, Expert Parallel）
- **R1-Distill-1.5B**: 1 NPU 即可
- **Flash BF16 单卡验证**: 1 NPU（adaption_test，max_seq_len=2048）

注意：经实测验证，Flash W8A8 模型在单节点 16 NPU 上无论 TP=8+DP=2 还是 TP=16 均会 OOM。必须使用双节点 32 NPU 部署。当集群只有一个 16-NPU 节点空闲时无法启动。

项目队列 52 NPU 足够同时部署 Flash + 留余量做其他实验。


## 尝试使用现有配置启动 DS v4

### 当前阻塞问题（2026-05-16）

经过多轮实测，发现以下问题：

1. **镜像兼容性**：`qwen3_5-v0-a3` 镜像的 transformers 不认识 `deepseek_v4` 架构，必须用 `deepseekv4-a3` 镜像
2. **单节点 OOM**：16 NPU 单节点无论 TP=8+DP=2 还是 TP=16 均 OOM，必须双节点
3. **vLLM-Ascend bug**：双节点 DP=2 跨节点部署时，worker 在 KV cache 初始化阶段报 `AttributeError: 'list' object has no attribute 'merge'`（kv_cache_spec_values 类型错误）



# 2026-05-16

## DeepSeek V4 Flash W8A8 部署总结

### 今日结论

- 任务 1058 已成功启动，服务地址为 `http://10.250.193.147:8005`。
- 当前唯一验证过的可用配置是 cdy 的原版配置：`/models/share/task/cdy/deepseek-v4-flash.yaml`。
- 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
- 启动前必须在 `/vllm-workspace/vllm` 中应用 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
- 单节点 16 NPU 可以跑通 DeepSeek V4 Flash W8A8，配置为 DP=2、TP=8、Expert Parallel。
- CPU 内存需要 1000Gi，CPU 需要 500 核。

### 立即可做

按照 `deepseek-v4-reasoning-eval.md` 中的测试矩阵，继续进行 DeepSeek V4 Flash 性能测试。

### 后续学习任务

1. **服务器 NPU 资源调度**

   管理员解释：提交任务后，调度系统会分配空闲节点。每个节点有 16 张 910 显卡，不同节点已有的镜像缓存不同，这会影响是否需要重新拉镜像。

   后续需要进一步理解服务器节点运行方式、节点间通信和并行配置。可参考：

   - 网络基础说明：https://lqhl.github.io/scaling-book/gpus/#%E7%BD%91%E7%BB%9C
   - 配置脚本：`/models/share/task/cdy/start_dsv4.sh`
   - 本文档附录中的 NPU 集群调度方案

2. **服务器集群镜像系统**

   关于“镜像拉取慢”的问题，需要学习服务器集群的镜像系统：https://luoss.nilpo.app/guide/image-storage。

   管理员建议先上传镜像到公开镜像池。上传完成后，服务器内部拉取镜像和模型权重都会明显变快：拉镜像约 10 秒，否则可能需要 10 分钟以上。

### 后续优化方向

1. 管理员提到自己曾跑通过 SGLang，后续可以尝试用 SGLang 启动 DeepSeek V4 Flash。

2. 管理员提到开源项目 [DFlash: Block Diffusion for Flash Speculative Decoding](https://github.com/z-lab/dflash)。该项目能显著提高解码速度，但目前似乎只能本机运行，不一定适合直接对外提供推理服务。后续可以考虑基于它改进 vLLM / SGLang 框架。

## 最终成功配置

**任务 1058**：使用 cdy 的原版配置成功启动。

| 项目 | 值 |
| --- | --- |
| yaml | `/models/share/task/cdy/deepseek-v4-flash.yaml` |
| 镜像 | `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3` |
| 节点 | atlas-19（单节点 16 NPU） |
| 配置 | DP=2, TP=8, Expert Parallel |
| 端口 | 8005 |
| 模型名 | deepseek-v4-flash |
| max_model_len | 524288 |
| 关键步骤 | 启动前先 `git apply` patch 到 `/vllm-workspace/vllm` |

## 这两天遇到的问题

### 1. 镜像不支持 `deepseek_v4` 架构

**现象**：`The checkpoint has model type deepseek_v4 but Transformers does not recognize this architecture`

**原因**：`qwen3_5-v0-a3` 和 `deepseekv4-a3` 镜像中的 transformers 库版本不包含 `deepseek_v4` 模型类型注册。

**解决方案**：使用 `v0.13.0rc3-a3` 镜像 + cdy 脚本中的 `git apply` patch。patch 位于 `/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`，它会修改 vLLM 代码，注册 `deepseek_v4` 相关组件。该镜像中的 vLLM 版本（v0.13）对 `model_type` 的检查逻辑与新版不同，patch 后即可通过。

### 2. `tool-call-parser deepseek_v4` 不支持

**现象**：`invalid tool call parser: deepseek_v4`

**原因**：`qwen3_5-v0-a3` 镜像的 vLLM 版本（v0.16.0rc2）不包含 `deepseek_v4` tool parser。

**解决方案**：

- 方案 A：使用 `v0.13.0rc3-a3` 镜像 + patch（cdy 方案，已验证）
- 方案 B：去掉 `--tool-call-parser` 和 `--reasoning-parser` 参数（性能测试不需要）

### 3. `speculative-config deepseek_mtp` 不支持

**现象**：`Unsupported speculative method: 'mtp'`

**原因**：`deepseekv4-a3` 镜像的 vLLM 版本不支持 MTP 投机解码。

**解决方案**：去掉 `--speculative-config` 参数，或使用 `v0.13.0rc3-a3` 镜像（支持 MTP）。

### 4. 单节点 16 NPU DP=2 TP=8 OOM（`deepseekv4-a3` 镜像）

**现象**：Worker 进程被 terminated，报错 `WorkerProc was terminated`。

**原因**：`deepseekv4-a3` 镜像的 vLLM 版本内存管理效率较低，DP=2 在单节点上 OOM。

**解决方案**：使用 `v0.13.0rc3-a3` 镜像（vLLM v0.13 内存管理更高效），并分配 1000Gi CPU 内存。cdy 配置证明同样的 DP=2 TP=8 单节点 16 NPU 可以跑通。

### 5. 双节点调度失败

**现象**：Worker pod 一直 Pending，无法分配第二个 16-NPU 节点。

**原因**：集群中空闲的 16-NPU 节点不足两个。

**解决方案**：使用单节点配置（cdy 方案证明可行）。

### 6. `deepseekv4-a3` 镜像双节点 KV cache bug

**现象**：`AttributeError: 'list' object has no attribute 'merge'`

**原因**：`deepseekv4-a3` 镜像中 vLLM-Ascend 的 KV cache 初始化代码在跨节点 DP 模式下有 bug。

**解决方案**：不使用该镜像，改用 `v0.13.0rc3-a3` 镜像。跨节点 DP 模式相关配置还需要进一步学习，尤其是 `/models/share/task/cdy/start_dsv4pro-worker.sh` 中的参数。

### 7. `cd vllm-ascend` 路径问题

**现象**：`cd: vllm-ascend: No such file or directory`

**原因**：不同镜像的工作目录不同。

**解决方案**：cdy 的脚本直接 `cd "$VLLM_REPO"`（即 `/vllm-workspace/vllm`），不需要进入 `vllm-ascend`。

### 8. 镜像拉取慢

**现象**：Pod 长时间 Pending（10-20 分钟）。

**原因**：`deepseekv4-a3` 和 `v0.13.0rc3-a3` 镜像在部分节点上没有缓存。

**解决方案**：等待拉取完成，或多次提交，直到调度到已有缓存的节点。

**管理员解决方案**：先上传镜像到公开镜像池，参考 https://luoss.nilpo.app/guide/image-storage。上传完成后，服务器内部拉取镜像和模型权重都会很快。

## 关键经验

1. 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
2. 必须先打 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
3. 单节点 16 NPU 可以跑，配置为 DP=2 TP=8，不需要双节点。
4. CPU 内存需要 1000Gi，200Gi / 800Gi 不够。参考管理员方案：`/models/share/task/cdy/deepseek-v4-flash.yaml` 第 17、18 行。
5. CPU 需要 500 核。
6. cdy 的脚本（管理员方案）是唯一验证过的可用配置，后续所有版本都应以此为基础。

## 附录：NPU 集群现有调度方案

本集群使用 **Kubernetes + Volcano 调度器** 管理 NPU 资源，并通过 `ktp` CLI 工具操作。

### 层级结构

```text
集群 (K8s Cluster)
 └── 节点 (Node): atlas-1, atlas-18, atlas-19, atlas-39, atlas-40, atlas-41 ...
      └── 每个节点有 16 NPU（8 张物理卡 x 2 chip）
           └── 每张卡 64GB HBM

用户通过 Queue（队列）获得 NPU 配额：
 ├── 个人队列: user-1-wangakang-compute (8 NPU)
 └── 项目队列: project-ascend-fit-wangakang (52 NPU)
```

### 调度流程

1. **提交任务**：执行 `ktp submit -f job.yaml`。yaml 中指定 queue、npu 数量、镜像和启动命令，任务类型为 `acjob`（Ascend Computing Job）。
2. **调度器分配节点**：Volcano 调度器根据队列配额和节点空闲情况分配资源，无法手动指定节点。请求 16 NPU 会分配一个完整节点；请求 32 NPU 需要两个空闲节点同时可用。
3. **Pod 创建**：每个 task 对应一个 Pod。Pod 运行在分配的节点上，并挂载 `/models/` 共享存储。平台会自动生成 `hccl.json`，Pod 内的 `init_env.sh` 等待该文件就绪后设置 `MASTER_IP` 等环境变量。
4. **分布式通信初始化**：单节点时，Pod 内所有 NPU 通过 HCCL（华为集合通信库）直接通信；多节点时，通过 `data-parallel-address`（`MASTER_IP`）跨节点 RPC 通信。
5. **任务生命周期**：状态流转为 Pending -> Running -> Succeeded / Failed。`resumable_training.enabled: true` 时，失败会自动重试（最多 `fault_retry_times` 次）；`max_runtime_minutes` 到期后自动终止。

### yaml 配置与调度的关系

```yaml
tasks:
  - name: master        # Pod 名称后缀
    replicas: 1         # 该角色的 Pod 数量
    cpu: "500"          # CPU 核数（影响调度，节点需有足够 CPU）
    memory: "1000Gi"    # 内存（影响调度，节点需有足够内存）
    npu: 16             # NPU 数量（决定分配几张卡/几个节点）
    command: "..."      # Pod 启动后执行的命令
  - name: worker        # 第二个 Pod（可选，用于多节点）
    replicas: 1
    npu: 16             # 又一个 16 NPU = 又一个完整节点
```

### 常用操作

| 命令 | 作用 |
| --- | --- |
| `ktp queues` | 查看队列配额和使用情况 |
| `ktp submit -f job.yaml` | 提交任务 |
| `ktp list` | 列出所有任务 |
| `ktp pods <ID>` | 查看任务的 Pod 状态和所在节点 |
| `ktp logs <ID>` | 查看日志（默认最新 100 行） |
| `ktp logs <ID> --follow` | 实时跟踪日志 |
| `ktp stop <ID>` | 停止任务 |
| `ktp restart <ID>` | 重启已停止的任务 |
| `ktp watch <ID>` | 实时监控任务状态 |

### 注意事项

- 不能指定调度到哪个节点，只能靠调度器自动分配。
- 不同节点上可能缓存了不同版本的同名镜像（tag 相同但内容不同）。
- 请求的 NPU 数量决定了需要几个节点：8 NPU = 半个节点，16 NPU = 一个节点，32 NPU = 两个节点。
- 如果集群没有足够空闲节点，Pod 会一直 Pending。
- `/models/` 是所有节点共享的 NFS 存储，脚本和权重文件对所有 Pod 可见。

## CUDA 编程实践：共享内存

### 核心概念

每个 Block 都有自己独立的共享内存。在 CUDA 中，下面这句声明的是块内私有共享内存：

```cpp
extern __shared__ float sdata[];
```

也就是说，Block 0、Block 1 和 Block 2 各自都有一份独立的 `sdata` 数组，它们互不干扰。

在这个例子中：

- `blockDim.x = 4`
- 每个 Block 的 `sdata` 长度都是 4
- 每个 Block 内部的索引都是 `[0, 1, 2, 3]`

当程序执行到下面这一行时：

```cpp
sdata[tid] = (i < N) ? input[i] : 0.0f;
```

每个线程会根据自己的局部 ID（`tid`）和全局 ID（`i`），把全局内存中的数据搬到自己 Block 的共享内存中。

### 数据映射关系

#### Block 0（`blockIdx.x = 0`）

| Thread | `tid` | 全局 `i` | 执行操作 |
| --- | --- | --- | --- |
| Thread 0 | 0 | 0 | `sdata[0] = input[0]`（1.0） |
| Thread 1 | 1 | 1 | `sdata[1] = input[1]`（2.0） |
| Thread 2 | 2 | 2 | `sdata[2] = input[2]`（3.0） |
| Thread 3 | 3 | 3 | `sdata[3] = input[3]`（4.0） |

此时 Block 0 的 `sdata` 为：

```text
[1.0, 2.0, 3.0, 4.0]
```

#### Block 1（`blockIdx.x = 1`）

| Thread | `tid` | 全局 `i` | 执行操作 |
| --- | --- | --- | --- |
| Thread 0 | 0 | 4 | `sdata[0] = input[4]`（5.0） |
| Thread 1 | 1 | 5 | `sdata[1] = input[5]`（6.0） |
| Thread 2 | 2 | 6 | `sdata[2] = input[6]`（7.0） |
| Thread 3 | 3 | 7 | `sdata[3] = input[7]`（8.0） |

此时 Block 1 的 `sdata` 为：

```text
[5.0, 6.0, 7.0, 8.0]
```

#### Block 2（`blockIdx.x = 2`）

| Thread | `tid` | 全局 `i` | 执行操作 |
| --- | --- | --- | --- |
| Thread 0 | 0 | 8 | `sdata[0] = input[8]`（9.0） |
| Thread 1 | 1 | 9 | `sdata[1] = input[9]`（10.0） |
| Thread 2 | 2 | 10 | `sdata[2] = input[10]`（11.0） |
| Thread 3 | 3 | 11 | `sdata[3] = input[11]`（12.0） |

此时 Block 2 的 `sdata` 为：

```text
[9.0, 10.0, 11.0, 12.0]
```
