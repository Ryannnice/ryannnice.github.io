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

## 知识补全：MVP 不是少做，而是少承担不确定性

MVP 经常被误解成“功能少一点”。更准确地说，MVP 是把当前阶段不需要承担的不确定性移出去。

对 Workshop 来说，完整 opencode 体系包含会话、工具、终端、编辑器、模型适配、状态流和复杂包结构。如果第一阶段目标只是“用户输入需求后得到可运行项目”，那么这些能力大多不是主路径。

Agent-Do 的瘦身价值在于把系统主路径压成：

```text
prompt -> generate -> write workspace -> run check -> return result
```

只要这条路径稳定，后续再加流式 UI、云部署、历史任务和复杂工具都更容易。

## 重构判断清单

遇到大型开源项目改造时，可以用这组问题判断是否该瘦身：

1. 我需要的是完整产品，还是其中一个能力。
2. 当前 bug 是业务逻辑问题，还是原项目运行时假设不匹配。
3. 新系统是否能用更少的状态表达同一条主路径。
4. 删除模块后是否会丢掉关键能力。
5. 未来扩展是否还能接回被删除的能力。

如果答案指向“主路径可以更短”，重构就不是倒退，而是把工程风险重新收束。

## 实际拆分步骤

把大系统瘦身成 MVP 时，可以按三个动作做。

第一，画出用户真正经过的主路径。Workshop 的主路径是输入需求、生成项目、验证运行、返回预览或文件。

第二，把不在主路径上的能力降级为后续插件。例如复杂会话管理、完整 IDE 体验、长期记忆、多模型工具链，都可以先不进入核心。

第三，为核心路径补 contract。生成器必须知道输出目录，运行器必须知道启动脚本，前端必须知道任务状态格式，容器必须知道 workspace 挂载点。

这样做的结果是：系统虽然小，但每一层边界更硬。后续加功能时，是在稳定主路径旁边扩展，而不是继续把不确定性塞进核心。

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-03-29](#source-log-2026-03-29) | 1315-1318 | 毕业设计优先日 |
| [2026-04-01](#source-log-2026-04-01) | 1421-1440 | Workshop MVP 重构启动 |
| [2026-04-02](#source-log-2026-04-02) | 1441-1485 | Docker 与项目未来定位 |
| [2026-04-03](#source-log-2026-04-03) | 1486-1540 | 容器 Workspace 与 Docker CLI 排障 |

<a id="source-log-2026-03-29"></a>
### Source Log: 2026-03-29

Source lines: `Renyuan_Log.md:1315-1318`

<pre class="tech-log-source"><code>
1315 |# 2026-03-29
1316 |
1317 |## 毕设毕设！
1318 |
</code></pre>


<a id="source-log-2026-04-01"></a>
### Source Log: 2026-04-01

Source lines: `Renyuan_Log.md:1421-1440`

<pre class="tech-log-source"><code>
1421 |# 2026-04-01
1422 |
1423 |## 知识学习
1424 |
1425 |#### Claude Code 框架
1426 |
1427 |Claude Code 源码泄露...
1428 |
1429 |学一波：[Bilibili: Claude Code源码泄露！首发解读51万行代码！](https://www.bilibili.com/video/BV11zXCBFEMo/?spm_id_from=333.1387.top_right_bar_window_default_collection.content.click)
1430 |
1431 |## 实践
1432 |
1433 |#### [Workshop 架构重构：MVP 版本](https://github.com/Ryannnice/Agent-Do)
1434 |
1435 |我们非常简洁、高效地实现了workshop。
1436 |
1437 |效果很好，并且摒弃了opencode的庞大源代码植入。
1438 |
1439 |优化前端，现在反应简洁迅速美观。
1440 |
</code></pre>


<a id="source-log-2026-04-02"></a>
### Source Log: 2026-04-02

Source lines: `Renyuan_Log.md:1441-1485`

<pre class="tech-log-source"><code>
1441 |# 2026-04-02
1442 |
1443 |## 知识学习
1444 |
1445 |#### Docker
1446 |
1447 |[Bilibili Docker](https://www.bilibili.com/video/BV1THKyzBER6/?spm_id_from=333.1387.favlist.content.click&amp;vd_source=487ef5084994b81a0ec05eeffa991ed2)
1448 |
1449 |#### 关于项目未来的讨论
1450 |
1451 |教育平台是核心竞争力
1452 |
1453 |下一阶段定位：用户每天早晨五分钟了解AI圈大事，甚至上手实践，学习一二。
1454 |
1455 |## 实践
1456 |
1457 |#### Workshop 架构重构：MVP 版本
1458 |
1459 |Debug, 增添流式输出功能
1460 |
1461 |#### Claude Code 宠物系统修复
1462 |
1463 |已经成功部署运行[“开源”的Claude Code](https://github.com/Ryannnice/claude-code)!
1464 |
1465 |修复了桌面宠物 /buddy 功能！
1466 |
1467 |#### Git Branch
1468 |
1469 |常见 type（非常重要）
1470 |```
1471 |feature	  新功能	  feature/payment-api
1472 |fix   	  修复 bug  fix/order-null-pointer
1473 |hotfix  	紧急修复	hotfix/login-crash
1474 |refactor	代码重构	refactor/cache-module
1475 |docs	    文档修改	docs/api-guide
1476 |test	    测试代码	test/user-service
1477 |chore	    杂项修改	chore/dependency-update
1478 |```
1479 |
1480 |#### Workshop
1481 |
1482 |尝试构建多项目运行时，并展示：
1483 |
1484 |我们发现似乎并不需要FC或者公网URL。
1485 |
</code></pre>


<a id="source-log-2026-04-03"></a>
### Source Log: 2026-04-03

Source lines: `Renyuan_Log.md:1486-1540`

<pre class="tech-log-source"><code>
1486 |# 2026-04-03
1487 |
1488 |## 知识学习
1489 |
1490 |#### git / docker
1491 |
1492 |- 用 `git pull` 和 `docker compose up --build -d` 熟悉基本更新与重建流程。
1493 |
1494 |这一天原本保留了整段学习对话，这里压缩为日志摘要：
1495 |
1496 |- 学习对象是 `assignment1-basics`，目标是把 Transformer 训练链路真正串起来理解。
1497 |- 当天抓住的主线是：
1498 |  `文本 -&gt; tokenizer -&gt; token id -&gt; embedding -&gt; Transformer -&gt; logits -&gt; cross entropy -&gt; 反向传播 -&gt; 参数更新`
1499 |- 核心代码入口包括：
1500 |  `cs336_basics/tokenizer.py`、
1501 |  `cs336_basics/model/modules.py`、
1502 |  `cs336_basics/model/transformer.py`、
1503 |  `cs336_basics/trainer/data_loading.py`、
1504 |  `cs336_basics/trainer/utils.py`、
1505 |  `cs336_basics/train.py`
1506 |- 最重要的认识有 6 点：
1507 |  1. 语言模型训练的本质是“给定前文，预测下一个 token”。
1508 |  2. `inputs` 是当前 token 序列，`targets` 是右移一位后的监督信号。
1509 |  3. Transformer 本体负责把上下文表示加工成下一个 token 的打分 `logits`。
1510 |  4. block 的核心结构是 Pre-Norm + Attention + FFN + Residual。
1511 |  5. `Linear`、`Embedding`、`RMSNorm`、`SwiGLU`、self-attention、RoPE 是后续必须啃透的基础模块。
1512 |  6. 训练闭环可以概括为：采样 -&gt; 前向 -&gt; 计算 loss -&gt; backward -&gt; 更新参数。
1513 |- 当天的直接产出：
1514 |  - 给 `trainer/data_loading.py`
1515 |  - 给 `trainer/utils.py`
1516 |    增加了逐行中文注释，作为第一部分学习基线。
1517 |- 下一步计划：
1518 |  继续理解 `Embedding`、`Linear`、attention 与 `transformer.py` 的整体拼装。
1519 |
1520 |## 实践
1521 |
1522 |#### Docker构建Claude Code
1523 |
1524 |遇到构建docker镜像时候地址错误问题：
1525 |
1526 |- Claude 看起来执行了
1527 |- 但改动写进了错误挂载目标
1528 |- 当前 session 的真实 workspace/ 还是空的
1529 |- 然后 runtime/start 检测不到 index.html / package.json，就返回 400 当前 session 没有可在线运行的项目
1530 |
1531 |问题不是 HTTP 400 本身，而是 Agent-Do 之前把 Claude 子容器的 workspace 挂到了错误的宿主机路径。
1532 |AGENT_DATA_HOST_ROOT 在 Backend/WorkShop/.env 里指向了旧机器上的 /root/internship-szdsjyjy/...，
1533 |但这台机器真实路径是 /home/ryan/CUHKSZ/Education_Platform/Backend/Agent-Do/data。
1534 |
1535 |- 修正了 Agent-Do 容器内 Docker CLI 的集成，避免之前的 input/output error: &#x27;docker&#x27;
1536 |- 修正了 Backend/WorkShop/.env 里的 AGENT_DATA_HOST_ROOT，并重启了 agent-do
1537 |
1538 |当前 qwen3-coder-next 这条模型链路有时会“看起来成功，实际上没写任何文件”。
1539 |我准备从 WorkShop 侧加兜底：当第一轮生成后没有形成可预览项目时，自动发一轮更强约束的修复 prompt，而不是直接把 runtime/start 400 暴露给前端。
1540 |
</code></pre>

<!-- source-log-coverage:end -->
