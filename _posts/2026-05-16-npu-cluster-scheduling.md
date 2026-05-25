---
layout: single
title: "NPU 集群调度实战：Kubernetes + Volcano + ktp 如何影响推理服务"
date: 2026-05-16
categories:
  - tech-blog
  - serving-deployment
series: "Serving & Deployment"
priority: P1
tags:
  - Kubernetes
  - Volcano
  - ktp
  - HCCL
  - NPU
excerpt: "模型服务启动失败时，问题可能不在模型，而在调度、镜像缓存、共享存储和跨节点通信。"
source_log:
  - "Renyuan_Log.md:3043-3052"
  - "Renyuan_Log.md:3131-3148"
  - "Renyuan_Log.md:3207-3239"
  - "Renyuan_Log.md:3250-3310"
---

大模型部署在集群上时，用户看到的只是一个任务状态，但背后是调度器、节点、镜像缓存、共享存储和通信初始化共同决定结果。

## 资源层级

一个 NPU 集群可以抽象成：

```text
Cluster -> Node -> NPU -> Queue -> Job -> Pod
```

节点通常有固定数量的 NPU。请求 8 NPU、16 NPU、32 NPU 对调度器来说是完全不同的资源形态。请求 16 NPU 可能意味着占用一个完整节点；请求 32 NPU 可能需要两个节点同时空闲。

## 调度流程

任务提交后，Volcano 根据队列配额和节点空闲情况分配资源。用户通常不能直接指定节点。Pod 被创建后会挂载共享存储，等待通信配置就绪，然后启动模型服务。

单节点通信和多节点通信的失败模式不同。单节点主要关注卡内通信和本地资源；多节点还要关注 master 地址、HCCL 初始化、跨节点 RPC 和网络。

## Pending 不只是排队

Pod 长时间 Pending 可能来自：

- 没有足够空闲 NPU。
- CPU 或内存请求过高。
- 镜像没有缓存，拉取时间很长。
- 队列配额不足。

因此观察任务时不能只看 NPU 数量，还要看 CPU、memory、queue 和镜像缓存。

## 部署排障分层

模型服务起不来时，可以按四层排查：

1. 模型和运行时是否兼容。
2. 镜像是否包含需要的代码和 parser。
3. 调度器是否分配到足够资源。
4. 通信和共享存储是否正常。

这比直接重复提交任务更有效。
