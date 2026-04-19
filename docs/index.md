---
title: 首頁
layout: default
nav_order: 1
description: "2F/C戶 雲川集合住宅 裝修工作區"
permalink: /
---

# 2F/C戶 · 雲川集合住宅
{: .fs-8 }

裝修細節工作區 — 收集合約條款、每面牆的細部決策、參考產品與靈感圖，方便與設計師討論對齊。
{: .fs-5 .fw-300 }

[變更日誌](./changelog/){: .btn .btn-primary .mr-2 }
[待確認](./open-items/){: .btn .mr-2 }
[預算](./budget/){: .btn .mr-2 }
[合約](./contract/){: .btn .mr-2 }
[房間](./rooms/){: .btn }

---

## 房間 / 牆面命名

以房間代號 + 方位命名，共 5 房 × 4 牆 = 20 面牆。代號跳過 E（保留給方位）。

| 房間 | 代號 | 用途 |
|---|---|---|
| 客廳 + 廚房 | A | 公共區 |
| 主臥房 | B | 東側 |
| 次臥房 | C | 西側 |
| 衛浴 | D | 中央 |
| 陽台 | F | 東側外部（洗衣 / 冷氣外機 / 貓砂 / 曬衣） |

方位：**N** 北 / **E** 東 / **S** 南 / **W** 西 → 例：`AN` = A 房北牆、`BW` = 主臥西牆、`FW` = 陽台西牆（與 AE 共用）。

## 平面概略

<div style="max-width: 720px;">
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="2F/C戶 平面圖" style="width: 100%; height: auto; font-family: system-ui, -apple-system, 'PingFang TC', sans-serif;">
  <rect x="0" y="0" width="800" height="500" fill="#fafafa"/>

  <!-- North arrow -->
  <g transform="translate(750, 40)">
    <text x="0" y="0" text-anchor="middle" font-size="14" font-weight="bold" fill="#666">N</text>
    <line x1="0" y1="10" x2="0" y2="35" stroke="#666" stroke-width="2"/>
    <polygon points="0,5 -5,15 5,15" fill="#666"/>
  </g>

  <!-- Building outline (L-shape) -->
  <path d="M 240,60 L 640,60 L 640,440 L 60,440 L 60,230 L 240,230 Z"
        fill="none" stroke="#333" stroke-width="3"/>

  <!-- Room A (客廳 + 廚房) -->
  <rect x="240" y="60" width="400" height="170" fill="#E3F2FD" stroke="#333" stroke-width="1.5"/>
  <line x1="400" y1="60" x2="400" y2="230" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="440" y="130" text-anchor="middle" font-size="22" font-weight="bold" fill="#1565C0">A</text>
  <text x="440" y="150" text-anchor="middle" font-size="13" fill="#333">客廳 + 廚房</text>
  <text x="320" y="195" text-anchor="middle" font-size="11" fill="#666" font-style="italic">廚房</text>
  <text x="525" y="195" text-anchor="middle" font-size="11" fill="#666" font-style="italic">客廳</text>

  <!-- Room F (陽台, outside AE, same N-S extent as A) -->
  <rect x="645" y="60" width="60" height="170" fill="#FFF3E0" stroke="#333" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="675" y="130" text-anchor="middle" font-size="18" font-weight="bold" fill="#E65100">F</text>
  <text x="675" y="150" text-anchor="middle" font-size="10" fill="#333">陽台</text>
  <text x="675" y="165" text-anchor="middle" font-size="8" fill="#999">(戶外)</text>

  <!-- Room C (次臥) -->
  <rect x="60" y="230" width="200" height="210" fill="#F3E5F5" stroke="#333" stroke-width="1.5"/>
  <text x="160" y="330" text-anchor="middle" font-size="22" font-weight="bold" fill="#6A1B9A">C</text>
  <text x="160" y="350" text-anchor="middle" font-size="13" fill="#333">次臥</text>

  <!-- Alley 走廊 -->
  <rect x="260" y="230" width="130" height="40" fill="#FFF9C4" stroke="#333" stroke-width="1.5"/>
  <text x="325" y="256" text-anchor="middle" font-size="11" fill="#795548" font-style="italic">走廊</text>

  <!-- Room D (衛浴) — shorter N-S -->
  <rect x="260" y="270" width="130" height="170" fill="#E0F7FA" stroke="#333" stroke-width="1.5"/>
  <text x="325" y="345" text-anchor="middle" font-size="22" font-weight="bold" fill="#00695C">D</text>
  <text x="325" y="365" text-anchor="middle" font-size="13" fill="#333">衛浴</text>

  <!-- Room B (主臥) -->
  <rect x="390" y="230" width="250" height="210" fill="#E8F5E9" stroke="#333" stroke-width="1.5"/>
  <text x="515" y="330" text-anchor="middle" font-size="22" font-weight="bold" fill="#2E7D32">B</text>
  <text x="515" y="350" text-anchor="middle" font-size="13" fill="#333">主臥</text>

  <!-- Wall labels -->
  <g font-size="12" fill="#0D47A1" font-weight="600">
    <text x="440" y="50" text-anchor="middle">AN</text>
    <text x="648" y="150" text-anchor="start">AE</text>
    <text x="440" y="223" text-anchor="middle">AS</text>
    <text x="232" y="150" text-anchor="end">AW</text>

    <text x="515" y="245" text-anchor="middle">BN</text>
    <text x="648" y="340" text-anchor="start">BE</text>
    <text x="515" y="458" text-anchor="middle">BS</text>
    <text x="398" y="340" text-anchor="start">BW</text>

    <text x="160" y="223" text-anchor="middle">CN</text>
    <text x="252" y="340" text-anchor="end">CE</text>
    <text x="160" y="458" text-anchor="middle">CS</text>
    <text x="52" y="340" text-anchor="end">CW</text>

    <text x="325" y="285" text-anchor="middle" font-size="10">DN</text>
    <text x="384" y="315" text-anchor="end" font-size="10">DE</text>
    <text x="325" y="458" text-anchor="middle">DS</text>
    <text x="266" y="315" text-anchor="start" font-size="10">DW</text>
  </g>
</svg>
</div>

### 空間關係

- **A 房** 寬度 ≈ **D + B**（A 只佔北側的 D + B 上方，不涵蓋 C 上方）
- **C 房向西突出**：全棟總寬 **C + D + B > A**（L 形）
- **C 寬度 > D 寬度**
- **D 南北深度 < C 和 B**：D 較短，北側留出空間給走廊
- **走廊**（黃色帶）位於 D 北側 — 也是 **B/C 共用更衣區**（見 [D 房](./rooms/D/)）
- **南牆共線**：CS、DS、BS 同一水平線
- **F 陽台** 位於 AE 牆外側（戶外，獨立成房）— 容納洗衣機 / 冷氣外機 / 貓砂盆 / 熱水器

### 真實建築平面圖（比例參考）

![2F/C戶 建築平面圖 H=360 cm](./assets/images/contract/floor-plan-arch.png){: .hover-lightbox-trigger width="600" }

樓高 **H = 360 cm**，RC 牆 15 cm。完整合約圖面在 [合約文件](./contract/)。

## 快速導覽

| 區塊 | 用途 |
|---|---|
| [變更日誌](./changelog/) | 時間序看哪些區塊有新細節（可個別標示已讀 / 分享單筆永久連結） |
| [待確認事項](./open-items/) | 自動彙整所有頁面的 `- [ ]` 待辦，按房間分組 |
| [預算總覽](./budget/) | 已購家具、裝修、家電合計與未納入項目 |
| [合約文件](./contract/) | 估價單、設計流程、里程碑、DWG/PDF 原檔 |
| [房間](./rooms/) | A/B/C/D/F 五房整合視角 — 地坪、天花、燈光、空調；每房下展開其 4 面牆 |
| [參考](./references/) | 參考產品連結、靈感圖、色卡 |

## 使用方式

- **上傳圖片**：丟到 `docs/assets/images/<主題>/`，用 `![說明](../assets/images/主題/檔名.jpg)` 引用
- **修改牆面頁**：編輯 `walls/<代號>.md`（如 `walls/AN.md`）
- **跨頁連結**：用 `[連結](../walls/AN.md)` 形式（帶 `.md` 讓 jekyll-relative-links 改寫為正確 URL）
- **變更日誌刷新**：commit 後執行 `./scripts/gen-changelog` 再 push
- **本地預覽**：`./scripts/preview`（clean rebuild + livereload）
- **與設計師分享**：整份網站發佈到 GitHub Pages，直接丟連結
