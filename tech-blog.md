---
permalink: /tech-blog/
title: "Tech Blog"
author_profile: true
---

<div class="tech-blog tech-blog--xhs">
  <section class="tech-hero">
    <p class="tech-hero__eyebrow">Renyuan's Engineering Field Notes</p>
    <p class="tech-hero__lead">
      A card-based map of coding agents, LLM routing, serving systems, CUDA/Triton kernels,
      and transformer foundations. Every date in <code>Renyuan_Log.md</code> is represented below.
    </p>
    <div class="tech-stats" aria-label="Tech blog coverage statistics">
      <span><strong>53</strong> log days</span>
      <span><strong>20</strong> deep dives</span>
      <span><strong>20</strong> concepts</span>
      <span><strong>5</strong> series</span>
    </div>
    <nav class="tech-blog__nav" aria-label="Tech blog topics">
      <a href="#deep-dives">Deep Dives</a>
      <a href="#concept-map">Concept Map</a>
      <a href="#log-map">Full Log Map</a>
      <a href="{{ '/tech-blog/full-log/' | relative_url }}">Original Archive</a>
    </nav>
  </section>

  <section class="tech-blog__section" id="deep-dives">
    <div class="tech-section-head">
      <p class="tech-section-head__eyebrow">Curated Posts</p>
      <h2>Deep Dives</h2>
      <p>Longer articles distilled from multiple related log dates.</p>
    </div>
    <div class="xhs-masonry">
      {% for post in site.posts %}
        {% if post.categories contains "tech-blog" %}
          <article class="xhs-card xhs-card--post">
            <a class="xhs-card__cover" href="{{ post.url | relative_url }}" aria-label="{{ post.title }}">
              <span>{{ post.series }}</span>
            </a>
            <div class="xhs-card__body">
              <p class="xhs-card__meta">{{ post.date | date: "%Y-%m-%d" }} · {{ post.priority }}</p>
              <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
              <p>{{ post.excerpt | strip_html }}</p>
              <div class="tech-tags">
                {% for tag in post.tags limit: 4 %}
                  <span class="tech-tag">{{ tag }}</span>
                {% endfor %}
              </div>
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="tech-blog__section" id="concept-map">
    <div class="tech-section-head">
      <p class="tech-section-head__eyebrow">Supplement</p>
      <h2>Concept Map</h2>
      <p>Short explanations added to fill gaps where the raw log only had keywords, links, or partial notes.</p>
    </div>
    <div class="xhs-masonry xhs-masonry--compact">
      {% for item in site.data.tech_concepts %}
        <article class="xhs-card xhs-card--concept">
          <div class="xhs-card__body">
            <p class="xhs-card__meta">{{ item.area }}</p>
            <h3>{{ item.concept }}</h3>
            <p>{{ item.summary }}</p>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section class="tech-blog__section" id="log-map">
    <div class="tech-section-head">
      <p class="tech-section-head__eyebrow">Complete Coverage</p>
      <h2>Full Log Map</h2>
      <p>Each card corresponds to one dated section in <code>Renyuan_Log.md</code>. Timeline-only cards preserve context without forcing weak notes into articles.</p>
    </div>
    <div class="xhs-masonry xhs-masonry--log">
      {% for item in site.data.tech_log %}
        <article class="xhs-card xhs-card--log xhs-card--{{ item.slug }}" id="log-{{ item.date }}">
          <div class="xhs-card__body">
            <p class="xhs-card__meta">{{ item.date }} · {{ item.series }} · {{ item.status }}</p>
            <h3>{{ item.title }}</h3>
            <p>{{ item.summary }}</p>
            <div class="tech-tags">
              {% for concept in item.concepts %}
                <span class="tech-tag">{{ concept }}</span>
              {% endfor %}
            </div>
            <p class="xhs-card__source">
              <a href="{{ '/tech-blog/full-log/' | relative_url }}#log-{{ item.date }}">Open original section</a>
            </p>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
</div>
