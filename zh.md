---
permalink: /zh/
seo_title: "刘稔远"
description: "刘稔远，香港中文大学（深圳）人工智能研究型硕士生，研究方向包括 AI 基础设施、AI Agent、大语言模型后训练、具身智能与机器视觉。"
lang: zh-CN
locale: zh_CN
alternate_url: /
alternate_lang: en
language_switch_label: EN
language_switch_aria_label: Switch to English
author_profile: true
github_activity_sidebar: true
hide_title: true
---

# Renyuan LIU（刘<ruby>稔<rt>rěn</rt></ruby>远）
---

你好，很高兴在这里认识你！
我是香港中文大学（深圳）人工智能学院的**人工智能研究型硕士生（MPhil）**，导师为[胡君杰教授](https://sai.cuhk.edu.cn/en/teacher/153)。

我目前的工作涵盖 **AI 基础设施（AI Infrastructure）**、**AI Agent** 与**大语言模型后训练（LLM Post-Training）**，同时持续关注具身智能与机器视觉。我希望构建高效、可靠的 AI 系统，并把研究想法落实为真正可运行的系统。

本科期间，我有幸在广州大学机器生命与智能研究中心接受[傅沁冰教授](https://www.researchgate.net/profile/Qinbing-Fu-2)指导，并在英国约克大学计算机科学系接受[刘鹏程教授](https://sites.google.com/view/pliu)指导。

欢迎计算机科学各方向的交流与合作。

[**查看个人简历**]({{ '/assets/CV_RenyuanLiu.pdf' | relative_url }}) · [**访问 TEAM NEXUS**](https://ryannnice.github.io/nexus/)

## 精选 AI 系统项目 {#projects-renyuan}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">100 工具电商智能导购与多轮工具规划 Agent 系统</h3>
      <p class="project-card__meta">2026 年 7 月 – 至今</p>
    </header>
    <div class="project-media-grid">
      <figure class="project-media">
        <a href="{{ '/assets/projects/ecommerce-agent/agent-full-trace-progress.svg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/assets/projects/ecommerce-agent/agent-full-trace-progress.svg' | relative_url }}" width="2200" height="1320" loading="lazy" decoding="async" alt="9,000 条请求上工具规划全链路准确率由 19.29% 提升至 92.62% 的折线图">
        </a>
        <figcaption>固定 9K 测试集上的全链路决策增益</figcaption>
      </figure>
      <figure class="project-media">
        <a href="{{ '/assets/projects/ecommerce-agent/agent-multiturn-trace-progress.svg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/assets/projects/ecommerce-agent/agent-multiturn-trace-progress.svg' | relative_url }}" width="2200" height="1360" loading="lazy" decoding="async" alt="多轮 Agent 在独立测试集上准确率提升至 94.56% 的折线图">
        </a>
        <figcaption>独立测试集上的多轮 Agent 消融</figcaption>
      </figure>
    </div>
    <p class="project-card__source"><a href="https://ryannnice.github.io/nexus/ecommerce-agent/">查看完整项目主页</a></p>
    <details class="project-details">
      <summary>展开项目详情</summary>
      <div class="project-details__content">
        <p><strong>项目背景：</strong>作为核心研发，负责 100 工具、8 大业务域电商导购 Agent 研发，解决全量工具开销、同类工具混淆、多需求顺序错误与跨轮历史污染。</p>
        <ul>
          <li><strong>意图分流（分类准确率 100.0%）：</strong>构建 4.8 万条电商/闲聊数据，LoRA 微调 Qwen3-0.6B，9,000 条隔离测试准确率 84.8%→100.0%；较 Qwen3-1.7B，推理中位延迟降低 34.3%、吞吐提升 52.0%。</li>
          <li><strong>高效工具检索（Top-10 工具全召回率 97.4%）：</strong>构建 7 万正对与 9.6 万类型化负例，采用多负例对比学习微调 bge-large，并以 1:7 正负难例组训练 bge-reranker-v2-m3；实现 BM25/向量双路召回、两级 RRF 融合与 Cross-Encoder 精排，采用“召回 40→精排 20→规划 10”的分层筛选，Top-10 全召回率 47.6%→97.4%；相较“精排 30→规划 20”方案，规划模型输入 Token/重排中位延迟降低 36.8%/33.7%。</li>
          <li><strong>多步工具规划（端到端准确率 92.6%）：</strong>构建 7.8 万条多风格工具调用轨迹，基于 MS-SWIFT 使用 LoRA 微调 Qwen3-8B，在固定 Top-10 候选中输出有序工具链；基于父模型真实错误构建 4,000 组偏好对，采用 RPO 主训练、DPO 低学习率收敛，规划模型工具链完全匹配率 85.7%→88.9%；在 9,000 条静态测试上，端到端准确率达 92.6%。</li>
          <li><strong>多轮 Agent 框架（上下文依赖请求准确率 92.8%）：</strong>设计模型外上下文编排器，以规则状态机调度近期状态、规则摘要与会话内 BM25，将必要历史压缩并补全为可独立规划的当前请求，再接入原规划模型，通过请求边界与整轮恢复抑制历史污染；基于近 2,000 段 2–7 轮自然短会话完成 12 阶段消融，独立测试整体准确率较直接拼接基线 50.5%→94.6%，上下文依赖/无关请求准确率达 92.8%/97.4%，版本校验缓存使规划模型调用减少 60.3%。</li>
        </ul>
        <p class="project-card__metrics"><strong>核心成果：</strong>9,000 条隔离测试意图准确率 100.0%；Top-10 工具全召回率 97.4%（基线 47.6%）；端到端准确率 92.6%；上下文依赖请求准确率 92.8%，规划模型调用减少 60.3%。</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">项目一｜DeepSeek-V4 国产算力适配与昇腾算子优化</h3>
      <p class="project-card__meta">2026 年 3 月 – 6 月 · 深圳市大数据研究院</p>
    </header>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/Kernel_Agent.png' | relative_url }}">
        <img src="{{ '/assets/Kernel_Agent.png' | relative_url }}" width="1718" height="916" loading="lazy" decoding="async" alt="昇腾算子优化 Agent 架构，包括规划、编码、验证、知识检索、性能画像、诊断、优化与测试">
      </a>
      <figcaption>昇腾算子优化 Agent 架构</figcaption>
    </figure>
    <details class="project-details">
      <summary>展开项目详情</summary>
      <div class="project-details__content">
        <p><strong>项目背景：</strong>作为核心研发，参与深圳河套学院联合华为、智子芯元开展的 DeepSeek-V4-Pro 国产算力全参数后训练。围绕 DeepSeek-V4 在国产算力上的推理与后训练落地，负责昇腾 910C 部署测评、算子优化 Agent 研发及融合反向算子优化。</p>
        <ul>
          <li><strong>910C 推理适配与测评（DeepSeek V4 Flash/Pro）：</strong>参与在昇腾 910C 集群部署与测评 DeepSeek V4 Flash/Pro，基于 ShareGPT 等数据对比 vLLM Ascend 与 SGLang 的 Prefill/Decode 性能，为推理框架选型与部署配置提供依据。</li>
          <li><strong>算子优化 Agent（昇腾迁移与开源）：</strong>针对昇腾算子依赖人工分析与反复试错的问题，基于 MIT Kernel Design Agents 重构适配 910B/910C 的算子知识库、优化规则与性能诊断工具，打通检索→生成→编译→精度/性能验证→保留/回退闭环，开源 Kernel-Agent-Ascend。</li>
          <li><strong>融合反向算子优化（耗时降低 20.9%）：</strong>基于 msprof 定位 AIV 侧标量地址计算、稀疏访存、同步等待与负载不均；通过地址计算化简、低命中搬运分支裁剪、冗余同步删除、分块/片上缓存优化及向量任务重分配，同时修复缓存扩容引发的尾块越界，算子耗时 22.603→17.88 ms（1.26×），四路输出余弦相似度均为 1.0。</li>
        </ul>
        <p class="project-card__metrics"><strong>核心成果：</strong>目标配置（BSND/BF16，B=1、S=4096、K=1024）下，融合反向算子耗时 22.603→17.88 ms，降低 20.9%（1.26×）；四路输出余弦相似度均为 1.0，最大相对误差 8.39e-4。</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">项目二｜LLM 语义路由与 AI Agent 应用</h3>
      <p class="project-card__meta">2026 年 3 月 – 5 月 · 深圳市大数据研究院</p>
    </header>
    <details class="project-details">
      <summary>展开项目详情</summary>
      <div class="project-details__content">
        <p><strong>项目背景：</strong>面向多模型服务成本控制与 AI 教育业务落地，负责轻量语义路由及 AI 教育平台后端开发。</p>
        <ul>
          <li><strong>轻量语义路由（成本降低 62%）：</strong>参与设计基于 Query 与领域原型向量的 Domain 划分，并结合模型内部表示判断问题难度、分配不同规模模型；在准确率损失控制于 10% 内将推理成本降低 62%。</li>
          <li><strong>AI Agent 应用（后端开发）：</strong>基于 Vue3/Vite/Vue Router + FastAPI/SQLite/Docker 从 0 搭建 Web AI 教育平台及 Android 端；封装 SSE 流式生成与多轮会话，完成用户/会话/Token 监控、附件上传、Markdown/代码/网页预览及移动端适配，支撑新闻筛选、学习与 Coding Agent 工坊。</li>
        </ul>
      </div>
    </details>
  </article>
</div>


## 最新动态 {#news}

* [2026 年 6 月] 创立 [*TEAM NEXUS*](https://ryannnice.github.io/nexus/)，一个学习小组。

* [2026 年 6 月] 本科毕业设计获广州大学*创新奖*，排名全校第 3。

* [2026 年 3 月 19 日] 加入[深圳市大数据研究院（SRIBD）](https://www.sribd.cn/)担任算法实习生，从事 AI Agent 与大语言模型算法研发。

* [2026 年 2 月 27 日] 获[香港科技大学（广州）数据科学与分析学域“以数据为中心的人工智能”硕士项目录取](/assets/Offer_HKUSTGZ_MSc_DCAI.pdf)。

* [2026 年 2 月 26 日] 在约克大学评选中排名第一，获[约克大学与国家留学基金管理委员会联合资助博士奖学金提名](/assets/York_CSC.png)。

* [2026 年 1 月 19 日] 获[香港中文大学（深圳）人工智能学院人工智能研究型硕士（MPhil）项目录取](/assets/Offer_CUHKSZ_MPhil_AI.pdf)。

* [2025 年 12 月 17 日] 获广州大学二等奖学金（前 8%）。

* [2025 年 11 月 27 日] 获[英国约克大学计算机科学博士项目录取](/assets/Offer_UoY_PhD_CS.pdf)。

* [2025 年 7 月 28 日] 论文被《电子学报》录用（CCF 中文 A 类）。

* [2025 年 7 月 22 日] 论文被 *Neurocomputing* 录用（JCR Q1、SCI 二区、IF = 6.5）。

* [2025 年 7 月 18 日] 在谢菲尔德大学举行的 Living Machines 2025 会议上完成 30 分钟口头报告。

* [2025 年 7 月 11 日] 海报被 TAROS 2025 接收。

* [2025 年 6 月 9 日] 论文被 Living Machines 2025 接收。

* [2025 年 4 月 1 日] 论文被 IJCNN 2025 接收（CCF-C，录用率 38%）。


## 研究兴趣 {#research-interest}

我关注从模型行为到高效部署的完整链路：

* **AI 基础设施：**高效推理与训练、加速器适配、性能分析及算子优化；
* **AI Agent：**工具检索与规划、多轮上下文编排、记忆、评测和具身决策；
* **大语言模型后训练：**监督微调、偏好优化、参数高效微调和以数据为中心的评测；
* **机器视觉（本科阶段）：**面向实时碰撞检测与机器人导航的昆虫视觉神经模型。

我的本科研究主要聚焦**类脑神经网络**与**机器视觉**：通过建模昆虫视觉回路实现鲁棒的实时运动感知，并将这些机制转化为机器人碰撞检测系统。我喜欢亲手完成编码、调试、性能分析和端到端系统实现。实验平台包括配备双目相机的 *TurtleBot* 与微型地面机器人 *Colias*。

面向神经具身微型机器人 [***Colias***](https://link.springer.com/chapter/10.1007/978-3-319-96728-8_17) 的部分代码：

* [果蝇视觉运动启发的 Attention-LPLC2 模型](https://github.com/Ryannnice/neuro-life-project/blob/main/micro_embodied/colias_core/coliasSense_LPLC2.c)（独立完成，约 2,000 行 C 代码）；
* [多注意力 LPLC2（mLPLC2）神经网络模型](https://github.com/Ryannnice/Offline_Multi-Attention_LPLC2_Model/blob/main/LPLC2.cpp)（独立完成，约 3,000 行 C/C++ 代码）；
* [蝗虫视觉启发的 Optimized-LGMD 模型](https://github.com/Ryannnice/Optimized-LGMD/blob/main/coliasSense_LGMD.c)（独立完成，约 1,000 行 C 代码）。


## 经历 {#experience-renyuan}

- **[香港中文大学（深圳）](https://cuhk.edu.cn/)**，中国深圳<br>
  2026 年 9 月 – 2028 年 6 月（预计）<br>
  **人工智能研究型硕士生（MPhil）**<br>
  导师：[胡君杰教授](https://sse.cuhk.edu.cn/en/faculty/hujunjie)

- **[香港大学](https://www.hku.hk/)**，中国香港<br>
  2026 年 7 月<br>
  **暑期学校学员**

- **[深圳市大数据研究院（SRIBD）](https://www.sribd.cn/)**，中国深圳<br>
  2026 年 3 月 – 2026 年 6 月<br>
  **算法实习生**<br>
  从事 AI 基础设施、加速器算子优化、大语言模型语义路由与 AI Agent 应用研发。

- **[英国约克大学](https://www.york.ac.uk/computer-science/research/)**，英国约克（线下）<br>
  2025 年 6 月 – 2025 年 9 月<br>
  **访问学生**<br>
  **实验室：**计算自主学习系统实验室，实时与分布式系统研究组，计算机科学系<br>
  导师：[刘鹏程教授](https://sites.google.com/view/pliu)<br>
  [\[证明材料\]](/assets/Evidence_York.pdf)

- **[香港大学](https://www.hku.hk/)/[澳门大学](https://www.um.edu.mo/)**，中国香港/澳门<br>
  2023 年 11 月<br>
  **跨学科项目组长**<br>
  **GPA：97.50/100.00；荣誉：**获胜团队杰出表现嘉奖信<br>
  [\[证明材料\]](/assets/Evidence_HKU.pdf)


## 在审稿件 {#publications-renyuan}

- **R. Liu**、H. Zhou、C. Fang、Q. Fu，\[稿件双盲评审中。\] *投稿至 2026 IEEE International Conference on Robotics and Automation（ICRA，CCF-B）。*

- M. Wang<sup>\*</sup>、**R. Liu**<sup>\*</sup>、Q. Fu，\[稿件双盲评审中。\] *投稿至 IEEE Transactions on Cognitive and Developmental Systems（JCR Q1，IF = 4.9）。*

- \[稿件双盲评审中。\] *投稿至 IEEE Robotics and Automation Letters（RA-L），研究方向为具身智能与语义导航。*


## 已发表论文 {#publications}

- **R. Liu** and Q. Fu, [Attention-Driven LPLC2 Neural Ensemble Model for Multi-Target Looming Detection and Localization](https://ieeexplore.ieee.org/document/11227781). *2025 International Joint Conference on Neural Networks（IJCNN，CCF-C，录用率约 38%）。*

- G. Gao<sup>\*</sup>, **R. Liu**, M. Wang and Q. Fu<sup>\*</sup>, [A Computationally Efficient Neuronal Model for Collision Detection With Contrast Polarity-Specific Feed-Forward Inhibition](https://www.mdpi.com/2313-7673/9/11/650). *Biomimetics, vol. 9, no. 11, p. 650, 2024（JCR Q1，IF = 3.9）。*

- C. Fang<sup>\*</sup>, H. Zhou, **R. Liu**, and Q. Fu<sup>\*</sup>, [A neuromorphic binocular framework fusing directional and depth motion cues towards precise collision prediction](https://www.sciencedirect.com/science/article/pii/S092523122502332X). *Neurocomputing, 131660（JCR Q1，IF = 6.5）。*

- H. Zhou, C. Fang, **R. Liu**, and Q. Fu, [A Bio-Plausible Neural Network Integrating Motion and Disparity Pathways for Looming Perception](https://www.ejournal.org.cn/thesisDetails#10.12263/DZXB.20250337&lang=en). *《电子学报》，p.1–16, 2025（CCF 中文 A 类）。*

- J. Huang<sup>\*</sup>, Z. Qin, M. Wang, **R. Liu**, and Q. Fu<sup>\*</sup>, [A Biomimetic Collision Detection Visual Neural Model Coordinating Self-and-Lateral Inhibitions](https://ryannnice.github.io/assets/A%20biomimetic%20collision%20detection%20visual%20neural%20model%20coordinating%20self-and-lateral%20inhibitions.pdf). *第 14 届仿生与生物混合系统国际会议（Living Machines 2025，口头报告）。*


## 荣誉与奖励 {#awards-renyuan}

- **省级一等奖（前 3%）**，中国大学生计算机设计大赛<br>
  2025 年 5 月 [\[证明材料\]](/assets/Evidence_Computer_Design.pdf)

- **国际二等奖（Honorable Mention）**，美国大学生数学建模竞赛（MCM）<br>
  2025 年 1 月 [\[证明材料\]](/assets/Evidence_MCM.pdf)

- **国家一等奖（前 5%）**，亚太地区大学生数学建模竞赛<br>
  2024 年 11 月 [\[证明材料\]](/assets/Evidence_APMCM.pdf)

- **省级一等奖、创新银奖（1,167 支队伍中第 2 名）**，“大湾区杯”粤港澳金融数学建模竞赛<br>
  2024 年 11 月 [\[证明材料\]](/assets/Evidence_GBA_Cup.pdf)

- **二等奖学金（前 8%）**，广州大学<br>
  2025 年 12 月 [\[证明材料\]](/assets/Evidence_Scholarship_2025.pdf)

- **三等奖学金（前 12%）**，广州大学<br>
  2024 年 11 月 [\[证明材料\]](/assets/Evidence_Scholarship_2024.pdf)

- **一等奖学金（前 5%）**，广州大学<br>
  2023 年 12 月 [\[证明材料\]](/assets/Evidence_Scholarship_2023.pdf)

- **获胜团队杰出表现嘉奖信**，香港大学与澳门大学跨学科项目——新媒体、科技创新、艺术与数据挖掘<br>
  2023 年 11 月 [\[证明材料\]](/assets/Evidence_Macao.pdf)

- **省级重点大学生创新创业训练计划项目：**基于光流与学习优化的仿生 LGMD 碰撞检测模型（S202411078014） [\[证明材料\]](/assets/Evidence_College_Student_Training.pdf)


## 技术能力 {#skills}

- **大语言模型后训练与 Agent：**Qwen3、Transformer、SFT、DPO/RPO、LoRA、Tool Calling、模型外记忆、多轮上下文编排与 Agent 评测
- **检索与模型服务：**Embedding、Reranker、BM25/向量混合检索、RRF、Cross-Encoder、vLLM 与 SGLang
- **AI 基础设施：**CUDA、昇腾 910B/910C、msprof 性能分析、推理基准测试与算子优化
- **工程开发：**Python、C/C++、PyTorch、Hugging Face、MS-SWIFT、FastAPI、SQLite、Docker、Git、Vue 3 与 Linux
- **机器人与嵌入式：**ROS、STM32、Keil、Webots、MATLAB，以及双目视觉/微型机器人平台
- **AI 辅助开发：**每日高强度使用 Codex 与 Claude Code，月消耗 Token 百亿量级
- **语言：** **IELTS 6.5**（阅读 8.0、听力 6.5、写作 6.0、口语 5.5）；**CET-6 564**（阅读 242/248.5）
- **文档与媒体：**LaTeX、Markdown、MS Office/Visio、Adobe Photoshop 与 Premiere Pro
- *<font color = '#000066'>学习是世界上最幸福的事情之一。</font>*

  *喜欢电影、音乐、摄影、篮球、跑步、羽毛球、徒步与烹饪……*


## 学术会议 {#misc-renyuan}

***<font color = '#000066'>TAROS 2025</font>***，英国约克

- Fly-Inspired Ultra-selective Looming Perception and Avoidance on Resource-Constrained Micro-Robots，[海报](/assets/TAROS_2025_Poster_100.pdf)。

***<font color = '#000066'>Living Machines 2025</font>***，英国谢菲尔德

- A Biomimetic Collision Detection Visual Neural Model Coordinating Self-and-Lateral Inhibitions，[30 分钟口头报告](/assets/LivingMachines.pdf)。

***<font color = '#000066'>IJCNN 2025</font>***，意大利罗马

- Attention-Driven LPLC2 Neural Ensemble Model for Multi-Target Looming Detection and Localization，[视频](https://www.bilibili.com/video/BV15F7HzyEy1/)。

***<font color = '#000066'>ICMPSO 2024</font>***，中国广州

- *走向更广阔的学术世界。*


## 启发我的文章 {#inspiring-articles}

- [How to Have a Bad Career in Research/Academia](https://people.eecs.berkeley.edu/~pattrsn/talks/BadCareer.pdf)
- [How to Do Great Work](https://www.paulgraham.com/greatwork.html)
- [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)
- [NG Gladiator](https://www.nationalgeographic.com/magazine/issue/august-2021)
- [NG Everest](https://www.nationalgeographic.com/magazine/issue/july-2020)
- [NG Anthropocene](https://education.nationalgeographic.org/resource/anthropocene/)


## 访客地图 {#visitor-map}

<figure class="visitor-map">
  <a href="https://info.flagcounter.com/mUi7" target="_blank" rel="noopener noreferrer" aria-label="查看访客统计">
    <img
      src="https://s01.flagcounter.com/map/mUi7/size_s/txt_6B7280/border_FFFFFF/pageviews_0/viewers_3/flags_0/"
      alt="访客来源国家地图"
      width="400"
      height="205"
      decoding="async">
  </a>
</figure>
