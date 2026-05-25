---
layout: single
title: "Agent 前端如何展示过程：SSE、JSONL、文件树、代码预览与安全状态"
date: 2026-03-28
categories:
  - tech-blog
  - agent-engineering
series: "Agent Engineering"
priority: P0
featured: true
tags:
  - SSE
  - JSONL
  - Agent UX
  - FastAPI
  - Streaming
excerpt: "把黑盒生成改成可观察任务流：文件树、代码预览、阶段状态和最终结果都通过事件驱动更新。"
source_log:
  - "Renyuan_Log.md:1171-1313"
  - "Renyuan_Log.md:1397-1419"
  - "Renyuan_Log.md:1457-1459"
---

Agent 生成项目时，如果前端只显示一个 loading，用户无法判断系统是在思考、写文件、构建、修复，还是已经卡死。更好的体验是把生成过程拆成事件流，让前端实时展示状态和产物。

## API 形态

推荐接口是任务式的：

```text
POST /generate/jobs
GET  /generate/jobs/{job_id}
GET  /generate/jobs/{job_id}/stream
GET  /generate/jobs/{job_id}/result
DELETE /generate/jobs/{job_id}
```

`POST` 创建任务，返回 `job_id`。前端用 `EventSource` 订阅 SSE。结果完成后再通过 result 接口获取最终文件集。

这种形态比同步 `/generate` 更容易处理长任务、断线重连和前端状态恢复。

## 事件协议

事件应该是稳定 JSON，而不是把模型的自然语言输出直接转给前端。

关键事件包括：

- `job.created`：任务创建。
- `thinking.status`：安全的阶段摘要，例如“正在规划项目结构”。
- `project.tree`：当前文件树。
- `file.snapshot`：某个文件的完整快照。
- `preview.code`：用于展示的少量代码行。
- `job.status`：queued、running、succeeded、failed。
- `job.result`：最终文件结果。

这个协议可以同时满足三个需求：展示文件结构、展示已有文件、展示当前阶段。

## 不暴露原始 reasoning

前端需要“过程感”，但不需要模型的原始推理。`thinking.status` 应该来自后端阶段摘要，而不是原样转发模型内部 reasoning。

可展示的状态是：

- 分析需求中
- 规划项目结构中
- 正在编写 package.json
- 正在修复启动脚本
- 正在校验最终结果

这样足够让用户理解进度，也不会把不该暴露的内容放到页面上。

## 后端桥接

一个实用实现是：生成器输出 JSONL 到 stdout，FastAPI 读取后转成 SSE。Bun 或 Node 侧负责在文件变化、阶段变化、结束时输出结构化事件；FastAPI 负责保存任务状态并向前端推流。

同步 `/generate` 可以保留，流式任务作为增强路径存在。这样不会破坏已有调用方。

这套设计的核心是：前端看到的不是模型文本，而是后端认可的任务事实。

## 知识补全：SSE、WebSocket 和轮询怎么选

前端展示 Agent 过程时，常见选择有三种：轮询、SSE、WebSocket。

轮询最简单，前端每隔一段时间请求一次任务状态。它适合状态变化少、实时性要求低的任务。缺点是延迟和请求浪费都明显，生成代码这种高频变化场景会显得迟钝。

WebSocket 是双向通道，适合多人协作、在线编辑、终端交互等双方都频繁发送消息的场景。但它会增加连接管理和重连复杂度。

SSE 是 HTTP 上的单向事件流，浏览器原生 `EventSource` 支持重连。Agent 生成过程通常是“后端不断推状态，前端只负责展示”，所以 SSE 是更轻的选择。

JSONL 则解决生成器和 FastAPI 之间的协议问题。每一行都是一个独立 JSON 事件，后端可以边读边转发，不必等整个任务结束。

## 学习检查清单

一个好的 Agent UX 不只是“有流式输出”，还应满足：

1. 用户能看到当前阶段，而不是只看到 token 流。
2. 文件树和文件内容来自真实写盘结果，而不是模型口头描述。
3. 错误状态能显示在哪个 step 失败。
4. 断线重连后能恢复当前快照。
5. 不展示原始 reasoning，只展示安全阶段摘要。
6. 最终结果和过程事件来自同一个任务状态源。

这样前端才不是给模型输出加动画，而是在展示系统真实进度。
