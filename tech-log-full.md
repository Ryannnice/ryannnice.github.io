---
permalink: /tech-blog/full-log/
title: "Full Learning Log"
author_profile: true
---

This archive is generated from `Renyuan_Log.md` so every original date section, table, code block, ASCII diagram, and explanation remains findable from the tech blog.

The original log is rendered as line-numbered source blocks on purpose. This avoids a malformed code fence in the source from swallowing later Markdown while still preserving every table, code block, flow diagram, link, command, and explanation in original order.

## Coverage Index

| Date | Source Lines | Code Blocks | Table Rows | Diagram Blocks | First Subheading |
| --- | ---: | ---: | ---: | ---: | --- |
| [Preamble](#log-preamble) | 1-4 | 0 | 0 | 0 | 稔远学习日志 |
| [2025-03-19](#log-2025-03-19) | 5-54 | 1 | 0 | 1 | 知识学习 |
| [2025-03-20](#log-2025-03-20) | 55-68 | 0 | 0 | 0 | 知识学习 |
| [2025-03-21](#log-2025-03-21) | 69-228 | 7 | 0 | 6 | 知识学习 |
| [2025-03-22](#log-2025-03-22) | 229-414 | 4 | 0 | 2 | 实践 |
| [2025-03-23](#log-2025-03-23) | 415-528 | 5 | 0 | 2 | 知识学习 |
| [2025-03-24](#log-2025-03-24) | 529-693 | 1 | 0 | 1 | 实践 |
| [2025-03-25](#log-2025-03-25) | 694-964 | 4 | 0 | 0 | 知识学习 |
| [2026-03-26](#log-2026-03-26) | 965-1092 | 2 | 0 | 1 | 实践 |
| [2026-03-27](#log-2026-03-27) | 1093-1143 | 0 | 0 | 0 | 知识学习 |
| [2026-03-28](#log-2026-03-28) | 1144-1314 | 3 | 0 | 0 | 知识学习 |
| [2026-03-29](#log-2026-03-29) | 1315-1318 | 0 | 0 | 0 | 毕设毕设！ |
| [2026-03-30](#log-2026-03-30) | 1319-1420 | 5 | 0 | 0 | 知识学习 |
| [2026-04-01](#log-2026-04-01) | 1421-1440 | 0 | 0 | 0 | 知识学习 |
| [2026-04-02](#log-2026-04-02) | 1441-1485 | 1 | 0 | 0 | 知识学习 |
| [2026-04-03](#log-2026-04-03) | 1486-1540 | 0 | 0 | 0 | 知识学习 |
| [2026-04-04](#log-2026-04-04) | 1541-1550 | 0 | 0 | 0 | 知识学习 |
| [2026-04-05](#log-2026-04-05) | 1551-1554 | 0 | 0 | 0 | 毕设毕设！ |
| [2026-04-06](#log-2026-04-06) | 1555-1561 | 0 | 0 | 0 | 拯救计划很好看 |
| [2026-04-07](#log-2026-04-07) | 1562-1621 | 0 | 0 | 0 | 知识学习 |
| [2026-04-08](#log-2026-04-08) | 1622-1690 | 0 | 0 | 0 | 实践 |
| [2026-04-09](#log-2026-04-09) | 1691-1710 | 0 | 0 | 0 | 尝试更多的开源策略 |
| [2026-04-10](#log-2026-04-10) | 1711-1773 | 0 | 0 | 0 | 尝试更多的开源策略 |
| [2026-04-11](#log-2026-04-11) | 1774-1870 | 0 | 29 | 0 | 实践 |
| [2026-04-12](#log-2026-04-12) | 1871-1899 | 1 | 0 | 1 | 知识学习 |
| [2026-04-13](#log-2026-04-13) | 1900-2002 | 2 | 0 | 0 | 实践 |
| [2026-04-14](#log-2026-04-14) | 2003-2127 | 1 | 0 | 1 | 知识学习 |
| [2026-04-15](#log-2026-04-15) | 2128-2129 | 0 | 0 | 0 | 原文 |
| [2026-04-16](#log-2026-04-16) | 2130-2132 | 0 | 0 | 0 | 原文 |
| [2026-04-17](#log-2026-04-17) | 2133-2255 | 2 | 0 | 2 | 知识学习 |
| [2026-04-20](#log-2026-04-20) | 2256-2270 | 0 | 0 | 0 | Encoder 输出Z矩阵的归宿：KV |
| [2026-04-22](#log-2026-04-22) | 2271-2309 | 0 | 0 | 0 | vLLM-Router 完整运行起来了 |
| [2026-04-26](#log-2026-04-26) | 2310-2393 | 1 | 0 | 0 | CUDA |
| [2026-04-27](#log-2026-04-27) | 2394-2410 | 0 | 0 | 0 | 远方 faraway |
| [2026-04-28](#log-2026-04-28) | 2411-2474 | 1 | 6 | 0 | CUDA 编程 |
| [2026-04-29](#log-2026-04-29) | 2475-2577 | 0 | 0 | 0 | RoPE |
| [2026-04-30](#log-2026-04-30) | 2578-2594 | 0 | 0 | 0 | 关于推理框架 |
| [2026-05-01](#log-2026-05-01) | 2595-2606 | 0 | 0 | 0 | GPU操作 |
| [2026-05-04](#log-2026-05-04) | 2607-2646 | 0 | 13 | 0 | vLLM 工程边界与目录地图 |
| [2026-05-05](#log-2026-05-05) | 2647-2818 | 1 | 0 | 1 | 不同的并行方式 |
| [2026-05-07](#log-2026-05-07) | 2819-2820 | 0 | 0 | 0 | 原文 |
| [2026-05-08](#log-2026-05-08) | 2821-2822 | 0 | 0 | 0 | 原文 |
| [2026-05-09](#log-2026-05-09) | 2823-2824 | 0 | 0 | 0 | 原文 |
| [2026-05-10](#log-2026-05-10) | 2825-2830 | 0 | 0 | 0 | 原文 |
| [2026-05-11](#log-2026-05-11) | 2831-3015 | 0 | 9 | 0 | FSDP / ZeRO-3 和张量并行 TP 的区别 |
| [2026-05-12](#log-2026-05-12) | 3016-3022 | 0 | 0 | 0 | mini-vllm 源码完结！ |
| [2026-05-13](#log-2026-05-13) | 3023-3068 | 0 | 12 | 0 | 尝试启动 DeepSeek V4 Flash 的推理服务 |
| [2026-05-14](#log-2026-05-14) | 3069-3082 | 0 | 0 | 0 | 手动配置一天的 DeepSeek V4 环境 |
| [2026-05-15](#log-2026-05-15) | 3083-3113 | 0 | 0 | 0 | 河套学院晟腾课程 |
| [2026-05-16](#log-2026-05-16) | 3114-3385 | 7 | 39 | 1 | DeepSeek V4 Flash W8A8 部署总结 |
| [2026-05-17](#log-2026-05-17) | 3386-3500 | 5 | 5 | 2 | CUDA kernel 与 device function |
| [2026-05-20](#log-2026-05-20) | 3501-3511 | 0 | 0 | 0 | 原文 |
| [2026-05-21](#log-2026-05-21) | 3512-3538 | 0 | 6 | 0 | 算子学习 Chapter 3：数值处理与规约 |
| [2026-05-22](#log-2026-05-22) | 3539-3596 | 2 | 4 | 0 | LayerNorm 和 RMSNorm 的几何理解 |

## Artifact Index

| Type | Date | Source Lines | Label |
| --- | --- | ---: | --- |
| code | [2025-03-19](#log-2025-03-19) | 35-45 | fenced block |
| diagram | [2025-03-19](#log-2025-03-19) | 35-45 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 85-92 | fenced block |
| code | [2025-03-21](#log-2025-03-21) | 93-116 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 93-116 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 130-135 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 130-135 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 149-169 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 149-169 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 172-184 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 172-184 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 189-197 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 189-197 | ASCII / flow diagram inside fenced block |
| code | [2025-03-21](#log-2025-03-21) | 200-225 | fenced block |
| diagram | [2025-03-21](#log-2025-03-21) | 200-225 | ASCII / flow diagram inside fenced block |
| code | [2025-03-22](#log-2025-03-22) | 242-292 | fenced block |
| diagram | [2025-03-22](#log-2025-03-22) | 242-292 | ASCII / flow diagram inside fenced block |
| code | [2025-03-22](#log-2025-03-22) | 307-309 | fenced block |
| code | [2025-03-22](#log-2025-03-22) | 326-352 | fenced block |
| diagram | [2025-03-22](#log-2025-03-22) | 326-352 | ASCII / flow diagram inside fenced block |
| code | [2025-03-22](#log-2025-03-22) | 368-413 | fenced block |
| code | [2025-03-23](#log-2025-03-23) | 421-423 | fenced block |
| code | [2025-03-23](#log-2025-03-23) | 428-430 | fenced block |
| code | [2025-03-23](#log-2025-03-23) | 431-433 | fenced block |
| code | [2025-03-23](#log-2025-03-23) | 440-458 | fenced block |
| diagram | [2025-03-23](#log-2025-03-23) | 440-458 | ASCII / flow diagram inside fenced block |
| code | [2025-03-23](#log-2025-03-23) | 463-527 | fenced block |
| diagram | [2025-03-23](#log-2025-03-23) | 463-527 | ASCII / flow diagram inside fenced block |
| code | [2025-03-24](#log-2025-03-24) | 551-636 | fenced block |
| diagram | [2025-03-24](#log-2025-03-24) | 551-636 | ASCII / flow diagram inside fenced block |
| code | [2025-03-25](#log-2025-03-25) | 736-741 | fenced block |
| code | [2025-03-25](#log-2025-03-25) | 744-759 | fenced block |
| code | [2025-03-25](#log-2025-03-25) | 837-853 | fenced block |
| code | [2025-03-25](#log-2025-03-25) | 861-912 | fenced block |
| code | [2026-03-26](#log-2026-03-26) | 974-997 | fenced block |
| diagram | [2026-03-26](#log-2026-03-26) | 974-997 | ASCII / flow diagram inside fenced block |
| code | [2026-03-26](#log-2026-03-26) | 1000-1063 | fenced block |
| code | [2026-03-28](#log-2026-03-28) | 1179-1191 | fenced block |
| code | [2026-03-28](#log-2026-03-28) | 1200-1256 | fenced block |
| code | [2026-03-28](#log-2026-03-28) | 1259-1279 | fenced block |
| code | [2026-03-30](#log-2026-03-30) | 1351-1356 | fenced block |
| code | [2026-03-30](#log-2026-03-30) | 1359-1363 | fenced block |
| code | [2026-03-30](#log-2026-03-30) | 1366-1370 | fenced block |
| code | [2026-03-30](#log-2026-03-30) | 1373-1378 | fenced block |
| code | [2026-03-30](#log-2026-03-30) | 1381-1390 | fenced block |
| code | [2026-04-02](#log-2026-04-02) | 1470-1478 | fenced block |
| table | [2026-04-11](#log-2026-04-11) | 1801-1820 | Markdown table |
| table | [2026-04-11](#log-2026-04-11) | 1824-1832 | Markdown table |
| code | [2026-04-12](#log-2026-04-12) | 1889-1898 | fenced block |
| diagram | [2026-04-12](#log-2026-04-12) | 1889-1898 | ASCII / flow diagram inside fenced block |
| code | [2026-04-13](#log-2026-04-13) | 1909-1928 | fenced block |
| code | [2026-04-13](#log-2026-04-13) | 1951-1957 | fenced block |
| code | [2026-04-14](#log-2026-04-14) | 2076-2103 | fenced block |
| diagram | [2026-04-14](#log-2026-04-14) | 2076-2103 | ASCII / flow diagram inside fenced block |
| code | [2026-04-17](#log-2026-04-17) | 2166-2175 | fenced block: python |
| diagram | [2026-04-17](#log-2026-04-17) | 2166-2175 | ASCII / flow diagram inside fenced block |
| code | [2026-04-17](#log-2026-04-17) | 2183-2202 | fenced block: RoPE |
| diagram | [2026-04-17](#log-2026-04-17) | 2183-2202 | ASCII / flow diagram inside fenced block |
| code | [2026-04-26](#log-2026-04-26) | 2352-2359 | fenced block: cpp |
| code | [2026-04-28](#log-2026-04-28) | 2427-2429 | fenced block: cpp |
| table | [2026-04-28](#log-2026-04-28) | 2438-2443 | Markdown table |
| table | [2026-05-04](#log-2026-05-04) | 2613-2625 | Markdown table |
| orphan_fence | [2026-05-05](#log-2026-05-05) | 2801-2801 | unpaired code fence marker within date section |
| code | [2026-05-05](#log-2026-05-05) | 2803-2814 | fenced block: 在 Megatron-LM / vLLM 中典型结构： |
| diagram | [2026-05-05](#log-2026-05-05) | 2803-2814 | ASCII / flow diagram inside fenced block |
| table | [2026-05-11](#log-2026-05-11) | 2840-2848 | Markdown table |
| table | [2026-05-13](#log-2026-05-13) | 3032-3039 | Markdown table |
| table | [2026-05-13](#log-2026-05-13) | 3045-3048 | Markdown table |
| table | [2026-05-16](#log-2026-05-16) | 3159-3168 | Markdown table |
| code | [2026-05-16](#log-2026-05-16) | 3256-3265 | fenced block: text |
| diagram | [2026-05-16](#log-2026-05-16) | 3256-3265 | ASCII / flow diagram inside fenced block |
| code | [2026-05-16](#log-2026-05-16) | 3277-3288 | fenced block: yaml |
| table | [2026-05-16](#log-2026-05-16) | 3292-3302 | Markdown table |
| code | [2026-05-16](#log-2026-05-16) | 3318-3320 | fenced block: cpp |
| code | [2026-05-16](#log-2026-05-16) | 3332-3334 | fenced block: cpp |
| table | [2026-05-16](#log-2026-05-16) | 3342-3347 | Markdown table |
| code | [2026-05-16](#log-2026-05-16) | 3351-3353 | fenced block: text |
| table | [2026-05-16](#log-2026-05-16) | 3357-3362 | Markdown table |
| code | [2026-05-16](#log-2026-05-16) | 3366-3368 | fenced block: text |
| table | [2026-05-16](#log-2026-05-16) | 3372-3377 | Markdown table |
| code | [2026-05-16](#log-2026-05-16) | 3381-3383 | fenced block: text |
| table | [2026-05-17](#log-2026-05-17) | 3409-3413 | Markdown table |
| code | [2026-05-17](#log-2026-05-17) | 3417-3423 | fenced block: cpp |
| code | [2026-05-17](#log-2026-05-17) | 3433-3435 | fenced block: text |
| diagram | [2026-05-17](#log-2026-05-17) | 3433-3435 | ASCII / flow diagram inside fenced block |
| code | [2026-05-17](#log-2026-05-17) | 3463-3467 | fenced block: cpp |
| code | [2026-05-17](#log-2026-05-17) | 3481-3483 | fenced block: text |
| diagram | [2026-05-17](#log-2026-05-17) | 3481-3483 | ASCII / flow diagram inside fenced block |
| code | [2026-05-17](#log-2026-05-17) | 3489-3491 | fenced block: text |
| table | [2026-05-21](#log-2026-05-21) | 3526-3531 | Markdown table |
| code | [2026-05-22](#log-2026-05-22) | 3567-3569 | fenced block: text |
| code | [2026-05-22](#log-2026-05-22) | 3575-3578 | fenced block: text |
| table | [2026-05-22](#log-2026-05-22) | 3584-3587 | Markdown table |

## Original Log

<a id="log-preamble"></a>
### Preamble

Source lines: `1-4`

<pre class="tech-log-source"><code>
0001  # 稔远学习日志
0002  
0003  仅个人学习与实践记录，便于回顾与整理。
0004  
</code></pre>

<a id="log-2025-03-19"></a>
### 2025-03-19

Source lines: `5-54`

<pre class="tech-log-source"><code>
0005  # 2025-03-19
0006  
0007  ## 知识学习
0008  
0009  #### 图解Transformer
0010  非常清晰的图示教程，用矩阵拆解Transformer，难度梯度很合适
0011  [教程](https://jalammar.github.io/illustrated-transformer/)
0012  
0013  #### TypeScript/npm包管理
0014  
0015  #### TypeScript[(清华大学的AI教育项目)](https://github.com/Ryannnice/CUHK-LLM-Edu/edit/main/README.md)
0016  
0017  整个项目绝大部分使用TypeScript,文件结构、调用逻辑非常复杂
0018  TypeScript 是 JavaScript 的超集
0019  
0020  #### npm
0021  
0022  npm = Node Package Manager（Node.js 包管理器）
0023  
0024  安装库和工具/管理依赖（项目里用到的第三方包）/**运行脚本**（比如启动 Vue、React 或 Node 项目）
0025  *npm run &lt;脚本名&gt;: 运行 package.json 里的脚本*
0026  
0027  #### FastAPI python框架了解
0028  第一次实习，第一次接触偏工程的项目：不同于科研的是，可行性/整体模块的缝合、运行似乎比细致的优化更重要
0029  
0030  清华的开源教育项目未采用前后端分离架构
0031  
0032  使用.json格式请求体完成数据/信息传递
0033  
0034  前端直接通过函数调用REST API:
0035  ```
0036   fastapi_backend/
0037      └── static/
0038          ├── index.html        # 主页（需求输入 + 设置）
0039          ├── generate.html     # 生成流程页（SSE 大纲流 + 进度）
0040          ├── classroom.html    # 课堂播放页（幻灯片/测验/聊天）
0041          ├── app.js            # 全局工具：API 调用、设置存储、路由
0042          ├── generate.js       # 生成流程逻辑
0043          ├── classroom.js      # 课堂播放逻辑（幻灯片渲染、测验、聊天）
0044          └── style.css         # 全局样式
0045  ```
0046  
0047  ## 实践
0048  
0049  #### FastAPI
0050  在原本的REST API接口上，建立/fastapi_backend文件夹，用FastAPI封装全部18个功能的api
0051  原有.ts文件前端直接调用api的所有逻辑均保留，与Fast后端接口不冲突
0052  
0053  实现后端分离之后，建立/fastapi_backend/static文件夹，仅使用js/html初步实现前端功能，以验证FastAPI后端接口可行性
0054  
</code></pre>

<a id="log-2025-03-20"></a>
### 2025-03-20

Source lines: `55-68`

<pre class="tech-log-source"><code>
0055  # 2025-03-20
0056  
0057  ## 知识学习
0058  
0059  #### 开源库OnlySpecs
0060  这是自动生成软件的agent系统，可能对项目第二部分*WorkShop*有帮助
0061  （上午团队实现workshop功能时发现直接调用LLM实现代码（软件编程）能力有限：贪吃蛇不成功，推箱子成功）
0062  试图部署该开源项目，接入我们的项目
0063  
0064  ## 实践
0065  
0066  #### Linux bash
0067  上午claude api爆了，以为是网络问题重新配置安装一遍windows WSL的linux的网络环境
0068  
</code></pre>

<a id="log-2025-03-21"></a>
### 2025-03-21

Source lines: `69-228`

<pre class="tech-log-source"><code>
0069  # 2025-03-21
0070  
0071  ## 知识学习
0072  
0073  #### 开源库OnlySpecs
0074  
0075  #### node-pty
0076  
0077  pty.spawn(&quot;claude&quot;)
0078  
0079  相当于**在程序里打开**一个**终端**窗口
0080  
0081  #### AIEngine
0082  
0083  一个“可以驱动 Claude CLI 干活”的执行器
0084  
0085  ```
0086  return new Promise((resolve, reject) =&gt; {
0087      proc.onExit((e) =&gt; {
0088          if (e.exitCode === 0) resolve()
0089          else reject(new Error(...))
0090      })
0091  })
0092  ```
0093  ```
0094  ┌─────────────┐
0095  │ run() 调用  │
0096  │ await engine│
0097  └─────┬───────┘
0098        │
0099        ▼
0100  ┌─────────────┐
0101  │ Promise     │   &lt;-- pending 状态
0102  │ resolve/reject 内部管子
0103  └─────┬───────┘
0104        │
0105        ▼
0106  ┌─────────────┐
0107  │ proc.onExit │  &lt;-- Claude CLI 退出触发
0108  │ e.exitCode  │
0109  └─────┬───────┘
0110        │
0111        ▼
0112  if(exitCode==0) resolve()  else reject(error)
0113        │
0114        ▼
0115  Promise 状态变更 → 外层 await/then/catch 收到结果
0116  ```
0117  
0118  #### Shim
0119  
0120  是一种兼容层或适配器，用于在不修改原有代码的情况下，让新旧接口或系统之间能够协同工作
0121  
0122  这很适用于最小化更改，让该开源项目快速应用于我们的项目中，以此为起点吧
0123  
0124  #### Node.js Web 服务器
0125  
0126  Node.js 是一个运行环境，可以用 JavaScript 写服务端程序
0127  
0128  &quot;Node.js Web 服务器&quot;就是用 Node.js 写的 HTTP 服务，比如用 Express、Fastify、Koa 等框架搭建的后端，和阿里云服务器不冲突
0129  
0130  ```
0131  阿里云 ECS（服务器硬件/系统）
0132      └── Nginx（反向代理，监听 80/443 端口）
0133            └── Node.js 进程（监听 3000 端口）
0134                  └── 你的业务代码
0135  ```
0136  
0137  ## 实践
0138  
0139  #### Web版OnlySpecs功能测试
0140  
0141  已完成在web上的部署，使用简单的html转跳
0142  
0143  汉化前端菜单栏
0144  
0145  #### 融入大项目的Workshop部分
0146  
0147  **我们项目Workshop的原架构：**
0148  
0149  ```
0150  用户 → Vue
0151          │
0152          ▼
0153  FastAPI /generate
0154          │
0155          ▼
0156  DeepSeek 生成 HTML
0157          │
0158          ▼
0159  FastAPI /upload
0160          │
0161          ▼
0162  阿里云 OSS
0163          │
0164          ▼
0165  返回 URL
0166          │
0167          ▼
0168  Vue 展示
0169  ```
0170  
0171  **开源软件OnlySpecs的原架构：**
0172  ```
0173  Electron UI
0174      ↓
0175  Renderer (DOM + Monaco)
0176      ↓
0177  IPC
0178      ↓
0179  Main Process
0180      ↓
0181  node-pty
0182      ↓
0183  Claude CLI
0184  ```
0185  
0186  **新架构融合，两种方案：**
0187  
0188  ***方案一，分离式：***
0189  ```
0190   大项目
0191   ├── Vue 仪表盘（前端）   → Docker: Nginx 静态托管，端口 80
0192   ├── FastAPI 后端         → Docker: Uvicorn，端口 9000
0193   │   ├── /generate        → DeepSeek 流式生成 HTML
0194   │   └── /upload          → 阿里云 OSS 上传
0195   └── OnlySpecs（待加入）  → Docker: Node.js，端口 3579
0196       └── 功能：Specs 编写、Claude AI 代码生成、终端
0197  ```
0198  
0199  ***方案二，通过FastAPI使用功能，仅替换掉LLM，使用claude agent编写软件：***
0200  ```
0201  Vue 前端
0202      ↓ POST /generate-software { prompt }
0203    FastAPI
0204      ↓ 调用 OnlySpecs Node.js 服务（HTTP 或子进程）
0205    OnlySpecs Web Server
0206      ↓ 写 specs.md → 启动 Claude CLI
0207    Claude CLI（node-pty）
0208      ↓ 生成代码
0209    返回结果（文件路径 / OSS URL）
0210      ↑ 流式进度推送（SSE / WebSocket）
0211    Vue 前端展示
0212  
0213  
0214  FastAPI 端点设计
0215    # POST /generate-software
0216    # 输入：用户 prompt
0217    # 输出：SSE 流式进度 + 最终代码 URL
0218  
0219    @app.post(&quot;/generate-software&quot;)
0220    async def generate_software(prompt: str):
0221        # 1. 调用 OnlySpecs API 创建 specs 文件
0222        # 2. 触发 Generate from Specs
0223        # 3. 流式返回进度
0224        # 4. 完成后上传到 OSS，返回 URL
0225  ```
0226  
0227  先尝试方案二，先设计无头OnlySpecs的API
0228  
</code></pre>

<a id="log-2025-03-22"></a>
### 2025-03-22

Source lines: `229-414`

<pre class="tech-log-source"><code>
0229  # 2025-03-22
0230  
0231  ## 实践
0232  
0233  FastAPI 编写完成，核心是/generate 根据用户指令来交给OnlySpecs，利用其功能生成
0234  
0235  api测试成功（文档：/home/ryan/OnlySpecs/docs/API_QUICKSTART.md，测试：终端运行 npm run test:api）
0236  
0237  接下来对接我们的项目第二部分Workshop：
0238  实现方式参考原框架，写出仿制的前端：/home/ryan/OnlySpecs/api-integration
0239  
0240  整个Pipeline:
0241  
0242  ```
0243    📁 Project Structure
0244  
0245    ~/OnlySpecs/api-integration/
0246    ├── app.py              # FastAPI backend (API proxy + SSE streaming)
0247    ├── requirements.txt    # Python dependencies
0248    ├── .env               # Environment configuration
0249    ├── .env.example       # Environment template
0250    ├── start.sh           # Quick start script
0251    ├── static/
0252    │   └── index.html     # Vue 3 frontend (312 lines)
0253    └── README.md          # Complete documentation
0254  
0255    🎯 Key Features Implemented
0256  
0257    Backend (FastAPI):
0258    - ✅ CORS-enabled API proxy to OnlySpecs API
0259    - ✅ SSE streaming for real-time log updates
0260    - ✅ Endpoints: /api/generate, /api/status, /api/logs, /api/tasks, /api/download
0261    - ✅ Error handling and timeout controls
0262  
0263    Frontend (Vue 3 + Tailwind):
0264    - ✅ Clean, responsive UI with Chinese localization
0265    - ✅ Real-time log display with auto-scroll
0266    - ✅ Task status tracking (pending/running/completed/failed)
0267    - ✅ History task list with click-to-load
0268    - ✅ Download generated code as ZIP
0269    - ✅ EventSource for SSE log streaming
0270  
0271    🚀 Quick Start
0272  
0273    # 1. Start OnlySpecs API (in one terminal)
0274    cd ~/OnlySpecs
0275    npm run api
0276  
0277    # 2. Start frontend (in another terminal)
0278    cd ~/OnlySpecs/api-integration
0279    ./start.sh
0280  
0281    Then visit: http://localhost:9000
0282  
0283    📝 Usage Flow
0284    1. Enter software requirements in the text area
0285    2. Click &quot;开始生成&quot; (Start Generation)
0286    3. Watch real-time Claude CLI logs
0287    4. Download code when complete or open in file explorer
0288    5. View history tasks in the collapsible section
0289  
0290    The implementation follows the plan exactly, using SSE for real-time updates and providing a simple, user-friendly interface for interacting
0291    with OnlySpecs.
0292  ```
0293  
0294  已经能完美运行，依靠简洁的web界面，通过FastAPI和OnlySpecs交互
0295  
0296  ***输入--&gt;OnlySpecs--&gt;Claude CLI--&gt;输出***，用户只负责敲几个字：项目第二部分低代码的思想
0297  
0298  debug修复内容：
0299  
0300  1. claude开始但是不工作，代码写不进去项目文件夹 / claude 不动，接收不到指令：--print 标志可以完全跳过交互式 UI，直接输出结果。不需要 pty 模拟，改用子进程即可。用 spawn + --print 替换整个 pty 方案，彻底解决交互式 UI 问题。
0301  
0302  2. 下载 ZIP之后win系统打不开：之前是把 OnlySpecs API 返回的 JSON 当 ZIP 存的，当然打不开。现在后端拿到 codePath，用 shutil.make_archive 真正打包成 ZIP，Win11 可以直接解压。
0303  
0304  3. “在文件管理器中打开”的按钮点不动：新增了 /api/open/{task_id} 接口，调用 xdg-open 打开 Linux 文件管理器，同时在界面显示代码路径。
0305  WSL2 里 xdg-open 无法直接打开 Windows 文件管理器。需要用 explorer.exe 来打开，但路径要转换成 Windows 格式。
0306  转换出来是 \\wsl.localhost\Ubuntu\... 格式，Win11 的文件资源管理器可以直接打开这个 UNC 路径。
0307  ```
0308  \\wsl.localhost\Ubuntu\home\ryan\Documents\OnlySpecs\api-workspaces\task_1774168877875_1u1yudaz6\code_v0001
0309  ```
0310  
0311  ***全部修复***
0312  
0313  朝着更更更低代码平台进发：
0314  
0315  📋 计划总结
0316  
0317  核心功能： 在 Web 界面添加 4 种输出类型选择：
0318  
0319  1. 📄 源代码 - 可编辑的源文件
0320  2. 🌐 Web 应用 - 单文件 HTML，浏览器直接运行
0321  3. 💻 桌面程序 - Windows .exe 可执行文件（自动打包）
0322  4. 📱 手机应用 - PWA 渐进式 Web 应用
0323  
0324  用户使用Pipeline:
0325  
0326  ```
0327  用户浏览器
0328      │
0329      ▼
0330  Vue 前端
0331      │
0332      ▼
0333  FastAPI API
0334      │
0335      ▼
0336  OnlySpecs AI Engine （调用Claude CLI）
0337      │
0338      ▼
0339  生成代码
0340      │
0341      ▼
0342  Build Worker（Docker）
0343      │
0344      ▼
0345  编译为 .exe
0346      │
0347      ▼
0348  上传到 OSS
0349      │
0350      ▼
0351  用户下载
0352  ```
0353  
0354  本地项目列表已更新：
0355  
0356  新功能：
0357  1. 类型标签 - 每个项目左侧显示彩色标签：
0358    - 📄 源代码（紫色）
0359    - 🌐 Web应用（靛蓝色）
0360    - 💻 桌面程序（橙色）
0361    - 📱 手机应用（粉色）
0362  2. 对应按钮 - 根据项目类型显示不同的主功能按钮：
0363    - 源代码：📄 线上查看 + 📦 下载源码
0364    - Web应用：🌐 线上运行 + 📦 下载源码
0365    - 桌面程序：💻 下载 .exe + 📦 下载源码
0366    - 手机应用：📱 下载应用 + 📦 下载源码
0367  
0368  ```
0369    部署步骤：
0370  
0371    1. 在阿里云服务器上安装依赖：
0372    安装Node.js
0373    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
0374    sudo apt-get install -y nodejs
0375  
0376    安装Python
0377    sudo apt-get install python3 python3-pip
0378  
0379    安装Docker
0380    curl -fsSL https://get.docker.com | sudo sh
0381    sudo usermod -aG docker $USER
0382  
0383    安装Claude CLI
0384    npm install -g @anthropic-ai/claude-code
0385  
0386    2. 配置Claude API密钥：
0387    export ANTHROPIC_API_KEY=&quot;your-api-key-here&quot;
0388  
0389    3. 打包项目：
0390    cd ~/OnlySpecs
0391    tar -czf onlyspecs-deploy.tar.gz \
0392      src/ \
0393      api-integration/ \
0394      package.json\
0395      tsconfig.json
0396    4. 上传到服务器：
0397    scp onlyspecs-deploy.tar.gz user@your-server:/home/user/
0398  
0399    5. 在服务器上解压并启动：
0400    tar -xzf onlyspecs-deploy.tar.gz
0401    npm install
0402    docker pull cdrx/pyinstaller-windows
0403  
0404    启动服务
0405    npm run api &amp;
0406    cd api-integration &amp;&amp; python3 app.py &amp;
0407  
0408    6. 配置防火墙：
0409    sudo ufw allow 3580
0410    sudo ufw allow 9000
0411  
0412    访问：http://your-server-ip:9000
0413  ```
0414  
</code></pre>

<a id="log-2025-03-23"></a>
### 2025-03-23

Source lines: `415-528`

<pre class="tech-log-source"><code>
0415  # 2025-03-23
0416  
0417  ## 知识学习
0418  
0419  #### Docker
0420  
0421  ```
0422  https://www.bilibili.com/video/BV1THKyzBER6/?share_source=copy_web&amp;vd_source=035cd776909e96dadfc9bbaeb1588cd4
0423  ```
0424  
0425  #### FastAPI
0426  
0427  FastAPI配合**后端开发**：
0428  ```
0429  https://www.bilibili.com/video/BV1eUxve7Ein/?share_source=copy_web&amp;vd_source=035cd776909e96dadfc9bbaeb1588cd4
0430  ```
0431  ```
0432  https://fastapi.org.cn/python-types/#pydantic-models
0433  ```
0434  
0435  上下文工程 Context Engineering
0436  
0437  #### 谕书的Workshop框架和API
0438  
0439  项目框架采用FC容器(每个项目一个)，而不是fs操作本地文件
0440  ```
0441  OSS+FC的架构：
0442  ┌─────────────────────────────────────────────────────┐
0443  │                    用户浏览器                         │
0444  │  左：对话+文件树    中：代码查看    右：预览iframe      │
0445  └──────────┬──────────────────────────────┬───────────┘
0446             │              │ iframe src
0447             ▼                             ▼
0448  ┌─────────────────┐            ┌──────────────────────┐
0449  │  你的FastAPI服务 │            │  FC容器(每个项目一个) │
0450  │  (项目管理/调度) │            │   dev server:9000    │
0451  └────────┬────────┘            └──────────┬───────────┘
0452           │                                │
0453      ┌────┴──────────────────────────┐     │
0454      │         阿里云基础设施         │     │
0455      │  OSS(代码+静态)  RDS(MySQL)    |◄───┘
0456      │  ACR(镜像仓库)   MNS(消息队列) │
0457      └───────────────────────────────┘
0458  ```
0459  这个线上部署运行架构值得融合，今天做这件事：
0460  
0461  ## 实践
0462  
0463  ```
0464  OnlySpecs 的现有架构梳理：
0465  
0466    四种运行模式:
0467    ┌──────────────┬───────────────┬──────┬─────────────────────┐
0468    │     模式     │     入口      │ 端口 │        说明         │
0469    ├──────────────┼───────────────┼──────┼─────────────────────┤
0470    │ 桌面应用     │ npm run dev   │ —    │ Electron + IPC      │
0471    ├──────────────┼───────────────┼──────┼─────────────────────┤
0472    │ 无头 API     │ npm run api   │ 3580 │ Express + 子进程    │
0473    ├──────────────┼───────────────┼──────┼─────────────────────┤
0474    │ Web 界面     │ npm run web   │ 3579 │ Express + WebSocket │
0475    ├──────────────┼───────────────┼──────┼─────────────────────┤
0476    │ FastAPI 前端 │ python app.py │ 9000 │ 代理 API + SSE      │
0477    └──────────────┴───────────────┴──────┴─────────────────────┘
0478    核心数据流:
0479  
0480    桌面模式：
0481    Renderer (Monaco/xterm) → IPC → ipc-handlers.ts → 文件系统 / node-pty / Claude SDK
0482  
0483    API模式：
0484    HTTP POST /generate → 创建任务 → 启动 claude CLI子进程 → 写入 code_v0001/
0485    HTTP GET /logs/:id→ 轮询日志
0486  
0487    Web 模式：
0488    浏览器 → WebSocket → web-server（复用 ipc-handlers 逻辑）→ 文件系统 / node-pty
0489    FastAPI 模式：
0490    Vue3 → FastAPI (9000) → HTTP → API Server (3580) → claude CLI↑ SSE 实时日志流
0491  
0492    关键文件
0493  
0494    ┌──────────────────────────┬─────────────────────────────────────────────┐
0495    │           文件           │                    作用                     │
0496    ├──────────────────────────┼─────────────────────────────────────────────┤
0497    │ src/main/ipc-handlers.ts │ 所有 IPC 处理（编辑器、终端、文件、GitHub） │
0498    ├──────────────────────────┼─────────────────────────────────────────────┤
0499    │ src/main/claude/sdk.ts   │ Claude Agent SDK 封装，流式输出             │
0500    ├──────────────────────────┼─────────────────────────────────────────────┤
0501    │ src/renderer/index.ts    │ 主App 类，组装所有 UI组件                   │
0502    ├──────────────────────────┼─────────────────────────────────────────────┤
0503    │ src/api-server/index.ts  │ 无头 API，任务管理 + 子进程调度             │
0504    ├──────────────────────────┼─────────────────────────────────────────────┤
0505    │ src/web-server/index.ts  │ WebSocket 服务，镜像 IPC 协议               │
0506    ├──────────────────────────┼─────────────────────────────────────────────┤
0507    │ api-integration/app.py   │ FastAPI 代理 + SSE + ZIP 下载 + 项目管理    │
0508    └──────────────────────────┴─────────────────────────────────────────────┘
0509  
0510    ---
0511    数据存储
0512  
0513    ~/Documents/OnlySpecs/
0514    ├── editors/          # 编辑器内容（每个 tab 一个 JSON）
0515    ├── config.json       # API Key、上次项目路径
0516    ├── api-workspaces/   # API 模式生成的代码
0517    │   └── task_*/
0518    │├── specs_v0001.md
0519    │       └── code_v0001/
0520    └── tmp/              # GitHub import 临时克隆目录
0521  
0522    两个独立的 Claude 调用路径：
0523    1. 桌面/Web 模式 — 通过 claude/sdk.ts 调用 @anthropic-ai/claude-agent-sdk，流式返回结果给 UI
0524    2. API 模式 — 直接 spawn claude CLI 子进程，用 node-pty 捕获输出，存入任务日志
0525  
0526    两条路径互相独立，不共享代码。
0527  ```
0528  
</code></pre>

<a id="log-2025-03-24"></a>
### 2025-03-24

Source lines: `529-693`

<pre class="tech-log-source"><code>
0529  # 2025-03-24
0530  
0531  ## 实践
0532  
0533  #### Debug 网络代理
0534  
0535  #### 完善数据流向
0536  
0537  优化prompt以暴露onlyspecs原有复杂文档生成能力
0538  
0539  #### FastAPI
0540  
0541  对接谕书的架构，我第一次跑通了FastAPI的agent接口！
0542  
0543  已成功完成/generate接口，成功对接、上传到OSS
0544  
0545  目前，需完善FC系统
0546  
0547  #### FC容器
0548  
0549  #### 方案规划
0550  **potential solution:**
0551  ```
0552  完成 FC 容器调度与多文件生成验证
0553  
0554   Context
0555  
0556   当前状态：
0557   - Claude CLI 集成完成：POST /generate → Claude CLI → 收集文件 → OSS
0558   - 标准化 prompt 已实现：build_enhanced_prompt() 注入 scripts/ 目录要求
0559   - FC API 调度完成：POST /containers/{project_id}/start → 创建 FC 函数 → 返回 preview_url
0560   - OSS 存储完成：save_project() 上传文件 + manifest.json
0561  
0562   核心问题：
0563   FC 容器无法启动生成的代码，因为缺少容器内的启动逻辑：
0564   1. 缺少 entrypoint.sh - 容器启动脚本，负责从 OSS 下载代码并执行标准化脚本
0565   2. 缺少容器镜像 - base-node18/base-python39/base-fullstack 镜像不存在
0566   3. 无法验证多文件生成 - 没有端到端测试验证 Claude CLI 生成的复杂项目能否正常运行
0567  
0568   目标：
0569   完成 FC 调度链路，实现：用户 prompt → Claude 生成 → OSS 存储 → FC 容器运行 → 前端 iframe 预览
0570  
0571   ---
0572   实现方案
0573  
0574   方案 A：完整 FC 容器方案（生产级）
0575  
0576   需要实现：
0577   1. 创建 3 个 Dockerfile（base-node18, base-python39, base-fullstack）
0578   2. 编写 entrypoint.sh 脚本（下载 OSS 代码 → 执行 prepare.sh → 执行 dev.sh）
0579   3. 构建镜像并推送到 ACR
0580   4. 验证完整链路
0581  
0582   优点： 真实生产环境，完全符合 goal.md 架构
0583   缺点： 需要 Docker 环境、ACR 推送权限、FC 配额
0584  
0585   ---
0586   方案 B：本地验证方案（快速验证）
0587  
0588   只验证文件生成和脚本执行，不依赖 FC：
0589   1. 调用 /generate 生成项目
0590   2. 从 OSS 下载生成的文件到本地临时目录
0591   3. 本地执行 scripts/prepare.sh 和 scripts/dev.sh
0592   4. 验证服务能在 9000 端口启动
0593  
0594   优点： 快速验证，无需云资源
0595   缺点： 不是真实 FC 环境
0596  
0597   ---
0598   推荐方案：方案 B（本地验证）+ 方案 A 的容器脚本准备
0599  
0600   分两步走：
0601  
0602   第一步：本地验证多文件生成（立即可做）
0603  
0604   创建测试脚本 test_generation.py：
0605   - 调用 /generate API 生成简单项目（如 &quot;创建一个 Hello World 网页&quot;）
0606   - 检查返回的 files 列表是否包含：
0607     - scripts/prepare.sh
0608     - scripts/dev.sh（包含端口 9000）
0609     - scripts/build.sh
0610     - scripts/start.sh
0611     - 业务代码文件（如 src/index.html）
0612   - 从 OSS 下载所有文件到 /tmp/test-{project_id}/
0613   - 执行 bash scripts/prepare.sh（安装依赖）
0614   - 后台执行 bash scripts/dev.sh（启动服务）
0615   - 验证 curl http://localhost:9000 返回 200
0616  
0617   验证目标： 确认 Claude CLI 生成的项目结构正确，脚本可执行
0618  
0619   ---
0620   第二步：准备 FC 容器资源（为生产部署做准备）
0621  
0622   创建 3 个容器镜像的 Dockerfile 和 entrypoint.sh：
0623  
0624   文件结构：
0625   Reference-framework/
0626     docker/
0627       base-node18/
0628         Dockerfile
0629         entrypoint.sh
0630       base-python39/
0631         Dockerfile
0632         entrypoint.sh
0633       base-fullstack/
0634         Dockerfile
0635         entrypoint.sh
0636  ```
0637  
0638  #### 本地运行测试
0639  
0640  为了验证代码树的运行可行性。之后再真正在云端FC环境运行代码
0641  
0642  先完成**本地测试**，之后“登录 ACR”（ACR 指的是 Alibaba Cloud Container Registry）：
0643  
0644  把构建的 Docker 镜像**上传到阿里云的镜像仓库**，让 **FC 容器**可以拉取运行
0645  
0646  排查出的三个问题:
0647  
0648  问题 1：系统代理拦截了 localhost 请求 → 502
0649  
0650    http_proxy=http://172.26.224.1:7890
0651    所有 requests 发出的请求（包括 localhost）都走了代理，代理无法转发本地流量，返回 502
0652    解决：对 localhost 请求显式禁用代理，对公网 OSS 保留代理:
0653    PROXY_FOR_LOCALHOST = {&quot;http&quot;: None, &quot;https&quot;: None}
0654    PROXY_FOR_OSS = {&quot;http&quot;: os.environ.get(&quot;http_proxy&quot;), ...}
0655  
0656  问题 2：FastAPI 和生成项目端口冲突（都是 9000）
0657  
0658    测试脚本发完请求后，Step 6 验证的 http://localhost:9000 其实打到了 FastAPI 自己
0659    解决：FastAPI 改用 9001 启动：
0660    uvicorn app:app --port 9001
0661  
0662  问题 3：prepare.sh 写死 /workspace 本地不存在
0663  
0664    Claude 生成的脚本是为 FC 容器设计的（容器里代码在 /workspace），本地 /workspace 不存在
0665    解决：下载脚本后自动替换路径： patched = content.replace(&quot;/workspace&quot;, test_dir)
0666  
0667    验证结果:
0668    ┌───────────────────────────┬────────────────────────────┐
0669    │           步骤            │            结果            │
0670    ├───────────────────────────┼────────────────────────────┤
0671    │ Claude CLI 生成文件       │  7个文件包含所有必需脚本 │
0672    ├───────────────────────────┼────────────────────────────┤
0673    │ OSS 上传/下载             │  正常                    │
0674    ├───────────────────────────┼────────────────────────────┤
0675    │ prepare.sh（npm install） │  成功                    │
0676    ├───────────────────────────┼────────────────────────────┤
0677    │ dev.sh（npx serve :9000） │  成功                    │
0678    ├───────────────────────────┼────────────────────────────┤
0679    │ HTTP 200 验证             │  返回完整 HTML           │
0680    └───────────────────────────┴────────────────────────────┘
0681    整条链路 prompt → Claude → OSS → 脚本执行 → HTTP服务 验证完毕。
0682  
0683    端口分配：
0684    ┌────────────────────────────┬──────┬────────────────────────────┐
0685    │            用途             │ 端口 │            备注
0686    ├────────────────────────────┼──────┼────────────────────────────┤
0687    │ FastAPI（uvicorn app:app）  │ 9000 │ 正常启动，不变
0688    ├────────────────────────────┼──────┼────────────────────────────┤
0689    │ 本地测试生成项目            │ 8080 │ 脚本自动 patch，测完还原
0690    ├────────────────────────────┼──────┼────────────────────────────┤
0691    │ FC 容器里生成项目           │ 9000 │ 真实环境不 patch，保持原样
0692    └────────────────────────────┴──────┴────────────────────────────┘
0693  
</code></pre>

<a id="log-2025-03-25"></a>
### 2025-03-25

Source lines: `694-964`

<pre class="tech-log-source"><code>
0694  # 2025-03-25
0695  
0696  ## 知识学习
0697  
0698  #### 更全面的Coding agent
0699  
0700                  Workshop UI
0701                       │
0702                       ▼
0703              FastAPI Agent Orchestrator
0704                       │
0705          ┌────────────┼────────────┐
0706          ▼            ▼            ▼
0707       Planner       Coder       Debugger
0708          │            │            │
0709          ▼            ▼            ▼
0710       spec.md      code tree      patch
0711          │            │            │
0712          └──────► OSS Storage ◄───┘
0713                        │
0714                        ▼
0715                  FC Container
0716                        │
0717                        ▼
0718                  Dev Server
0719                        │
0720                        ▼
0721                     iframe
0722  
0723  ## 实践
0724  
0725  Multi-Agent的使用！震撼！
0726  
0727  #### OpenAI Codex, WSL2 CLI 模式运行
0728  
0729  Claude的API实在不稳定，50%时间403/503 error，换用Codex分组：
0730  
0731  VS Code的json配置openai codex默认不读取，所以需配置文件：
0732  
0733  我使用终端模式在WSL2，配置两个文件后成功运行gpt 5.4 model（默认的gpt 5 拥挤，不行）：
0734  
0735  **GNU nano 7.2    /home/ryan/.codex/auth.json**
0736  ```
0737  {
0738    &quot;auth_mode&quot;: &quot;apikey&quot;,
0739    &quot;OPENAI_API_KEY&quot;: &quot;&lt;REDACTED&gt;&quot;
0740  }
0741  ```
0742  
0743  **GNU nano 7.2    /home/ryan/.config/openai/config.toml**
0744  ```
0745  disable_response_storage = true
0746  model = &quot;gpt-5-codex&quot;
0747  model_provider = &quot;custom&quot;
0748  model_reasoning_effort = &quot;high&quot;
0749  windows_wsl_setup_acknowledged = true
0750  
0751  [model_providers.custom]
0752  base_url = &quot;https://hone.vvvv.ee/v1&quot;
0753  name = &quot;custom&quot;
0754  requires_openai_auth = true
0755  wire_api = &quot;responses&quot;
0756  
0757  [notice]
0758  hide_full_access_warning = true
0759  ```
0760  
0761  #### 优化LLM-CLI
0762  
0763  整个调用流程已换成阿里千问百炼
0764  
0765  #### 沙箱
0766  
0767  容器实例已经被创建并注册成功，现在要让容器运行起来
0768  核心思想：AI 不直接运行代码，而是在 sandbox container 里运行。
0769  
0770  常规的AI Coding 沙箱架构：
0771  User
0772    │
0773    ▼
0774  Workshop UI (Web IDE)
0775    │
0776    ▼
0777  Agent Service
0778    │
0779    ▼
0780  Task Queue
0781    │
0782    ▼
0783  Sandbox Manager
0784    │
0785    ▼
0786  Container Runtime
0787    │
0788    ▼
0789  Dev Server
0790    │
0791    ▼
0792  Preview Router
0793    │
0794    ▼
0795  Preview URL
0796  
0797  流程：
0798  create container
0799        ↓
0800  git clone / oss pull
0801        ↓
0802  npm install
0803        ↓
0804  start dev server
0805        ↓
0806  expose preview url
0807  
0808  Response body
0809  Download
0810  {
0811    &quot;project_ids&quot;: [
0812      &quot;proj-1774117999499&quot;,
0813      &quot;proj-1774118618839&quot;,
0814      &quot;proj-1774118736018&quot;,
0815      &quot;proj-1774118993314&quot;,
0816      &quot;proj-1774119281456&quot;,
0817      &quot;proj-1774119530520&quot;,
0818      &quot;proj-1774261757601&quot;,
0819      &quot;proj-1774334030907&quot;,
0820      &quot;proj-1774336370281&quot;,
0821      &quot;proj-1774345523559&quot;,
0822      &quot;proj-1774365171381&quot;,
0823      &quot;proj-1774365451436&quot;,
0824      &quot;proj-1774365898657&quot;,
0825      &quot;proj-1774366108059&quot;,
0826      &quot;proj-1774366895437&quot;,
0827      &quot;proj-1774367246631&quot;,
0828      &quot;proj-1774402506350&quot;,
0829      &quot;proj-1774403324560&quot;,
0830      &quot;proj-1774424651687&quot;,
0831      &quot;string&quot;
0832    ]
0833  }
0834  
0835  已经添加排查各个项目信息的接口：**GET /projects/summary**
0836  **接口返回：**
0837  ```
0838  {
0839    &quot;projects&quot;: [
0840      {
0841        &quot;project_id&quot;: &quot;proj-1774117999499&quot;,
0842        &quot;manifest_exists&quot;: true,
0843        &quot;template&quot;: &quot;base-node18&quot;,
0844        &quot;created_at&quot;: &quot;2026-03-21T18:33:20Z&quot;,
0845        &quot;preview_url&quot;: &quot;http://snake.fortuneai.cc/projects/proj-1774117999499/index.html&quot;,
0846        &quot;file_count&quot;: 12,
0847        &quot;has_fc&quot;: false,
0848        &quot;fc_status&quot;: &quot;NotFound&quot;,
0849        &quot;fc_preview_url&quot;: null,
0850        &quot;manifest_error&quot;: null,
0851        &quot;fc_error&quot;: null
0852      },
0853  ```
0854  排查之后，已经逐一删除现存的FC
0855  
0856  现在，添加删除某项目的功能
0857  
0858  已经全部删除！现在有很多新接口，皆可使用：
0859  
0860  **目前的 FastAPI 接口：**
0861  ```
0862  
0863  POST
0864  /generate
0865  Generate With Openai
0866  
0867  POST
0868  /upload
0869  Upload
0870  
0871  POST
0872  /save-project
0873  Save Project
0874  
0875  GET
0876  /projects
0877  Get Projects
0878  
0879  GET
0880  /projects/summary
0881  Get Projects Summary
0882  
0883  GET
0884  /projects/{project_id}
0885  Get Project
0886  
0887  DELETE
0888  /projects/{project_id}
0889  Delete Project
0890  
0891  GET
0892  /projects/{project_id}/tree
0893  Get Project Tree
0894  
0895  GET
0896  /projects/{project_id}/file
0897  Get Project File
0898  
0899  ***container***
0900  
0901  POST
0902  /containers/{project_id}/start
0903  Start Container
0904  
0905  GET
0906  /containers/{project_id}/status
0907  Get Container Status
0908  
0909  DELETE
0910  /containers/{project_id}
0911  Delete Container
0912  ```
0913  
0914  #### 实现较复杂的 Coding Agent（方案2）
0915  
0916  **Coding Agent方案2：** ***/generate/agent***
0917  
0918  把现在的“一次 LLM 调用吐全量文件”升级成
0919  “多轮：生成 -&gt; 本地验证 -&gt; 读错误 -&gt; 修复 -&gt; 再验证”
0920  的闭环，让产物在上传 OSS/跑 FC 前就尽量稳定
0921  
0922  架构规划：
0923  把它从“一个接口里把所有事做完”拆成三层，并且用“可组合的工作流 + 可插拔的工具”承载未来功能增长。
0924  
0925    1) 分层与边界（关键）
0926    - API 层（routers/*）：只负责参数校验、创建任务、返回 run_id/结果，不写业务逻辑。
0927    - Agent 编排层（agent/*）：状态机 + 工作流引擎。负责多轮循环、停止条件、重试、取消、超时、产物汇总。
0928    - 工具与基础设施层（tools/* + services/*）：把所有副作用封装成工具接口（LLM、文件系统、命令执行、HTTP 探测、OSS、FC），Agent 只能通过工具做
0929      事。
0930  
0931    2) 推荐目录结构（可扩展）
0932    - Reference-framework/routers/agent.py：/generate/agent、/runs/{run_id}、/runs/{run_id}/events、/runs/{run_id}/cancel
0933    - Reference-framework/agent/core.py：Run 状态机、Step 约定、上下文（Context）
0934    - Reference-framework/agent/workflows/*.py：工作流定义（生成-only、生成+验证、生成+上传OSS、生成+上传+部署FC…）
0935    - Reference-framework/agent/steps/*.py：原子步骤（generate_draft、normalize、write_workspace、validate、llm_patch、package、upload_oss、
0936      deploy_fc…）
0937    - Reference-framework/agent/tools/*.py：工具接口与实现适配（llm_tool、exec_tool、fs_tool、oss_tool、fc_tool、http_probe_tool）
0938    - Reference-framework/agent/store/*.py：RunStore/EventStore/ArtifactStore（先本地文件或内存，后续可换 Redis/DB，不影响上层）
0939  
0940    3) 核心数据模型（未来加功能不乱）
0941    - Run：run_id、status(queued/running/succeeded/failed/canceled)、workflow_name、config、created_at、updated_at
0942    - RunEvent：按时间追加（step_start/step_end/tool_call/tool_result/log/error），用于调试和前端展示
0943    - Artifact：生成文件集、workspace 路径、打包产物、OSS key、FC 预览 URL 等（都挂在 run 上）
0944  
0945    4) 工作流设计（把“越来越多功能”变成组合）
0946    - 每个 workflow 只是一个 step 列表 + 分支条件，例如：
0947        - generate_only: LLM生成 -&gt; 规范化 -&gt; 返回文件
0948        - generate_validate: LLM生成 -&gt; 规范化 -&gt; 落盘 -&gt; prepare/build/start -&gt; 健康检查 -&gt; (失败则 patch 循环N次) -&gt; 返回文件+报告
0949        - generate_save_oss: 在通过验证后追加 upload_oss -&gt; 写manifest
0950        - generate_save_deploy_fc: 再追加 deploy_fc -&gt; 探测预览URL
0951    - 每个 step 输入/输出都只读写 Context，不直接互相调用；这样加新能力只要“加 step + 改 workflow 配置”，不会把代码越堆越硬。
0952  
0953    5) LLM 交互规范（降低一次性大生成的 bug）
0954    - 修复轮：强制返回“补丁格式”，只允许改动少量文件（例如 {patches:[{path,content,op}]}），避免模型每轮重写全仓导致漂移。
0955    - 观察输入：只喂“失败日志摘要 + 相关文件（有限数量/有限字节）+ 明确目标”，并设置 max_iters、timeout、stop_condition。
0956  
0957    6) 执行与安全（必须提前规划）
0958    - exec_tool 统一加：工作目录隔离、命令白名单/模板、CPU/时间/输出大小上限、端口占用检查、进程回收。
0959    - fs_tool 统一加：路径穿越防护、只允许写入 run 的 workspace。
0960    - 日志与密钥脱敏：event 里禁止落 API_KEY/AK/SK 原文。
0961  
0962    这个结构最小闭环：/generate/agent + RunStore(EventStore) + generate_validate 工作流（多轮 patch 修
0963    复），其余 workflow（上传 OSS、部署 FC）用同一套 step 机制往后叠加
0964  
</code></pre>

<a id="log-2026-03-26"></a>
### 2026-03-26

Source lines: `965-1092`

<pre class="tech-log-source"><code>
0965  # 2026-03-26
0966  
0967  ## 实践
0968  
0969  #### Coding Agent的较复杂实现与调用
0970  
0971  **Coding Agent方案2：** ***/generate/agent***
0972  
0973  方案2**函数调用流程图：**
0974  ```
0975    POST /generate/agent
0976    -&gt; routers/agent.generate_with_agent()
0977    -&gt; RunStore.create_run()
0978    -&gt; run_generate_validate()
0979    -&gt; build_enhanced_prompt()
0980    -&gt; OpenAI-compatible /chat/completions 生成 files[]
0981    -&gt; normalize_generated_files()
0982    -&gt; materialize_files() 写入 run workspace
0983    -&gt; _validate_workspace()
0984       -&gt; prepare.sh
0985       -&gt; build.sh
0986       -&gt; start.sh / dev.sh
0987       -&gt; HTTP probe
0988    -&gt; 如果失败且 auto_fix=true
0989       -&gt; pick_context_files()
0990       -&gt; OpenAI-compatible /chat/completions 生成 patches[]
0991       -&gt; apply_patches()
0992       -&gt; normalize_generated_files()
0993       -&gt; materialize_files()
0994       -&gt; 再次验证
0995    -&gt; RunStore.set_result() / set_status()
0996    -&gt; GET /runs/{run_id} 轮询结果
0997  ```
0998  
0999  方案2，根据大型agent框架构建的**数据流向：**
1000  ```
1001    1. 请求进入 generate_with_agent()。它把 prompt/template/model/max_iters/... 组装进 config，创建一个 run_id。见 Reference-framework/routers/
1002       agent.py:61、Reference-framework/routers/agent.py:78。
1003    2. RunStore.create_run() 会在本地创建目录：
1004       /tmp/reference-agent-runs/{run_id}/
1005       里面至少有：
1006    - run.json
1007    - events.jsonl
1008    - workspace/
1009      见 Reference-framework/agent/store.py:57、Reference-framework/agent/store.py:45。
1010    3. 如果 wait=false，路由只是 asyncio.create_task(coro) 把 workflow 丢到后台；如果 wait=true，当前请求会一直等到 workflow 结束。见 Reference-
1011       framework/routers/agent.py:95。
1012    4. workflow 入口是 run_generate_validate()。它先把 run 状态改成 running，然后调用 build_enhanced_prompt() 拼模板约束，再调用
1013       generate_project_with_openai()。见 Reference-framework/agent/workflows/generate_validate.py:230、Reference-framework/agent/workflows/
1014       generate_validate.py:252、Reference-framework/services/generation_rules.py:481。
1015    5. LLM 层当前不是 Responses API，也不是 Codex CLI 配置链路，而是后端自己读取 .env，直接请求 OPENAI_BASE_URL/chat/completions，并要求返回严格
1016       JSON schema。见 Reference-framework/services/openai_service.py:18、Reference-framework/services/openai_service.py:162、Reference-
1017       framework/services/openai_service.py:226。
1018    6. 生成结果被规范成 List[SaveFileItem]，也就是最核心的内部文件格式：
1019    - path
1020    - content
1021      见 Reference-framework/models.py:140。
1022    7. 生成完以后，会执行 normalize_generated_files()。这一步会强改模板相关内容，比如 Node18 依赖版本、补齐 scripts/*.sh、补 vite.config.js、修
1023       index.html 位置。见 Reference-framework/services/generation_rules.py:538。
1024    8. 然后 materialize_files() 把内存里的 files[] 写进 workspace/。注意这里是“覆盖同名文件”，不是“同步整个目录”。旧文件不会被删。见 Reference-
1025       framework/agent/tools/fs_tool.py:34。
1026    9. 如果 run_validation=false，workflow 到这里就结束，直接把 files[] 写入 run.result。见 Reference-framework/agent/workflows/
1027       generate_validate.py:264。
1028    10. 如果开启验证，会进入 _validate_workspace()：
1029    - 找一个空闲本地端口
1030    - 注入环境变量 WORKSPACE/HOST/PORT
1031    - 顺序跑 prepare.sh、build.sh
1032    - 再启动 start.sh，没有就退回 dev.sh
1033    - 用 HTTP 探测本地地址
1034      见 Reference-framework/agent/workflows/generate_validate.py:62、Reference-framework/agent/workflows/generate_validate.py:75、Reference-
1035      framework/agent/workflows/generate_validate.py:143。
1036    11. 验证时实际执行 shell 的地方在 exec_tool.py：
1037    - run_bash_script() 跑 prepare/build
1038    - start_bash_script() 起长跑进程
1039    - wait_http_ready() 轮询页面
1040    - 成功后马上 terminate_process()
1041      见 Reference-framework/agent/tools/exec_tool.py:37、Reference-framework/agent/tools/exec_tool.py:98、Reference-framework/agent/tools/
1042      exec_tool.py:191。
1043    12. 如果验证失败且 auto_fix=true，才会进入 patch 回路：
1044    - pick_context_files() 选少量关键文件
1045    - _build_fix_prompt() 拼失败日志和上下文
1046    - generate_project_patches_with_openai() 让模型返回 patches[]
1047    - apply_patches() 应用补丁
1048    - 再次 normalize_generated_files()
1049    - 再次 materialize_files()
1050    - 再验证
1051      见 Reference-framework/agent/workflows/generate_validate.py:323、Reference-framework/agent/tools/fs_tool.py:80、Reference-framework/
1052      services/openai_service.py:254。
1053    13. 当前 patch 的语义只有“按 path 覆盖/新增”，没有 delete，没有 rename，也没有“按最终 files 全量同步 workspace”。这正是你说要先修的 4。见
1054       Reference-framework/agent/tools/fs_tool.py:60。
1055    14. 成功或失败后，workflow 会把结果写回 run.json。result 里会直接带完整文件内容和 validation report。见 Reference-framework/agent/workflows/
1056       generate_validate.py:297、Reference-framework/agent/store.py:123。
1057    run 的状态和文件
1058    当前 run 的生命周期基本是：
1059    - queued
1060    - running
1061    - succeeded / failed / canceled
1062    状态变化和关键动作都会追加到 events.jsonl。见 Reference-framework/agent/store.py:119。
1063  ```
1064  
1065  现在简化Agent流程：
1066  
1067  **Coding Agent 方案3：** ***/runs***
1068  
1069  舍弃了大型agent的流程（）简化为简单的workflow。
1070  **完整链路成功：**
1071    - 生成成功
1072    - 本机 prepare/build/start 全部成功
1073    - 发布成功
1074    - 已创建 OSS 项目和 FC
1075  关键结果是：
1076    - run_id: run-1774496744666-42124bb9
1077    - project_id: proj-1774496798261
1078    - 最终状态：succeeded
1079  
1080  简化成功debug成功。
1081  
1082  ### Docker打包成功
1083  
1084  (base) ryan@ENVYKatana:/mnt/c/Desktop/generate/Reference-framework$ curl --noproxy &#x27;*&#x27; -i http://127.0.0.1:9000/healthz
1085  HTTP/1.1 200 OK
1086  date: Thu, 26 Mar 2026 07:33:08 GMT
1087  server: uvicorn
1088  content-length: 166
1089  content-type: application/json
1090  
1091  {&quot;ok&quot;:true,&quot;service&quot;:&quot;reference-framework&quot;,&quot;runs_dir&quot;:&quot;/data/reference-agent-runs&quot;,&quot;checks&quot;:{&quot;runs_dir_writable&quot;:true,&quot;openai_configured&quot;:true,&quot;oss_configured&quot;:true}}(base)
1092  
</code></pre>

<a id="log-2026-03-27"></a>
### 2026-03-27

Source lines: `1093-1143`

<pre class="tech-log-source"><code>
1093  # 2026-03-27
1094  
1095  ## 知识学习
1096  
1097  ### 探讨Coding Agent架构
1098  
1099  最终我们决定先完成强大的agent，再通过微调workflow的结构，格式化输出内容，以对接OSS/FC
1100  
1101  而不是一开始根据OSS/FC的结构化需求设计Agent
1102  
1103  逻辑关系是本末倒置的
1104  
1105  ### TypeScript
1106  
1107  [TypeScript教程](https://www.runoob.com/typescript/ts-tutorial.html)
1108  
1109  非常多的开源项目用 TS 写成！
1110  
1111  ## 实践
1112  
1113  ### 设计能够格式化输出的Coding Agent
1114  
1115  按现在这个目标，不需要把主流程改成“先输出 {&quot;files&quot;:[...]} 再落盘”，具体而言：
1116  
1117  现有 coding agent 的主链路：
1118  1. 用户输入进入 SessionPrompt.prompt()
1119  2. 主 agent 开始推理
1120  3. agent 在过程中调用 write / edit / apply_patch
1121  4. 文件直接写到当前工作目录，比如你指定的 TEST/
1122  
1123  所以要加的，其实只是前置的一层：
1124  1. 检测是否是“生成项目”意图
1125  2. 如果不是，原样走现有聊天/分析流程
1126  3. 如果是，先把简单 prompt 例如“生成贪吃蛇游戏”增强成一条完整、规范、工程化的 prompt
1127  4. 然后把这条增强后的 prompt 继续交给现有 coding agent
1128  5. 后面的文件创建仍然由现有 agent 正常完成
1129  
1130  落实到改动操作：
1131  1. IntentDetector
1132     输入简单 prompt，比如“生成贪吃蛇游戏”。
1133     输出结构化判断：intent=generate_project | normal_chat，以及 template=base-node18 | base-python39。
1134  2. ProjectPromptEnhancer
1135     只在 intent=generate_project 时运行。
1136     用专门的 enhancer agent 深度理解、补全约束、规划输出。
1137     输出结构化结果建议是：
1138     template
1139     enhancedPrompt
1140     constraints
1141  3. 把 enhancedPrompt 覆盖原始 text part，再把这条增强后的 user message 交给现有主生成链路。
1142     后面的文件生成仍然由 write/edit/apply_patch 完成，直接落到 TEST/
1143  
</code></pre>

<a id="log-2026-03-28"></a>
### 2026-03-28

Source lines: `1144-1314`

<pre class="tech-log-source"><code>
1144  # 2026-03-28
1145  
1146  ## 知识学习
1147  
1148  ### Opencode
1149  
1150  Opencode 内部调用逻辑
1151  
1152  ## 实践
1153  
1154  ### Coding Agent
1155  
1156  我通过修改opencode的工作流，实现了我们项目所需的Coding Agent!
1157  
1158  ### 封装 Coding Agent 到 FastAPI
1159  
1160  我找到更稳的落点了：直接给 opencode 加一个正式 CLI 子命令，比如 generate-project --prompt ...
1161  这样 FastAPI 只需要调用这个命令拿 JSON，完全绕开“内部再起一个 HTTP 服务”的不稳定链路
1162  
1163  我已经封装成功！
1164  现在能稳定输出.json格式的文件。
1165  
1166  ### 删改opencode大项目结构
1167  
1168  这很像我一年前删除Colias项目文件的过程......
1169  已完成并存档。这是目前的baseline版本。
1170  
1171  ### 流式输出架构
1172  
1173  我的流式推送接口应能：
1174  1.我希望前端能展示出当前项目的文件结构文件树、已有的文件。
1175  2.我希望不仅能够展示工作状态，还要有一行或者几行，实时显示LLM正在生成的代码。
1176  3.我希望用“思考状态”展示agent的工作状态。
1177  
1178  **推荐接口：**
1179  ```
1180  
1181  - POST /generate/jobs
1182    提交生成任务，返回 job_id
1183  - GET /generate/jobs/{job_id}/stream
1184    SSE 流式输出
1185  - GET /generate/jobs/{job_id}/result
1186    获取最终 { &quot;files&quot;: [...] }
1187  - GET /generate/jobs/{job_id}
1188    获取任务当前快照
1189  - DELETE /generate/jobs/{job_id}
1190    可选，取消任务
1191  ```
1192  
1193  为什么这样设计：
1194  - 前端更容易接。POST 提交，GET 用 EventSource 收流。
1195  - 能断线重连。
1196  - 能同时拿“状态流”和“最终结果”。
1197  - 不破坏现有 /generate。
1198  
1199  **SSE 事件设计：**
1200  ```
1201  建议统一 JSON，事件名固定。
1202  - job.created
1203    {&quot;job_id&quot;:&quot;gen_xxx&quot;,&quot;status&quot;:&quot;queued&quot;}
1204  - thinking.status
1205    不传原始 CoT，只传安全摘要
1206    {
1207      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1208      &quot;phase&quot;:&quot;planning&quot;,
1209      &quot;label&quot;:&quot;正在规划项目结构&quot;,
1210      &quot;detail&quot;:&quot;分析需求，确定模板和最小文件集&quot;
1211    }
1212  - project.tree
1213    前端文件树用这个
1214    {
1215      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1216      &quot;paths&quot;:[&quot;package.json&quot;,&quot;scripts/start.sh&quot;,&quot;src/main.js&quot;]
1217    }
1218  - file.snapshot
1219    当前已有文件内容
1220    {
1221      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1222      &quot;path&quot;:&quot;src/main.js&quot;,
1223      &quot;content&quot;:&quot;...&quot;
1224    }
1225  - file.delta
1226    可选，给前端展示“刚写出来的几行代码”
1227    {
1228      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1229      &quot;path&quot;:&quot;src/main.js&quot;,
1230      &quot;append&quot;:&quot;const app = ...\n&quot;
1231    }
1232  - preview.code
1233    专门给你第二个需求
1234    {
1235      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1236      &quot;path&quot;:&quot;src/main.js&quot;,
1237      &quot;lines&quot;:[&quot;const app = ...&quot;,&quot;app.listen(...)&quot;]
1238    }
1239  - session.status
1240    忙闲状态
1241    {
1242      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1243      &quot;status&quot;:{&quot;type&quot;:&quot;busy&quot;}
1244    }
1245  - job.completed
1246    {
1247      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1248      &quot;file_count&quot;:9,
1249      &quot;result_url&quot;:&quot;/generate/jobs/gen_xxx/result&quot;
1250    }
1251  - job.failed
1252    {
1253      &quot;job_id&quot;:&quot;gen_xxx&quot;,
1254      &quot;error&quot;:&quot;...&quot;
1255    }
1256  ```
1257  
1258  **怎么满足 3 个需求：**
1259  ```
1260  
1261  - 文件树、已有文件：
1262    用 project.tree + file.snapshot
1263  - 实时显示 LLM 正在生成的代码：
1264    用 file.delta 或 preview.code
1265    这个不要依赖模型“口头输出代码”，而要监听真实文件写入
1266  - 用“思考状态”展示 agent 状态：
1267    用 thinking.status内容来自阶段摘要，不直接暴露模型原始推理后端实现建议基于现有 packages/opencode/src/generate-api.ts 和 packages/opencode/src/server/generate-projectts改：
1268  - Python FastAPI 负责：
1269      - 创建 job
1270      - 保存 job 状态
1271      - 返回 SSE StreamingResponse
1272  - Bun 生成器负责：
1273      - 输出 JSONL 事件到 stdout
1274      - 最后一条输出最终 files
1275  - 生成器内部增加 3 类 hook：
1276      - 阶段变化 hook：发 thinking.status
1277      - 文件变化 hook：发 project.tree、file.snapshot、preview.code
1278      - 结束 hook：发 job.completed
1279  ```
1280  
1281  最重要的一点：thinking.status 不建议传模型原始 reasoning。
1282  建议只传这种：
1283  - 分析需求中
1284  - 规划项目结构中
1285  - 正在编写 package.json
1286  - 正在修复启动脚本
1287  - 正在校验最终结果
1288  这样前端效果够好，也安全。
1289  
1290  已实现
1291  
1292    改动在 app.py、packages/opencode/src/generate-api.ts、packages/opencode/src/server/generate-project.ts、packages/opencode/
1293    test/generate-api.test.ts。
1294  
1295    现在接口是：
1296  
1297    - POST /generate：保留原来的同步返回 { files: [...] }
1298    - POST /generate/jobs：创建流式生成任务
1299    - GET /generate/jobs/{job_id}：拿当前快照，里面有文件树、已有文件、预览代码、thinking 状态
1300    - GET /generate/jobs/{job_id}/stream：SSE 流
1301    - GET /generate/jobs/{job_id}/result：任务完成后拿最终 { files: [...] }
1302  
1303    流式行为现在支持：
1304  
1305    - 文件树：project.tree
1306    - 文件内容快照：file.snapshot
1307    - 代码预览：preview.code
1308    - 安全的工作状态：thinking.status
1309    - 任务状态：job.status
1310    - 最终结果：job.result
1311  
1312    另外，Bun 内部生成入口加了 --stream-jsonl，FastAPI 会把它解析成 job 状态并转成 SSE。同步 /generate 不受影响。reasoning 原文没
1313    有直接暴露给前端，只保留了状态级事件。
1314  
</code></pre>

<a id="log-2026-03-29"></a>
### 2026-03-29

Source lines: `1315-1318`

<pre class="tech-log-source"><code>
1315  # 2026-03-29
1316  
1317  ## 毕设毕设！
1318  
</code></pre>

<a id="log-2026-03-30"></a>
### 2026-03-30

Source lines: `1319-1420`

<pre class="tech-log-source"><code>
1319  # 2026-03-30
1320  
1321  ## 知识学习
1322  
1323  #### 对现有工程的思考：我们的目的是什么？
1324  
1325  ***真正缺的，不是“再造一个能连续对话的 /generate”，而是把 /generate 里更强的那部分能力搬进 web 的标准 session 路径里***
1326  
1327  #### 如果是workshop，那重心在于强大的coding agent、在线运行。但“生成自己的openclaw”这样级别的要求难以实现
1328  “贪吃蛇”是远远不够的。目前，coding agent已经足够强大，但在云端运行“用户生成的程序”仍需细致对接
1329  
1330  #### 如果是能解决具体需求的agent，那重心在于SKILL.md, 理解需求、细致的构造pipeline，通过多个skill真正去解决问题
1331  
1332  #### TODO List
1333  
1334  - find skills的SKILL.md, 进一步的，一堆工具skills，如何调用
1335  
1336  - 需求分析的SKILL.md
1337  
1338  - 不同应用场景，写paper，写report，上网
1339  
1340  - AI降重：带上自己的思想;  降重 SKILL.md
1341  
1342  - 让claude触手可得
1343  
1344  ## 实践
1345  
1346  #### Coding Agent网页版在线运行
1347  
1348  在现有网页应用上加OSS/FC在线运行：
1349  
1350  #### 第一阶段
1351  ```
1352    - 从 packages/opencode/src/server/generate-project.ts 抽出“项目 contract 校验”模块。
1353    - 保留现有规则：模板识别、必需文件、scripts/*.sh 约束、Vite/Vue 版本约束、Python/FastAPI约束。
1354    - 目标文件建议新建为 packages/opencode/src/server/project-contract.ts 或相近位置。
1355    - /generate 和 web session 后续都复用这一个模块。
1356  ```
1357  
1358  #### 第二阶段
1359  ```
1360    - 在 web 端加“在线构建并在线运行模式”开关。
1361    - 入口优先放在 packages/app/src/components/prompt-input/submit.ts 所在提交链路附近。
1362    - 这一步只做“把模式标记传到后端 prompt 流程”，不要先做部署。
1363  ```
1364  
1365  #### 第三阶段
1366  ```
1367    - 扩展 packages/opencode/src/plugin/prompt-enhancer.ts，让它在该模式下启用更强 project contract。
1368    - 普通聊天不受影响。
1369    - 项目生成首条消息启用：固定模板规则、输出目录规则、运行脚本规则、可部署规则。
1370  ```
1371  
1372  #### 第四阶段
1373  ```
1374    - 在标准 session 流里接入“校验失败自动修复”。
1375    - 不再走临时 /generate session。
1376    - 在同一 session 内，首轮生成完成后校验；失败时自动追加 repair prompt；成功则结束。
1377    - 这样 web 的持续对话、流式状态、消息历史都天然保留。
1378  ```
1379  
1380  #### 第五阶段
1381  ```
1382    - 只约束部署必需接口，不先绑定具体云厂商实现细节。
1383    - 先稳定：
1384      scripts/prepare.sh
1385      scripts/build.sh
1386      scripts/start.sh
1387      HOST
1388      PORT
1389      WORKSPACE
1390  ```
1391  
1392  保留 /generate: 作为外部 API、作为 contract 回归测试入口、作为未来批量生成入口
1393  
1394  最值得先做的是第 1 步和第 2 步。做完这两步，主路径就从“独立 /generate”转成“web session + 强约束项目模式”。
1395  下一步直接改两处：packages/opencode/src/server/generate-project.ts、packages/opencode/src/plugin/、prompt-enhancer.ts，然后再接 web 的模式开关。
1396  
1397  现在 web 版已经接上这条链路了：
1398  新会话输入框里新增了一个持久化的 “Run Online / 在线构建运行” 开关
1399  打开后，首条普通 prompt 会带上在线运行 mode marker；后端prompt-enhancer会据此启用之前加的“在线构建并运行”约束
1400  相关改动在 packages/app/src/components/prompt-input.tsx
1401  packages/app/src/components/prompt-input/submit.ts
1402  packages/opencode/src/plugin/prompt-enhancer.ts
1403  以及新的共享模块 packages/util/src/project-mode.ts
1404  
1405  ## 知识学习
1406  
1407  #### Workshop数据流动、架构细节分析讨论
1408  
1409  #### Seminar: World Model
1410  
1411  ## 实践
1412  
1413  #### Debug Web应用
1414  
1415  已添加“构建项目”模式，并在前端展示现已生成的文件
1416  
1417  带前端版本的完整pipeline已跑通！
1418  
1419  现在，对接CUHKSZ的第二前端。
1420  
</code></pre>

<a id="log-2026-04-01"></a>
### 2026-04-01

Source lines: `1421-1440`

<pre class="tech-log-source"><code>
1421  # 2026-04-01
1422  
1423  ## 知识学习
1424  
1425  #### Claude Code 框架
1426  
1427  Claude Code 源码泄露...
1428  
1429  学一波：[Bilibili: Claude Code源码泄露！首发解读51万行代码！](https://www.bilibili.com/video/BV11zXCBFEMo/?spm_id_from=333.1387.top_right_bar_window_default_collection.content.click)
1430  
1431  ## 实践
1432  
1433  #### [Workshop 架构重构：MVP 版本](https://github.com/Ryannnice/Agent-Do)
1434  
1435  我们非常简洁、高效地实现了workshop。
1436  
1437  效果很好，并且摒弃了opencode的庞大源代码植入。
1438  
1439  优化前端，现在反应简洁迅速美观。
1440  
</code></pre>

<a id="log-2026-04-02"></a>
### 2026-04-02

Source lines: `1441-1485`

<pre class="tech-log-source"><code>
1441  # 2026-04-02
1442  
1443  ## 知识学习
1444  
1445  #### Docker
1446  
1447  [Bilibili Docker](https://www.bilibili.com/video/BV1THKyzBER6/?spm_id_from=333.1387.favlist.content.click&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1448  
1449  #### 关于项目未来的讨论
1450  
1451  教育平台是核心竞争力
1452  
1453  下一阶段定位：用户每天早晨五分钟了解AI圈大事，甚至上手实践，学习一二。
1454  
1455  ## 实践
1456  
1457  #### Workshop 架构重构：MVP 版本
1458  
1459  Debug, 增添流式输出功能
1460  
1461  #### Claude Code 宠物系统修复
1462  
1463  已经成功部署运行[“开源”的Claude Code](https://github.com/Ryannnice/claude-code)!
1464  
1465  修复了桌面宠物 /buddy 功能！
1466  
1467  #### Git Branch
1468  
1469  常见 type（非常重要）
1470  ```
1471  feature	  新功能	  feature/payment-api
1472  fix   	  修复 bug  fix/order-null-pointer
1473  hotfix  	紧急修复	hotfix/login-crash
1474  refactor	代码重构	refactor/cache-module
1475  docs	    文档修改	docs/api-guide
1476  test	    测试代码	test/user-service
1477  chore	    杂项修改	chore/dependency-update
1478  ```
1479  
1480  #### Workshop
1481  
1482  尝试构建多项目运行时，并展示：
1483  
1484  我们发现似乎并不需要FC或者公网URL。
1485  
</code></pre>

<a id="log-2026-04-03"></a>
### 2026-04-03

Source lines: `1486-1540`

<pre class="tech-log-source"><code>
1486  # 2026-04-03
1487  
1488  ## 知识学习
1489  
1490  #### git / docker
1491  
1492  - 用 `git pull` 和 `docker compose up --build -d` 熟悉基本更新与重建流程。
1493  
1494  这一天原本保留了整段学习对话，这里压缩为日志摘要：
1495  
1496  - 学习对象是 `assignment1-basics`，目标是把 Transformer 训练链路真正串起来理解。
1497  - 当天抓住的主线是：
1498    `文本 -&gt; tokenizer -&gt; token id -&gt; embedding -&gt; Transformer -&gt; logits -&gt; cross entropy -&gt; 反向传播 -&gt; 参数更新`
1499  - 核心代码入口包括：
1500    `cs336_basics/tokenizer.py`、
1501    `cs336_basics/model/modules.py`、
1502    `cs336_basics/model/transformer.py`、
1503    `cs336_basics/trainer/data_loading.py`、
1504    `cs336_basics/trainer/utils.py`、
1505    `cs336_basics/train.py`
1506  - 最重要的认识有 6 点：
1507    1. 语言模型训练的本质是“给定前文，预测下一个 token”。
1508    2. `inputs` 是当前 token 序列，`targets` 是右移一位后的监督信号。
1509    3. Transformer 本体负责把上下文表示加工成下一个 token 的打分 `logits`。
1510    4. block 的核心结构是 Pre-Norm + Attention + FFN + Residual。
1511    5. `Linear`、`Embedding`、`RMSNorm`、`SwiGLU`、self-attention、RoPE 是后续必须啃透的基础模块。
1512    6. 训练闭环可以概括为：采样 -&gt; 前向 -&gt; 计算 loss -&gt; backward -&gt; 更新参数。
1513  - 当天的直接产出：
1514    - 给 `trainer/data_loading.py`
1515    - 给 `trainer/utils.py`
1516      增加了逐行中文注释，作为第一部分学习基线。
1517  - 下一步计划：
1518    继续理解 `Embedding`、`Linear`、attention 与 `transformer.py` 的整体拼装。
1519  
1520  ## 实践
1521  
1522  #### Docker构建Claude Code
1523  
1524  遇到构建docker镜像时候地址错误问题：
1525  
1526  - Claude 看起来执行了
1527  - 但改动写进了错误挂载目标
1528  - 当前 session 的真实 workspace/ 还是空的
1529  - 然后 runtime/start 检测不到 index.html / package.json，就返回 400 当前 session 没有可在线运行的项目
1530  
1531  问题不是 HTTP 400 本身，而是 Agent-Do 之前把 Claude 子容器的 workspace 挂到了错误的宿主机路径。
1532  AGENT_DATA_HOST_ROOT 在 Backend/WorkShop/.env 里指向了旧机器上的 /root/internship-szdsjyjy/...，
1533  但这台机器真实路径是 /home/ryan/CUHKSZ/Education_Platform/Backend/Agent-Do/data。
1534  
1535  - 修正了 Agent-Do 容器内 Docker CLI 的集成，避免之前的 input/output error: &#x27;docker&#x27;
1536  - 修正了 Backend/WorkShop/.env 里的 AGENT_DATA_HOST_ROOT，并重启了 agent-do
1537  
1538  当前 qwen3-coder-next 这条模型链路有时会“看起来成功，实际上没写任何文件”。
1539  我准备从 WorkShop 侧加兜底：当第一轮生成后没有形成可预览项目时，自动发一轮更强约束的修复 prompt，而不是直接把 runtime/start 400 暴露给前端。
1540  
</code></pre>

<a id="log-2026-04-04"></a>
### 2026-04-04

Source lines: `1541-1550`

<pre class="tech-log-source"><code>
1541  # 2026-04-04
1542  
1543  ## 知识学习
1544  
1545  #### PageAttention
1546  [怎么加快大模型推理？10分钟学懂VLLM内部原理，KV Cache，PageAttention](https://www.bilibili.com/video/BV1kx4y1x7bu/?spm_id_from=333.1391.0.0&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1547  
1548  #### Flash Attention
1549  [Flash Attention 为什么那么快？原理讲解](https://www.bilibili.com/video/BV1UT421k7rA/?spm_id_from=333.1391.0.0&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1550  
</code></pre>

<a id="log-2026-04-05"></a>
### 2026-04-05

Source lines: `1551-1554`

<pre class="tech-log-source"><code>
1551  # 2026-04-05
1552  
1553  ## 毕设毕设！
1554  
</code></pre>

<a id="log-2026-04-06"></a>
### 2026-04-06

Source lines: `1555-1561`

<pre class="tech-log-source"><code>
1555  # 2026-04-06
1556  
1557  ## 拯救计划很好看
1558  我觉得可以和星际穿越媲美。
1559  太空的浪漫很纯粹。
1560  [Bilibili细节解析](https://www.bilibili.com/video/BV1oSQZBRE8j/?spm_id_from=333.337.search-card.all.click)
1561  
</code></pre>

<a id="log-2026-04-07"></a>
### 2026-04-07

Source lines: `1562-1621`

<pre class="tech-log-source"><code>
1562  # 2026-04-07
1563  
1564  ## 知识学习
1565  
1566  #### AI Station
1567  
1568  [AI Station 教程](https://xxl9u0uq9y2.feishu.cn/wiki/LVHvw3GCWiMlV4kjH25clngHnVf)
1569  
1570  #### LLM Router
1571  
1572  谕书的完整Pipeline
1573  
1574  #### Router 综述
1575  
1576  #### LLM 路由的概念设计空间
1577  本综述涵盖的范式（参见 1.3 节）为组织和理解文献提供了基础 。
1578  在实践中，现实世界的系统往往同时借鉴了不止一种范式 。
1579  为了补充基于范式的组织方式，路由方法还可以从更广泛的维度进行分类 ：
1580  
1581  #### 决策时机 (When)：指路由决策何时做出 。
1582  路由系统可以依赖生成前 (Pre-generation) 决策或生成后 (Post-generation) 决策，也可以采用多阶段过程 。
1583  生成前路由在产生任何输出前选择模型，完全依赖于输入查询的属性；而生成后路由则在产生初始响应后，根据输出质量或置信度信号做出决定 。
1584  
1585  #### 使用信息 (What)：路由机制使用的信号丰富程度各不相同 。最简单的方法仅基于查询本身，利用词法或语义特征来刻画请求 。
1586  更进阶的系统还会加入可用模型的元数据来指导选择，如成本、延迟或领域专长 。生成后方法则进一步引入响应级信号，如置信度得分、Token 概率或验证器输出 。
1587  
1588  #### 计算方式 (How)：路由决策的计算复杂度差异显著 。一端是简单的阈值规则或基于成本的启发式方法，无需训练即可直接应用 ；
1589  另一端是基于历史表现数据训练的监督分类器，用于预测哪个模型最适合处理给定查询 。
1590  更复杂的方法采用自适应策略，通过与环境的持续交互来更新路由行为 。
1591  
1592  #### 主流技术路线
1593  1. 难度感知路由 (Difficulty-aware Routing)
1594    这是最直观的路线，核心是**“看题下菜”** 。
1595    原理：在推理前评估查询的复杂度，将简单题分给小模型，难题分给大模型 。
1596    评估手段：包括启发式规则（如文本长度、词汇稀缺度）、训练专门的分类器（如你计划使用的 0.5B 模型）或使用 “LLM 作为评判者” 。
1597    代表案例：BEST-Route（动态分配并选择采样策略）和 VLLM Semantic Router（识别是否需要开启昂贵的思维链推理） 。
1598  2. 人类偏好对齐路由 (Human Preference-aligned Routing)
1599    不看“对错”，看**“好坏”** 。
1600    原理：模拟人类的主观评价，预测大模型生成的答案是否会比小模型显著“更好” 。
1601    训练数据：利用 Chatbot Arena 等人类真实偏好数据或 LLM 自动生成的对比数据 。
1602    代表案例：RouteLLM（预测强模型是否会胜出）和 Arch-Router（允许用户自定义不同领域的路由偏好） 。
1603  3. 基于聚类的路由 (Clustering-based Routing)
1604    核心是**“找规律”** 。
1605    原理：利用无监督学习（如 K-means）将语义相似的查询聚类，并为每个簇分配表现最好的模型 。
1606    优势：具有极强的扩展性，添加新模型时无需重新训练路由器，只需测试新模型在各个簇上的表现即可 。
1607    代表案例：UniRoute 和 Avengers-Pro 。
1608  4. 强化学习路由 (Reinforcement Learning Routing)
1609    核心是**“实战进化”** 。
1610    策略优化：通过多步交互（思考 -&gt; 路由 -&gt; 再思考）迭代改进答案，适合复杂推理，但延迟较高（如 Router-R1） 。
1611    在线老虎机 (Bandit)：在实时交互中通过用户反馈（点赞/踩）动态调整路由策略，平衡“探索新模型”与“利用已知强模型” 。
1612    代表案例：MixLLM（实现 97% 的 GPT-4 质量且仅需 24% 的成本） 。
1613  5. 基于不确定性的路由 (Uncertainty-based Routing)这是你项目中 Logprobs 熵值 策略的理论依据 。
1614    原理：监控模型对自身回答的“信心” 。如果内部数学信号（如概率分布）显示模型在犹豫，则触发升级 。
1615    关键点：研究证明，模型内部的探测信号（Logits）远比模型自己口头说的“我很确定”要准得多 。
1616    代表案例：CP-Router（利用共形预测处理不确定性） 。
1617  6. 级联系统 (Cascading)这是你项目中 Binary Gate 和逐级踢球架构的归属 。
1618    原理：顺序执行。先让小模型试，不行再给中模型，最后大模型保底 。
1619    核心逻辑：引入了“后悔药”机制，通过自我验证或外部评估器决定是否停止或升级 。
1620    代表案例：FrugalGPT（三大组件：路由器、质量评估器、停止判断器）和 AutoMix 。
1621  
</code></pre>

<a id="log-2026-04-08"></a>
### 2026-04-08

Source lines: `1622-1690`

<pre class="tech-log-source"><code>
1622  # 2026-04-08
1623  
1624  ## 实践
1625  
1626  搭建了自己的完整Pipeline
1627  质量不变的情况下，cluster方法效果最好，成本降低了 ***10%***
1628  
1629  ## 知识学习
1630  
1631  #### Router 经典论文总结
1632  本文档面向后续逐篇复现，聚焦综述 《Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey》 中以下三节的代表性工作：
1633  
1634  Section 2: Difficulty-aware Routing
1635  Section 6: Uncertainty-based Routing
1636  Section 7: Cascades
1637  整理原则：
1638  
1639  只优先采用原论文、官方项目页、官方代码仓库、会议页面。
1640  如果某些细节在摘要页看不到，我会明确标注“需要补读 PDF/附录”。
1641  如果仓库 README 展示的是论文发布后的扩展结果，我会明确写成“仓库后续更新”，避免和论文主结果混淆。
1642  一页结论
1643  如果你接下来要逐一复现，我建议按这个顺序推进：
1644  
1645  AutoMix：代码、数据、任务说明最完整，最适合先跑通一个 cascade 基线。
1646  FrugalGPT：工程可用性强，官方仓库完整，适合改造成商业 API 版本。
1647  BEST-Route：代码完整，但包含 reward model、best-of-n、多阶段数据构造，工程复杂度高于前两者。
1648  GraphRouter：官方代码已放出，但图构建与数据预处理更复杂。
1649  EmbedLLM：数据和代码齐全，但更像“模型表示学习 + routing 下游头”，对实验环境要求更高。
1650  CP-Router：训练自由、思路清晰，但我当前未检索到官方代码，复现需要自己补实现。
1651  Self-REF / Learning to Route LLMs with Confidence Tokens：论文价值高，但目前未检索到官方公开代码。
1652  Confidence-Driven LLM Router：适合后续用商业 API 重做，但目前主要能拿到论文页面信息，代码未公开。
1653  
1654  #### 开源Router方案总结
1655  本文档对 4 个你点名的开源 router / router 模型做统一拆解：
1656  
1657  1. `RouteLLM`
1658  2. `semantic-router`
1659  3. `notdiamond-0001`
1660  4. `knn-router`
1661  整理维度尽量与 `经典论文.md` 保持一致：
1662  - 项目定位
1663  - 相关论文或技术来源
1664  - 数据集
1665  - 测试用大模型 / 候选模型池
1666  - router 模型 / 机制
1667  - 效果 / benchmark
1668  - 创新点
1669  - 实验与工程形态
1670  - 开源代码位置
1671  - 复现建议
1672  
1673  #### RouteLLM
1674  
1675  这一段原本保留了完整的操作指令，整理后保留关键信息：
1676  
1677  - `RouteLLM` 的 GSM8K 基本链路已经打通，2 题 smoke test 可以分别产出 strong / weak model 结果。
1678  - 当时最后的阻塞点只是 `outputs/` 目录不存在，后来已经补成自动创建。
1679  - 关键修复包括：
1680    - `bert` 路径不再强依赖 `OPENAI_API_KEY`
1681    - `openai_server.py` 不再在 import 阶段崩溃
1682    - `gsm8k.generate_responses` 支持自定义模型对和输出文件
1683    - 评测脚本可以直接读取自定义 GSM8K 响应 CSV 并做可视化
1684  - 固定执行顺序被整理成：
1685    1. 保持 `routellm.openai_server` 运行
1686    2. 先做 5 题 smoke test
1687    3. 成功后再跑全量生成
1688    4. 最后执行 evaluate 出图
1689  - 这一段最重要的收获不是命令本身，而是把 `RouteLLM` 的“响应生成 -&gt; 评测 -&gt; 可视化”链路真正跑通了。
1690  
</code></pre>

<a id="log-2026-04-09"></a>
### 2026-04-09

Source lines: `1691-1710`

<pre class="tech-log-source"><code>
1691  # 2026-04-09
1692  
1693  ## 尝试更多的开源策略
1694  
1695  #### [RouteLLM](https://github.com/aurelio-labs/semantic-router)
1696  
1697  准确率（Accuracy）:
1698  
1699  在 GSM8K 数据集上，不同策略的表现如下：
1700  策略              准确率 (Accuracy)    相比 Random 的提升                     评价
1701  Random (随机)        88.93%                  -                     基准线：无脑混合强弱模型的结果。
1702  Causal_LLM         0.52%+1.59%           显著胜出：                成功识别了模型专长，捕获了互补性 。
1703  MF (矩阵分解)      90.30%+1.37%           优于随机：                即使只有部分数据，也展现了预判能力。
1704  BERT/SW_Ranking     ~88.7%             -0.2%(负优化)           低于随机：说明这些路由器在数学逻辑上出现了误判。
1705  
1706  策略,               准确率 (Accuracy),   成本 (CNY),性能/成本效率评价
1707  Weak (7B),          85.90%,0.58,        成本极低，但存在能力天花板
1708  Strong (72B),       92.87%,1.77,        准确率最高，但成本是 7B 的 3.06 倍
1709  Causal_LLM (Router),90.52%,1.20,        最优解：用 67% 的成本换取了 97.5% 的最强性能
1710  
</code></pre>

<a id="log-2026-04-10"></a>
### 2026-04-10

Source lines: `1711-1773`

<pre class="tech-log-source"><code>
1711  # 2026-04-10
1712  
1713  ## 尝试更多的开源策略
1714  
1715  #### 现有Pipeline
1716  
1717  - `llmrouter` 当前主链路是：
1718    数据合并与切分 -&gt; 全模型 benchmark -&gt; 自动打 tier 标签 -&gt; 训练 classifier / 调 cascade 阈值 -&gt; test 集统一评测 -&gt; 出图。
1719  - benchmark 阶段才会真实调用各模型；训练和评测阶段主要基于已保存结果做监督训练或离线模拟。
1720  - 因此当前 accuracy / cost 基本可直接比较，但 flat router 自身的 routing latency 并没有被完整计入。
1721  - 当前主评测策略包括：
1722    `baseline-32b / 14b / 7b / 3b / 1.5b`、
1723    `random`、
1724    `oracle`、
1725    `cascade-default`、
1726    `cascade-optimized`、
1727    `classifier`、
1728    `binary-gate-logprobs`
1729  
1730  #### [Semantic-router](https://github.com/aurelio-labs/semantic-router)
1731  - 我把 `semantic-router` 理解成“检索式分类器”，它更适合先以 `query -&gt; predicted_label` 的形式接入 Phase 3 evaluation，而不是直接改 benchmark 主干。
1732  - 接入思路被收敛为：
1733    - 用 `unified/train` + `routing_labels` 构建 5 路 semantic routes
1734    - 对 `unified/test` 做 semantic routing
1735    - 输出 `predicted_label`
1736    - 复用现有 `simulate_strategy` 和 metrics
1737  - 需要提前注意的风险：
1738    - 路径硬编码较多
1739    - 需要可用的 encoder backend
1740    - Python 3.13 对部分本地 encoder 兼容性一般
1741    - 当前延迟口径仍不是端到端 latency
1742  - 已完成远程单独评测：
1743    - Accuracy: 68.18%
1744    - Cost Ratio: 25.9%
1745    - Avg Latency: 857ms
1746    - P99 Latency: 8308ms
1747  - 相对位置：
1748    - 比 `classifier` 更准，但成本更高
1749    - 略低于 `cascade-optimized` 的准确率，但延迟明显更好
1750  - 远程结果和对比文件都已经单独保存，后续可以直接回看 summary / comparison 产物。
1751  
1752  #### Router Latency
1753  
1754  - 我专门确认了一个问题：论文和综述通常会提到 latency / overhead，但很少把 `router decision latency` 单独定义为最终实验指标。
1755  - 更常见的口径仍然是端到端响应时间，因此 router 本身的额外决策开销在很多对比里其实是模糊的。
1756  
1757  - 当前诊断已经比较明确：
1758    - route 分布严重不平衡，32B route 太小
1759    - hardest 样本识别不足
1760    - 排除 `all_wrong` 样本会进一步削弱 hardest route
1761  - 后续调参顺序也已经确定：
1762    1. 先加 `all_wrong`
1763    2. 再做 per-route cap，处理类不平衡
1764    3. 最后再调 `top-k` 和 aggregation
1765  - 已跑出的关键实验结果：
1766    - `semantic_router_gpu`: 68.18% / 25.9%
1767    - `include_all_wrong`: 68.91% / 33.2%
1768    - `include_all_wrong + cap2000`: 70.29% / 36.7%
1769    - `include_all_wrong + top5 + max`: 62.94% / 20.6%
1770    - `bge-m3 + include_all_wrong`: 68.72% / 31.8%
1771    - `bge-m3 + include_all_wrong + cap2000`: 69.34% / 33.7%
1772  - 这一轮最重要的结论是：真正决定效果的不是“semantic-router”这个名字，而是 route 形态、数据分布和 threshold 策略。
1773  
</code></pre>

<a id="log-2026-04-11"></a>
### 2026-04-11

Source lines: `1774-1870`

<pre class="tech-log-source"><code>
1774  # 2026-04-11
1775  
1776  ## 实践
1777  
1778  #### 追求极致的正确率
1779  
1780  - 当前 best semantic-router: 79.61% / 97.2%
1781  - 提升是 +0.08 个点 accuracy，同时成本从 100% 降到 97.2%
1782  
1783  最新结果：
1784    跑完了 4 组cost &lt;= 40% 的 semantic-router 新实验。当前最优是：
1785    - semantic_router_override14b_7b_meta_mpnet_cost40_fresh4xa100
1786    - Accuracy: 76.28%
1787    - Cost Ratio: 38.6%
1788    - Avg Latency: 1054ms
1789    - P99 Latency: 9744ms
1790  
1791    关键配置：
1792    - encoder: sentence-transformers/all-mpnet-base-v2
1793    - routing mode: 32b-override 这一套逻辑被我用作“base model default + semantic override”，这里 base 是 qwen2.5-14b
1794    - override candidate: qwen2.5-7b
1795    - text fields: dataset,subject,difficulty
1796    - tuned threshold: qwen2.5-7b = 0.8628563005596404
1797    - routing distribution: qwen2.5-14b = 4935, qwen2.5-7b = 1514
1798  
1799  #### 已知方案总体对比
1800  
1801  | 策略 | 准确率 | 相对成本 | 平均延迟 | P99 延迟 |
1802  |------|--------|----------|----------|----------|
1803  | Always 32B | 79.53% | 100.0% | 1539ms | 18354ms |
1804  | Always 14B | 76.73% | 43.7% | 1248ms | 13021ms |
1805  | Always 7B | 72.58% | 22.1% | 659ms | 4878ms |
1806  | Always 3B | 63.92% | 9.4% | 621ms | 4673ms |
1807  | Always 1.5B | 55.93% | 4.7% | 624ms | 4280ms |
1808  | Random | 69.64% | 36.6% | 897ms | 7977ms |
1809  | Oracle | 90.80% | 20.3% | 824ms | 6848ms |
1810  | Cascade (default) | 62.35% | 10.3% | 951ms | 6759ms |
1811  | Cascade (optimized) | 68.85% | 24.7% | 2053ms | 21973ms |
1812  | Binary Gate (logprobs) | 68.85% | 24.7% | 2053ms | 21973ms |
1813  | Classifier (0.5B) | 60.89% | 12.3% | 765ms | 6386ms |
1814  | Semantic Tiered MiniLM cap2000 | 70.71% | 37.2% | 968ms | 9624ms |
1815  | Semantic Tiered MiniLM cost33 | 70.12% | 33.8% | 942ms | 9019ms |
1816  | Semantic Tiered MiniLM cost35.5 | 70.62% | 36.8% | 963ms | 9503ms |
1817  | Semantic Override 32B-&gt;14B MPNet | 79.61% | 97.2% | 1525ms | 17398ms |
1818  | Semantic Override 14B-&gt;7B MPNet | 76.28% | 38.6% | 1054ms | 9744ms |
1819  | Semantic Override 14B-&gt;3B MPNet | 74.57% | 35.7% | 1017ms | 9050ms |
1820  | Semantic Override 14B-&gt;1.5B/3B MPNet | 73.67% | 35.1% | 1023ms | 8919ms |
1821  
1822  #### 最新 Semantic Router 内部对比
1823  
1824  | 方案 | Encoder | 路由形式 | 关键设置 | 准确率 | 成本 |
1825  |------|---------|----------|----------|--------|------|
1826  | Tiered MiniLM cap2000 | all-MiniLM-L6-v2 | 五路 tiered | include_all_wrong + cap2000 | 70.71% | 37.2% |
1827  | Tiered MiniLM tuned cost33 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.33 | 70.12% | 33.8% |
1828  | Tiered MiniLM tuned cost35.5 | all-MiniLM-L6-v2 | 五路 tiered | 32B 阈值调优，target cost=0.355 | 70.62% | 36.8% |
1829  | Override 32B-&gt;14B MPNet | all-mpnet-base-v2 | 32B 默认，命中后降到 14B | metadata: dataset/subject/difficulty，threshold=0.9364 | 79.61% | 97.2% |
1830  | Override 14B-&gt;7B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 7B | metadata: dataset/subject/difficulty，threshold=0.8629 | 76.28% | 38.6% |
1831  | Override 14B-&gt;3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 3B | metadata: dataset/subject/difficulty，threshold=0.8585 | 74.57% | 35.7% |
1832  | Override 14B-&gt;1.5B/3B MPNet | all-mpnet-base-v2 | 14B 默认，命中后降到 1.5B/3B | metadata: dataset/subject/difficulty，threshold=0.8818 | 73.67% | 35.1% |
1833  
1834  #### 关键结论
1835  1. **Semantic Router 的当前最高准确率方案**是 `32B 默认 + 14B override + MPNet + metadata`，达到 **79.61% / 97.2%**。相比 Always 32B，准确率仅提高 **0.08** 个百分点，成本下降 **2.8** 个百分点，收益很小，但它证明 semantic override 已经可以做到几乎不掉点。
1836  2. **在 cost &lt;= 40% 约束下，当前最优方案**是 `14B 默认 + 7B override + MPNet + metadata`，达到 **76.28% / 38.6%**。相比 Always 14B，准确率只低 **0.45** 个百分点，但成本少 **5.1** 个百分点。
1837  3. **旧的 tiered semantic-router 已经被 override 方案明显压制。** 最好的 tiered 版本是 `include_all_wrong + cap2000`，只有 **70.71% / 37.2%**；而 `14B-&gt;7B override` 在几乎相同成本下把准确率再拉高了 **5.57** 个百分点，成本只增加 **1.4** 个百分点。
1838  4. **真正带来提升的不是“semantic-router”这个名字本身，而是方案形态变化。** 从五路 tiered 改成“强模型默认 + 低一级模型 override”，再叠加 `all-mpnet-base-v2` 和结构化 metadata，效果才明显跃升。
1839  5. **如果目标是把 semantic-router 接到现有 llmrouter pipeline 做单独验证，当前最值得保留的候选只需要两条：**
1840     - `semantic-override32b-14b-mpnet-meta-acc`：用于验证语义路由的准确率上限。
1841     - `semantic-override14b-7b-mpnet-meta-cost40`：用于验证成本受限场景下的真实收益。
1842  
1843  #### 和已有 Router 方案的相对位置
1844  - 相比 `classifier`，`14B-&gt;7B semantic override` 准确率从 **60.89%** 提升到 **76.28%**，但成本也从 **12.3%** 提升到 **38.6%**。
1845  - 相比 `cascade-optimized` / `binary-gate-logprobs` 的 **68.85% / 24.7%**，`14B-&gt;7B semantic override` 在准确率上高出 **7.43** 个百分点，但成本也更高。
1846  - 在“可直接上线的简单策略”里，Always 14B 仍然是很强的朴素基线：**76.73% / 43.7%**。Semantic override 的价值在于把这条强基线压到 40% 左右成本时，仍能尽量保留准确率。
1847  
1848  ## 知识学习
1849  
1850  #### 参数矩阵 Checkpoint
1851  参数矩阵只保存某些checkpoint：
1852  训练时，**时间换空间**
1853  
1854  为什么 checkpoint 不只存第一层：
1855  反向传播需要 每一层的输入激活值。如果只存第一层：
1856  L1 (存)
1857  L2
1858  L3
1859  L4
1860  反向传播时会反复从 L1 重新算：
1861  L1→L2→L3
1862  L1→L2
1863  ...
1864  计算量会爆炸。因此实际做法是 每隔几层存一个：
1865  L1 (存)
1866  L2
1867  L3
1868  L4 (存)
1869  这样反向时最多只需要 重新算中间几层，计算量可控，同时减少显存。
1870  
</code></pre>

<a id="log-2026-04-12"></a>
### 2026-04-12

Source lines: `1871-1899`

<pre class="tech-log-source"><code>
1871  # 2026-04-12
1872  
1873  ## 知识学习
1874  
1875  #### assignment1-basics/cs336_basics/trainer/utils.py
1876  
1877  #### assignment1-basics/cs336_basics/model/modules.py
1878  
1879  #### einsum()
1880  
1881  #### 常见显卡
1882  
1883  #### LLM参数量估算
1884  
1885  #### MoE模型
1886  
1887  #### PPO/GRPO/DPO
1888  
1889  ```
1890  # 定义前向传播：给定输入 x，输出线性变换后的结果。
1891  def forward(self, x: torch.Tensor) -&gt; torch.Tensor:
1892      # 用 einsum 实现矩阵乘法。
1893      # 这里的含义是：
1894      # 输入 x 的最后一维是 d_in，
1895      # 权重 weight 的形状是 (d_out, d_in)，
1896      # 输出的最后一维就变成 d_out。
1897      return einsum(x, self.weight, &#x27;... d_in,  d_out d_in -&gt; ... d_out&#x27;)
1898  ```
1899  
</code></pre>

<a id="log-2026-04-13"></a>
### 2026-04-13

Source lines: `1900-2002`

<pre class="tech-log-source"><code>
1900  # 2026-04-13
1901  
1902  ## 实践
1903  
1904  1. Semantic Router 的流程
1905  
1906  这版实现入口在 llmrouter/src/router/semantic_router_strategy.py 和 llmrouter/src/evaluate/run_evaluation.py。
1907  
1908  **完整流程**
1909  ```
1910  1. 从训练集读取已标注样本。
1911     代码会把 /tangboyan/llmrouter/data/unified/train.jsonl 和 /tangboyan/llmrouter/results/labels/routing_labels.jsonl 对齐，只保留 unified train 里的 query。对应 load_train_labeled_queries()。
1912  2. 把每条训练样本变成 semantic text。
1913     默认就是 query 本身；如果开了 semantic-text-fields，会把 dataset/subject/difficulty 这类 metadata 也拼进去。对应 build_semantic_text()。
1914  3. 按路由目标组织成 route。
1915     当前支持两种模式：
1916      - tiered：5 路分类，直接建 1.5b / 3b / 7b / 14b / 32b 五个 route。
1917      - 32b-override：不是五路平权，而是“默认强模型 + 若干小模型 override”。例如 14B 默认，7B override。对应 prepare_route_training_records()。
1918  4. 用预训练 encoder 建索引。
1919     每个 route 里放一批 utterances，semantic-router 用 HuggingFaceEncoder 编码后建立向量索引。对应 build_routes() 和 build_semantic_router_from_train_records()。
1920  5. 推理时对测试 query 编码并检索。
1921     对测试 query 用同一个 encoder 编码，检索 top-k 相似 utterances，然后按 route 聚合分数。对应 score_routes_for_vector()。
1922  6. 决策。
1923      - 如果是普通 tiered 且没调阈值：直接取 router 返回的最佳 route。
1924      - 如果开了 threshold tuning：按阈值判断，没过阈值就 fallback 到默认大模型。
1925      - 如果是 32b-override：必须走 threshold 逻辑，否则代码直接报错。对应 choose_route_with_thresholds() 和 run_semantic_router_inference()。
1926  7. 评测。
1927     路由结果不会真实再调模型，而是去查已经离线跑好的 benchmark 结果，看被路由到的模型在该题上是否答对，然后统计 accuracy / cost / latency。对应 simulate_strategy() 和 compute_all_metrics()。
1928  ```
1929  
1930  2. 测试用了什么数据集？
1931  测试集是 unified_test，入口写在 llmrouter/src/evaluate/run_evaluation.py。
1932  具体是：
1933  - 测试切分文件：/tangboyan/llmrouter/data/unified/test.jsonl
1934  - 训练切分文件：/tangboyan/llmrouter/data/unified/train.jsonl
1935  - 评测时会读取 5 个模型在各数据集上的 benchmark 结果，再筛出 unified_test 里的 query
1936  - 当前这套 v2_5tier 评测覆盖的数据集，从结果里看是：
1937      - agieval
1938      - ceval
1939      - cmath
1940      - cmmlu
1941      - gsm8k
1942      - logiqa2
1943  当前统一测试集规模是 6449 条。
1944  
1945  3. Semantic Router 需要训练吗？
1946  结论：不需要像 classifier 那样做参数训练。
1947  - classifier：要训练一个新模型
1948  - semantic-router：不训练新分类器参数，只是“拿预训练 embedding 模型 + 训练集样本建语义路由索引”
1949  
1950  **semantic-router**
1951  ```
1952  - 需要一套已标注的训练样本，用来构建 route utterances
1953  - 需要一个预训练 encoder，例如你现在用过的：
1954      - sentence-transformers/all-MiniLM-L6-v2
1955      - sentence-transformers/all-mpnet-base-v2
1956  - 可选地需要做一次阈值调优，但这不是模型训练，只是用训练集里再切一小块验证集做搜索
1957  ```
1958  
1959  现在这版代码里，threshold tuning 也只是：
1960  - 切一部分 unified_train
1961  - 搜索阈值
1962  - 选 accuracy/cost 最优点
1963  不是 gradient finetune。
1964  
1965  ## 知识学习
1966  
1967  #### 为什么不直接存“参数矩阵的转置”？
1968  
1969  Y = X x W^T
1970  
1971  你可能会问：既然都要转置，为什么不直接把 self.weight 定义成 (in_features, out_features)？
1972  
1973  答案是：为了计算效率（和历史习惯）。
1974  逻辑直观：在 (out, in) 的存储方式下，weight[0]（矩阵的第一行）直接对应于第一个输出神经元的所有权重。这在逻辑上非常清晰。
1975  算子优化：底层硬件（如 NVIDIA GPU）在执行 Linear 算子时，针对这种存储方式做了深度优化。
1976  
1977  #### 常见数据类型详解
1978  
1979  通过浮点数的三个组成部分来理解它们：
1980  符号位（Sign）、指数位（Exponent，决定范围）和尾数位（Fraction/Mantissa，决定精度）。
1981  
1982  #### FP32 (Full Precision / Single Precision)
1983  结构： 1位符号，8位指数，23位尾数。
1984  特点： 精度极高，数值范围广。
1985  LLM 中的角色： 曾经是标准。但在如今的 LLM 训练中，它通常只作为“主权重（Master Weights）”存在，用来在优化器更新时保持微小的梯度变化。
1986  
1987  #### FP16 (Half Precision)
1988  结构： 1位符号，5位指数，10位尾数。
1989  优点： 内存占用减半，计算速度极快。
1990  缺点： 数值范围窄（最大约 65504）。在训练 LLM 时，极易产生“梯度溢出（Overflow）”或“下溢（Underflow）”，导致训练崩溃。
1991  对策： 需要使用混合精度训练（Mixed Precision Training）和损失缩放（Loss Scaling）。
1992  
1993  #### BF16 (Brain Floating Point 16) —— LLM 的宠儿
1994  结构： **1**位符号，**8**位指数，**7**位尾数。
1995  特点： 它是 Google 为了深度学习专门设计的。它的指数位与 FP32 一样长。
1996  为什么好用： 它的精度（尾数）虽然不如 FP16，但它的数值范围（Range）和 FP32 完全一样。
1997  意义： 在训练 LLM 时，你不需要担心梯度溢出，不需要搞复杂的 Loss Scaling。目前主流的大模型（Llama 3, GPT-4 等）基本都采用 BF16 进行预训练。
1998  
1999  #### einsum()
2000  通过 einsum，即使输入是一个高维张量（例如 x 的形状是 (batch_size, L, d_model)），我们仍然可以通过 广播 规则来进行矩阵乘法（在这种情况下，广播会自动应用到批次维度和其他维度）。
2001  所以，即使 x 不是二维矩阵，einsum 也能处理高维张量并正确地进行矩阵运算，保证维度匹配。
2002  
</code></pre>

<a id="log-2026-04-14"></a>
### 2026-04-14

Source lines: `2003-2127`

<pre class="tech-log-source"><code>
2003  # 2026-04-14
2004  
2005  ## 知识学习
2006  
2007  #### vLLM Semantic Router
2008  是一个面向 多模型系统 的“语义路由与运行控制层”，不是单纯的模型网关，也不是只做学术路由实验的分类器。
2009  它的官方定位是：在云、数据中心、边缘侧，为 Mixture-of-Models 提供系统级智能路由。README.md
2010  - 不同模型在能力、成本、延迟、隐私边界上差异很大，单一模型很难覆盖所有流量。
2011  - 真实请求不仅要“选模型”，还要同时处理安全、缓存、记忆、RAG、工具调用、回放审计等系统能力。
2012  - 路由逻辑不能只停留在一个分类器上，而要变成可配置、可验证、可部署、可观测的运行时系统。
2013  这个项目本质上更像一个 LLM 流量控制平面。它位于客户端和后端模型之间，理解请求，再决定走哪条路、用哪个模型、是否启用插件能力、是否需要额外的安全或工具策略。README.md docs/agent/repo-map.md
2014  
2015  #### 系统架构
2016  把“路由”拆成了几个清晰层次，而不是用一个黑盒分类器直接输出模型名：
2017  - signal evaluation
2018  - projection coordination
2019  - decision selection
2020  - model selection
2021  - plugin handling
2022  在 AMD 参考 profile 里，这条链路写得很明确：先做多种信号检测，再做投影/分区，再选路由决策，最后把请求转发到对应模型别名。deploy/amd/README.md
2023  
2024  - Signals：检测层。定义“识别到了什么”。支持关键词、语言、上下文长度、结构、权限、embedding、domain、complexity、fact-check、jailbreak、PII、preference、reask、user-feedback、knowledge base 等。website/docs/tutorials/signal/overview.md
2025  - Projections：协调层。把多个弱信号合成为可复用的中间事实，比如 intent partition、difficulty band、verification_required 这类 band，而不是把数值逻辑散落在每个 route 里。website/docs/tutorials/projection/overview.md
2026  - Decisions：策略层。用布尔规则、优先级、tier 选出一条 route。这里是“哪条策略赢”。website/docs/tutorials/decision/overview.md src/semantic-router/pkg/config/decision_config.go
2027  - Algorithms / Model Selection：候选模型选择层。一个 decision 可以挂多个候选模型，再用静态或学习式算法选最优，包括 static、elo、router_dc、automix、hybrid、rl_driven、gmtrouter、latency_aware，以及 looper 类的 confidence、ratings、remom。config/README.md src/semantic-router/pkg/extproc/req_filter_classification_runtime.go src/semantic-router/pkg/modelselection/selector.go
2028  - Plugins：路由后处理层。匹配到某条 route 后，可以附加 route-local 行为，比如 semantic cache、RAG、memory、router replay、tools、system prompt、request params、content safety、hallucination、response jailbreak、image generation 等。website/docs/tutorials/plugin/overview.md
2029  
2030  不只是“把问题分类到模型”，而是在做 信号驱动的策略编排:
2031  比如可以先识别“这是法律高风险请求”，再叠加“需要核验来源”“上下文很长”“用户在追问纠错”，最后才决定走 premium specialist 路线，并启用相应插件。
2032  
2033  #### 配置与运行方式
2034  这个项目的另一大特点是配置体系比较完整，而且是统一的。
2035  它采用一套 canonical YAML 合同：
2036  - version
2037  - listeners
2038  - providers
2039  - routing
2040  - global
2041  其中：
2042  - routing 负责语义路由本身，包括 modelCards、signals、projections、decisions
2043  - providers 负责具体部署绑定和默认模型
2044  - global 负责全局运行时能力，比如 observability、router replay、stores、tools、looper、modelcatalog 等。这套约定写在公开配置文档里，也被仓库测试强约束。website/docs/installation/configuration.md configREADME.md
2045  
2046  此外，这个项目同时支持两种配置视角：
2047  - YAML canonical config
2048  - DSL authoring surface
2049  也就是说，用户既可以直接写 config.yaml，也可以用 DSL/可视化编辑器去表达路由图，然后再编译回canonical YAML。这让它既适合工程部署，也适合调参和策略设计。
2050  website/docs/installation/configuration.md
2051  
2052  在部署侧，它不是单一路径，而是支持多种环境：
2053  - 本地 CPU 开发
2054  - 本地 AMD/ROCm 开发
2055  - Kubernetes / Helm / Operator
2056  - Dashboard 控制台
2057  - E2E profile 驱动的测试环境
2058  
2059  仓库文档给出的本地默认流程是：
2060  - make vllm-sr-dev
2061  - vllm-sr serve --image-pull-policy never
2062  对应 CPU / AMD 两套本地环境说明也很清楚。docs/agent/environments.md
2063  
2064  #### 仓库组成
2065  从代码组织上看，这个仓库已经不是一个单体 router，而是一整套平台：
2066  - src/semantic-router：Go 核心路由器，包含 config、classification、decision engine、Envoy extproc、selection、plugin runtime。
2067  - src/vllm-sr：Python CLI，负责本地启动、配置校验、Docker 编排、开发体验。
2068  - dashboard：前后端控制台，用于配置编辑、部署、状态查看、playground、可视化。
2069  - deploy/operator：Kubernetes Operator 和 CRD。
2070  - deploy/helm：Helm chart。
2071  - src/training：模型选择与分类相关训练脚本、数据、推理服务。
2072  - e2e：端到端测试框架，覆盖 routing、safety、cache、response-api、dashboard、authz、streaming 多 profile。
2073  - candle-binding ml-binding nlp-binding：Rust/native bindings，用于更底层的推理或 ML 能力接入。
2074  
2075  **架构图**
2076  ```
2077    Authoring / Control Plane
2078      Dashboard / DSL / YAML / CLI / Helm / Operator
2079            |
2080            v
2081    Canonical Config v0.3
2082      version / listeners / providers / routing / global
2083            |
2084            v
2085    Runtime Plane
2086      Client
2087        -&gt; Envoy
2088        -&gt; semantic-router extproc (OpenAIRouter)
2089           -&gt; Signals
2090           -&gt; Projections
2091           -&gt; Decisions
2092           -&gt; Algorithms / Looper
2093           -&gt; Route-local Plugins
2094           -&gt; Provider binding / endpoint selection / alias rewrite
2095           -&gt; Upstream model backends
2096        &lt;- Response filters / replay / cache / warnings / headers
2097            |
2098            v
2099    Observability / Replay / Dashboard Insight
2100  
2101    Validation / Support Plane
2102      E2E profiles / deploy recipes / training stack / Rust-native bindings
2103  ```
2104  这张图背后的关键点是：
2105  - 这套系统有一个统一配置合同，不是 CLI 一套、Dashboard 一套、Operator 一套。仓库明确把入口统一为 version / listeners / providers / routing / global，其中 routing 负责 `modelCards5), website/docs/tutorials/projection/overview.md:9, website/docs/tutorials/decision/overview.md:7, website/docs/tutorials/algorithm/overview.md:7, website/docs/tutorials/plugin/overview.md:5, deploy/amd/README.md:100)
2106  - 仓库形态也说明它是平台，不是单一 router binary。src/semantic-router 是 Go 路由内核，src/vllm-sr 是 Python CLI，dashboard/ 是控制台，deploy/operator/ 和 deploy/helm/ 是 K8s 部署面，e2e/ 是验证框架，src/training/ 和 Rust bindings 是算法/模型支持层。(docs/agent/repo-map.md:3)
2107  
2108  所以一句话说，它更像“LLM 流量控制平面 + 运行时策略编排层”，而不是“模型网关 + 少量规则”。
2109  
2110  #### 一次请求怎么被路由
2111  1. 启动阶段先由 vllm-sr serve 做 bootstrap，解析配置、选择 Docker/K8s backend、准备 runtime config，然后把本地或集群拓扑拉起来。(src/vllm-sr/cli/commands/runtime.py:57, src/vllm-sr/cli/commands/runtime.py:214)
2112  2. 真正请求进入时，Go 侧的 OpenAIRouter 作为 Envoy extproc server 工作。它不是只处理 request body，而是完整跑四个阶段：request headers -&gt; request body -&gt; response headers -&gt; response body。(src/semantic-router/pkg/extproc/router.go:24, src/semantic-router/pkg/extproc/processor_core.go:48)
2113  3. request headers 阶段会先抓 request_id、:path、:method、streaming 预期、looper 内部请求标记等。也就是说，这里先决定“这是普通 chat、Response API、models 接口，还是 looper 内部调用”。(src/semantic-router/pkg/extproc/processor_req_header.go:17)
2114  4. request body 阶段先走一个快路径：如果是 Response API，就先翻译成 chat completions 形态；然后做 body 校验；再用 fast extractor 直接拿到 model / userContent / firstImageURL / stream，避免一开始就完整反序列化。(src/semantic-router/pkg/extproc/processor_req_body.go:22, /home/ryan/CUHKSZ/LLM-Router/V:61, src/semantic-router/pkg/decision/engine.go:60, src/semantic-router/pkg/decision/engine.go:199)
2115  5. decision engine 本身是个布尔规则树求值器。叶子节点是 type + name，支持 AND / OR / NOT，命中后会得到 confidence；多个 decision 都命中时，再按 tier -&gt; confidence -&gt; priority 或 priority -&gt; confidence 选出最终 route。(src/semantic-router/pkg/config/decision_config.go:3, src/semantic-router/pkg/decision/engine.go:151, src/semantic-router/pkg/decision/engine.go:335)
2116  6. route 选出来以后，不一定立刻等于“最终模型已定”。
2117  如果用户显式指定模型，router 会保留原模型，但仍然保留 decision 结果给插件使用。
2118  如果用户走的是 auto model，router 才会根据 decision.modelRefs + decision.algorithm 去做候选选择。(src/semantic-router/pkg/extproc/req_filter_classification_runtime.go:138, src/semantic-router/pkg/extproc/req_filter_classification.go:61)
2119  7. 候选模型选择分两类。单模型选择算法走 selector registry，比如 static / elo / router_dc / automix / hybrid / rl_driven / gmtrouter / latency_aware / knn / kmeans / svm。多模型编排算法走 looper，比如 confidence / ratings / remom。(website/docs/tutorials/algorithm/overview.md:55, src/semantic-router/pkg/selection/factory.go:96, src/semantic-router/pkg/extproc/req_filter_looper.go:45)
2120  8. 在真正发往上游前，router 还会跑一组 route-local 行为：fast_response、rate limit、semantic cache short-circuit、RAG 检索、modality 处理、memory 注入、request params、system prompt、tools 选择。然后才做 endpoint 选择、alias 到 provider-specific model id 的映射，并把修改后的 body 发给上游。(src/semantic-router/pkg/extproc/processor_req_body_prepare.go:63, src/semantic-router/pkg/extproc/req_filter_rag.go:19, src/semantic-router/pkg/extproc/processor_req_body_routing.go:28, src/semantic-router/pkg/extproc/processor_req_body_routing.go:65, /home/ryan/CUHKSZ/LLM-Router/VLLM-sem)
2121  
2122  把这 12 步压成一句话就是：
2123  客户端只发出一次 OpenAI 兼容请求，但 router 在内部实际完成了:
2124  “请求理解、信号抽取、投影协调、策略命中、候选模型选择、插件执行、后端绑定、响应审计与告警”
2125  这整条系统链路。
2126  
2127  
</code></pre>

<a id="log-2026-04-15"></a>
### 2026-04-15

Source lines: `2128-2129`

<pre class="tech-log-source"><code>
2128  # 2026-04-15
2129  
</code></pre>

<a id="log-2026-04-16"></a>
### 2026-04-16

Source lines: `2130-2132`

<pre class="tech-log-source"><code>
2130  # 2026-04-16
2131  
2132  
</code></pre>

<a id="log-2026-04-17"></a>
### 2026-04-17

Source lines: `2133-2255`

<pre class="tech-log-source"><code>
2133  # 2026-04-17
2134  
2135  ## 知识学习
2136  
2137  ### RoPE
2138  
2139  - 今天把 RoPE 的几何直觉重新想清楚了：一个 `D` 维向量会被拆成 `D/2` 个二维平面，每个平面都以原点 `(0, 0)` 为旋转中心。
2140  - 第 `k` 个平面由 `(x_{2k}, x_{2k+1})` 组成，位置编码的本质就是把这一对坐标绕原点旋转角度 `theta_k`。
2141  - 不同平面之间是正交、互不干涉的：
2142    - 平面 0 只影响 `(x0, x1)`
2143    - 平面 1 只影响 `(x2, x3)`
2144    - 各平面独立旋转，不会互相混入
2145  - 它们唯一的系统性联系是频率分布：
2146    - 低频平面旋转慢，更偏向捕捉长距离关系
2147    - 高频平面旋转快，更偏向捕捉短距离细节
2148  
2149  ### 维度与旋转
2150  
2151  - 另一个关键理解是：RoPE 不是“单维缩放”，而是二维成对旋转。
2152  - 在第 `k` 个平面中：
2153    - `x_{2k}` 是横坐标
2154    - `x_{2k+1}` 是纵坐标
2155    - 它们共同组成平面上的点 `P`
2156  - 当 token 位于第 `m` 个位置时，这个点会被旋转 `m * theta_k`。
2157  - 旋转后的核心性质：
2158    - 方向改变
2159    - 向量长度不变
2160    - 因而保留了幅值信息，同时把位置信息写进方向关系里
2161  - 这也解释了为什么必须“成对旋转”：
2162    只动一个维度会更像缩放；只有 `(x_{2k}, x_{2k+1})` 联动，才是真正的圆周旋转。
2163  
2164  对应代码理解：
2165  
2166  ```python
2167  x = rearrange(x, &#x27;... (s r) -&gt; ... s r&#x27;, r=2)
2168  
2169  [
2170    [x0, x1],   # 第 1 个平面的坐标
2171    [x2, x3],   # 第 2 个平面的坐标
2172    ...
2173    [x62, x63]  # 第 32 个平面的坐标
2174  ]
2175  ```
2176  
2177  这段代码本质上就是把一维向量按两维一组重排，显式变成“多个二维旋转平面”。
2178  
2179  
2180  
2181  ### 代码实现详解
2182  
2183  ``` RoPE
2184      def rotate_tensor(self, x: torch.Tensor) -&gt; torch.Tensor:
2185          &#x27;&#x27;&#x27;
2186          create a rotated tensor (x_2k, x_2k+1) -&gt; (-x_2k+1, x_2k)
2187          &#x27;&#x27;&#x27;
2188          # 先把最后一维按两两一组重排：
2189          # (..., Dh) -&gt; (..., Dh/2, 2)
2190          # 最后那个长度为 2 的维度分别存放偶数位和奇数位。
2191          x = rearrange(x, &#x27;... (s r) -&gt; ... s r&#x27;, r=2)
2192  
2193          # 拆出每一对中的偶数位和奇数位。
2194          x_even, x_odd = x.unbind(dim=-1)
2195  
2196          # 完成二维平面旋转中的“正交向量”构造：
2197          # (x_even, x_odd) -&gt; (-x_odd, x_even)
2198          x = torch.stack((-x_odd, x_even), dim=-1)
2199  
2200          # 再还原回原始最后一维的布局，方便和输入逐元素相乘。
2201          return rearrange(x, &#x27;... s r -&gt; ... (s r)&#x27;)
2202  ```
2203  
2204  1. 核心算子：从“一排”到“一对” (rearrange)
2205  在进行旋转前，必须将平铺的隐藏维度 Dh 进行两两分组。
2206  
2207  代码：x = rearrange(x, &#x27;... (s r) -&gt; ... s r&#x27;, r=2)
2208  
2209  形状流：(..., 64) -&gt; (..., 32, 2)
2210  
2211  意义：物理上确立了 32 个平面。最后一维的 2 代表每个平面内的坐标点 (x_even, x_odd)。
2212  
2213  2. 拆解与重组：实现 90° 垂直旋转
2214  RoPE 的旋转公式中，关键在于构造 rotate_half(x)。其内部逻辑如下：
2215  
2216  A. 拆分 (unbind)
2217  操作：x_even, x_odd = x.unbind(dim=-1)
2218  
2219  维度变化：
2220  
2221  x (原变量): 保持 (..., 32, 2) 不变。
2222  
2223  x_even / x_odd (新变量): 变为 (..., 32)。最后那个 2 被拆掉了。
2224  
2225  直观理解：像是把一叠双层卡片拆成了“上层”和“下层”两堆。
2226  
2227  B. 取反与配对 (stack)
2228  操作：x_rotated = torch.stack((-x_odd, x_even), dim=-1)
2229  
2230  逻辑：这里的 stack 会新建一个维度，将 -x_odd 和 x_even 按位置重新配对。
2231  
2232  变换结果：[a, b] -&gt; [-b, a]。
2233  
2234  几何意义：这在二维平面上对应一个标准的逆时针 90° 旋转。
2235  
2236  3. 全程形状流动图 (Shape Flow)
2237  这是理解 RoPE 变换最清晰的视角：
2238  
2239  原始输入：(B, H, S, 64)
2240  —— 64 个特征平铺。
2241  
2242  分组 (rearrange)：(B, H, S, 32, 2)
2243  —— 形成 32 个平面坐标系。
2244  
2245  提取 (unbind)：x_even: (B, H, S, 32) | x_odd: (B, H, S, 32)
2246  —— 坐标分量拆分。
2247  
2248  旋转 (stack)：(B, H, S, 32, 2)
2249  —— 得到 [-x_odd, x_even] 组合。
2250  
2251  还原 (rearrange)：(B, H, S, 64)
2252  —— 旋转后的向量重新进入后续点积计算。
2253  
2254  
2255  
</code></pre>

<a id="log-2026-04-20"></a>
### 2026-04-20

Source lines: `2256-2270`

<pre class="tech-log-source"><code>
2256  # 2026-04-20
2257  
2258  ## Encoder 输出Z矩阵的归宿：KV
2259   
2260  内部循环：Z 矩阵是“中间产物”，负责特征的层层叠加。  
2261  对外接口：Encoder 整体的最终输出被视作一个 Memory（记忆库）。  
2262  
2263  KV 的功能分工：  
2264  Key (K)：相当于 Encoder 给每个词打的“索引标签”，供 Decoder 查找。    
2265  Value (V)：相当于 Encoder 给每个词提取的“语义精华”，供 Decoder 提取。   
2266  总结：Encoder 最后的 Z 矩阵就是 KV 的母体。在翻译模型中，我们常说 Encoder 将输入序列“编码成了一个 KV 缓存（KV Cache）”。  
2267  
2268  
2269  
2270  
</code></pre>

<a id="log-2026-04-22"></a>
### 2026-04-22

Source lines: `2271-2309`

<pre class="tech-log-source"><code>
2271  # 2026-04-22
2272  
2273  ## vLLM-Router 完整运行起来了
2274  
2275  这次真正跑通后，我对当前配置的理解是：
2276  
2277  - `model: &quot;MoM&quot;` 时，router 才会接管选模；否则就是普通模型直连。
2278  - 现在的 `decision -&gt; route -&gt; model` 里，大多数 route 只挂了 1 个 `modelRef`，所以它本质上还是“先分类，再直接转发”，还不是“同一路由内多模型竞争”。
2279  - 全局虽然开了 `model_selection.method: static`，但在单 `modelRef` 配置下，这一层几乎没有发挥作用。
2280  
2281  当前路由大致可分为两类：
2282  
2283  - 强制标签路由：`#flash / #plus / #max / #deepseek / #kimi / #coder` 分别固定到对应模型。
2284  - 语义路由：
2285    - 代码 / 报错 / 编程类 -&gt; `qwen3-coder-plus`
2286    - 深度分析 / 长上下文 -&gt; `qwen3.6-max-preview`
2287    - 规划 / 路线图 / 分步骤执行 -&gt; `kimi-k2.5`
2288    - 多问题分析 -&gt; `deepseek-v3.2`
2289    - 简短简单问题 -&gt; `qwen3.6-flash`
2290    - 兜底 -&gt; `qwen3.6-plus`
2291  
2292  这条 pipeline 可以概括成：
2293  
2294  1. 客户端请求打到 `8899`，并指定 `model: &quot;MoM&quot;`。
2295  2. Router 先根据消息内容抽取 signals。
2296  3. Decision engine 用这些 signals 命中某条 route。
2297  4. 当前 route 里通常只有一个 `modelRef`，所以直接选中该模型并转发到对应 provider。
2298  
2299  我现在的判断：
2300  
2301  - 这套配置已经能稳定完成“按请求类型分流”。
2302  - 但它还不算真正的多模型选择系统，更像是“规则分类器 + 单模型映射”。
2303  - 如果要验证 model selection 的价值，下一步必须让同一条 decision 挂多个 `modelRef`，否则 selection 层基本没有实验意义。
2304  
2305  补充定位：
2306  - 路由规则主要看 `config.yaml`
2307  - 分类入口在 `src/semantic-router/pkg/extproc/req_filter_classification*.go`
2308  
2309  
</code></pre>

<a id="log-2026-04-26"></a>
### 2026-04-26

Source lines: `2310-2393`

<pre class="tech-log-source"><code>
2310  # 2026-04-26
2311  
2312  ## CUDA
2313  
2314  今天主要先把 CUDA 的整体脉络理顺了，重点不是背文档，而是搞清楚它和 LLM 优化到底怎么接上。
2315  
2316  ### 先建立整体图景
2317  
2318  - CUDA 是让 CPU 发起、GPU 执行并行任务的编程模型；主机代码负责分配内存、发射 kernel、同步结果。
2319  - GPU 追求吞吐量，适合海量并行；CPU 追求低延迟和复杂控制。
2320  - CUDA 程序常见分层：高层框架 / 库（PyTorch、cuBLAS、cuDNN、Triton） -&gt; CUDA Runtime / Driver -&gt; PTX / cubin -&gt; GPU 硬件。
2321  
2322  ### 我真正需要记住的执行模型
2323  
2324  - kernel 是站在“单个线程”的视角写的：先算出自己的全局索引，再决定自己处理哪一段数据。
2325  - 启动方式是 `&lt;&lt;&lt;grid, block&gt;&gt;&gt;`；`blockIdx`、`blockDim`、`threadIdx` 不是函数参数，而是 CUDA 提供的内置上下文。
2326  - `.x / .y / .z` 只是数据维度的映射方式：向量通常只用 `.x`，图像或矩阵才会自然用到 `.x + .y`。
2327  - `grid` 负责覆盖总任务量，`block` 负责组织线程协作；简单向量加法只用 thread 视角，矩阵乘法 / attention 这类问题必须引入 block 视角。
2328  - warp 是 32 个线程的执行单位，因此 block 大小通常尽量设成 32 的倍数，避免浪费 lane。
2329  - 不同 block 之间默认不能相互依赖；块内协作靠 shared memory 和 `__syncthreads()`。
2330  
2331  ### 内存与性能直觉
2332  
2333  - 全局内存大但慢，寄存器和 shared memory 小但快。
2334  - 线程多不等于快，常见瓶颈反而在内存访问。
2335  - 一个 kernel 的性能，往往取决于：
2336    - 是否减少了全局内存读写
2337    - 是否避免了 warp divergence
2338    - 是否让访问尽量 coalesced
2339    - 寄存器 / shared memory 占用是否把 occupancy 压得太低
2340  
2341  ### 从代码层面想明白的几个点
2342  
2343  - `(N + threads - 1) / threads` 是为了向上取整，保证任务不漏；多开的线程再用 `if (i &lt; N)` 挡住。
2344  - `cudaDeviceSynchronize()` 是显式同步点。调试时很好用，也能暴露前面 kernel 的错误；但在性能敏感场景里不能滥用。
2345  - `extern &quot;C&quot;` 是为了关闭 C++ 名字修饰，方便被其他语言或动态加载逻辑找到。
2346  - `__global__` 表示“CPU 发起、GPU 执行”的 kernel 入口，必须 `void` 返回。
2347  
2348  ## CUDA 编程
2349  
2350  今天这部分最大的转变，是把“写循环”改成“做映射”。
2351  
2352  ```cpp
2353  __global__ void vector_add(const float* A, const float* B, float* C, int N) {
2354      int i = blockIdx.x * blockDim.x + threadIdx.x;
2355      if (i &lt; N) {
2356          C[i] = A[i] + B[i];
2357      }
2358  }
2359  ```
2360  
2361  我现在的理解：
2362  
2363  - CPU 时代的思路是“for 循环遍历数组”。
2364  - CUDA 的思路是“每个线程只负责自己的那个索引”。
2365  - 所以 kernel 本质上是在写 SPMD：同一段程序，被很多线程拿去处理不同数据。
2366  
2367  ### 和 LLM 优化怎么接上
2368  
2369  - Python / PyTorch 负责模型结构、调度和实验；CUDA kernel 负责真正重的并行算子。
2370  - 真正值得自己写 kernel 的地方，通常不是标准 GEMM，而是：
2371    - Attention / KV Cache 这类特殊访问模式
2372    - 量化解码
2373    - 多个小算子的融合
2374  - 如果只是标准矩阵乘法，优先用 `cuBLAS`；如果要在 GEMM 周围融合逻辑，再考虑 `CUTLASS`；如果想先快速试验，自定义 kernel 之前可以先看 `Triton`。
2375  
2376  ### 目前的工程判断
2377  
2378  - 写 CUDA 的核心不是“会不会语法”，而是能不能判断瓶颈在算力还是带宽。
2379  - 定位瓶颈不能靠猜，至少要会用：
2380    - `Nsight Systems` 看整体时间线
2381    - `Nsight Compute` 看单 kernel 的 roofline、memory throughput、occupancy
2382    - `torch.profiler` 把 Python 层和 CUDA kernel 对上
2383  
2384  ### 这次学习后我给自己的路线
2385  
2386  1. 先把 thread / block / warp / memory hierarchy 彻底吃透。
2387  2. 用最小例子把 kernel launch、同步、索引映射跑顺。
2388  3. 再进入 LLM 相关的 Triton / PyTorch Extension / CUTLASS。
2389  4. 真做优化时，先判断是 memory bound 还是 compute bound，再决定要不要手写 kernel。
2390  
2391  
2392  
2393  
</code></pre>

<a id="log-2026-04-27"></a>
### 2026-04-27

Source lines: `2394-2410`

<pre class="tech-log-source"><code>
2394  # 2026-04-27
2395  
2396  ## 远方 faraway
2397  
2398  基于腾讯云对接完整的后端
2399  
2400  [网页版APP](https://faraway-app-d0gpvf2ko79ceaba3-1426371841.tcloudbaseapp.com/)
2401  
2402  ### 安卓 APP 打包成功
2403  
2404  [目前版本 GihHub 仓库](https://github.com/Tt200411/faraway)
2405  
2406  待对接、开发更详细的后端功能
2407  
2408  
2409  
2410  
</code></pre>

<a id="log-2026-04-28"></a>
### 2026-04-28

Source lines: `2411-2474`

<pre class="tech-log-source"><code>
2411  # 2026-04-28
2412  
2413  ## CUDA 编程
2414  
2415  ### 内存分配
2416  
2417  #### 今日要点
2418  
2419  - `cudaMemcpyDefault` 的核心是让 CUDA 驱动自动判断搬运方向。
2420  - `cudaMallocManaged` 的核心不是复制两份数据，而是统一地址空间下的按需页迁移。
2421  - `cudaMemcpy` 更像“复制 + 粘贴”，`cudaMallocManaged` 更像“同一份逻辑数据在 CPU / GPU 之间迁移”。
2422  
2423  #### `cudaMemcpy` 第一个参数永远是目标地址（Destination）
2424  
2425  示例：
2426  
2427  ```cpp
2428  cudaMemcpy(devA, A, vectorLength * sizeof(float), cudaMemcpyDefault);
2429  ```
2430  
2431  理解：
2432  
2433  - `cudaMemcpyDefault` 就是让 CUDA 驱动开启“自动驾驶”模式。
2434  - CUDA 驱动会通过 PCIe 总线自动把数据从内存搬到显存。
2435  
2436  常见搬运方向：
2437  
2438  | 源地址（Source） | 目的地址（Destination） | 驱动实际执行的操作 |
2439  | --- | --- | --- |
2440  | CPU（`A`） | GPU（`devA`） | `HtoD`（上传到显卡） |
2441  | GPU（`devA`） | CPU（`A`） | `DtoH`（下载到内存） |
2442  | GPU1（`devA`） | GPU2（`devB`） | `Peer-to-Peer`（显卡间直接对传） |
2443  | GPU1（`devA`） | GPU1（`devB`） | `Device Copy`（显存内部搬运） |
2444  
2445  #### `cudaMallocManaged`：原来位于 CPU 的数据还在吗？
2446  
2447  这是一个非常深刻的问题，涉及到操作系统的虚拟内存管理和 CUDA 驱动的数据一致性策略。
2448  
2449  简单来说：
2450  
2451  - 数据依然“存在”，但在物理上它可能已经从 CPU 内存中“搬”走了。
2452  
2453  为了理解这一点，需要把“数据”拆分为逻辑地址和物理位置来看：
2454  
2455  1. 逻辑上：它一直都在  
2456     对于你的程序代码来说，变量 `A` 指向的地址（比如 `0x7f8000`）始终有效。无论数据当前是在显存里还是在主存里，都可以通过这个指针访问它。
2457  
2458  2. 物理上：它是“按需移动”的  
2459     统一内存（Unified Memory）的核心机制是页迁移（Page Migration）。它的行为非常像操作系统里的“交换文件（Swap）”：
2460     - GPU 访问时：如果数据在 CPU 内存中，驱动会产生一个“页错误”（Pa
2461    ge Fault）。此时，驱动会将这一页数据（通常是 `4KB` 或 `2MB`）通过 PCIe 总线拷贝到显存，并更新 GPU 的页表。
2462     - 原来在 CPU 的副本：在大多数现代系统（如 Pascal 架构及之后的 GPU）上，为了保证数据一致性，CPU 端的这一页内存会被标记为“无效”或直接被物理释放。
2463  
2464  #### `cudaMemcpy` 和 `cudaMallocManaged` 的本质区别
2465  
2466  使用 `cudaMemcpy` 时，数据是“复制 + 粘贴”：
2467  
2468  - 物理存在：拷贝完成后，CPU 内存（地址 `A`）和 GPU 显存（地址 `devA`）中各有一份完整的数据副本。
2469  - 独立性：如果随后在 CPU 上修改了 `A[0]`，GPU 上的 `devA[0]` 不会跟着变。它们是两个完全独立的物理实体。
2470  - LLM 场景应用：在加载大模型权重时，通常把权重从主存（RAM）拷贝到显存。
2471  
2472  
2473  
2474  
</code></pre>

<a id="log-2026-04-29"></a>
### 2026-04-29

Source lines: `2475-2577`

<pre class="tech-log-source"><code>
2475  # 2026-04-29
2476  
2477  ## RoPE
2478  
2479  $n$ 是动力源： 随着 $n$ 的增加（即 Token 越来越靠后），旋转的角度 $n\theta_i$ 就会越来越大。
2480  
2481  
2482  
2483  刚才不是说越大，频率越低，角度越小吗
2484  
2485  这是个非常棒的观察！这里其实涉及两个不同的变量在“赛跑”，你的直觉敏锐地捕捉到了它们的矛盾点。
2486  
2487  我们要区分 位置 n 和 频率 θ 
2488  i
2489  ​
2490    对最终角度的贡献：
2491  
2492  1. 核心公式：角度 = 位置 × 频率
2493  旋转的角度公式是：
2494  
2495  Angle=n×θ 
2496  i
2497  ​
2498   
2499  这里有两个变量：
2500  
2501  n (位置索引)：指 Token 是第几个（0,1,2,…）。
2502  
2503  θ 
2504  i
2505  ​
2506    (频率)：指某个维度旋转的“步长”（由 inv_freq 决定）。
2507  
2508  2. 回答你的疑问：为什么你觉得“矛盾”？
2509  你说的“越大越小”是指维度 i 越大，频率 θ 
2510  i
2511  ​
2512    越小：
2513  
2514  在 高维度（i 很大时），频率 θ 
2515  i
2516  ​
2517    极其微小（比如 0.0001）。
2518  
2519  这意味着在这个维度上，位置 n 每增加 1，角度只增加一点点。
2520  
2521  但我说的“越大越大”是指位置 n 增加时，角度会变大：
2522  
2523  即使频率 θ 
2524  i
2525  ​
2526    很小（比如 0.0001），当位置 n 从 1 变成 10000 时，角度也会从 0.0001 变成 1.0。
2527  
2528  3. 用“时钟”类比（解决你的困惑）
2529  想象一个时钟，里面有秒针、分针和时针。它们代表了不同的维度 i。
2530  
2531  频率 θ 
2532  i
2533  ​
2534   （由维度决定）：
2535  
2536  秒针：频率最高（转得最快）。
2537  
2538  时针：频率最低（转得最慢，也就是你说的“维度越大，频率越低”）。
2539  
2540  位置 n（动力源）：
2541  
2542  n 就是流逝的时间。
2543  
2544  随着时间 n 的流逝，所有的针都在往前转，角度都在变大。
2545  
2546  重点来了：
2547  
2548  当 n 增加时（时间流逝），秒针转得飞快，很快就转满一圈回到原点（容易产生你之前担心的“碰撞”）。
2549  
2550  当 n 增加时，时针转得极慢。虽然它的角度也在变大，但它转得很稳，能区分非常遥远的时间点。
2551  
2552  4. 总结：到底谁大谁小？
2553  变量增加	对频率的影响	对角度 (nθ 
2554  i
2555  ​
2556   ) 的影响	物理意义
2557  维度 i 变大	变小	变小	旋转步长变短（从秒针变成时针）
2558  位置 n 变大	无关	变大	随着 Token 靠后，总旋转量累积
2559  你的困惑点在于： 你把“维度带来的频率衰减”和“位置带来的角度累加”搞混了。
2560  
2561  维度决定了这根针转得有多快。
2562  
2563  位置决定了这根针转了多久。
2564  
2565  所以，在同一个维度下，Token 越靠后（n 越大），角度肯定越大；但在同一个位置下，维度越高，旋转的角度反而越小。
2566  
2567  
2568  你现在能理解为什么 NTK-aware Scaling 很有用了：
2569  当我们想把上下文从 2k 扩展到 8k 时，如果我们直接把所有维度都“调慢”（位置内插），那么原本就很快的高频维度变慢了，会导致模型在短距离内的分辨精度下降（模型变糊了）。
2570  
2571  所以聪明的做法是：保持高频维度不动，只把那些本来就很慢的低频维度变得更慢。 这样既保住了“近视”的清晰度，又获得了“远视”的广度。
2572  
2573  现在的逻辑是不是彻底闭环了？低频维度在短距离确实“废”，但它们是为长跑而生的。
2574  
2575  
2576  
2577  
</code></pre>

<a id="log-2026-04-30"></a>
### 2026-04-30

Source lines: `2578-2594`

<pre class="tech-log-source"><code>
2578  # 2026-04-30
2579  
2580  ## 关于推理框架
2581  
2582  我们两个小时的组会讨论了各个主流的推理框架  
2583  我们排除了OmniInfer、ChiTu  
2584  最终，决定在vLLM、vLLM-Ascend、SGLang-Ascend、xLLM中选取  
2585  
2586  
2587  ## 港中深新生见面会
2588  
2589  七八个新的志同道合者  
2590  受益！  
2591  
2592  
2593  
2594  
</code></pre>

<a id="log-2026-05-01"></a>
### 2026-05-01

Source lines: `2595-2606`

<pre class="tech-log-source"><code>
2595  # 2026-05-01
2596  
2597  ## GPU操作
2598  
2599  Gather  
2600  All-Gather  
2601  Reduce  
2602  All-Reduce  
2603  Reduce-Scatter  
2604  All-to-All  
2605  
2606  
</code></pre>

<a id="log-2026-05-04"></a>
### 2026-05-04

Source lines: `2607-2646`

<pre class="tech-log-source"><code>
2607  # 2026-05-04
2608  
2609  ## vLLM 工程边界与目录地图
2610  
2611  理解 vLLM，先不要盯住某个 kernel；先看它把 serving runtime 切成了哪些稳定边界。
2612  
2613  | 层次 | 关键文件 | 主要契约 | 为什么关键 |
2614  | --- | --- | --- | --- |
2615  | 用户入口 | [`v1/engine/llm_engine.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) | 请求规范化、输出回组装 | 把 API 面和 runtime 面隔开 |
2616  | EngineCore | [`v1/engine/core.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) | `add_request()` / `step()` 主循环 | 是 V1 runtime 总装点 |
2617  | Scheduler | [`v1/core/sched/scheduler.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) | 本轮谁前进、前进多少、是否抢占 | continuous batching 的真正核心 |
2618  | KV 系统 | [`v1/core/kv_cache_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py)、[`v1/core/block_pool.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/block_pool.py) | prefix hit、slot 分配、block 生命周期 | PagedAttention 的系统收益都在这里释放 |
2619  | 协议对象 | [`v1/request.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/request.py)、[`v1/core/sched/output.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py) | Request、SchedulerOutput、status 字段 | feature 越多，越要靠协议对象稳住边界 |
2620  | Worker / ModelRunner | [`v1/worker/gpu/model_runner.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py)、[`v1/worker/gpu/input_batch.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py) | 把 scheduler output 变成设备输入批次 | 调度和算子之间的翻译层 |
2621  | Attention backend | [`v1/attention/backend.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/backend.py)、[`v1/attention/selector.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/selector.py) | backend 选择、metadata 协议 | attention 不是单函数而是一套派发体系 |
2622  | Paged Attention 执行 | [`v1/attention/ops/paged_attn.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/attention/ops/paged_attn.py)、[`v1/worker/gpu/block_table.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/block_table.py) | block table、slot mapping、decode 访存路径 | 把 block 化 KV 变成真实执行 |
2623  | 编译与图执行 | [`compilation/cuda_graph.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/cuda_graph.py)、[`compilation/passes/pass_manager.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/compilation/passes/pass_manager.py) | capture/replay、pass 重写、runtime wrapper | 压低 decode 高频小步固定开销 |
2624  | 执行器与分布式 | [`v1/executor/abstract.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/executor/abstract.py)、[`distributed/parallel_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/parallel_state.py) | 单进程/多进程/Ray、TP/EP/CP 进程组 | 把单卡 runtime 拉成服务系统 |
2625  | Connector / 外部缓存 | [`distributed/kv_transfer/kv_connector/base.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/kv_transfer/kv_connector/base.py)、[`distributed/ec_transfer/ec_transfer_state.py`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/distributed/ec_transfer/ec_transfer_state.py) | KV/encoder cache 搬运协议 | disaggregated serving 的关键拼图 |
2626  
2627  
2628  
2629  ## 一次请求在 vLLM 里如何被推进
2630  
2631  把一条请求主链拉直之后，很多“为什么快”都会落回同一条控制流。
2632  
2633  1. 用户请求经 [`LLMEngine`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/llm_engine.py) 标准化，形成 engine request。
2634  2. [`EngineCore.add_request()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 把请求交给 runtime，进入 waiting queue。
2635  3. [`EngineCore.step()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/engine/core.py) 驱动一轮 scheduler + executor 主循环。
2636  4. [`Scheduler.schedule()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/scheduler.py) 计算该请求本轮还能前进多少 token。
2637  5. [`KVCacheManager.get_computed_blocks()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 查 prefix hit，再由 [`allocate_slots()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/kv_cache_manager.py) 申请 block。
2638  6. Scheduler 产出 [`SchedulerOutput`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/core/sched/output.py)，executor 把它下发到 worker。
2639  7. [`GPUModelRunner.prepare_inputs()`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/model_runner.py) 构造 [`InputBatch`](https://github.com/vllm-project/vllm/blob/92a7c121b62a1484b68c0a27d1ecefd1a84f78fc/vllm/v1/worker/gpu/input_batch.py)，再由 `prepare_attn()` 拼出 block tables 和 slot mappings。
2640  8. `model_state.prepare_attn()` 与 attention backend 生成 metadata，按 full graph / piecewise / eager 路径执行模型。
2641  9. `sample()` 或 rejection sampler 产出 token，`postprocess()` 更新 host/device 两侧状态镜像。
2642  10. output processor 把底层 token 流整理成用户侧可见结果。
2643  
2644  
2645  
2646  
</code></pre>

<a id="log-2026-05-05"></a>
### 2026-05-05

Source lines: `2647-2818`

<pre class="tech-log-source"><code>
2647  # 2026-05-05  
2648  
2649  分层 AllReduce + SHARP合在一起的真实执行路径讲清楚，并给一个具体数值例子。重点关注：哪一步在节点内做、哪一步跨节点、谁在算、谁在发。
2650  
2651  场景设定（例子）
2652  2 个节点（Node A / Node B）
2653  每个节点 4 张 GPU（共 8 张）
2654  每张 GPU 有数据大小 B = 8 MB
2655  网络：
2656  节点内：NVLink / NVSwitch（很快）
2657  节点间：InfiniBand + SHARP（较慢但可做网络内归约）
2658  总体流程（一句话）
2659  
2660  先在节点内“压缩”（AllReduce），再把“压缩结果”交给交换机做全局归约，最后再分发回节点内。
2661  
2662  Step 1️⃣ 节点内 AllReduce（intra-node）⚡
2663  
2664  在 Node A 内（4 张 GPU）：
2665  
2666  用 NCCL 做一次 AllReduce
2667  Node B 同样做一遍
2668  
2669  结果：
2670  
2671  Node A 的每张 GPU 都拿到：A 节点的归约结果（8 MB）
2672  Node B 同理
2673  
2674  👉 这里通信量确实是 B×N = 8MB × 4 = 32MB（节点内）
2675  但因为 NVLink 很快，这一步不是瓶颈
2676  
2677  Step 2️⃣ 选“代表”参与跨节点 🌐
2678  
2679  每个节点选一个“代表”（通常是一个 GPU 或 NIC）：
2680  
2681  Node A：选 GPU0
2682  Node B：选 GPU0
2683  
2684  👉 注意：
2685  不再是 4 张 GPU 都出去通信，而是每个节点只出 1 份数据
2686  
2687  Step 3️⃣ GPU → 交换机（上行）⬆️
2688  Node A 的代表发送 8 MB
2689  Node B 的代表发送 8 MB
2690  
2691  👉 跨节点总发送：
2692  
2693  每节点只发 B = 8MB
2694  而不是 B×N = 32MB
2695  Step 4️⃣ 交换机内做 Reduce（SHARP 核心）🧠
2696  
2697  在支持 SHARP 的交换机里（由 NVIDIA 网络实现）：
2698  
2699  收到来自 Node A / B 的数据
2700  直接在交换机 ASIC 里做：
2701  result = A + B
2702  
2703  👉 这一步原本是在 GPU 上做的，现在搬到网络里
2704  
2705  Step 5️⃣ 交换机 → GPU（下行，多播）⬇️
2706  交换机把结果（8 MB）广播回：
2707  Node A 的代表
2708  Node B 的代表
2709  Step 6️⃣ 节点内广播（intra-node broadcast）🔁
2710  
2711  在每个节点内部：
2712  
2713  代表 GPU 把结果发给本节点其他 GPU（NVLink）
2714  
2715  最终：
2716  
2717  所有 8 张 GPU 都拿到全局 AllReduce 结果（8 MB）
2718  📊 对比数据量（关键）
2719  ❌ 不用分层 + 不用 SHARP
2720  
2721  跨节点：
2722  
2723  4 张 GPU × 8MB = 32MB / 节点
2724  ✅ 分层 + SHARP
2725  
2726  跨节点：
2727  
2728  每节点只发 8MB
2729  
2730  👉 直接减少 4 倍（= N）
2731  
2732  🧠 直觉总结
2733  
2734  把整个过程想成“三段式”：
2735  
2736  ① 节点内（快）
2737  
2738  “我们自己先算好一个结果”
2739  
2740  ② 网络（SHARP）
2741  
2742  “交换机帮我们把各节点结果再合并”
2743  
2744  ③ 节点内（快）
2745  
2746  “把最终答案发给自己人”
2747  
2748  🔥 为什么这是大模型训练的标配
2749  
2750  在：
2751  
2752  Megatron-LM
2753  DeepSpeed
2754  大规模 DDP
2755  
2756  中都会这样做，因为：
2757  
2758  NVLink 带宽 ≫ IB 带宽
2759  跨节点才是瓶颈
2760  SHARP 能进一步减少 GPU 参与通信
2761  一句话总结
2762  
2763  分层 AllReduce 负责减少“谁跨节点通信”，SHARP 负责减少“通信时谁做归约 + 几轮通信”，两者结合把跨节点流量从 B×N 降到 B，并减少一轮计算/通信。
2764  
2765  
2766  
2767  4️⃣ 总体时间模型（关键）
2768  
2769  可以写成：
2770  
2771  不分层：
2772  T = T_slow(BN)
2773  
2774  分层 + SHARP：
2775  T = T_fast(BN) + T_slow(B)
2776  
2777  
2778  
2779  ## 不同的并行方式
2780  
2781  ### ColumnParallelLinear: 
2782  **按照列维度分开。 某个GPU计算完后，结果的*某个维度*是*最终结果*，但是某GPU只有这些局部维度的信息。所以最后通过通讯来收集别的GPU结果**
2783  
2784  ### RowParallelLinear:
2785  **按照行维度分开。 某个GPU计算完后，有*每个*维度的信息，但是完整的维度上，都不是最终结果。所以最后*每个维度都*要再与来自其他GPU的中间信息进行计算，得到最终结果**
2786  
2787  
2788    ┌────────────────────────────┬─────────────┬──────────┬──────────────────────────┬────────────┬────────────────────┐
2789    │             类             │  切哪一维   │ 输入状态 │         输出状态         │    通信    │      放在哪里      │
2790    ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
2791    │ ReplicatedLinear           │ 不切        │ 完整     │ 完整                     │ 无         │ 非并行场景或小矩阵 │
2792    ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
2793    │ ColumnParallelLinear       │ out (dim 0) │ 完整     │ 切开                     │ 无         │ 一段计算的入口     │
2794    ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
2795    │ RowParallelLinear          │ in (dim 1)  │ 切开     │ 完整（需 all-reduce）    │ all-reduce │ 一段计算的出口     │
2796    ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
2797    │ MergedColumnParallelLinear │ out (dim 0) │ 完整     │ 切开（由多个子矩阵拼成） │ 无         │ gate+up 合并       │
2798    ├────────────────────────────┼─────────────┼──────────┼──────────────────────────┼────────────┼────────────────────┤
2799    │ QKVColumnParallelLinear    │ out (dim 0) │ 完整     │ 切开（Q/K/V 三段）       │ 无         │ attention 的 QKV   │
2800    └────────────────────────────┴─────────────┴──────────┴──────────────────────────┴────────────┴────────────────────┘
2801  ```
2802  
2803  ```在 Megatron-LM / vLLM 中典型结构：
2804  X
2805   │
2806   ├── ColumnParallel + Merged (QKV / MLP expand)
2807   │
2808   ▼
2809   attention / activation
2810   │
2811   ├── RowParallel
2812   ▼
2813   Y
2814  ```
2815  
2816  
2817  
2818  
</code></pre>

<a id="log-2026-05-07"></a>
### 2026-05-07

Source lines: `2819-2820`

<pre class="tech-log-source"><code>
2819  # 2026-05-07
2820  I can do this all day ...   
</code></pre>

<a id="log-2026-05-08"></a>
### 2026-05-08

Source lines: `2821-2822`

<pre class="tech-log-source"><code>
2821  # 2026-05-08  
2822  赶路到广州    
</code></pre>

<a id="log-2026-05-09"></a>
### 2026-05-09

Source lines: `2823-2824`

<pre class="tech-log-source"><code>
2823  # 2026-05-09  
2824  毕业照  
</code></pre>

<a id="log-2026-05-10"></a>
### 2026-05-10

Source lines: `2825-2830`

<pre class="tech-log-source"><code>
2825  # 2026-05-10  
2826  赶路到深圳  
2827  
2828  
2829  
2830  
</code></pre>

<a id="log-2026-05-11"></a>
### 2026-05-11

Source lines: `2831-3015`

<pre class="tech-log-source"><code>
2831  # 2026-05-11
2832  
2833  ## FSDP / ZeRO-3 和张量并行 TP 的区别
2834  
2835    FSDP：切“模型状态”，主要为了省显存
2836    TP：切“单层计算”，主要为了让多卡一起算一个大矩阵
2837  
2838    更具体地说：
2839  
2840    | 对比点 | FSDP / ZeRO-3 | 张量并行 TP |
2841    |---|---|---|
2842    | 切什么 | 参数、梯度、优化器状态 | 线性层/注意力层里的大矩阵 |
2843    | 激活怎么切 | 通常按 batch/token 切 | 通常按 hidden dim / intermediate dim 切 |
2844    | 每张卡算什么 | 每张卡处理不同 batch 数据 | 多张卡一起算同一个 token 的同一层 |
2845    | 主要目的 | 降低显存占用 | 降低单卡计算量，并让超大层能并行计算 |
2846    | 通信内容 | 主要通信权重/梯度 | 主要通信激活/中间结果 |
2847    | 常见通信 | AllGather 参数，ReduceScatter 梯度 | AllGather 激活，ReduceScatter 或 AllReduce 输出 |
2848    | 对模型结构的侵入 | 相对低 | 较高，需要改 Linear/Attention 的实现 |
2849  
2850    举个线性层例子：
2851  
2852    Y = X @ W
2853  
2854    假设：
2855  
2856    X: [B, D]
2857    W: [D, F]
2858    Y: [B, F]
2859  
2860    FSDP 的思路
2861  
2862    每张卡存一部分 W，但真正算这一层时，会先把完整 W 收集回来：
2863  
2864    平时：
2865    GPU0: W 第 0 片
2866    GPU1: W 第 1 片
2867    GPU2: W 第 2 片
2868    GPU3: W 第 3 片
2869  
2870    计算前：
2871    AllGather -&gt; 每张卡临时拿到完整 W
2872  
2873    计算时：
2874    GPU0 算 batch 第 0 份
2875    GPU1 算 batch 第 1 份
2876    GPU2 算 batch 第 2 份
2877    GPU3 算 batch 第 3 份
2878  
2879    所以 FSDP 本质上还是偏 数据并行：每张卡处理不同数据，只是参数平时不完整保存。
2880  
2881    TP 的思路
2882  
2883    每张卡不收集完整 W，而是真的只用自己那片 W 参与计算：
2884  
2885    GPU0: W[:, 0:F/4]      -&gt; 算 Y[:, 0:F/4]
2886    GPU1: W[:, F/4:F/2]    -&gt; 算 Y[:, F/4:F/2]
2887    GPU2: W[:, F/2:3F/4]   -&gt; 算 Y[:, F/2:3F/4]
2888    GPU3: W[:, 3F/4:F]     -&gt; 算 Y[:, 3F/4:F]
2889  
2890    最后再通过通信把结果拼起来或规约。
2891  
2892    所以 TP 是真正把 一个矩阵乘法拆开计算。
2893  
2894    一个简单类比：
2895  
2896    FSDP：
2897    书太大，每个人平时只背几章。
2898    要读某一页时，大家临时把整本书凑出来，各自读自己的题。
2899  
2900    TP：
2901    一道题太大，一个人算不完。
2902    大家每人算这道题的一部分，最后合并答案。
2903  
2904  
2905  ## narrow
2906  
2907  narrow 是 PyTorch 里用来沿某一个维度取连续切片的方法。
2908  
2909    你的代码：
2910  
2911    sliced_weight = loaded_weights.narrow(0, start_index, shard_size)
2912  
2913    意思是：
2914  
2915    从 loaded_weights 的第 0 维开始切
2916    起点是 start_index
2917    长度是 shard_size
2918  
2919    等价于常见切片：
2920  
2921    sliced_weight = loaded_weights[start_index : start_index + shard_size]
2922  
2923    如果写完整一点：
2924  
2925    loaded_weights.narrow(dim, start, length)
2926  
2927    参数含义是：
2928  
2929    dim: 沿哪个维度切
2930    start: 从这个维度的哪个下标开始
2931    length: 取多少个元素
2932  
2933  
2934  ## slided_weight = loaded_weights.narrow(0, start_index, shard_size)
2935  
2936  slided_weight 不是“纯指针”，而是一个 Tensor 视图（view）对象。
2937  
2938    可以粗略理解成：
2939  
2940    slided_weight = 指向原始数据的一张“切片窗口”
2941  
2942    它本身是个 Tensor，带着：
2943  
2944    - 数据在哪
2945    - 形状是多少
2946    - 从原始 loaded_weights 的哪一段开始看
2947    - 步长怎么走
2948  
2949    但它通常不拷贝底层数据。
2950  
2951    例如：
2952  
2953    slided_weight = loaded_weights.narrow(0, start_index, shard_size)
2954  
2955    这里 slided_weight 和 loaded_weights 共享同一块底层存储，只是 slided_weight 只看其中一部分。
2956  
2957    所以你可以把它理解成：
2958  
2959    - 不是新开一份完整内存
2960    - 也不是 C 语言里那种裸指针
2961    - 更像“带形状信息的视图引用”
2962  
2963    真正把数据写进本地参数的是：
2964  
2965    param_data.copy_(slided_weight)
2966  
2967    这一步才发生拷贝。
2968  
2969    一句话：
2970  
2971    slided_weight 不是数据副本，而是原 tensor 上的一个切片视图。
2972  
2973  
2974  ## offset：
2975  
2976  offset = sum(self.output_sizes[:loaded_weight_id]) // self.tp_size ，// self.tp_size是什么作用
2977  
2978  // self.tp_size 的作用是：
2979  
2980    把“完整大矩阵里的偏移量”换算成“当前 rank 本地分片里的偏移量”。
2981  
2982    ———
2983  
2984    假设：
2985  
2986    output_sizes = [4096, 4096, 4096]
2987    tp_size = 4
2988  
2989    完整合并矩阵是：
2990  
2991    [ q: 4096 行 ][ k: 4096 行 ][ v: 4096 行 ]
2992  
2993    如果现在加载 k，也就是：
2994  
2995    loaded_weight_id = 1
2996  
2997    完整矩阵里的偏移是：
2998  
2999    sum(output_sizes[:1]) = 4096
3000  
3001    也就是 k 在完整大矩阵里从第 4096 行开始。
3002  
3003    但是当前 rank 本地只保存每个子矩阵的 1/4：
3004  
3005    rank 本地矩阵:
3006    [ q shard: 1024 行 ][ k shard: 1024 行 ][ v shard: 1024 行 ]
3007  
3008    所以 k 在本地矩阵里的起点不是 4096，而是：
3009  
3010    4096 // 4 = 1024
3011  
3012  
3013  
3014  
3015    
</code></pre>

<a id="log-2026-05-12"></a>
### 2026-05-12

Source lines: `3016-3022`

<pre class="tech-log-source"><code>
3016  # 2026-05-12
3017  
3018  ## mini-vllm 源码完结！
3019  
3020  前海湾公园的海与落日很美 ...
3021  
3022  
</code></pre>

<a id="log-2026-05-13"></a>
### 2026-05-13

Source lines: `3023-3068`

<pre class="tech-log-source"><code>
3023  # 2026-05-13
3024  
3025  ## 尝试启动 DeepSeek V4 Flash 的推理服务
3026  
3027  
3028  ## 1. 可用模型与硬件资源
3029  
3030  ### 可用模型版本（/models/share/）
3031  
3032  | 模型 | 路径 | 量化/精度 | 架构 | 推理框架 | 最低 NPU 需求 | 能否直接跑 |
3033  |------|------|----------|------|---------|-------------|-----------|
3034  | **DeepSeek-V4-Flash (W8A8)** | `DeepSeek-V4-Flash-w8a8-mtp/` | W8A8 Ascend 量化 | 43层/4096d/256专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
3035  | **DeepSeek-V4-Flash (compressed-tensors)** | `deepseek-v4-flash-mtp/` | W8A8 compressed-tensors | 同上 | vLLM-Ascend | 32 NPU (2节点x16) | 改 MODEL_PATH + quantization 参数即可 |
3036  | DeepSeek-V4-Flash (BF16) | `DeepSeek-V4-Flash-bf16/` | BF16 原始精度 | 同上 | 自研 NPU 推理脚本 | 1 NPU（单卡验证） | adaption_test/ 下有 quick_verify.py |
3037  | **DeepSeek-V4-Pro** | `DeepSeek-V4-Pro-w4a8-mtp/` | W4A8 Ascend 量化 | 61层/7168d/384专家 | vLLM-Ascend | 32 NPU (2节点x16) | 有现成 yaml，直接跑 |
3038  | DeepSeek-R1-Distill-Qwen-1.5B | `DeepSeek-R1-Distill-Qwen-1.5B/` | BF16 | Qwen2 28层/1536d | vLLM-Ascend | 1 NPU | 有现成 yaml，直接跑 |
3039  | DeepSeek-V4-Flash-Base (BF16) | `DeepSeek-V4-Flash-Base-bf16/` | BF16 | 同 Flash | 无推理脚本 | — | 不适合评测（base 模型，无 instruct 对齐） |
3040  
3041  所有 V4 模型均为 MoE 架构，支持最大 1M token 上下文（max_position_embeddings=1048576），使用 YaRN RoPE 扩展。
3042  
3043  ### 可用 NPU 资源
3044  
3045  | 队列 | 类型 | 配额 (NPU) | 物理规格 | 状态 |
3046  |------|------|-----------|---------|------|
3047  | user-1-wangakang-compute | 个人 | 8 | 8卡 x 2chip = 16 Ascend910 chip | ok |
3048  | project-ascend-fit-wangakang | 项目 | 52 | 52卡 x 2chip = 104 Ascend910 chip | ok |
3049  
3050  硬件说明：每张 Ascend910 物理卡包含 2 个 AI 处理器（chip），每 chip 64GB HBM。ktp 调度以&quot;NPU&quot;（物理卡）为单位。vLLM 的 `--tensor-parallel-size` 等参数也以 NPU（卡）为单位。
3051  
3052  总计可用：**60 NPU**（个人 8 + 项目 52）。
3053  
3054  尝试使用镜像启动：镜像拉取失败。  
3055  尝试手动配置。
3056  
3057  ## 河套学院晟腾课程
3058  
3059  ### 关于 Linux 命令操作 ...
3060  
3061  在我们的个人 docker 运行实验
3062  
3063  ### Kerminal 自动适配部署大模型 
3064  
3065  跑了90分钟，最后还是成功了！ 
3066  
3067  
3068  
</code></pre>

<a id="log-2026-05-14"></a>
### 2026-05-14

Source lines: `3069-3082`

<pre class="tech-log-source"><code>
3069  # 2026-05-14
3070  
3071  ## 手动配置一天的 DeepSeek V4 环境
3072  
3073  各种包依赖、环境冲突、未更新问题  
3074  最棘手的是环境不支持  
3075  
3076  ## 结束所有 LeetGPU Easy 题目！
3077  
3078  感觉还行。  
3079  但是 Medium 题目一下就难起来了。  
3080  
3081  
3082  
</code></pre>

<a id="log-2026-05-15"></a>
### 2026-05-15

Source lines: `3083-3113`

<pre class="tech-log-source"><code>
3083  # 2026-05-15
3084  
3085  ## 河套学院晟腾课程
3086  
3087  使用 Kerminal 写算子。  
3088  讨论了关于文件目录。  
3089  
3090  ### 讨论了部署需求
3091  
3092  - **Flash (W8A8)**: 2 节点 x 16 NPU = 32 NPU（TP=8, DP=2, Expert Parallel）— **最低要求，不可降低**
3093  - **Pro (W4A8)**: 2 节点 x 16 NPU = 32 NPU（TP=16, DP=2, Expert Parallel）
3094  - **R1-Distill-1.5B**: 1 NPU 即可
3095  - **Flash BF16 单卡验证**: 1 NPU（adaption_test，max_seq_len=2048）
3096  
3097  注意：经实测验证，Flash W8A8 模型在单节点 16 NPU 上无论 TP=8+DP=2 还是 TP=16 均会 OOM。必须使用双节点 32 NPU 部署。当集群只有一个 16-NPU 节点空闲时无法启动。
3098  
3099  项目队列 52 NPU 足够同时部署 Flash + 留余量做其他实验。
3100  
3101  
3102  ## 尝试使用现有配置启动 DS v4
3103  
3104  ### 当前阻塞问题（2026-05-16）
3105  
3106  经过多轮实测，发现以下问题：
3107  
3108  1. **镜像兼容性**：`qwen3_5-v0-a3` 镜像的 transformers 不认识 `deepseek_v4` 架构，必须用 `deepseekv4-a3` 镜像
3109  2. **单节点 OOM**：16 NPU 单节点无论 TP=8+DP=2 还是 TP=16 均 OOM，必须双节点
3110  3. **vLLM-Ascend bug**：双节点 DP=2 跨节点部署时，worker 在 KV cache 初始化阶段报 `AttributeError: &#x27;list&#x27; object has no attribute &#x27;merge&#x27;`（kv_cache_spec_values 类型错误）
3111  
3112  
3113  
</code></pre>

<a id="log-2026-05-16"></a>
### 2026-05-16

Source lines: `3114-3385`

<pre class="tech-log-source"><code>
3114  # 2026-05-16
3115  
3116  ## DeepSeek V4 Flash W8A8 部署总结
3117  
3118  ### 今日结论
3119  
3120  - 任务 1058 已成功启动，服务地址为 `http://10.250.193.147:8005`。
3121  - 当前唯一验证过的可用配置是 cdy 的原版配置：`/models/share/task/cdy/deepseek-v4-flash.yaml`。
3122  - 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
3123  - 启动前必须在 `/vllm-workspace/vllm` 中应用 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
3124  - 单节点 16 NPU 可以跑通 DeepSeek V4 Flash W8A8，配置为 DP=2、TP=8、Expert Parallel。
3125  - CPU 内存需要 1000Gi，CPU 需要 500 核。
3126  
3127  ### 立即可做
3128  
3129  按照 `deepseek-v4-reasoning-eval.md` 中的测试矩阵，继续进行 DeepSeek V4 Flash 性能测试。
3130  
3131  ### 后续学习任务
3132  
3133  1. **服务器 NPU 资源调度**
3134  
3135     管理员解释：提交任务后，调度系统会分配空闲节点。每个节点有 16 张 910 显卡，不同节点已有的镜像缓存不同，这会影响是否需要重新拉镜像。
3136  
3137     后续需要进一步理解服务器节点运行方式、节点间通信和并行配置。可参考：
3138  
3139     - 网络基础说明：https://lqhl.github.io/scaling-book/gpus/#%E7%BD%91%E7%BB%9C
3140     - 配置脚本：`/models/share/task/cdy/start_dsv4.sh`
3141     - 本文档附录中的 NPU 集群调度方案
3142  
3143  2. **服务器集群镜像系统**
3144  
3145     关于“镜像拉取慢”的问题，需要学习服务器集群的镜像系统：https://luoss.nilpo.app/guide/image-storage。
3146  
3147     管理员建议先上传镜像到公开镜像池。上传完成后，服务器内部拉取镜像和模型权重都会明显变快：拉镜像约 10 秒，否则可能需要 10 分钟以上。
3148  
3149  ### 后续优化方向
3150  
3151  1. 管理员提到自己曾跑通过 SGLang，后续可以尝试用 SGLang 启动 DeepSeek V4 Flash。
3152  
3153  2. 管理员提到开源项目 [DFlash: Block Diffusion for Flash Speculative Decoding](https://github.com/z-lab/dflash)。该项目能显著提高解码速度，但目前似乎只能本机运行，不一定适合直接对外提供推理服务。后续可以考虑基于它改进 vLLM / SGLang 框架。
3154  
3155  ## 最终成功配置
3156  
3157  **任务 1058**：使用 cdy 的原版配置成功启动。
3158  
3159  | 项目 | 值 |
3160  | --- | --- |
3161  | yaml | `/models/share/task/cdy/deepseek-v4-flash.yaml` |
3162  | 镜像 | `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3` |
3163  | 节点 | atlas-19（单节点 16 NPU） |
3164  | 配置 | DP=2, TP=8, Expert Parallel |
3165  | 端口 | 8005 |
3166  | 模型名 | deepseek-v4-flash |
3167  | max_model_len | 524288 |
3168  | 关键步骤 | 启动前先 `git apply` patch 到 `/vllm-workspace/vllm` |
3169  
3170  ## 这两天遇到的问题
3171  
3172  ### 1. 镜像不支持 `deepseek_v4` 架构
3173  
3174  **现象**：`The checkpoint has model type deepseek_v4 but Transformers does not recognize this architecture`
3175  
3176  **原因**：`qwen3_5-v0-a3` 和 `deepseekv4-a3` 镜像中的 transformers 库版本不包含 `deepseek_v4` 模型类型注册。
3177  
3178  **解决方案**：使用 `v0.13.0rc3-a3` 镜像 + cdy 脚本中的 `git apply` patch。patch 位于 `/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`，它会修改 vLLM 代码，注册 `deepseek_v4` 相关组件。该镜像中的 vLLM 版本（v0.13）对 `model_type` 的检查逻辑与新版不同，patch 后即可通过。
3179  
3180  ### 2. `tool-call-parser deepseek_v4` 不支持
3181  
3182  **现象**：`invalid tool call parser: deepseek_v4`
3183  
3184  **原因**：`qwen3_5-v0-a3` 镜像的 vLLM 版本（v0.16.0rc2）不包含 `deepseek_v4` tool parser。
3185  
3186  **解决方案**：
3187  
3188  - 方案 A：使用 `v0.13.0rc3-a3` 镜像 + patch（cdy 方案，已验证）
3189  - 方案 B：去掉 `--tool-call-parser` 和 `--reasoning-parser` 参数（性能测试不需要）
3190  
3191  ### 3. `speculative-config deepseek_mtp` 不支持
3192  
3193  **现象**：`Unsupported speculative method: &#x27;mtp&#x27;`
3194  
3195  **原因**：`deepseekv4-a3` 镜像的 vLLM 版本不支持 MTP 投机解码。
3196  
3197  **解决方案**：去掉 `--speculative-config` 参数，或使用 `v0.13.0rc3-a3` 镜像（支持 MTP）。
3198  
3199  ### 4. 单节点 16 NPU DP=2 TP=8 OOM（`deepseekv4-a3` 镜像）
3200  
3201  **现象**：Worker 进程被 terminated，报错 `WorkerProc was terminated`。
3202  
3203  **原因**：`deepseekv4-a3` 镜像的 vLLM 版本内存管理效率较低，DP=2 在单节点上 OOM。
3204  
3205  **解决方案**：使用 `v0.13.0rc3-a3` 镜像（vLLM v0.13 内存管理更高效），并分配 1000Gi CPU 内存。cdy 配置证明同样的 DP=2 TP=8 单节点 16 NPU 可以跑通。
3206  
3207  ### 5. 双节点调度失败
3208  
3209  **现象**：Worker pod 一直 Pending，无法分配第二个 16-NPU 节点。
3210  
3211  **原因**：集群中空闲的 16-NPU 节点不足两个。
3212  
3213  **解决方案**：使用单节点配置（cdy 方案证明可行）。
3214  
3215  ### 6. `deepseekv4-a3` 镜像双节点 KV cache bug
3216  
3217  **现象**：`AttributeError: &#x27;list&#x27; object has no attribute &#x27;merge&#x27;`
3218  
3219  **原因**：`deepseekv4-a3` 镜像中 vLLM-Ascend 的 KV cache 初始化代码在跨节点 DP 模式下有 bug。
3220  
3221  **解决方案**：不使用该镜像，改用 `v0.13.0rc3-a3` 镜像。跨节点 DP 模式相关配置还需要进一步学习，尤其是 `/models/share/task/cdy/start_dsv4pro-worker.sh` 中的参数。
3222  
3223  ### 7. `cd vllm-ascend` 路径问题
3224  
3225  **现象**：`cd: vllm-ascend: No such file or directory`
3226  
3227  **原因**：不同镜像的工作目录不同。
3228  
3229  **解决方案**：cdy 的脚本直接 `cd &quot;$VLLM_REPO&quot;`（即 `/vllm-workspace/vllm`），不需要进入 `vllm-ascend`。
3230  
3231  ### 8. 镜像拉取慢
3232  
3233  **现象**：Pod 长时间 Pending（10-20 分钟）。
3234  
3235  **原因**：`deepseekv4-a3` 和 `v0.13.0rc3-a3` 镜像在部分节点上没有缓存。
3236  
3237  **解决方案**：等待拉取完成，或多次提交，直到调度到已有缓存的节点。
3238  
3239  **管理员解决方案**：先上传镜像到公开镜像池，参考 https://luoss.nilpo.app/guide/image-storage。上传完成后，服务器内部拉取镜像和模型权重都会很快。
3240  
3241  ## 关键经验
3242  
3243  1. 正确镜像是 `quay.io/ascend/vllm-ascend:v0.13.0rc3-a3`。
3244  2. 必须先打 patch：`/models/share/DeepSeek-V4-Flash/deepseek-v4-agentic-support.patch`。
3245  3. 单节点 16 NPU 可以跑，配置为 DP=2 TP=8，不需要双节点。
3246  4. CPU 内存需要 1000Gi，200Gi / 800Gi 不够。参考管理员方案：`/models/share/task/cdy/deepseek-v4-flash.yaml` 第 17、18 行。
3247  5. CPU 需要 500 核。
3248  6. cdy 的脚本（管理员方案）是唯一验证过的可用配置，后续所有版本都应以此为基础。
3249  
3250  ## 附录：NPU 集群现有调度方案
3251  
3252  本集群使用 **Kubernetes + Volcano 调度器** 管理 NPU 资源，并通过 `ktp` CLI 工具操作。
3253  
3254  ### 层级结构
3255  
3256  ```text
3257  集群 (K8s Cluster)
3258   └── 节点 (Node): atlas-1, atlas-18, atlas-19, atlas-39, atlas-40, atlas-41 ...
3259        └── 每个节点有 16 NPU（8 张物理卡 x 2 chip）
3260             └── 每张卡 64GB HBM
3261  
3262  用户通过 Queue（队列）获得 NPU 配额：
3263   ├── 个人队列: user-1-wangakang-compute (8 NPU)
3264   └── 项目队列: project-ascend-fit-wangakang (52 NPU)
3265  ```
3266  
3267  ### 调度流程
3268  
3269  1. **提交任务**：执行 `ktp submit -f job.yaml`。yaml 中指定 queue、npu 数量、镜像和启动命令，任务类型为 `acjob`（Ascend Computing Job）。
3270  2. **调度器分配节点**：Volcano 调度器根据队列配额和节点空闲情况分配资源，无法手动指定节点。请求 16 NPU 会分配一个完整节点；请求 32 NPU 需要两个空闲节点同时可用。
3271  3. **Pod 创建**：每个 task 对应一个 Pod。Pod 运行在分配的节点上，并挂载 `/models/` 共享存储。平台会自动生成 `hccl.json`，Pod 内的 `init_env.sh` 等待该文件就绪后设置 `MASTER_IP` 等环境变量。
3272  4. **分布式通信初始化**：单节点时，Pod 内所有 NPU 通过 HCCL（华为集合通信库）直接通信；多节点时，通过 `data-parallel-address`（`MASTER_IP`）跨节点 RPC 通信。
3273  5. **任务生命周期**：状态流转为 Pending -&gt; Running -&gt; Succeeded / Failed。`resumable_training.enabled: true` 时，失败会自动重试（最多 `fault_retry_times` 次）；`max_runtime_minutes` 到期后自动终止。
3274  
3275  ### yaml 配置与调度的关系
3276  
3277  ```yaml
3278  tasks:
3279    - name: master        # Pod 名称后缀
3280      replicas: 1         # 该角色的 Pod 数量
3281      cpu: &quot;500&quot;          # CPU 核数（影响调度，节点需有足够 CPU）
3282      memory: &quot;1000Gi&quot;    # 内存（影响调度，节点需有足够内存）
3283      npu: 16             # NPU 数量（决定分配几张卡/几个节点）
3284      command: &quot;...&quot;      # Pod 启动后执行的命令
3285    - name: worker        # 第二个 Pod（可选，用于多节点）
3286      replicas: 1
3287      npu: 16             # 又一个 16 NPU = 又一个完整节点
3288  ```
3289  
3290  ### 常用操作
3291  
3292  | 命令 | 作用 |
3293  | --- | --- |
3294  | `ktp queues` | 查看队列配额和使用情况 |
3295  | `ktp submit -f job.yaml` | 提交任务 |
3296  | `ktp list` | 列出所有任务 |
3297  | `ktp pods &lt;ID&gt;` | 查看任务的 Pod 状态和所在节点 |
3298  | `ktp logs &lt;ID&gt;` | 查看日志（默认最新 100 行） |
3299  | `ktp logs &lt;ID&gt; --follow` | 实时跟踪日志 |
3300  | `ktp stop &lt;ID&gt;` | 停止任务 |
3301  | `ktp restart &lt;ID&gt;` | 重启已停止的任务 |
3302  | `ktp watch &lt;ID&gt;` | 实时监控任务状态 |
3303  
3304  ### 注意事项
3305  
3306  - 不能指定调度到哪个节点，只能靠调度器自动分配。
3307  - 不同节点上可能缓存了不同版本的同名镜像（tag 相同但内容不同）。
3308  - 请求的 NPU 数量决定了需要几个节点：8 NPU = 半个节点，16 NPU = 一个节点，32 NPU = 两个节点。
3309  - 如果集群没有足够空闲节点，Pod 会一直 Pending。
3310  - `/models/` 是所有节点共享的 NFS 存储，脚本和权重文件对所有 Pod 可见。
3311  
3312  ## CUDA 编程实践：共享内存
3313  
3314  ### 核心概念
3315  
3316  每个 Block 都有自己独立的共享内存。在 CUDA 中，下面这句声明的是块内私有共享内存：
3317  
3318  ```cpp
3319  extern __shared__ float sdata[];
3320  ```
3321  
3322  也就是说，Block 0、Block 1 和 Block 2 各自都有一份独立的 `sdata` 数组，它们互不干扰。
3323  
3324  在这个例子中：
3325  
3326  - `blockDim.x = 4`
3327  - 每个 Block 的 `sdata` 长度都是 4
3328  - 每个 Block 内部的索引都是 `[0, 1, 2, 3]`
3329  
3330  当程序执行到下面这一行时：
3331  
3332  ```cpp
3333  sdata[tid] = (i &lt; N) ? input[i] : 0.0f;
3334  ```
3335  
3336  每个线程会根据自己的局部 ID（`tid`）和全局 ID（`i`），把全局内存中的数据搬到自己 Block 的共享内存中。
3337  
3338  ### 数据映射关系
3339  
3340  #### Block 0（`blockIdx.x = 0`）
3341  
3342  | Thread | `tid` | 全局 `i` | 执行操作 |
3343  | --- | --- | --- | --- |
3344  | Thread 0 | 0 | 0 | `sdata[0] = input[0]`（1.0） |
3345  | Thread 1 | 1 | 1 | `sdata[1] = input[1]`（2.0） |
3346  | Thread 2 | 2 | 2 | `sdata[2] = input[2]`（3.0） |
3347  | Thread 3 | 3 | 3 | `sdata[3] = input[3]`（4.0） |
3348  
3349  此时 Block 0 的 `sdata` 为：
3350  
3351  ```text
3352  [1.0, 2.0, 3.0, 4.0]
3353  ```
3354  
3355  #### Block 1（`blockIdx.x = 1`）
3356  
3357  | Thread | `tid` | 全局 `i` | 执行操作 |
3358  | --- | --- | --- | --- |
3359  | Thread 0 | 0 | 4 | `sdata[0] = input[4]`（5.0） |
3360  | Thread 1 | 1 | 5 | `sdata[1] = input[5]`（6.0） |
3361  | Thread 2 | 2 | 6 | `sdata[2] = input[6]`（7.0） |
3362  | Thread 3 | 3 | 7 | `sdata[3] = input[7]`（8.0） |
3363  
3364  此时 Block 1 的 `sdata` 为：
3365  
3366  ```text
3367  [5.0, 6.0, 7.0, 8.0]
3368  ```
3369  
3370  #### Block 2（`blockIdx.x = 2`）
3371  
3372  | Thread | `tid` | 全局 `i` | 执行操作 |
3373  | --- | --- | --- | --- |
3374  | Thread 0 | 0 | 8 | `sdata[0] = input[8]`（9.0） |
3375  | Thread 1 | 1 | 9 | `sdata[1] = input[9]`（10.0） |
3376  | Thread 2 | 2 | 10 | `sdata[2] = input[10]`（11.0） |
3377  | Thread 3 | 3 | 11 | `sdata[3] = input[11]`（12.0） |
3378  
3379  此时 Block 2 的 `sdata` 为：
3380  
3381  ```text
3382  [9.0, 10.0, 11.0, 12.0]
3383  ```
3384  
3385  
</code></pre>

<a id="log-2026-05-17"></a>
### 2026-05-17

Source lines: `3386-3500`

<pre class="tech-log-source"><code>
3386  # 2026-05-17
3387  
3388  ## CUDA kernel 与 device function
3389  
3390  ### 问题
3391  
3392  为什么到了 `reduce_max_kernel` 才说 “kernel 1”？前面的几个函数不是 kernel 吗？
3393  
3394  前面的函数包括：
3395  
3396  - `warpReduceMax`
3397  - `warpReduceSum`
3398  - `blockReduceMax`
3399  - `blockReduceSum`
3400  
3401  ### 结论
3402  
3403  这些函数都不是 CUDA kernel，而是 device function（设备函数）。
3404  
3405  在 CUDA 中，**kernel = GPU 并行执行入口**，也就是能被 CPU 端用 `&lt;&lt;&lt;blocks, threads&gt;&gt;&gt;` 启动的函数。
3406  
3407  ### CUDA 中三类关键函数
3408  
3409  | 类型 | 示例 | 运行位置 | 是否 kernel | 是否能用 `&lt;&lt;&lt;&gt;&gt;&gt;` 启动 |
3410  | --- | --- | --- | --- | --- |
3411  | `__global__` | `__global__ void reduce_max_kernel(...)` | GPU | 是 | 是 |
3412  | `__device__` | `__device__ float warpReduceMax(float val)` | GPU | 否 | 否 |
3413  | 普通 CPU 函数 | `extern &quot;C&quot; void solve(...)` | CPU | 否 | 否 |
3414  
3415  `__global__` 函数是真正的 GPU 启动入口，例如：
3416  
3417  ```cpp
3418  __global__ void reduce_max_kernel(...) {
3419    // GPU kernel body
3420  }
3421  
3422  reduce_max_kernel&lt;&lt;&lt;blocks, threads&gt;&gt;&gt;(...);
3423  ```
3424  
3425  `__device__` 函数只能被 GPU 代码调用，它是 GPU 内部的辅助函数，不是执行入口。
3426  
3427  ## Reduction 规约操作
3428  
3429  ### 执行层级
3430  
3431  CUDA 的执行层级是：
3432  
3433  ```text
3434  Grid -&gt; Block -&gt; Warp -&gt; Thread
3435  ```
3436  
3437  关键限制：
3438  
3439  - 一个 warp 固定 32 个线程。
3440  - 一个 block 最多 1024 个线程。
3441  - 因此一个 block 最多只有 32 个 warp。
3442  
3443  ### Warp-level reduction
3444  
3445  Warp 内通信主要使用 `__shfl_down_sync`。它允许线程直接读取其他 lane 的寄存器数据，比 shared memory 更快。
3446  
3447  Warp reduction 的本质是：**信息向低 lane 聚合**。最终只有 `lane 0` 一定保存整个 warp 的规约结果。
3448  
3449  ### Block-level reduction
3450  
3451  Block reduction 通常采用两级结构：
3452  
3453  1. 每个 warp 内部先做 reduction。
3454  2. 每个 warp 把自己的结果写入 `shared[32]`。
3455  3. 第一个 warp 继续对这些 partial results 做 reduction。
3456  
3457  `shared[32]` 足够的原因是：一个 block 最多只有 32 个 warp，而第一个 warp 正好有 32 个 lane，可以覆盖全部 warp partial results。
3458  
3459  ## Grid-Stride Loop
3460  
3461  Grid-Stride Loop 是 CUDA 中处理超大数据的经典模式：
3462  
3463  ```cpp
3464  for (int i = idx; i &lt; N; i += stride) {
3465    // process input[i]
3466  }
3467  ```
3468  
3469  其中：
3470  
3471  - `idx` 是当前线程的全局编号。
3472  - `stride = blockDim.x * gridDim.x`，表示整个 grid 的线程总数。
3473  - 一个线程会循环处理多个元素。
3474  
3475  ### `local_max` 的含义
3476  
3477  `local_max` 不是全局最大值，而是当前线程负责的数据分片中的局部最大值（thread-local max）。
3478  
3479  完整规约路径是：
3480  
3481  ```text
3482  thread-local max -&gt; warpReduceMax -&gt; blockReduceMax -&gt; global reduction -&gt; final max
3483  ```
3484  
3485  ### CUDA reduction 优化直觉
3486  
3487  优先级通常是：
3488  
3489  ```text
3490  register &gt; shuffle &gt; shared memory &gt; global memory
3491  ```
3492  
3493  因此优化方向是：
3494  
3495  - warp 内尽量使用 shuffle。
3496  - warp 间使用 shared memory。
3497  - 尽可能减少 global memory 访问。
3498  
3499  
3500  
</code></pre>

<a id="log-2026-05-20"></a>
### 2026-05-20

Source lines: `3501-3511`

<pre class="tech-log-source"><code>
3501  # 2026-05-20
3502  
3503  Chapter2：简单融合算子与激活函数 (softmax, relu, silu, sigmoid)	&quot;录制: Wang Akang (SRIBD)预定的会议
3504  日期: 2026-05-20 13:57:08
3505  录制文件：https://meeting.tencent.com/crm/2BYebVgo61
3506  密码：JAIW&quot;	算子学习第二节课复盘_融合算子与FusedSoftmax_整理与补充版.pdf	session5(20min)：基本融合算子：softmax	朱子为	以 fused-softmax为例，讲一下融合算子（fused softmax，不是 softmax）
3507  			session6：融合的“模型”	杨明哲	把 fused softmax 的数据流动画出来，讲讲为什么要融合，数学本质是什么（函数复合，一次加载多次计算）
3508  			session7（20min）：融合算子练习	占贺深	relu、gelu、x*sigmoid(x)融合与不融合的版本、x + sigmoid(x) + silu(x)（如何加载一次 x 就算 3 个值）
3509  
3510  
3511  
</code></pre>

<a id="log-2026-05-21"></a>
### 2026-05-21

Source lines: `3512-3538`

<pre class="tech-log-source"><code>
3512  # 2026-05-21
3513  
3514  ## 算子学习 Chapter 3：数值处理与规约
3515  
3516  ### 课程主题
3517  
3518  - `log softmax`
3519  - `relu softmax`
3520  - `softmax dropout`
3521  - softmax 与 element-wise 操作的融合
3522  - block 划分与规约
3523  
3524  ### Session 安排
3525  
3526  | Session | 负责人 | 主题 | 重点 |
3527  | --- | --- | --- | --- |
3528  | session8 | 刘欣 | 简单的算子优化方法 | 以 `log-softmax` 为例，展示简单算子优化方法 |
3529  | session9（20min） | 付谕书 | softmax 与 element-wise 的组合 | 以 `log-softmax + nll_loss`、`softmax + dropout` 为例，理解 softmax 与 element-wise 的融合方式 |
3530  | session10 | 崔诺拉 | 融合算子中的 block 划分与规约 | 实现 softmax 分块版本（不 fused） |
3531  | session11 | 刘稔远 | 实现 `relu(softmax(x))` | 讲解 Triton 实现代码，涉及 block 内部 program 计算和 block 之间的规约 |
3532  
3533  ### 今日关注
3534  
3535  - softmax 相关算子不仅要理解数学形式，也要理解内存读写路径。
3536  - softmax 与 element-wise 操作融合时，关键问题是哪些中间结果不需要写回 global memory。
3537  - block 划分会直接影响规约方式，需要同时考虑 block 内 program 计算和 block 间结果合并。
3538  
</code></pre>

<a id="log-2026-05-22"></a>
### 2026-05-22

Source lines: `3539-3596`

<pre class="tech-log-source"><code>
3539  # 2026-05-22
3540  
3541  ## LayerNorm 和 RMSNorm 的几何理解
3542  
3543  ### 今日结论
3544  
3545  - RMSNorm 后的数据分布在完整的 $M$ 维超球面上，自由度为 $M-1$。
3546  - LayerNorm 后的数据分布在被超平面切开的“大圆”上，自由度为 $M-2$。
3547  - RMSNorm 只去掉向量长度信息；LayerNorm 同时去掉向量长度信息和平移基准（直流分量）。
3548  - 从 Triton 算子角度看，RMSNorm 计算开销更低，因为它只需要维护平方和累加器；LayerNorm 需要同时维护均值和方差。
3549  
3550  ### 几何直觉
3551  
3552  当一个超平面去切割一个超球面，并且这个平面正好穿过球心时，切出来的交集是一个大圆（Great Circle）。
3553  
3554  在 $M$ 维空间里，这个交集可以理解为一个 $M-2$ 维的子超球面。
3555  
3556  因此：
3557  
3558  - RMSNorm：只把数据投影到完整超球面上。
3559  - LayerNorm：先要求数据落在超球面上，又要求数据落在过球心的超平面上。
3560  
3561  ### 三维空间例子（$M=3$）
3562  
3563  假设特征维度为 3，一行数据为 $[x, y, z]$。
3564  
3565  RMSNorm 的约束是：
3566  
3567  ```text
3568  x^2 + y^2 + z^2 = 3
3569  ```
3570  
3571  这对应一个普通的三维球面。
3572  
3573  LayerNorm 的约束是：
3574  
3575  ```text
3576  x^2 + y^2 + z^2 = 3
3577  x + y + z = 0
3578  ```
3579  
3580  也就是说，LayerNorm 不仅要求数据落在球面上，还要求数据落在过球心的平面上。最终数据只能落在球面和平面的交线上，也就是一条圆形轨道。
3581  
3582  ### 对大模型和 Triton 算子的意义
3583  
3584  | 归一化方式 | 几何形态 | 损失的信息 | Triton 计算开销 |
3585  | --- | --- | --- | --- |
3586  | RMSNorm | 完整的超球面 | 向量的绝对长度 | 低，只需维护 1 个平方和累加器 |
3587  | LayerNorm | 超球面上的“平切圆” | 向量的绝对长度 + 平移基准（直流分量） | 高，需要维护均值和方差 2 个累加器 |
3588  
3589  ### 物理本质
3590  
3591  从几何上看：
3592  
3593  - RMSNorm 是“只缩放长度”，保留方向和平移基准。
3594  - LayerNorm 是“去均值 + 缩放长度”，同时去掉平移基准和长度尺度。
3595  
3596  这也是为什么在大模型推理和 Triton kernel 实现中，RMSNorm 往往比 LayerNorm 更轻量。
</code></pre>

