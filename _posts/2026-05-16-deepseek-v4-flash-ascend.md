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
