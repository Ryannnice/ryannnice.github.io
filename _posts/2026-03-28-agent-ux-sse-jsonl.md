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
