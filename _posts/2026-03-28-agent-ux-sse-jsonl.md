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

<!-- source-log-coverage:start -->

## Source Log Coverage

The excerpts below are generated from `Renyuan_Log.md` and preserve the original tables, code fences, ASCII diagrams, commands, links, and explanations with source line numbers.

| Source | Lines | Title |
| --- | ---: | --- |
| [2026-03-28](#source-log-2026-03-28) | 1144-1314 | opencode 改造与流式 Agent UX |

<a id="source-log-2026-03-28"></a>
### Source Log: 2026-03-28

Source lines: `Renyuan_Log.md:1144-1314`

<pre class="tech-log-source"><code>
1144 |# 2026-03-28
1145 |
1146 |## 知识学习
1147 |
1148 |### Opencode
1149 |
1150 |Opencode 内部调用逻辑
1151 |
1152 |## 实践
1153 |
1154 |### Coding Agent
1155 |
1156 |我通过修改opencode的工作流，实现了我们项目所需的Coding Agent!
1157 |
1158 |### 封装 Coding Agent 到 FastAPI
1159 |
1160 |我找到更稳的落点了：直接给 opencode 加一个正式 CLI 子命令，比如 generate-project --prompt ...
1161 |这样 FastAPI 只需要调用这个命令拿 JSON，完全绕开“内部再起一个 HTTP 服务”的不稳定链路
1162 |
1163 |我已经封装成功！
1164 |现在能稳定输出.json格式的文件。
1165 |
1166 |### 删改opencode大项目结构
1167 |
1168 |这很像我一年前删除Colias项目文件的过程......
1169 |已完成并存档。这是目前的baseline版本。
1170 |
1171 |### 流式输出架构
1172 |
1173 |我的流式推送接口应能：
1174 |1.我希望前端能展示出当前项目的文件结构文件树、已有的文件。
1175 |2.我希望不仅能够展示工作状态，还要有一行或者几行，实时显示LLM正在生成的代码。
1176 |3.我希望用“思考状态”展示agent的工作状态。
1177 |
1178 |**推荐接口：**
1179 |```
1180 |
1181 |- POST /generate/jobs
1182 |  提交生成任务，返回 job_id
1183 |- GET /generate/jobs/{job_id}/stream
1184 |  SSE 流式输出
1185 |- GET /generate/jobs/{job_id}/result
1186 |  获取最终 { &quot;files&quot;: [...] }
1187 |- GET /generate/jobs/{job_id}
1188 |  获取任务当前快照
1189 |- DELETE /generate/jobs/{job_id}
1190 |  可选，取消任务
1191 |```
1192 |
1193 |为什么这样设计：
1194 |- 前端更容易接。POST 提交，GET 用 EventSource 收流。
1195 |- 能断线重连。
1196 |- 能同时拿“状态流”和“最终结果”。
1197 |- 不破坏现有 /generate。
1198 |
1199 |**SSE 事件设计：**
1200 |```
1201 |建议统一 JSON，事件名固定。
1202 |- job.created
1203 |  {&quot;job_id&quot;:&quot;gen_xxx&quot;,&quot;status&quot;:&quot;queued&quot;}
1204 |- thinking.status
1205 |  不传原始 CoT，只传安全摘要
1206 |  {
1207 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1208 |    &quot;phase&quot;:&quot;planning&quot;,
1209 |    &quot;label&quot;:&quot;正在规划项目结构&quot;,
1210 |    &quot;detail&quot;:&quot;分析需求，确定模板和最小文件集&quot;
1211 |  }
1212 |- project.tree
1213 |  前端文件树用这个
1214 |  {
1215 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1216 |    &quot;paths&quot;:[&quot;package.json&quot;,&quot;scripts/start.sh&quot;,&quot;src/main.js&quot;]
1217 |  }
1218 |- file.snapshot
1219 |  当前已有文件内容
1220 |  {
1221 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1222 |    &quot;path&quot;:&quot;src/main.js&quot;,
1223 |    &quot;content&quot;:&quot;...&quot;
1224 |  }
1225 |- file.delta
1226 |  可选，给前端展示“刚写出来的几行代码”
1227 |  {
1228 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1229 |    &quot;path&quot;:&quot;src/main.js&quot;,
1230 |    &quot;append&quot;:&quot;const app = ...\n&quot;
1231 |  }
1232 |- preview.code
1233 |  专门给你第二个需求
1234 |  {
1235 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1236 |    &quot;path&quot;:&quot;src/main.js&quot;,
1237 |    &quot;lines&quot;:[&quot;const app = ...&quot;,&quot;app.listen(...)&quot;]
1238 |  }
1239 |- session.status
1240 |  忙闲状态
1241 |  {
1242 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1243 |    &quot;status&quot;:{&quot;type&quot;:&quot;busy&quot;}
1244 |  }
1245 |- job.completed
1246 |  {
1247 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1248 |    &quot;file_count&quot;:9,
1249 |    &quot;result_url&quot;:&quot;/generate/jobs/gen_xxx/result&quot;
1250 |  }
1251 |- job.failed
1252 |  {
1253 |    &quot;job_id&quot;:&quot;gen_xxx&quot;,
1254 |    &quot;error&quot;:&quot;...&quot;
1255 |  }
1256 |```
1257 |
1258 |**怎么满足 3 个需求：**
1259 |```
1260 |
1261 |- 文件树、已有文件：
1262 |  用 project.tree + file.snapshot
1263 |- 实时显示 LLM 正在生成的代码：
1264 |  用 file.delta 或 preview.code
1265 |  这个不要依赖模型“口头输出代码”，而要监听真实文件写入
1266 |- 用“思考状态”展示 agent 状态：
1267 |  用 thinking.status内容来自阶段摘要，不直接暴露模型原始推理后端实现建议基于现有 packages/opencode/src/generate-api.ts 和 packages/opencode/src/server/generate-projectts改：
1268 |- Python FastAPI 负责：
1269 |    - 创建 job
1270 |    - 保存 job 状态
1271 |    - 返回 SSE StreamingResponse
1272 |- Bun 生成器负责：
1273 |    - 输出 JSONL 事件到 stdout
1274 |    - 最后一条输出最终 files
1275 |- 生成器内部增加 3 类 hook：
1276 |    - 阶段变化 hook：发 thinking.status
1277 |    - 文件变化 hook：发 project.tree、file.snapshot、preview.code
1278 |    - 结束 hook：发 job.completed
1279 |```
1280 |
1281 |最重要的一点：thinking.status 不建议传模型原始 reasoning。
1282 |建议只传这种：
1283 |- 分析需求中
1284 |- 规划项目结构中
1285 |- 正在编写 package.json
1286 |- 正在修复启动脚本
1287 |- 正在校验最终结果
1288 |这样前端效果够好，也安全。
1289 |
1290 |已实现
1291 |
1292 |  改动在 app.py、packages/opencode/src/generate-api.ts、packages/opencode/src/server/generate-project.ts、packages/opencode/
1293 |  test/generate-api.test.ts。
1294 |
1295 |  现在接口是：
1296 |
1297 |  - POST /generate：保留原来的同步返回 { files: [...] }
1298 |  - POST /generate/jobs：创建流式生成任务
1299 |  - GET /generate/jobs/{job_id}：拿当前快照，里面有文件树、已有文件、预览代码、thinking 状态
1300 |  - GET /generate/jobs/{job_id}/stream：SSE 流
1301 |  - GET /generate/jobs/{job_id}/result：任务完成后拿最终 { files: [...] }
1302 |
1303 |  流式行为现在支持：
1304 |
1305 |  - 文件树：project.tree
1306 |  - 文件内容快照：file.snapshot
1307 |  - 代码预览：preview.code
1308 |  - 安全的工作状态：thinking.status
1309 |  - 任务状态：job.status
1310 |  - 最终结果：job.result
1311 |
1312 |  另外，Bun 内部生成入口加了 --stream-jsonl，FastAPI 会把它解析成 job 状态并转成 SSE。同步 /generate 不受影响。reasoning 原文没
1313 |  有直接暴露给前端，只保留了状态级事件。
1314 |
</code></pre>

<!-- source-log-coverage:end -->
