---
layout: page
title: Search
permalink: /search/
---

<div class="search-page">
  <div class="search-container">
    <input type="text" id="searchInput" placeholder="Search posts..." />
    <div id="searchResults"></div>
  </div>
</div>

<style>
.search-page {
  max-width: 800px;
  margin: 0 auto;
}

.search-container {
  margin: 20px 0;
}

#searchInput {
  width: 100%;
  padding: 12px 16px;
  font-size: 16px;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  background: var(--bg-secondary);
  color: var(--text-primary);
  outline: none;
  transition: border-color 0.2s ease;
}

#searchInput:focus {
  border-color: var(--accent-primary);
}

#searchResults {
  margin-top: 20px;
}

.search-result {
  padding: 16px;
  margin: 10px 0;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  transition: transform 0.1s ease;
}

.search-result:hover {
  transform: scale(0.98);
  background: var(--code-bg);
}

.search-result h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
}

.search-result h3 a {
  color: var(--text-primary);
  text-decoration: none;
}

.search-result h3 a:hover {
  color: var(--accent-primary);
}

.search-result .excerpt {
  color: var(--text-secondary);
  font-size: 14px;
  line-height: 1.5;
  margin-bottom: 8px;
}

.search-result .meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--text-secondary);
}

.search-result .tags {
  display: flex;
  gap: 4px;
}

.search-result .tag {
  background: var(--code-bg);
  color: var(--text-primary);
  padding: 2px 6px;
  border-radius: 12px;
  font-size: 11px;
  border: 1px solid var(--border-color);
}

.no-results {
  text-align: center;
  color: var(--text-secondary);
  font-style: italic;
  margin: 40px 0;
}
</style>

<script>
// Simple search implementation
let searchData = [];

// Load posts data
fetch('/search.json')
  .then(response => response.json())
  .then(data => {
    searchData = data;
  })
  .catch(error => {
    console.error('Error loading search data:', error);
    // Fallback: create search data from page context if available
    searchData = [
      {% for post in site.posts %}
      {
        "title": {{ post.title | jsonify }},
        "url": {{ post.url | jsonify }},
        "date": {{ post.date | date: "%B %d, %Y" | jsonify }},
        "excerpt": {{ post.excerpt | strip_html | truncatewords: 50 | jsonify }},
        "content": {{ post.content | strip_html | jsonify }},
        "tags": {{ post.tags | jsonify }}
      }{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ];
  });

function performSearch(query) {
  const results = document.getElementById('searchResults');
  
  if (!query.trim()) {
    results.innerHTML = '';
    return;
  }

  const searchTerms = query.toLowerCase().split(' ');
  const matches = searchData.filter(post => {
    const searchText = `${post.title} ${post.excerpt} ${post.content} ${post.tags.join(' ')}`.toLowerCase();
    return searchTerms.every(term => searchText.includes(term));
  });

  if (matches.length === 0) {
    results.innerHTML = '<div class="no-results">No posts found matching your search.</div>';
    return;
  }

  const resultsHTML = matches.map(post => `
    <div class="search-result">
      <h3><a href="${post.url}">${post.title}</a></h3>
      <div class="excerpt">${post.excerpt}</div>
      <div class="meta">
        <span class="date">${post.date}</span>
        <div class="tags">
          ${post.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
        </div>
      </div>
    </div>
  `).join('');

  results.innerHTML = resultsHTML;
}

// Search input handler
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  
  searchInput.addEventListener('input', function() {
    performSearch(this.value);
  });
  
  // Handle URL parameters for direct search
  const urlParams = new URLSearchParams(window.location.search);
  const query = urlParams.get('q');
  if (query) {
    searchInput.value = query;
    performSearch(query);
  }
});
</script> 