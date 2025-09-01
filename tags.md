---
layout: page
title: Tags
permalink: /tags/
---

<div class="tags-page">
  {% assign tag_counts = site.tags | map: 'size' %}
  {% assign sorted_tags = site.tags | sort %}
  
  <div class="tag-cloud">
    {% for tag in sorted_tags %}
      {% assign tag_name = tag[0] %}
      {% assign posts = tag[1] %}
      {% assign post_count = posts | size %}
      
      <div class="tag-item">
        <a href="#{{ tag_name | slugify }}" class="tag-link">
          {{ tag_name }} <span class="tag-count">({{ post_count }})</span>
        </a>
      </div>
    {% endfor %}
  </div>

  <div class="tag-sections">
    {% for tag in sorted_tags %}
      {% assign tag_name = tag[0] %}
      {% assign posts = tag[1] %}
      
      <section id="{{ tag_name | slugify }}" class="tag-section">
        <h2>{{ tag_name }} <span class="tag-count">({{ posts | size }})</span></h2>
        <ul class="post-list">
          {% for post in posts %}
            <li>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
            </li>
          {% endfor %}
        </ul>
      </section>
    {% endfor %}
  </div>
</div>

<style>
.tags-page {
  max-width: 800px;
  margin: 0 auto;
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 40px;
  padding: 20px;
  background: var(--code-bg);
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.tag-item {
  display: inline-block;
}

.tag-link {
  display: inline-block;
  padding: 6px 12px;
  background: var(--bg-secondary);
  color: var(--text-primary);
  text-decoration: none;
  border-radius: 16px;
  font-size: 14px;
  border: 1px solid var(--border-color);
  transition: all 0.2s ease;
}

.tag-link:hover {
  background: var(--accent-primary);
  color: var(--bg-primary);
  transform: scale(0.98);
}

.tag-count {
  font-weight: bold;
  color: var(--text-secondary);
}

.tag-sections {
  margin-top: 40px;
}

.tag-section {
  margin-bottom: 40px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
}

.tag-section h2 {
  color: var(--text-primary);
  margin-bottom: 20px;
  font-size: 24px;
}

.post-list {
  list-style: none;
  padding: 0;
}

.post-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  border-bottom: 1px solid var(--border-color);
}

.post-list li:last-child {
  border-bottom: none;
}

.post-list a {
  color: var(--text-primary);
  text-decoration: none;
  font-weight: 500;
  flex: 1;
}

.post-list a:hover {
  color: var(--accent-primary);
}

.post-date {
  color: var(--text-secondary);
  font-size: 14px;
  margin-left: 20px;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .post-list li {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .post-date {
    margin-left: 0;
    margin-top: 4px;
  }
  
  .tag-cloud {
    padding: 15px;
  }
}
</style> 