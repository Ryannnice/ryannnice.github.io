---
permalink: /tech-blog/
title: "Tech Blog"
author_profile: true
---

<div class="tech-blog">
  <section class="tech-blog__intro">
    <p class="tech-blog__lead">
      Engineering notes on coding agents, LLM routing, serving systems, and GPU/NPU kernels.
      The posts are reorganized from Renyuan's learning log into durable technical themes.
    </p>
    <nav class="tech-blog__nav" aria-label="Tech blog topics">
      <a href="#agent-engineering">Agent Engineering</a>
      <a href="#llm-routing">LLM Routing</a>
      <a href="#serving-deployment">Serving &amp; Deployment</a>
      <a href="#kernel-notes">CUDA / Triton / NPU</a>
      <a href="#transformer-foundations">Transformer Foundations</a>
      <a href="#timeline">Timeline</a>
    </nav>
  </section>

  <section class="tech-blog__section" id="featured">
    <h2 class="tech-blog__section-heading">Featured Posts</h2>
    <div class="tech-blog__grid">
      {% for post in site.posts %}
        {% if post.categories contains "tech-blog" %}
          {% if post.featured %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · {{ post.series }}</p>
              <h3 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 4 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="tech-blog__section">
    <h2 class="tech-blog__section-heading">Series</h2>

    <section class="tech-series" id="agent-engineering">
      <h3>Agent Engineering</h3>
      <div class="tech-blog__list">
        {% for post in site.posts %}
          {% if post.series == "Agent Engineering" %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · Priority {{ post.priority }}</p>
              <h4 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 5 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endfor %}
      </div>
    </section>

    <section class="tech-series" id="llm-routing">
      <h3>LLM Routing</h3>
      <div class="tech-blog__list">
        {% for post in site.posts %}
          {% if post.series == "LLM Routing" %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · Priority {{ post.priority }}</p>
              <h4 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 5 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endfor %}
      </div>
    </section>

    <section class="tech-series" id="serving-deployment">
      <h3>Serving &amp; Deployment</h3>
      <div class="tech-blog__list">
        {% for post in site.posts %}
          {% if post.series == "Serving & Deployment" %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · Priority {{ post.priority }}</p>
              <h4 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 5 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endfor %}
      </div>
    </section>

    <section class="tech-series" id="kernel-notes">
      <h3>CUDA / Triton / Kernel Notes</h3>
      <div class="tech-blog__list">
        {% for post in site.posts %}
          {% if post.series == "CUDA / Triton / Kernel Notes" %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · Priority {{ post.priority }}</p>
              <h4 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 5 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endfor %}
      </div>
    </section>

    <section class="tech-series" id="transformer-foundations">
      <h3>Transformer Foundations</h3>
      <div class="tech-blog__list">
        {% for post in site.posts %}
          {% if post.series == "Transformer Foundations" %}
            <article class="tech-card">
              <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · Priority {{ post.priority }}</p>
              <h4 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
              <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 5 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </article>
          {% endif %}
        {% endfor %}
      </div>
    </section>
  </section>

  <section class="tech-blog__section" id="all-posts">
    <h2 class="tech-blog__section-heading">All Posts</h2>
    <div class="tech-blog__list">
      {% for post in site.posts %}
        {% if post.categories contains "tech-blog" %}
          <article class="tech-card">
            <p class="tech-card__meta">{{ post.date | date: "%Y-%m-%d" }} · {{ post.series }} · Priority {{ post.priority }}</p>
            <h3 class="tech-card__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
            <p class="tech-card__excerpt">{{ post.excerpt | strip_html }}</p>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="tech-blog__section" id="timeline">
    <h2 class="tech-blog__section-heading">Timeline</h2>
    <ul class="tech-timeline">
      <li><strong>2025-03 to 2026-04:</strong> Workshop and Coding Agent experiments evolved from FastAPI wrappers to streaming Agent UX and an MVP rewrite.</li>
      <li><strong>2026-04:</strong> LLM routing work moved from survey notes to RouteLLM reproduction, semantic-router experiments, and vLLM Semantic Router architecture analysis.</li>
      <li><strong>2026-05:</strong> Serving and systems notes focused on vLLM, tensor parallelism, DeepSeek V4 Flash on Ascend, CUDA reduction, and normalization kernels.</li>
    </ul>
  </section>
</div>
