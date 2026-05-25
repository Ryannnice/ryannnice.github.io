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

## 知识补全：为什么必须先本地验证再部署

云端部署失败的成本比本地验证失败高得多。上传 OSS、创建 FC、拉镜像、启动容器、等待健康检查，每一步都会消耗时间，也会把错误传播到更多系统。

本地验证的目标是把错误压缩在 workspace 内。依赖安装失败、构建失败、端口没监听、入口文件不存在，这些都应该在上传前发现。

一个可靠的验证报告至少应包含：

- 执行了哪些脚本。
- 每个脚本的退出码。
- stdout / stderr 摘要。
- 服务监听端口。
- HTTP probe 的状态码和响应摘要。
- 如果失败，下一轮 patch 应该优先查看哪些文件。

这份报告同时服务三类对象：开发者看日志、前端展示状态、LLM 进行修复。

## 部署链路的分层思维

Workshop 的部署问题可以分成四层：

1. 代码层：文件是否完整，入口是否正确。
2. 构建层：依赖是否可安装，build 是否通过。
3. 运行层：端口、环境变量、进程生命周期是否正确。
4. 云资源层：OSS、FC、镜像、权限和网络是否可用。

排障时应从下往上确认。否则很容易把代码错误误判成云平台问题，或把镜像问题误判成模型生成问题。
