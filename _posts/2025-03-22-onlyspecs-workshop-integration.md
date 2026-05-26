---
layout: single
title: "把 OnlySpecs 接入 Workshop：从 Electron Coding Agent 到 Web 低代码生成器"
date: 2025-03-22
categories:
  - tech-blog
  - agent-engineering
series: "Agent Engineering"
priority: P1
tags:
  - OnlySpecs
  - Claude CLI
  - FastAPI
  - SSE
  - Low Code
excerpt: "一次开源项目改造笔记：理解 Electron、IPC、node-pty 和 Claude CLI 后，把桌面 Agent 接到 Web 平台。"
source_log:
  - "Renyuan_Log.md:59-128"
  - "Renyuan_Log.md:139-313"
---

OnlySpecs 的原始形态更接近桌面端 Coding Agent。它有 Electron UI、Renderer、IPC、Main Process，并通过终端能力驱动 Claude CLI。Workshop 的目标则是 Web 用户输入需求，后端生成项目，再给出可下载或可预览结果。

这两个形态的差异决定了接入方式：不能只搬 UI，也不能直接把 Electron 当成后端服务。

## 架构理解

关键点在于 `node-pty`。它可以在程序里打开一个伪终端，让代码驱动 CLI 工作。对桌面应用来说这很自然，但对 Web 服务来说，交互式终端会带来状态、并发、超时和输出解析问题。

因此更稳的接入方式是让生成器尽量无头化：输入结构化 prompt，输出结构化文件或事件。Web 后端负责排队、流式输出、保存任务和打包下载。

## Web 集成路径

接入方案可以分成几步：

1. 用 FastAPI 封装 OnlySpecs 的生成入口。
2. 前端通过 HTTP 或 SSE 提交任务并接收状态。
3. 生成结果整理成文件树。
4. 后端提供 ZIP 下载。
5. 历史任务保存在服务侧，方便重新下载或查看。

这个过程的重点不是“立刻做完低代码平台”，而是把桌面 Agent 的核心生成能力从 GUI 中剥离出来。

## 输出物抽象

Workshop 不只需要源代码。更完整的产品形态还包括：

- 源代码下载。
- Web 应用预览。
- PWA。
- 桌面程序打包。

不同输出物需要不同构建链路。源代码只需要打包，Web 应用需要构建和静态托管，桌面程序需要额外 build worker。这个抽象会直接影响后续 Docker、OSS 和 FC 的设计。

## 复盘

改造开源项目时，最重要的是先识别稳定边界：哪些是核心能力，哪些只是原项目 UI 或运行环境的副产物。OnlySpecs 的价值在生成链路，而不是 Electron 外壳。把能力服务化后，它才适合进入 Workshop。

## 知识补全：Electron 项目为什么不等于后端服务

Electron 应用通常把 UI、状态、文件系统和进程控制放在同一个桌面运行时里。Renderer 负责界面，Main Process 负责系统能力，IPC 在两者之间传消息。这种结构适合个人电脑上的交互应用。

Web 服务的约束完全不同。它必须处理多用户、并发、超时、权限隔离、日志追踪和无界面运行。一个 Electron 项目直接搬到服务器，最容易遇到的问题是：原本依赖用户交互的流程没有稳定 API，原本依赖本机路径的逻辑无法多租户隔离，原本在 GUI 里展示的状态没有结构化事件。

所以改造路线不是“把 Electron 跑在服务器上”，而是抽出生成核心，给它设计输入输出 contract。

## 接入开源 Agent 的方法论

评估一个开源 Agent 能不能接入自己的平台，可以问五个问题：

1. 核心能力是否能在无 GUI 环境运行。
2. 输入是否能变成结构化 prompt 或配置。
3. 输出是否能稳定变成文件树、事件流或 JSON。
4. 运行过程是否能设置超时和取消。
5. 失败时是否能拿到足够日志做自动修复。

OnlySpecs 的调研价值在于，它暴露了桌面 Agent 和 Web Agent 的边界差异。理解这个差异后，后续改造 opencode、Agent-Do 或其他 Coding Agent 会更有方向。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [Preamble](#source-log-preamble) | 1-4 | 稔远学习日志 |
| [2025-03-19](#source-log-2025-03-19) | 5-54 | FastAPI、TypeScript 与第一次工程化拆分 |
| [2025-03-20](#source-log-2025-03-20) | 55-68 | OnlySpecs 调研与 WSL 网络修复 |
| [2025-03-21](#source-log-2025-03-21) | 69-228 | Electron Agent 如何改造成 Web 服务 |
| [2025-03-22](#source-log-2025-03-22) | 229-414 | OnlySpecs Web 化与输出物抽象 |

<a id="source-log-preamble"></a>
### Source Log: Preamble

Source lines: `Renyuan_Log.md:1-4`

<pre class="tech-log-source"><code>
0001 |# 稔远学习日志
0002 |
0003 |仅个人学习与实践记录，便于回顾与整理。
0004 |
</code></pre>


<a id="source-log-2025-03-19"></a>
### Source Log: 2025-03-19

Source lines: `Renyuan_Log.md:5-54`

<pre class="tech-log-source"><code>
0005 |# 2025-03-19
0006 |
0007 |## 知识学习
0008 |
0009 |#### 图解Transformer
0010 |非常清晰的图示教程，用矩阵拆解Transformer，难度梯度很合适
0011 |[教程](https://jalammar.github.io/illustrated-transformer/)
0012 |
0013 |#### TypeScript/npm包管理
0014 |
0015 |#### TypeScript[(清华大学的AI教育项目)](https://github.com/Ryannnice/CUHK-LLM-Edu/edit/main/README.md)
0016 |
0017 |整个项目绝大部分使用TypeScript,文件结构、调用逻辑非常复杂
0018 |TypeScript 是 JavaScript 的超集
0019 |
0020 |#### npm
0021 |
0022 |npm = Node Package Manager（Node.js 包管理器）
0023 |
0024 |安装库和工具/管理依赖（项目里用到的第三方包）/**运行脚本**（比如启动 Vue、React 或 Node 项目）
0025 |*npm run &lt;脚本名&gt;: 运行 package.json 里的脚本*
0026 |
0027 |#### FastAPI python框架了解
0028 |第一次实习，第一次接触偏工程的项目：不同于科研的是，可行性/整体模块的缝合、运行似乎比细致的优化更重要
0029 |
0030 |清华的开源教育项目未采用前后端分离架构
0031 |
0032 |使用.json格式请求体完成数据/信息传递
0033 |
0034 |前端直接通过函数调用REST API:
0035 |```
0036 | fastapi_backend/
0037 |    └── static/
0038 |        ├── index.html        # 主页（需求输入 + 设置）
0039 |        ├── generate.html     # 生成流程页（SSE 大纲流 + 进度）
0040 |        ├── classroom.html    # 课堂播放页（幻灯片/测验/聊天）
0041 |        ├── app.js            # 全局工具：API 调用、设置存储、路由
0042 |        ├── generate.js       # 生成流程逻辑
0043 |        ├── classroom.js      # 课堂播放逻辑（幻灯片渲染、测验、聊天）
0044 |        └── style.css         # 全局样式
0045 |```
0046 |
0047 |## 实践
0048 |
0049 |#### FastAPI
0050 |在原本的REST API接口上，建立/fastapi_backend文件夹，用FastAPI封装全部18个功能的api
0051 |原有.ts文件前端直接调用api的所有逻辑均保留，与Fast后端接口不冲突
0052 |
0053 |实现后端分离之后，建立/fastapi_backend/static文件夹，仅使用js/html初步实现前端功能，以验证FastAPI后端接口可行性
0054 |
</code></pre>


<a id="source-log-2025-03-20"></a>
### Source Log: 2025-03-20

Source lines: `Renyuan_Log.md:55-68`

<pre class="tech-log-source"><code>
0055 |# 2025-03-20
0056 |
0057 |## 知识学习
0058 |
0059 |#### 开源库OnlySpecs
0060 |这是自动生成软件的agent系统，可能对项目第二部分*WorkShop*有帮助
0061 |（上午团队实现workshop功能时发现直接调用LLM实现代码（软件编程）能力有限：贪吃蛇不成功，推箱子成功）
0062 |试图部署该开源项目，接入我们的项目
0063 |
0064 |## 实践
0065 |
0066 |#### Linux bash
0067 |上午claude api爆了，以为是网络问题重新配置安装一遍windows WSL的linux的网络环境
0068 |
</code></pre>


<a id="source-log-2025-03-21"></a>
### Source Log: 2025-03-21

Source lines: `Renyuan_Log.md:69-228`

<pre class="tech-log-source"><code>
0069 |# 2025-03-21
0070 |
0071 |## 知识学习
0072 |
0073 |#### 开源库OnlySpecs
0074 |
0075 |#### node-pty
0076 |
0077 |pty.spawn(&quot;claude&quot;)
0078 |
0079 |相当于**在程序里打开**一个**终端**窗口
0080 |
0081 |#### AIEngine
0082 |
0083 |一个“可以驱动 Claude CLI 干活”的执行器
0084 |
0085 |```
0086 |return new Promise((resolve, reject) =&gt; {
0087 |    proc.onExit((e) =&gt; {
0088 |        if (e.exitCode === 0) resolve()
0089 |        else reject(new Error(...))
0090 |    })
0091 |})
0092 |```
0093 |```
0094 |┌─────────────┐
0095 |│ run() 调用  │
0096 |│ await engine│
0097 |└─────┬───────┘
0098 |      │
0099 |      ▼
0100 |┌─────────────┐
0101 |│ Promise     │   &lt;-- pending 状态
0102 |│ resolve/reject 内部管子
0103 |└─────┬───────┘
0104 |      │
0105 |      ▼
0106 |┌─────────────┐
0107 |│ proc.onExit │  &lt;-- Claude CLI 退出触发
0108 |│ e.exitCode  │
0109 |└─────┬───────┘
0110 |      │
0111 |      ▼
0112 |if(exitCode==0) resolve()  else reject(error)
0113 |      │
0114 |      ▼
0115 |Promise 状态变更 → 外层 await/then/catch 收到结果
0116 |```
0117 |
0118 |#### Shim
0119 |
0120 |是一种兼容层或适配器，用于在不修改原有代码的情况下，让新旧接口或系统之间能够协同工作
0121 |
0122 |这很适用于最小化更改，让该开源项目快速应用于我们的项目中，以此为起点吧
0123 |
0124 |#### Node.js Web 服务器
0125 |
0126 |Node.js 是一个运行环境，可以用 JavaScript 写服务端程序
0127 |
0128 |&quot;Node.js Web 服务器&quot;就是用 Node.js 写的 HTTP 服务，比如用 Express、Fastify、Koa 等框架搭建的后端，和阿里云服务器不冲突
0129 |
0130 |```
0131 |阿里云 ECS（服务器硬件/系统）
0132 |    └── Nginx（反向代理，监听 80/443 端口）
0133 |          └── Node.js 进程（监听 3000 端口）
0134 |                └── 你的业务代码
0135 |```
0136 |
0137 |## 实践
0138 |
0139 |#### Web版OnlySpecs功能测试
0140 |
0141 |已完成在web上的部署，使用简单的html转跳
0142 |
0143 |汉化前端菜单栏
0144 |
0145 |#### 融入大项目的Workshop部分
0146 |
0147 |**我们项目Workshop的原架构：**
0148 |
0149 |```
0150 |用户 → Vue
0151 |        │
0152 |        ▼
0153 |FastAPI /generate
0154 |        │
0155 |        ▼
0156 |DeepSeek 生成 HTML
0157 |        │
0158 |        ▼
0159 |FastAPI /upload
0160 |        │
0161 |        ▼
0162 |阿里云 OSS
0163 |        │
0164 |        ▼
0165 |返回 URL
0166 |        │
0167 |        ▼
0168 |Vue 展示
0169 |```
0170 |
0171 |**开源软件OnlySpecs的原架构：**
0172 |```
0173 |Electron UI
0174 |    ↓
0175 |Renderer (DOM + Monaco)
0176 |    ↓
0177 |IPC
0178 |    ↓
0179 |Main Process
0180 |    ↓
0181 |node-pty
0182 |    ↓
0183 |Claude CLI
0184 |```
0185 |
0186 |**新架构融合，两种方案：**
0187 |
0188 |***方案一，分离式：***
0189 |```
0190 | 大项目
0191 | ├── Vue 仪表盘（前端）   → Docker: Nginx 静态托管，端口 80
0192 | ├── FastAPI 后端         → Docker: Uvicorn，端口 9000
0193 | │   ├── /generate        → DeepSeek 流式生成 HTML
0194 | │   └── /upload          → 阿里云 OSS 上传
0195 | └── OnlySpecs（待加入）  → Docker: Node.js，端口 3579
0196 |     └── 功能：Specs 编写、Claude AI 代码生成、终端
0197 |```
0198 |
0199 |***方案二，通过FastAPI使用功能，仅替换掉LLM，使用claude agent编写软件：***
0200 |```
0201 |Vue 前端
0202 |    ↓ POST /generate-software { prompt }
0203 |  FastAPI
0204 |    ↓ 调用 OnlySpecs Node.js 服务（HTTP 或子进程）
0205 |  OnlySpecs Web Server
0206 |    ↓ 写 specs.md → 启动 Claude CLI
0207 |  Claude CLI（node-pty）
0208 |    ↓ 生成代码
0209 |  返回结果（文件路径 / OSS URL）
0210 |    ↑ 流式进度推送（SSE / WebSocket）
0211 |  Vue 前端展示
0212 |
0213 |
0214 |FastAPI 端点设计
0215 |  # POST /generate-software
0216 |  # 输入：用户 prompt
0217 |  # 输出：SSE 流式进度 + 最终代码 URL
0218 |
0219 |  @app.post(&quot;/generate-software&quot;)
0220 |  async def generate_software(prompt: str):
0221 |      # 1. 调用 OnlySpecs API 创建 specs 文件
0222 |      # 2. 触发 Generate from Specs
0223 |      # 3. 流式返回进度
0224 |      # 4. 完成后上传到 OSS，返回 URL
0225 |```
0226 |
0227 |先尝试方案二，先设计无头OnlySpecs的API
0228 |
</code></pre>


<a id="source-log-2025-03-22"></a>
### Source Log: 2025-03-22

Source lines: `Renyuan_Log.md:229-414`

<pre class="tech-log-source"><code>
0229 |# 2025-03-22
0230 |
0231 |## 实践
0232 |
0233 |FastAPI 编写完成，核心是/generate 根据用户指令来交给OnlySpecs，利用其功能生成
0234 |
0235 |api测试成功（文档：/home/ryan/OnlySpecs/docs/API_QUICKSTART.md，测试：终端运行 npm run test:api）
0236 |
0237 |接下来对接我们的项目第二部分Workshop：
0238 |实现方式参考原框架，写出仿制的前端：/home/ryan/OnlySpecs/api-integration
0239 |
0240 |整个Pipeline:
0241 |
0242 |```
0243 |  📁 Project Structure
0244 |
0245 |  ~/OnlySpecs/api-integration/
0246 |  ├── app.py              # FastAPI backend (API proxy + SSE streaming)
0247 |  ├── requirements.txt    # Python dependencies
0248 |  ├── .env               # Environment configuration
0249 |  ├── .env.example       # Environment template
0250 |  ├── start.sh           # Quick start script
0251 |  ├── static/
0252 |  │   └── index.html     # Vue 3 frontend (312 lines)
0253 |  └── README.md          # Complete documentation
0254 |
0255 |  🎯 Key Features Implemented
0256 |
0257 |  Backend (FastAPI):
0258 |  - ✅ CORS-enabled API proxy to OnlySpecs API
0259 |  - ✅ SSE streaming for real-time log updates
0260 |  - ✅ Endpoints: /api/generate, /api/status, /api/logs, /api/tasks, /api/download
0261 |  - ✅ Error handling and timeout controls
0262 |
0263 |  Frontend (Vue 3 + Tailwind):
0264 |  - ✅ Clean, responsive UI with Chinese localization
0265 |  - ✅ Real-time log display with auto-scroll
0266 |  - ✅ Task status tracking (pending/running/completed/failed)
0267 |  - ✅ History task list with click-to-load
0268 |  - ✅ Download generated code as ZIP
0269 |  - ✅ EventSource for SSE log streaming
0270 |
0271 |  🚀 Quick Start
0272 |
0273 |  # 1. Start OnlySpecs API (in one terminal)
0274 |  cd ~/OnlySpecs
0275 |  npm run api
0276 |
0277 |  # 2. Start frontend (in another terminal)
0278 |  cd ~/OnlySpecs/api-integration
0279 |  ./start.sh
0280 |
0281 |  Then visit: http://localhost:9000
0282 |
0283 |  📝 Usage Flow
0284 |  1. Enter software requirements in the text area
0285 |  2. Click &quot;开始生成&quot; (Start Generation)
0286 |  3. Watch real-time Claude CLI logs
0287 |  4. Download code when complete or open in file explorer
0288 |  5. View history tasks in the collapsible section
0289 |
0290 |  The implementation follows the plan exactly, using SSE for real-time updates and providing a simple, user-friendly interface for interacting
0291 |  with OnlySpecs.
0292 |```
0293 |
0294 |已经能完美运行，依靠简洁的web界面，通过FastAPI和OnlySpecs交互
0295 |
0296 |***输入--&gt;OnlySpecs--&gt;Claude CLI--&gt;输出***，用户只负责敲几个字：项目第二部分低代码的思想
0297 |
0298 |debug修复内容：
0299 |
0300 |1. claude开始但是不工作，代码写不进去项目文件夹 / claude 不动，接收不到指令：--print 标志可以完全跳过交互式 UI，直接输出结果。不需要 pty 模拟，改用子进程即可。用 spawn + --print 替换整个 pty 方案，彻底解决交互式 UI 问题。
0301 |
0302 |2. 下载 ZIP之后win系统打不开：之前是把 OnlySpecs API 返回的 JSON 当 ZIP 存的，当然打不开。现在后端拿到 codePath，用 shutil.make_archive 真正打包成 ZIP，Win11 可以直接解压。
0303 |
0304 |3. “在文件管理器中打开”的按钮点不动：新增了 /api/open/{task_id} 接口，调用 xdg-open 打开 Linux 文件管理器，同时在界面显示代码路径。
0305 |WSL2 里 xdg-open 无法直接打开 Windows 文件管理器。需要用 explorer.exe 来打开，但路径要转换成 Windows 格式。
0306 |转换出来是 \\wsl.localhost\Ubuntu\... 格式，Win11 的文件资源管理器可以直接打开这个 UNC 路径。
0307 |```
0308 |\\wsl.localhost\Ubuntu\home\ryan\Documents\OnlySpecs\api-workspaces\task_1774168877875_1u1yudaz6\code_v0001
0309 |```
0310 |
0311 |***全部修复***
0312 |
0313 |朝着更更更低代码平台进发：
0314 |
0315 |📋 计划总结
0316 |
0317 |核心功能： 在 Web 界面添加 4 种输出类型选择：
0318 |
0319 |1. 📄 源代码 - 可编辑的源文件
0320 |2. 🌐 Web 应用 - 单文件 HTML，浏览器直接运行
0321 |3. 💻 桌面程序 - Windows .exe 可执行文件（自动打包）
0322 |4. 📱 手机应用 - PWA 渐进式 Web 应用
0323 |
0324 |用户使用Pipeline:
0325 |
0326 |```
0327 |用户浏览器
0328 |    │
0329 |    ▼
0330 |Vue 前端
0331 |    │
0332 |    ▼
0333 |FastAPI API
0334 |    │
0335 |    ▼
0336 |OnlySpecs AI Engine （调用Claude CLI）
0337 |    │
0338 |    ▼
0339 |生成代码
0340 |    │
0341 |    ▼
0342 |Build Worker（Docker）
0343 |    │
0344 |    ▼
0345 |编译为 .exe
0346 |    │
0347 |    ▼
0348 |上传到 OSS
0349 |    │
0350 |    ▼
0351 |用户下载
0352 |```
0353 |
0354 |本地项目列表已更新：
0355 |
0356 |新功能：
0357 |1. 类型标签 - 每个项目左侧显示彩色标签：
0358 |  - 📄 源代码（紫色）
0359 |  - 🌐 Web应用（靛蓝色）
0360 |  - 💻 桌面程序（橙色）
0361 |  - 📱 手机应用（粉色）
0362 |2. 对应按钮 - 根据项目类型显示不同的主功能按钮：
0363 |  - 源代码：📄 线上查看 + 📦 下载源码
0364 |  - Web应用：🌐 线上运行 + 📦 下载源码
0365 |  - 桌面程序：💻 下载 .exe + 📦 下载源码
0366 |  - 手机应用：📱 下载应用 + 📦 下载源码
0367 |
0368 |```
0369 |  部署步骤：
0370 |
0371 |  1. 在阿里云服务器上安装依赖：
0372 |  安装Node.js
0373 |  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
0374 |  sudo apt-get install -y nodejs
0375 |
0376 |  安装Python
0377 |  sudo apt-get install python3 python3-pip
0378 |
0379 |  安装Docker
0380 |  curl -fsSL https://get.docker.com | sudo sh
0381 |  sudo usermod -aG docker $USER
0382 |
0383 |  安装Claude CLI
0384 |  npm install -g @anthropic-ai/claude-code
0385 |
0386 |  2. 配置Claude API密钥：
0387 |  export ANTHROPIC_API_KEY=&quot;your-api-key-here&quot;
0388 |
0389 |  3. 打包项目：
0390 |  cd ~/OnlySpecs
0391 |  tar -czf onlyspecs-deploy.tar.gz \
0392 |    src/ \
0393 |    api-integration/ \
0394 |    package.json\
0395 |    tsconfig.json
0396 |  4. 上传到服务器：
0397 |  scp onlyspecs-deploy.tar.gz user@your-server:/home/user/
0398 |
0399 |  5. 在服务器上解压并启动：
0400 |  tar -xzf onlyspecs-deploy.tar.gz
0401 |  npm install
0402 |  docker pull cdrx/pyinstaller-windows
0403 |
0404 |  启动服务
0405 |  npm run api &amp;
0406 |  cd api-integration &amp;&amp; python3 app.py &amp;
0407 |
0408 |  6. 配置防火墙：
0409 |  sudo ufw allow 3580
0410 |  sudo ufw allow 9000
0411 |
0412 |  访问：http://your-server-ip:9000
0413 |```
0414 |
</code></pre>

<!-- source-log-coverage:end -->
