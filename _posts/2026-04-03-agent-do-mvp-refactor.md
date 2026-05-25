---
layout: single
title: "从 opencode 到 Agent-Do：Workshop MVP 的瘦身重构"
date: 2026-04-03
categories:
  - tech-blog
  - agent-engineering
series: "Agent Engineering"
priority: P2
tags:
  - Agent-Do
  - MVP
  - Docker
  - Refactor
excerpt: "复杂项目集成不总是正确方向；当目标是 Workshop MVP 时，更小的系统反而更容易稳定。"
source_log:
  - "Renyuan_Log.md:1425-1439"
  - "Renyuan_Log.md:1457-1484"
  - "Renyuan_Log.md:1522-1539"
---

opencode 提供了强大的 Agent 基础，但把一个大项目深度植入 Workshop 会引入额外复杂度。生成、流式输出、会话、工具调用、文件写入、运行预览，每一层都有自己的状态和假设。

当目标是快速做出可用 MVP 时，正确方向不一定是继续集成大系统，而是重新收窄边界。

## MVP 边界

Agent-Do 的目标可以更明确：接收需求，生成项目，运行验证，返回结果。它不需要一开始覆盖 opencode 的完整交互体验，也不需要继承所有内部结构。

边界越窄，调试越直接。

## 真实问题

重构阶段暴露出的关键问题包括：

- 容器内 workspace 挂载到错误宿主路径。
- Docker CLI 在容器中不可用或路径不稳定。
- 生成结果为空时缺少兜底。
- 启动脚本和预览服务之间的约定不够清晰。

这些问题都说明：Agent 系统的稳定性不只来自模型能力，也来自运行环境 contract。

## 复盘

从 opencode 到 Agent-Do 的瘦身，不是推翻前面的探索，而是把探索过的能力压缩成最小可控链路。复杂系统适合提供参考，MVP 则必须保留最短路径。

工程上真正重要的问题是：当前阶段需要的是平台能力，还是可验证闭环。Workshop 的第一阶段答案是后者。
