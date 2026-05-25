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
