---
title: 待確認事項
layout: default
nav_order: 6
permalink: /open-items/
---

# 待確認事項（跨頁彙整）
{: .no_toc }

自動從每一頁抓出未完成的 `- [ ]` 待辦項目。牆面（AN/AE 等）會歸到各自的房間（A/B/C/D）下，方便按房間討論。產品頁的項目前會標示所屬小節的藍色 tag（因為單一頁上有多個產品）。
{: .fs-5 .fw-300 }

<style>
  .oi-group { margin-bottom: 2.5rem; }
  .oi-group > h2 { margin-bottom: 0.5rem; }
  .oi-subgroup { margin: 1rem 0 1rem 1rem; padding-left: 1rem; border-left: 3px solid #d5dde8; }
  .oi-subgroup h3 { font-size: 1.05rem; margin: 0.25rem 0 0.5rem; color: #374a63; font-weight: 600; }
  .oi-subgroup h3 a { color: inherit; text-decoration: none; border-bottom: 1px dotted #999; }
  .oi-list { padding-left: 1.2rem; margin: 0.3rem 0; }
  .oi-list li { margin: 0.35rem 0; line-height: 1.5; }
  .oi-list .tag {
    display: inline-block;
    background: #eaf1ff;
    color: #1a4a8a;
    padding: 1px 8px;
    border-radius: 4px;
    margin-right: 8px;
    font-size: 0.82em;
    font-weight: 600;
    white-space: nowrap;
  }
</style>

{% assign total_count = 0 %}
{% assign pages_sorted = site.pages | sort: "path" %}
{% assign room_codes = "A,B,C,D" | split: "," %}

{%- for rc in room_codes -%}
  {%- assign room_path_match = "rooms/" | append: rc | append: "." -%}
  {%- assign walls_path_match = "walls/" | append: rc -%}
  {%- assign room_page = pages_sorted | where_exp: "p", "p.path contains room_path_match" | first -%}
  {%- assign room_walls = pages_sorted | where_exp: "p", "p.path contains walls_path_match" -%}

  {%- capture inner -%}
    {%- if room_page -%}
      {%- capture r_items -%}{%- include open_items_body.html page_obj=room_page show_tag=false -%}{%- endcapture -%}
      {%- assign r_count = r_items | split: "<li>" | size | minus: 1 -%}
      {%- if r_count > 0 -%}
<div class="oi-subgroup">
  <h3><a href="{{ room_page.url | relative_url }}">{{ room_page.title }}</a> · {{ r_count }} 項</h3>
  <ul class="oi-list">{{ r_items }}</ul>
</div>
      {%- endif -%}
    {%- endif -%}
    {%- for w in room_walls -%}
      {%- capture w_items -%}{%- include open_items_body.html page_obj=w show_tag=false -%}{%- endcapture -%}
      {%- assign w_count = w_items | split: "<li>" | size | minus: 1 -%}
      {%- if w_count > 0 -%}
<div class="oi-subgroup">
  <h3><a href="{{ w.url | relative_url }}">{{ w.title }}</a> · {{ w_count }} 項</h3>
  <ul class="oi-list">{{ w_items }}</ul>
</div>
      {%- endif -%}
    {%- endfor -%}
  {%- endcapture -%}

  {%- assign group_count = inner | split: "<li>" | size | minus: 1 -%}

  {%- if group_count > 0 -%}
    {%- assign total_count = total_count | plus: group_count -%}

<div class="oi-group" markdown="0">
  <h2>{{ rc }} 房 · {{ group_count }} 項</h2>
  {{ inner }}
</div>

  {%- endif -%}
{%- endfor -%}

{%- for p in pages_sorted -%}
  {%- unless p.url == page.url or p.path contains "_template" or p.path contains "rooms/" or p.path contains "walls/" -%}
    {%- assign _p_show_tag = true -%}
    {%- if p.path contains "contract/" -%}{%- assign _p_show_tag = false -%}{%- endif -%}
    {%- capture p_items -%}{%- include open_items_body.html page_obj=p show_tag=_p_show_tag -%}{%- endcapture -%}
    {%- assign p_count = p_items | split: "<li>" | size | minus: 1 -%}
    {%- if p_count > 0 -%}
      {%- assign total_count = total_count | plus: p_count -%}

<div class="oi-group" markdown="0">
  <h2><a href="{{ p.url | relative_url }}">{{ p.title }}</a> · {{ p_count }} 項</h2>
  <ul class="oi-list">{{ p_items }}</ul>
</div>

    {%- endif -%}
  {%- endunless -%}
{%- endfor -%}

---

**總計 {{ total_count }} 項待確認**
