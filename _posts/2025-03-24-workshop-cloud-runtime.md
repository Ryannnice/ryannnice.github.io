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
