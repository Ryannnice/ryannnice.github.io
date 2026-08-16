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
---

{% include language-switch.html %}

# Renyuan LIU（刘<ruby>稔<rt>rěn</rt></ruby>远）
---

你好，很高兴在这里认识你！
我是香港中文大学（深圳）人工智能学院的**人工智能研究型硕士生（MPhil）**，导师为[胡君杰教授](https://sai.cuhk.edu.cn/en/teacher/153)。

我目前的工作涵盖 **AI 基础设施（AI Infrastructure）**、**AI Agent** 与**大语言模型后训练（LLM Post-Training）**，同时持续关注具身智能与机器视觉。我希望构建高效、可靠的 AI 系统，并把研究想法落实为真正可运行的系统。

本科期间，我有幸在广州大学机器生命与智能研究中心接受[傅沁冰教授](https://www.researchgate.net/profile/Qinbing-Fu-2)指导，并在英国约克大学计算机科学系接受[刘鹏程教授](https://sites.google.com/view/pliu)指导。

欢迎计算机科学各方向的交流与合作。2026 年 6 月，我创立了 [**TEAM NEXUS**](https://ryannnice.github.io/nexus/)——一个连接 AI Agent、AI 基础设施、泛在系统与大模型规模化训练学习者的 AI 学习与研究组织。

<div class="profile-actions">
  <a class="btn btn--primary" href="{{ '/assets/CV_RenyuanLiu.pdf' | relative_url }}">查看个人简历</a>
  <a class="btn btn--inverse" href="https://ryannnice.github.io/nexus/">访问 TEAM NEXUS</a>
</div>

{% include github-activity.html %}


## 最新动态 {#news}

* [2026 年 6 月] 创立 [*TEAM NEXUS*](https://ryannnice.github.io/nexus/)——聚焦 AI 基础设施、Agent、泛在系统与大语言模型后训练的 AI 学习与研究组织。

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
* **仿生感知：**面向实时碰撞检测与机器人导航的昆虫视觉神经模型。

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

- **[香港大学](https://www.hku.hk/)**，中国香港（线下）<br>
  2026 年 7 月 – 2026 年 8 月<br>
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


## 精选 AI 系统项目 {#projects-renyuan}

<div class="project-grid">
  <article class="project-card project-card--featured">
    <h3 class="project-card__title">100 工具电商智能导购与多轮工具规划 Agent</h3>
    <p class="project-card__meta">2026 年 7 月 – 至今 · 核心研发</p>
    <p>构建覆盖 100 个工具、8 大业务域的 Agent 系统，整合 LoRA 微调的 Qwen3 意图路由、BM25/向量混合检索与 Cross-Encoder 精排、经偏好优化的工具规划模型，以及处理多轮请求的模型外上下文编排器。</p>
    <p class="project-card__metrics">意图准确率 <strong>100.0%</strong> · Top-10 工具全召回率 <strong>97.4%</strong> · 端到端准确率 <strong>92.6%</strong> · 版本校验缓存减少规划模型调用 <strong>60.3%</strong></p>
  </article>

  <article class="project-card">
    <h3 class="project-card__title">昇腾算子优化与 Kernel Agent</h3>
    <p class="project-card__meta">2026 年 3 月 – 6 月 · 深圳市大数据研究院</p>
    <p>面向昇腾 910B/910C 适配“检索—生成—编译—验证”的自动优化闭环，建设硬件感知知识库、性能诊断工具及安全的保留/回退评测流程，形成 Kernel-Agent-Ascend 系统。</p>
    <p class="project-card__metrics">将融合反向算子耗时从 <strong>22.603 ms 降至 17.88 ms</strong>（降低 <strong>20.9%</strong>），四路输出余弦相似度均保持 1.0。</p>
  </article>

  <article class="project-card">
    <h3 class="project-card__title">大语言模型语义路由与 AI 教育 Agent</h3>
    <p class="project-card__meta">2026 年 3 月 – 5 月 · 深圳市大数据研究院</p>
    <p>结合领域原型向量与模型内部表示完成多模型请求路由，在准确率损失低于 10% 的前提下降低推理成本 <strong>62%</strong>；并使用 FastAPI、SQLite、Docker、SSE 流式传输、多轮会话与文件处理能力搭建 AI 教育平台后端及移动端支持。</p>
  </article>
</div>


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
- **AI 辅助开发：**Codex 与 Claude Code
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
