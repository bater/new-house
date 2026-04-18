---
title: 待確認事項
layout: default
nav_order: 6
permalink: /open-items/
---

# 待確認事項（跨頁彙整）
{: .no_toc }

自動從每一頁抓出未完成的 `- [ ]` 待辦項目。修改頁面後網站會自動更新。
{: .fs-5 .fw-300 }

<style>
  .open-items-group { margin-bottom: 2rem; }
  .open-items-group h2 { margin-bottom: 0.5rem; }
  .open-items-list { padding-left: 1.25rem; }
  .open-items-list li { margin: 0.25rem 0; }
</style>

{% assign newline = "
" %}
{% assign total_count = 0 %}
{% assign pages_sorted = site.pages | sort: "path" %}

{% for p in pages_sorted %}
{% unless p.url == page.url or p.path contains "_template" %}
  {% assign lines = p.content | split: newline %}
  {% assign count = 0 %}
  {% capture items %}{% for line in lines %}{% assign t = line | strip %}{% if t contains "- [ ]" %}{% assign count = count | plus: 1 %}<li>{{ t | remove_first: "- [ ]" | strip | markdownify | remove: "<p>" | remove: "</p>" }}</li>{% elsif t contains "task-list-item-checkbox" and t contains 'disabled="disabled"' %}{% assign after = t | split: '<input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />' %}{% if after.size > 1 %}{% assign payload = after[1] | split: "</li>" | first %}{% if payload != "" %}{% assign count = count | plus: 1 %}<li>{{ payload }}</li>{% endif %}{% endif %}{% endif %}{% endfor %}{% endcapture %}
  {% if count > 0 %}
  {% assign total_count = total_count | plus: count %}

<div class="open-items-group" markdown="0">
  <h2><a href="{{ p.url | relative_url }}">{{ p.title }}</a> · {{ count }} 項</h2>
  <ul class="open-items-list">{{ items }}</ul>
</div>

  {% endif %}
{% endunless %}
{% endfor %}

---

**總計 {{ total_count }} 項待確認**
