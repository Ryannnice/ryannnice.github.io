---
permalink: /
seo_title: "Renyuan Liu"
description: "Renyuan Liu is a Research Master's (MPhil) student working on AI infrastructure, AI agents, LLM post-training, embodied AI, and machine vision."
lang: en
locale: en_US
alternate_url: /zh/
alternate_lang: zh-CN
language_switch_label: 中文
language_switch_aria_label: Switch to Chinese
author_profile: true
github_activity_sidebar: true
hide_title: true
redirect_from: 
  - /about/
  - /about.html
---  

<!--
<p align="center">
  <img src="/images/CUHK-SAI-Logo-01_1.png" width="800">
</p>
-->

# Renyuan LIU (刘<ruby>稔<rt>rěn</rt></ruby>远)
---

Nice to meet you here!
I am a **Research Master's (MPhil) student in Artificial Intelligence** at the School of Artificial Intelligence, The Chinese University of Hong Kong, Shenzhen, under the supervision of [Prof. Junjie Hu](https://sai.cuhk.edu.cn/en/teacher/153).

My current work spans **AI infrastructure**, **AI agents**, and **LLM post-training**, with a continuing interest in embodied intelligence and machine vision. I care about building efficient, reliable systems and turning research ideas into working implementations.

During my undergraduate studies, I was fortunate to be advised by [Prof. Qinbing Fu](https://www.researchgate.net/profile/Qinbing-Fu-2) at the Machine Life and Intelligence Research Centre, Guangzhou University, and [Prof. Pengcheng Liu](https://sites.google.com/view/pliu) at the Department of Computer Science, University of York, UK.

I welcome collaborations across computer science. [**Curriculum Vitae**]({{ '/assets/CV_RenyuanLiu.pdf' | relative_url }}) · [**TEAM NEXUS**](https://ryannnice.github.io/nexus/)

## Selected AI Systems Projects {#projects-renyuan}

<div class="project-list">
  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">100-Tool E-Commerce Shopping Assistant and Multi-Turn Tool Planning Agent System</h3>
      <p class="project-card__meta">Jul. 2026 – Present</p>
    </header>
    <div class="project-media-grid">
      <figure class="project-media">
        <a href="{{ '/assets/projects/ecommerce-agent/agent-full-trace-progress.svg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/assets/projects/ecommerce-agent/agent-full-trace-progress.svg' | relative_url }}" width="2200" height="1320" loading="lazy" decoding="async" alt="Line chart showing the full tool-planning pipeline improving from 19.29% to 92.62% on 9,000 requests">
        </a>
        <figcaption>Full-pipeline gains on the frozen 9K test set</figcaption>
      </figure>
      <figure class="project-media">
        <a href="{{ '/assets/projects/ecommerce-agent/agent-multiturn-trace-progress.svg' | relative_url }}" target="_blank" rel="noopener noreferrer">
          <img src="{{ '/assets/projects/ecommerce-agent/agent-multiturn-trace-progress.svg' | relative_url }}" width="2200" height="1360" loading="lazy" decoding="async" alt="Line chart showing multi-turn Agent accuracy improving to 94.56% on the independent test set">
        </a>
        <figcaption>Multi-turn Agent ablation on the independent test set</figcaption>
      </figure>
    </div>
    <p class="project-card__source"><a href="https://ryannnice.github.io/nexus/ecommerce-agent/">View the complete project page</a></p>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <p><strong>Project Background:</strong> As a core developer, I worked on an e-commerce shopping Agent spanning 100 tools and eight business domains, addressing full-tool overhead, confusion among similar tools, incorrect ordering of multi-intent requests, and cross-turn history contamination.</p>
        <ul>
          <li><strong>Intent Routing (100.0% Classification Accuracy):</strong> Built 48K e-commerce and casual-conversation samples and LoRA-tuned Qwen3-0.6B, raising accuracy on 9,000 isolated test cases from 84.8% to 100.0%. Compared with Qwen3-1.7B, median inference latency fell by 34.3% and throughput rose by 52.0%.</li>
          <li><strong>Efficient Tool Retrieval (97.4% Top-10 Full Tool Recall):</strong> Built 70K positive pairs and 96K typed negatives, fine-tuned bge-large with multi-negative contrastive learning, and trained bge-reranker-v2-m3 with 1:7 positive-to-hard-negative groups. Implemented dual BM25/vector recall, two-stage RRF fusion, and Cross-Encoder reranking with a “recall 40 → rerank 20 → plan 10” funnel. Top-10 full recall rose from 47.6% to 97.4%; compared with “rerank 30 → plan 20,” planner input tokens and median reranking latency fell by 36.8% and 33.7%.</li>
          <li><strong>Multi-Step Tool Planning (92.6% End-to-End Accuracy):</strong> Built 78K multi-style tool-call trajectories and LoRA-tuned Qwen3-8B with MS-SWIFT to output ordered tool chains from a fixed Top-10 candidate set. Constructed 4,000 preference pairs from real parent-model errors, using RPO for main training and low-learning-rate DPO for convergence. Exact tool-chain match improved from 85.7% to 88.9%, with 92.6% end-to-end accuracy on 9,000 static tests.</li>
          <li><strong>Multi-Turn Agent Framework (92.8% Context-Dependent Request Accuracy):</strong> Designed an external context orchestrator whose rule-based state machine schedules recent state, rule summaries, and in-session BM25 retrieval. It compresses necessary history into a standalone current request before invoking the original planner, while request boundaries and full-turn recovery suppress history contamination. A 12-stage ablation on nearly 2,000 natural conversations of 2–7 turns raised independent-test overall accuracy from a 50.5% direct-concatenation baseline to 94.6%; context-dependent and context-independent request accuracy reached 92.8% and 97.4%, while version-validation caching reduced planner calls by 60.3%.</li>
        </ul>
        <p class="project-card__metrics"><strong>Core Results:</strong> 100.0% intent accuracy on 9,000 isolated tests; 97.4% Top-10 full tool recall (47.6% baseline); 92.6% end-to-end accuracy; 92.8% context-dependent request accuracy; and 60.3% fewer planner calls.</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">Project 1 | DeepSeek-V4 Domestic-Accelerator Adaptation and Ascend Kernel Optimization</h3>
      <p class="project-card__meta">Mar. – Jun. 2026 · Shenzhen Research Institute of Big Data</p>
    </header>
    <figure class="project-media project-media--wide">
      <a href="{{ '/assets/Kernel_Agent.png' | relative_url }}">
        <img src="{{ '/assets/Kernel_Agent.png' | relative_url }}" width="1718" height="916" loading="lazy" decoding="async" alt="Architecture of the Ascend kernel optimization Agent, including planning, coding, verification, knowledge retrieval, profiling, diagnosis, optimization, and testing">
      </a>
      <figcaption>Ascend kernel optimization Agent architecture</figcaption>
    </figure>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <p><strong>Project Background:</strong> As a core developer, I participated in the full-parameter post-training of DeepSeek-V4-Pro on domestic accelerators, jointly conducted by Shenzhen Hetao College, Huawei, and 智子芯元. For DeepSeek-V4 inference and post-training on domestic hardware, I worked on Ascend 910C deployment evaluation, kernel-optimization Agent development, and fused backward-kernel optimization.</p>
        <ul>
          <li><strong>910C Inference Adaptation and Evaluation (DeepSeek V4 Flash/Pro):</strong> Participated in deploying and evaluating DeepSeek V4 Flash/Pro on an Ascend 910C cluster. Compared Prefill/Decode performance between vLLM Ascend and SGLang on ShareGPT and other datasets to support inference-framework selection and deployment configuration.</li>
          <li><strong>Kernel Optimization Agent (Ascend Migration and Open Source):</strong> Addressed the manual analysis and repeated trial-and-error required by Ascend kernels by rebuilding MIT Kernel Design Agents for 910B/910C with a kernel knowledge base, optimization rules, and performance-diagnostic tools. Connected retrieval → generation → compilation → accuracy/performance verification → retain/rollback into a closed loop and open-sourced Kernel-Agent-Ascend.</li>
          <li><strong>Fused Backward-Kernel Optimization (20.9% Lower Latency):</strong> Used msprof to locate scalar address calculation on AIV, sparse memory access, synchronization waits, and load imbalance. Simplified address calculation, pruned low-hit data-movement branches, removed redundant synchronization, optimized tiling/on-chip caching, redistributed vector tasks, and fixed tail-block out-of-bounds access introduced by cache expansion. Kernel latency fell from 22.603 ms to 17.88 ms (1.26×), while cosine similarity remained 1.0 for all four outputs.</li>
        </ul>
        <p class="project-card__metrics"><strong>Core Results:</strong> Under the target configuration (BSND/BF16, B=1, S=4096, K=1024), fused backward-kernel latency fell from 22.603 ms to 17.88 ms, a 20.9% reduction (1.26×). All four output cosine similarities were 1.0, with a maximum relative error of 8.39e-4.</p>
      </div>
    </details>
  </article>

  <article class="project-card">
    <header class="project-card__header">
      <h3 class="project-card__title">Project 2 | LLM Semantic Routing and AI Agent Applications</h3>
      <p class="project-card__meta">Mar. – May 2026 · Shenzhen Research Institute of Big Data</p>
    </header>
    <details class="project-details">
      <summary>View project details</summary>
      <div class="project-details__content">
        <p><strong>Project Background:</strong> To control multi-model serving costs and deliver an AI education product, I developed a lightweight semantic router and the backend of an AI education platform.</p>
        <ul>
          <li><strong>Lightweight Semantic Routing (62% Cost Reduction):</strong> Helped design domain partitioning from queries and domain-prototype embeddings, then combined model-internal representations to estimate question difficulty and assign models of different sizes. Reduced inference cost by 62% while keeping accuracy loss within 10%.</li>
          <li><strong>AI Agent Application (Backend Development):</strong> Built a Web AI education platform and Android client from scratch with Vue 3/Vite/Vue Router + FastAPI/SQLite/Docker. Implemented SSE streaming and multi-turn sessions, user/session/token monitoring, attachment upload, Markdown/code/web preview, and mobile adaptation, supporting news filtering, learning, and a Coding Agent workshop.</li>
        </ul>
      </div>
    </details>
  </article>
</div>

## News {#news}

* [Jun. 2026] Founded [*TEAM NEXUS*](https://ryannnice.github.io/nexus/), a learning group.

* [Jun. 2026] My undergraduate thesis received an *Innovation Award* and ranked 3rd university-wide at *Guangzhou University*.

* [Mar 19th, 2026] Joined [*Shenzhen Research Institute of Big Data (SRIBD)*](https://www.sribd.cn/en) as an *Intern*, working on AI agent development and large language model algorithms.

* [Feb 27th, 2026] [Admitted to the *MSc program in Data-Centric Artificial Intelligence*](/assets/Offer_HKUSTGZ_MSc_DCAI.pdf) at *The Hong Kong University of Science and Technology (Guangzhou), Data Science and Analytics Thrust*!

* [Feb 26th, 2026] [Scored the highest and nominated for the *CSC Joint Funded PhD Scholarship by the University of York*](/assets/York_CSC.png), in collaboration with the *China Scholarship Council*! 
  
* [Jan 19th, 2026] [Admitted to the *Research Master's (MPhil) program in Artificial Intelligence*](/assets/Offer_CUHKSZ_MPhil_AI.pdf) at *The Chinese University of Hong Kong, Shenzhen, School of Artificial Intelligence*!

* [Dec 17th, 2025] Second-Class Scholarship Awarded by *Guangzhou University* [Top 8%].

* [Nov 27th, 2025] [Admitted to the *PhD program in Computer Science*](/assets/Offer_UoY_PhD_CS.pdf) at *the University of York, Department of Computer Science*.

* [Jul 28th, 2025] Paper accepted at *Acta Electronica Sinica* [CCF-A in the Chinese category].

* [Jul 22nd, 2025] Paper accepted at *Neurocomputing* [JCR Q1, SCI-2, IF = 6.5]!
  
* [July 18th, 2025] 30‑min oral presentation at *Living Machines 2025*, University of Sheffield.

* [Jul 11th, 2025] Poster accepted at *TAROS 2025*.

* [Jun 9th, 2025] Paper accepted at *Living Machines 2025*.
  
* [Apr 1st, 2025] Paper accepted at *IJCNN 2025* [CCF-C, AR = 38%].


## Research Interest {#research-interest}

I am interested in the full path from model behavior to efficient deployment:

* **AI Infrastructure:** efficient inference and training, accelerator adaptation, profiling, and kernel optimization;
* **AI Agents:** tool retrieval and planning, multi-turn context orchestration, memory, evaluation, and embodied decision-making;
* **LLM Post-Training:** supervised fine-tuning, preference optimization, parameter-efficient fine-tuning, and data-centric evaluation;
* **Machine Vision (Undergraduate):** neural models of insect vision for real-time collision detection and robotic navigation.

My undergraduate research focused on **brain-inspired neural networks** and **machine vision**. I modeled insect visual circuits for robust motion perception and translated them into collision-detection systems for robots. I enjoy hands-on coding, debugging, profiling, and end-to-end system implementation. My experimental platforms include *TurtleBot*s equipped with a binocular camera and the micro ground robot *Colias*.

Selected code for neuro-embodied micro-robot [***Colias***](https://link.springer.com/chapter/10.1007/978-3-319-96728-8_17) is available at:  
* [Fly Visuomotor-Inspired Attention-LPLC2 Model](https://github.com/Ryannnice/neuro-life-project/blob/main/micro_embodied/colias_core/coliasSense_LPLC2.c) (independently, 2k lines of code in C);  
* [Multi-Attention LPLC2 (mLPLC2) Neural Network Model](https://github.com/Ryannnice/Offline_Multi-Attention_LPLC2_Model/blob/main/LPLC2.cpp) (independently, 3k lines of code in C/C++);  
* [Locust Vision-Inspired Optimized-LGMD Model](https://github.com/Ryannnice/Optimized-LGMD/blob/main/coliasSense_LGMD.c) (independently, 1k lines of code in C).  


## Experience {#experience-renyuan}


- **[The Chinese University of Hong Kong, Shenzhen](https://cuhk.edu.cn/en)**, Shenzhen, China<br>
  Sept. 2026 - Jun. 2028 (Expected)  
  **Research Master's (MPhil) Student in Artificial Intelligence**<br>
  Supervisor: [Prof. Junjie Hu](https://sse.cuhk.edu.cn/en/faculty/hujunjie)
  

- **[The University of Hong Kong](https://www.hku.hk/)**, Hong Kong, China<br>
  Jul. 2026<br>
  **Summer School Student**



- **[Shenzhen Research Institute of Big Data (SRIBD)](https://www.sribd.cn/en)**, Shenzhen, China  
  Mar. 2026 - Jun. 2026<br>
  **Algorithm Intern**<br>
  Worked on AI infrastructure, accelerator kernel optimization, LLM semantic routing, and AI agent applications.
  

- **[The University of York](https://www.york.ac.uk/computer-science/research/)**, York, UK (On-Site)  
  Jun. 2025 - Sept. 2025  
  **Visiting Student**  
  **Lab:** Computational Autonomous Learning Systems Lab, Real-Time and Distributed Systems Research Group, Department of Computer Science  
  Supervisor: [Prof. Pengcheng Liu](https://sites.google.com/view/pliu)  
  [\[Evidence\]](/assets/Evidence_York.pdf)


- **[The University of Hong Kong](https://www.hku.hk/)/[University of Macau](https://www.um.edu.mo/)**, Hong Kong/Macao, China  
  Nov. 2023  
  **Interdisciplinary Programme Leader**  
  **GPA: 97.50/100.00**; **Honor:** Commendation Letter for Outstanding Performance in the Winning Team  
  [\[Evidence\]](/assets/Evidence_HKU.pdf)


## Manuscripts Under Review {#publications-renyuan}

- **R. Liu**, H. Zhou, C. Fang and Q. Fu, \[Manuscript under double-blind review.\] *Under review in The 2026 International Conference on Robotics and Automation (ICRA)(CCF-B).*

- M. Wang<sup>\*</sup>, **R. Liu**<sup>\*</sup>, and Q. Fu, \[Manuscript under double-blind review.\] *Under review in IEEE Transactions on Cognitive and Developmental Systems (JCR Q1, IF = 4.9).*

- \[Manuscript under double-blind review.\] *Under review in IEEE Robotics and Automation Letters (RA-L), in the area of embodied AI and semantic navigation.*



## Publications {#publications}

- **R. Liu** and Q. Fu, [Attention-Driven LPLC2 Neural Ensemble Model for Multi-Target Looming Detection and Localization](https://ieeexplore.ieee.org/document/11227781). *The 2025 International Joint Conference on Neural Networks (CCF-C, acceptance rate ≈ 38%).*

- G. Gao<sup>\*</sup>, **R. Liu**, M. Wang and Q. Fu<sup>\*</sup>, [A Computationally Efficient Neuronal Model for Collision Detection With Contrast Polarity-Specific Feed-Forward Inhibition](https://www.mdpi.com/2313-7673/9/11/650). *Biomimetics, vol. 9, no. 11, p. 650, 2024 (JCR Q1, IF = 3.9).*

- C. Fang<sup>\*</sup>, H. Zhou, **R. Liu**, and Q. Fu<sup>\*</sup>, [A neuromorphic binocular framework fusing directional and depth motion cues towards precise collision prediction](https://www.sciencedirect.com/science/article/pii/S092523122502332X). *Neurocomputing, 131660 (JCR Q1, IF = 6.5).*

- H. Zhou, C. Fang, **R. Liu**, and Q. Fu, [A Bio-Plausible Neural Network Integrating Motion and Disparity Pathways for Looming Perception](https://www.ejournal.org.cn/thesisDetails#10.12263/DZXB.20250337&lang=en). *Acta Electronica Sinica, p.1-16, 2025 (CCF-A in Chinese Category).*

- J. Huang<sup>\*</sup>, Z. Qin, M. Wang, **R. Liu**, and Q. Fu<sup>\*</sup>, [A Biomimetic Collision Detection Visual Neural Model Coordinating Self-and-Lateral Inhibitions](https://ryannnice.github.io/assets/A biomimetic collision detection visual neural model coordinating self-and-lateral inhibitions.pdf). *The 14th International Conference on Biomimetic and Biohybrid Systems (Living Machines 2025)(Oral)*.



## Honors and Awards {#awards-renyuan}


- **First Prize (Provincial; Top 3%)**, Chinese Collegiate Computing Competition (4C)  
  May 2025  [\[Evidence\]](/assets/Evidence_Computer_Design.pdf)  
  
- **Honorable Mention (International)**, Mathematical Contest in Modeling (MCM)  
  Jan. 2025  [\[Evidence\]](/assets/Evidence_MCM.pdf)  

- **First Prize (National; Top 5%)**, Asia and Pacific Mathematical Contest in Modeling (APMCM)  
  Nov. 2024  [\[Evidence\]](/assets/Evidence_APMCM.pdf)  

- **First Prize & Innovation Silver Award (Provincial; Top 2 out of 1,167 Teams)**,  
  "Greater Bay Area Cup" Guangdong-Hong Kong-Macao Financial Mathematics Modeling Competition  
  Nov. 2024  [\[Evidence\]](/assets/Evidence_GBA_Cup.pdf)  
  
- **Second-Class Scholarship (Top 8%)**, *Guangzhou University*  
  Dec. 2025  [\[Evidence\]](/assets/Evidence_Scholarship_2025.pdf)  

- **Third-Class Scholarship (Top 12%)**, *Guangzhou University*  
  Nov. 2024  [\[Evidence\]](/assets/Evidence_Scholarship_2024.pdf)  

- **First-Class Scholarship (Top 5%)**, *Guangzhou University*  
  Dec. 2023  [\[Evidence\]](/assets/Evidence_Scholarship_2023.pdf)  

- **Commendation Letter for Outstanding Performance in the Winning Team**,  
  Interdisciplinary Programme - New Media, Technological Innovation, Art and Data Mining at University of Hong Kong and The University of Macao  
  Nov. 2023  [\[Evidence\]](/assets/Evidence_Macao.pdf)  

- ***Provincial Key** College Students' Innovative Entrepreneurial Training Plan Program*: Bio-Inspired LGMD Collision Detection Model Leveraging Optical Flow and Learning-Based Optimization *(S202411078014)*  [\[Evidence\]](/assets/Evidence_College_Student_Training.pdf)  




## Skills {#skills}

- **LLM Post-Training & Agents:** Qwen3, Transformers, SFT, DPO/RPO, LoRA, tool calling, external memory, multi-turn orchestration, and agent evaluation
- **Retrieval & Model Serving:** embeddings, rerankers, BM25/vector hybrid retrieval, RRF, cross-encoders, vLLM, and SGLang
- **AI Infrastructure:** CUDA, Ascend 910B/910C, profiling with msprof, inference benchmarking, and kernel optimization
- **Engineering:** Python, C/C++, PyTorch, Hugging Face, MS-SWIFT, FastAPI, SQLite, Docker, Git, Vue 3, and Linux
- **Robotics & Embedded Systems:** ROS, STM32, Keil, Webots, MATLAB, and binocular/micro-robot platforms
- **AI-Assisted Development:** intensive daily use of Codex and Claude Code, with monthly usage on the order of 10 billion tokens
- **Languages:** **IELTS 6.5** (R8.0, L6.5, W6.0, S5.5) and **CET-6 564** (242/248.5 in reading)
- **Documentation & Media:** LaTeX, Markdown, MS Office/Visio, Adobe Photoshop, and Premiere Pro
- *<font color = '#000066'>Learning is one of the happiest things in the world.</font>*

  *I enjoy movies, music, photography, basketball, jogging, badminton, hiking, and cooking.*
  





## Conference {#misc-renyuan}

***<font color = '#000066'>TAROS 2025</font>***, *York, United Kingdom*
- Fly-Inspired Ultra-selective Looming Perception and Avoidance on Resource-Constrained Micro-Robots, [Poster](/assets/TAROS_2025_Poster_100.pdf). 


***<font color = '#000066'>Living Machines 2025</font>***, *Sheffield, United Kingdom*
- A Biomimetic Collision Detection Visual Neural Model Coordinating Self-and-Lateral Inhibitions, [30-min Oral](/assets/LivingMachines.pdf).

***<font color = '#000066'>IJCNN 2025</font>***, *Rome, Italy*
- Attention-Driven LPLC2 Neural Ensemble Model for Multi-Target Looming Detection and Localization, [Video](https://www.bilibili.com/video/BV15F7HzyEy1/).

***<font color = '#000066'>ICMPSO 2024</font>***, *Guangzhou, China*   
- *A Broader Academic World.*  
<br>
<br>
<br>



## Inspiring Articles {#inspiring-articles}

- [How to Have a Bad Career in Research/Academia](https://people.eecs.berkeley.edu/~pattrsn/talks/BadCareer.pdf)
- [How to Do Great Work](https://www.paulgraham.com/greatwork.html)
- [How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)
- [NG Gladiator](https://www.nationalgeographic.com/magazine/issue/august-2021)
- [NG Everest](https://www.nationalgeographic.com/magazine/issue/july-2020)
- [NG Anthropocene](https://education.nationalgeographic.org/resource/anthropocene/)  
<br>
<br>
<br>



## Visitor Map {#visitor-map}

<figure class="visitor-map">
  <a href="https://info.flagcounter.com/mUi7" target="_blank" rel="noopener noreferrer" aria-label="View visitor statistics">
    <img
      src="https://s01.flagcounter.com/map/mUi7/size_s/txt_6B7280/border_FFFFFF/pageviews_0/viewers_3/flags_0/"
      alt="Map of visitor countries"
      width="400"
      height="205"
      decoding="async">
  </a>
</figure>
