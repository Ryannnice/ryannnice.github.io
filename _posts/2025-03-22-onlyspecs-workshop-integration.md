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
