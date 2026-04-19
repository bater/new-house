---
title: 變更日誌
layout: default
nav_order: 2
permalink: /changelog/
---

# 變更日誌
{: .no_toc }

本頁由 `scripts/gen-changelog` 從 git commit history 生成。藍色邊框為**你尚未讀過的變更**，點右上「標示全部為已讀」後就只剩下新的改動突顯。已讀狀態存在瀏覽器 cookie，一年有效。
{: .fs-5 .fw-300 }

<style>
  .cl-actions {
    position: sticky; top: 0.5em; margin: 1em 0; padding: 0.6em 1em;
    background: #fff; border: 1px solid #d5dde8; border-radius: 6px;
    display: flex; gap: 0.6em; align-items: center; z-index: 10;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }
  .cl-actions button {
    padding: 0.35em 0.9em; cursor: pointer; border-radius: 4px;
    border: 1px solid #1565C0; background: #fff; color: #1565C0;
    font-size: 0.9em;
  }
  .cl-actions button:hover { background: #1565C0; color: #fff; }
  .cl-count { margin-left: auto; color: #777; font-size: 0.88em; }
  .cl-count b { color: #1565C0; }

  .cl-day { margin: 1.5em 0 0.3em; padding-bottom: 0.2em; border-bottom: 1px solid #e3e8ef; font-size: 1rem; color: #555; font-weight: 600; }

  .cl-commit {
    position: relative;
    border-left: 4px solid #d5dde8;
    padding: 0.7em 2.8em 0.7em 1em; margin: 0.6em 0;
    background: #fafbfc; border-radius: 0 4px 4px 0;
    transition: all 0.2s;
  }
  .cl-commit.new {
    border-left-color: #1565C0;
    background: #eef5ff;
  }
  .cl-commit.new .cl-subj::before {
    content: "NEW";
    display: inline-block;
    background: #1565C0; color: #fff;
    font-size: 0.72em; padding: 1px 6px; border-radius: 3px;
    margin-right: 7px; vertical-align: middle; font-weight: 700;
    letter-spacing: 0.05em;
  }
  .cl-toggle {
    position: absolute; top: 8px; right: 8px;
    border: 1px solid #c5cfdd; background: #fff; color: #4a5566;
    font-size: 0.72em; font-weight: 600; letter-spacing: 0.04em;
    padding: 2px 8px; border-radius: 3px; cursor: pointer;
    transition: all 0.15s;
    font-family: inherit;
  }
  .cl-toggle:hover { border-color: #1565C0; color: #1565C0; }
  .cl-commit.new .cl-toggle { border-color: #1565C0; color: #1565C0; }
  .cl-commit.new .cl-toggle:hover { background: #1565C0; color: #fff; }

  /* Permalink anchor on meta line */
  .cl-meta a.cl-perma {
    color: inherit; text-decoration: none;
    border-bottom: 1px dotted #bbb;
    padding-bottom: 1px;
  }
  .cl-meta a.cl-perma:hover { color: #1565C0; border-bottom-color: #1565C0; }

  /* Highlight when linked to via URL hash (#abc1234) */
  .cl-commit:target {
    border-left-color: #e8a100;
    background: #fff7e0;
    box-shadow: 0 0 0 2px rgba(232, 161, 0, 0.35);
    scroll-margin-top: 72px;
    animation: cl-flash 1.4s ease-out;
  }
  @keyframes cl-flash {
    0%   { background: #ffe680; }
    100% { background: #fff7e0; }
  }
  .cl-meta { color: #888; font-size: 0.82em; margin-bottom: 0.25em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  .cl-subj { font-weight: 600; font-size: 1.02em; }
  .cl-body { color: #4a5566; font-size: 0.92em; margin-top: 0.4em; white-space: pre-wrap; }
  .cl-tags { margin-top: 0.5em; display: flex; flex-wrap: wrap; gap: 4px; }
  .cl-tag {
    background: #eaf1ff; color: #1a4a8a; padding: 1px 8px; border-radius: 3px;
    font-size: 0.78em; font-weight: 500; white-space: nowrap;
  }
  a.cl-tag-link { text-decoration: none; }
  a.cl-tag-link:hover { background: #1565C0; color: #fff; }
</style>

<div class="cl-actions">
  <button id="cl-mark-all">標示全部為已讀</button>
  <button id="cl-unmark-all">重設為未讀</button>
  <span class="cl-count"><b id="cl-new-count">…</b> 項未讀 / <span id="cl-total-count">…</span> 項</span>
</div>



<h2 class="cl-day" markdown="0">2026-04-19</h2>

<div class="cl-commit" id="1f3a96a" data-hash="1f3a96a">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#1f3a96a" title="複製此變更的永久連結">1f3a96a</a> · 2026-04-19 22:16</div>
  <div class="cl-subj">D 衛浴實景 + 馬桶上方軟裝留空</div>
  <div class="cl-body">- 淺灰石紋大板磁磚 + 長條地排 + 乾濕分離 + 黑石檯面白下嵌盆
- 對外窗需釐清哪一面 (DN/DS/DE/DW)
- 馬桶上方不做固定吊櫃 — 由軟裝 (層架/磁吸/壁掛籃) 彈性處理</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/D/' | relative_url }}">房間 D</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="05ee92f" data-hash="05ee92f">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#05ee92f" title="複製此變更的永久連結">05ee92f</a> · 2026-04-19 22:11</div>
  <div class="cl-subj">Fix broken relative wall/room links by switching to .md extension</div>
  <div class="cl-body">Previous form [AN](../walls/AN) stayed literal in the rendered HTML,
so from /rooms/A/ it resolved to /rooms/walls/AN (404). The
jekyll-relative-links plugin only rewrites links that point to an
actual .md file, so any bare path without extension was left alone.

Bulk-swap 20+ wall/room links to the .md form — the plugin now emits
absolute /new-house/walls/XX/ URLs across all room and wall pages,
plus budget and products cross-links.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/budget/' | relative_url }}">預算</a><a class="cl-tag cl-tag-link" href="{{ '/contract/estimate/' | relative_url }}">工程估價單</a><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/D/' | relative_url }}">房間 D</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/F/' | relative_url }}">房間 F</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/' | relative_url }}">房間目錄</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BE/' | relative_url }}">牆 BE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BS/' | relative_url }}">牆 BS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CE/' | relative_url }}">牆 CE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CN/' | relative_url }}">牆 CN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CS/' | relative_url }}">牆 CS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FE/' | relative_url }}">牆 FE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FN/' | relative_url }}">牆 FN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FS/' | relative_url }}">牆 FS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FW/' | relative_url }}">牆 FW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/' | relative_url }}">牆面總表</a></div>
</div>

<div class="cl-commit" id="ce4a44b" data-hash="ce4a44b">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#ce4a44b" title="複製此變更的永久連結">ce4a44b</a> · 2026-04-19 22:02</div>
  <div class="cl-subj">AN 上掀站立桌: 三種機構參考 + 比較表</div>
  <div class="cl-body">- 方案 1 (鉸鍊 180° 反折): 收起是平板視覺 — 用戶偏好
- 方案 2 (金屬線張力支撐): 備案, 收起會下垂, 需客製托架卡卡扣槽
- 方案 3 (橫向溝槽插拔): 最單純零活動件, 與 AN 卡扣系統邏輯天然契合,
  高度任意可調, 但需加深書牆深度

三方案比較表: 收納視覺 / 機構複雜度 / 高度可調 / AN 系統相容</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><span class="cl-tag">圖片 ×6</span></div>
</div>

<div class="cl-commit" id="aae7e77" data-hash="aae7e77">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#aae7e77" title="複製此變更的永久連結">aae7e77</a> · 2026-04-19 21:48</div>
  <div class="cl-subj">BS/CS/CW site photos + 壁床施工前牆面淨空 + 水電重配</div>
  <div class="cl-body">- BS real photo: 對外窗 (黑框方窗, 只右上一小段外推可開). 加窗邊
  矮櫃/坐臥窗 TODO, 面鄰舊棟 + 鐵窗需私密處理.
- CS/CW 角落照: CS = 黑框細長直立窗面街 (可見「港」字招牌, 採光佳但
  噪音/隱私議題). CW 白牆乾淨, 底部 3 個插座 + 右上可能預留冷媒/新風
  孔需釐清.
- BE + CW 加「壁床施工前牆面淨空 + 水電重配」: 牆面貼齊、原插座封死
  移開、水電重新配線到其他牆, 追加估價項目 (目前估價單未含).</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/walls/BE/' | relative_url }}">牆 BE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BS/' | relative_url }}">牆 BS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CS/' | relative_url }}">牆 CS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><span class="cl-tag">圖片 ×2</span></div>
</div>

<div class="cl-commit" id="11919cf" data-hash="11919cf">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#11919cf" title="複製此變更的永久連結">11919cf</a> · 2026-04-19 21:04</div>
  <div class="cl-subj">Design pass: ceilings, windows, 投影布幕 → AE, 玄關, C 房策略</div>
  <div class="cl-body">Ceilings:
- AN goes full-height; decorative ceiling sets back at AN/AE corners
- B/C prefer no dropped ceiling (paint RC + ceiling-mount lighting)
- AE/AS 轉角的白盒子原來是「新風系統」不是分離式冷氣 — 跨站校正
  (AE/AS/A/F 相關段落全部更新)

投影布幕: moved from AW to AE, shares the 升降曬衣桿 pole (no power
 needed, height controlled by pole). AW 不再預留內嵌盒; CE 白牆可兼作
 C 房投影幕面.

A 玄關 (AN 西端對講機段): 鞋櫃 6-8 雙 + 上櫃放包 / 購物袋 + 雨傘架
 with 滴水盤, 不常用鞋轉放 C 儲藏夾層.

B/C 窗戶: evaluate enlarging 建商原窗 可開啟面積 (subject to not
 breaking 建物外觀). CS 已確認為對外窗.

C 房空間策略:
- 重點 CW (KL 120 翻轉床 + 架高夾層上層), 層架下緣 ≥140-150 cm 保書桌可用
- CE 留白 (通風 + 投影幕面), CN 樓梯櫃整合上層取物 + 每階收納抽屜
- CS 對外窗加大

F: 貓砂抽屜櫃 momo ref; A 客廳空調室內機位置重新開放 (原以為是冷氣
 的 AE/AS 轉角其實是新風).</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/F/' | relative_url }}">房間 F</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CE/' | relative_url }}">牆 CE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CN/' | relative_url }}">牆 CN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CS/' | relative_url }}">牆 CS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="0b2395d" data-hash="0b2395d">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#0b2395d" title="複製此變更的永久連結">0b2395d</a> · 2026-04-19 15:00</div>
  <div class="cl-subj">Consolidate 共用更衣區 into D + fix sliding-door direction (west, not north)</div>
  <div class="cl-body">- 共用更衣區 now lives only on rooms/D (it&#x27;s physically in the alley
  outside D&#x27;s door, not inside B or C). B/C keep one-line pointers to D
  to avoid duplicate 待辦 across pages.
- Sliding door retracts 面北時往左(西) into AW 冰箱南側縫隙, not 朝北.
  Added explicit &quot;需實際評估冰箱空間&quot; TODOs on D/DN/AW/AS — the fridge
  南側 縫隙 width must physically accommodate door + mirror.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/D/' | relative_url }}">房間 D</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a></div>
</div>

<div class="cl-commit" id="d9c6d69" data-hash="d9c6d69">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#d9c6d69" title="複製此變更的永久連結">d9c6d69</a> · 2026-04-19 14:53</div>
  <div class="cl-subj">Flesh out F: 一對三冷氣 (Panasonic CU-3J90 候選) + 三層配置 ref + 貓門</div>
  <div class="cl-body">- F 空調: 一對三 1 outdoor + 3 indoor (A/B/C), 噸數以 2 間同開為上限,
  三間同開接受略不夠冷. Panasonic CU-3J90BHA2/BCA2 (9.0kW, R32) 納入
  候選 — 室內機建議配比 36+28+22 等
- F 三層配置: 加入堆疊參考圖並註明本案差異 (中層為洗脫烘而非第二台冷氣,
  最下方預留貓砂盆)
- FW 貓門: 樂天 linzhishe 四段鎖寵物門連結, 3 種安裝選項, 黑色客製待定</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/F/' | relative_url }}">房間 F</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FW/' | relative_url }}">牆 FW</a><span class="cl-tag">圖片 ×3</span></div>
</div>

<div class="cl-commit" id="809a05b" data-hash="809a05b">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#809a05b" title="複製此變更的永久連結">809a05b</a> · 2026-04-19 14:40</div>
  <div class="cl-subj">Restructure site: nest walls under rooms, add F (陽台) as separate room</div>
  <div class="cl-body">Sidebar changes:
- Reorder top level: 首頁 → 待確認 → 預算 → 合約 → 房間 → 參考
- Walls now nest under their rooms (A/B/C/D/F) via parent + grand_parent;
  walls/index hidden from nav (kept as reference table)
- Swap 房間 / 代號 columns in home page naming table so names read naturally

Add F (陽台) as its own room so 洗衣機 / 冷氣外機 / 貓砂 / 瓦斯熱水器
 / 隱形鐵窗 get dedicated pages instead of crowding AE:
- rooms/F.md: 三層垂直堆疊配置、貓門、雨遮、排水、現場照片
- walls/FN: 瓦斯管線預留（熱水器 櫻花/Panasonic 待定、洗脫烘瓦斯線）
- walls/FE: 直立式隱形鐵窗（鋼絲地板→屋簷、線距 ≤6cm、黑色）
- walls/FS/FW: stubs; FW = AE 的陽台側，記貓門相關決策
- AE trimmed to 客廳側決策（門收邊 + 天花冷氣 + 室內升降曬衣桿）
- 代號跳過 E（保留作方位 E=東），故 5 房 = ABCDF, 20 面牆</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/budget/' | relative_url }}">預算</a><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a><a class="cl-tag cl-tag-link" href="{{ '/open-items/' | relative_url }}">待確認</a><a class="cl-tag cl-tag-link" href="{{ '/references/' | relative_url }}">參考</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/D/' | relative_url }}">房間 D</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/F/' | relative_url }}">房間 F</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/' | relative_url }}">房間目錄</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BE/' | relative_url }}">牆 BE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BN/' | relative_url }}">牆 BN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BS/' | relative_url }}">牆 BS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CE/' | relative_url }}">牆 CE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CN/' | relative_url }}">牆 CN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CS/' | relative_url }}">牆 CS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DE/' | relative_url }}">牆 DE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DS/' | relative_url }}">牆 DS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DW/' | relative_url }}">牆 DW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FE/' | relative_url }}">牆 FE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FN/' | relative_url }}">牆 FN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FS/' | relative_url }}">牆 FS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/FW/' | relative_url }}">牆 FW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/' | relative_url }}">牆面總表</a><span class="cl-tag">圖片 ×2</span></div>
</div>

<div class="cl-commit" id="48d2c8a" data-hash="48d2c8a">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#48d2c8a" title="複製此變更的永久連結">48d2c8a</a> · 2026-04-19 14:21</div>
  <div class="cl-subj">Add simple daily-rotating password gate (deterrent, not security)</div>
  <div class="cl-body">Password = browser-local yyyyMMdd. 30-day cookie on success. No
format hint shown to strangers; only people told the pattern can
guess it. Client-side only — anyone with devtools can bypass, so
this is purely a polite &quot;not for you&quot; sign for a public GH Pages URL.</div>
</div>

<div class="cl-commit" id="0924934" data-hash="0924934">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#0924934" title="複製此變更的永久連結">0924934</a> · 2026-04-19 14:14</div>
  <div class="cl-subj">Record purchases: Panasonic NR-E507XT-W1 冰箱 + 合豐訂單 60646</div>
  <div class="cl-body">- Panasonic NR-E507XT-W1 (輕暖白, 502L, W650×D699×H1828)
  via 燦坤提貨券 NT$47,872, 需 2027-01-07 前換貨
- 合豐訂單 60646 (2026-03-29 訂金): TA-175 / KL 120 +床頭片(FINLAND)
  / LD002 (NOCE-DESERTO) +床頭片(PLUM), 共 NT$735,700,
  交期 6–8 個月 → 2026-09-29~2026-11-29 到貨, 尾款 NT$367,700 待付
- Budget 小計更新: 已知合計 NT$1,604,337 (含冰箱)
- PII 原件 (提貨券 barcode / 訂單含姓名電話) 存於 contract/private/ 僅本地</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/budget/' | relative_url }}">預算</a><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="c795588" data-hash="c795588">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#c795588" title="複製此變更的永久連結">c795588</a> · 2026-04-19 14:14</div>
  <div class="cl-subj">Log design directions across 6 walls (客廳/廚房/陽台 + kid/cat safety)</div>
  <div class="cl-body">- AN: 書牆軌道燈供電方案、森林風 / 純深色背板考量、頂天立地置物架
  ref、Dyson 支架釘牆（靠 AE 角落）
- AE: 陽台三層配置（冷氣室外機 / 洗衣機 / 貓砂抽屜）+ 貓門 + 防潑雨
- AS: 客廳↔主臥上方通風採光窗（避貓 / 可全暗 / 避開錨點）；
  拉門收納口袋由 AS 改到冰箱縫隙，AS 與 BN 保留完整
- AW: 磁吸收納牆、冰箱散熱接新風防貓；冰箱位置確定 AW 靠 AS 側、
  背靠 W 右開東；冰箱架高給掃地機器人 + 重型滑軌前推構想
- BW: 頂天立地掛衣架 ref（展示雙層吊桿 + 網籃的分層邏輯）
- DN: 拉門口袋改到冰箱縫隙</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><span class="cl-tag">圖片 ×3</span></div>
</div>

<div class="cl-commit" id="007e158" data-hash="007e158">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#007e158" title="複製此變更的永久連結">007e158</a> · 2026-04-19 00:48</div>
  <div class="cl-subj">Refresh CLAUDE.md + README to match current workspace</div>
  <div class="cl-body">Correct stale bits: wall filenames are &lt;ROOM&gt;&lt;DIR&gt; (AN.md), not
living-north.md; image paths must be relative (baseurl /new-house);
./scripts/preview is the supported local workflow (not bundle init).
Also surface budget.md, open-items.md, _includes/, private/ folder.</div>
</div>

<div class="cl-commit" id="fe39b10" data-hash="fe39b10">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#fe39b10" title="複製此變更的永久連結">fe39b10</a> · 2026-04-19 00:45</div>
  <div class="cl-subj">Sync budget page: LD002 → BE, drop resolved 架高 open item</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/budget/' | relative_url }}">預算</a></div>
</div>

<div class="cl-commit" id="cff7f85" data-hash="cff7f85">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#cff7f85" title="複製此變更的永久連結">cff7f85</a> · 2026-04-19 00:44</div>
  <div class="cl-subj">Log AS↔DN sliding-door + full mirror reference image on DN</div>
  <div class="cl-body">Barn-door style reference (ceiling track only, dark metal frame
around full-length mirror, door reveals space behind). Matches
the design brief documented earlier in both AS and DN pages.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="b7a366b" data-hash="b7a366b">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#b7a366b" title="複製此變更的永久連結">b7a366b</a> · 2026-04-19 00:44</div>
  <div class="cl-subj">Confirm 架高工程 = C 房: 上儲藏 / 下床+書桌</div>
  <div class="cl-body">The 架高 line in the contract estimate (NT$56,000) is for C room:
upper loft is storage, lower level is the Murphy bed + desk on CW.
Update the CW wall, C room page, and estimate cross-references so
the vertical layout is consistent across pages.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/estimate/' | relative_url }}">工程估價單</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a></div>
</div>

<div class="cl-commit" id="bf26939" data-hash="bf26939">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#bf26939" title="複製此變更的永久連結">bf26939</a> · 2026-04-19 00:43</div>
  <div class="cl-subj">Pin LD002 翻轉床 to BE; BW is 衣櫃</div>
  <div class="cl-body">Confirm LD002 installs on BE (east wall); BW stays dedicated to
modular wardrobe (Elfa/Boaxel style), so the two walls are
complementary rather than competing for the same function.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BE/' | relative_url }}">牆 BE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a></div>
</div>

<div class="cl-commit" id="8ce67c0" data-hash="8ce67c0">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#8ce67c0" title="複製此變更的永久連結">8ce67c0</a> · 2026-04-19 00:43</div>
  <div class="cl-subj">Refine open-items aggregator: nest walls under rooms, selective tags, hide (待填)</div>
  <div class="cl-body">Group walls (AN/AE/...) as sub-entries under their room (A/B/C/D).
Blue section tag now only shows for product pages (where one page
covers many items); rooms, walls, and contract pages rely on the group
heading. Skip any &quot;- [ ] (待填)&quot; placeholder lines.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/open-items/' | relative_url }}">待確認</a></div>
</div>

<div class="cl-commit" id="8f2dbd3" data-hash="8f2dbd3">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#8f2dbd3" title="複製此變更的永久連結">8f2dbd3</a> · 2026-04-19 00:09</div>
  <div class="cl-subj">Add /budget/ rollup page</div>
  <div class="cl-body">Single view of all known costs: 驗屋 NT$15,499, 裝修工程
NT$805,266 (incl. tax, 拾間), 已購家具 NT$692k–699k (Hefeng × 3),
家具選配可達 +NT$105k–110k. Known lower bound ≈ NT$1.51M,
upper with all options ≈ NT$1.63M. Explicitly excludes
房價, 家電, 軟件, 管委會 fees, and un-priced estimate lines.

Cross-links back to estimate, products, and milestone entries
so numbers stay auditable against their source.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/budget/' | relative_url }}">預算</a></div>
</div>

<div class="cl-commit" id="b53ce4f" data-hash="b53ce4f">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#b53ce4f" title="複製此變更的永久連結">b53ce4f</a> · 2026-04-19 00:06</div>
  <div class="cl-subj">Add auto-aggregated open-items page</div>
  <div class="cl-body">/open-items/ scans every page and pulls out every unchecked
- [ ] task into a single grouped view. Each source page gets
its own section with a back-link and item count; total summary
at the bottom. Templates (_template.md, _change-template.md)
are excluded so placeholders don&#x27;t pad the count.

The scanner handles both raw-markdown task items and
post-rendered HTML task-list-item elements so pages processed
in either order still get picked up.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/open-items/' | relative_url }}">待確認</a></div>
</div>

<div class="cl-commit" id="8b50a7d" data-hash="8b50a7d">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#8b50a7d" title="複製此變更的永久連結">8b50a7d</a> · 2026-04-19 00:04</div>
  <div class="cl-subj">Log 驗屋 service receipt under 2026-03-29 milestone</div>
  <div class="cl-body">好日子科技驗屋 (戶 2C) 新成屋安心完整方案 NT$15,499
(18,000 − 4,001 優惠 + 1,500 假日出班費). 6-month
validity; change/cancel ≥8 days free, &lt;7 days costs 3k.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="38f05f5" data-hash="38f05f5">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#38f05f5" title="複製此變更的永久連結">38f05f5</a> · 2026-04-19 00:03</div>
  <div class="cl-subj">Add hidden lift drying rack on AE ceiling</div>
  <div class="cl-body">Hand-crank aluminium lift rack (ANASA FJ-01 style) recessed into
the AE side of A&#x27;s ceiling. Doubles as a rainy-day drying spot
and a drop-off 污衣區 when coming in from outside. Retracts into
the ceiling so it&#x27;s invisible when not in use. Needs positional
coordination with the 2 central anchors and AW projector screen.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><span class="cl-tag">圖片 ×1</span></div>
</div>


<h2 class="cl-day" markdown="0">2026-04-18</h2>

<div class="cl-commit" id="27b45c2" data-hash="27b45c2">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#27b45c2" title="複製此變更的永久連結">27b45c2</a> · 2026-04-18 23:39</div>
  <div class="cl-subj">Log project milestones with photos on contract page</div>
  <div class="cl-body">- 2024-05-09 購屋簽約 — building still wrapped in scaffold netting
- 2026-03-02 交屋期 (from drawing 115.03.02)
- 2026-03-29 第一次驗屋 + 設計師現場丈量 — building finished
- 2026-04-18 拾間估價單

Each milestone row links to its own anchor; photos embedded for
the two with site shots.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><span class="cl-tag">圖片 ×2</span></div>
</div>

<div class="cl-commit" id="fec4856" data-hash="fec4856">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#fec4856" title="複製此變更的永久連結">fec4856</a> · 2026-04-18 23:39</div>
  <div class="cl-subj">Spec A-room hero wall + ceiling anchors + projector screen</div>
  <div class="cl-body">- AN (北牆 核心重點)：整面卡扣書牆系統，從入口對講機區的上下
  簍空櫃，延伸至 AE 轉角。淺木色可調層板、其中一塊作為站立
  辦公桌；電箱段做成可轉開/滑開的機關式書架；書板下 LED
  條兼顧書本與貓咪玩耍區的照明；螢幕手臂固定於卡扣中。
- 天花板雙吊點：客廳中央留兩個結構吊點供空中瑜伽、TRX、
  懸吊沙發、盪鞦韆、貓繩、曬棉被用，需鎖入 RC 樓板。
- 投影布幕預留 AW 側天花（估價 六-5 已列）：投影時廚房停用，
  但水槽 / 冰箱仍須保留可取用動線。</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a></div>
</div>

<div class="cl-commit" id="9253ce8" data-hash="9253ce8">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#9253ce8" title="複製此變更的永久連結">9253ce8</a> · 2026-04-18 23:20</div>
  <div class="cl-subj">Add AS↔DN sliding door with shared dressing mirror (B/C)</div>
  <div class="cl-body">Pocket-style ceiling-track sliding door between the living area
(AS) and the alley/bathroom zone (DN), no floor rail. Door&#x27;s
D-facing side is a full-length dressing mirror with surrounding
LED lighting — doubles as a shared changing area for B and C.

When the door retracts, it slides behind the AS wall and the
mirror is hidden between the door and AS, keeping the living
side visually clean. AS wall needs a matching pocket depth.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a></div>
</div>

<div class="cl-commit" id="f830228" data-hash="f830228">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#f830228" title="複製此變更的永久連結">f830228</a> · 2026-04-18 23:11</div>
  <div class="cl-subj">Embed real architectural floor plan under SVG</div>
  <div class="cl-body">Places the contract 2F/C戶-建築平面圖 (H=360 cm, 15 cm RC walls)
below the stylised SVG on the home page so viewers can cross-check
the schematic against the real dimensions.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a><span class="cl-tag">圖片 ×1</span></div>
</div>

<div class="cl-commit" id="ee50fa1" data-hash="ee50fa1">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#ee50fa1" title="複製此變更的永久連結">ee50fa1</a> · 2026-04-18 23:04</div>
  <div class="cl-subj">Add contract estimate + process pages (拾間設計)</div>
  <div class="cl-body">- contract/estimate.md: full 11-category line-item estimate
  digitised from 拾間&#x27;s 估價單. Total NT$805,266 (incl. tax).
  Flags discussion-priced items and 預估依實際計價 lines.
- contract/process.md: 9-step design flow, design &amp; construction
  payment schedules (50/50 design; 20/25/25/25/5 construction),
  engagement-letter terms.
- contract/index.md: summary totals, designer info (redacted —
  full-name shown only on local cert scan), payment rhythms.
- Original scans of service flow, timeline, engagement letter,
  and three estimate pages embedded for reference.

技術士證 scan with national ID lives under docs/contract/private/
(gitignored) so it isn&#x27;t pushed to the public Pages site.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/estimate/' | relative_url }}">工程估價單</a><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><a class="cl-tag cl-tag-link" href="{{ '/contract/process/' | relative_url }}">設計流程</a><span class="cl-tag">圖片 ×6</span></div>
</div>

<div class="cl-commit" id="732bdfb" data-hash="732bdfb">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#732bdfb" title="複製此變更的永久連結">732bdfb</a> · 2026-04-18 23:02</div>
  <div class="cl-subj">Log site-condition photos for AN, AE, AW</div>
  <div class="cl-body">- AN: electrical panel + intercom; concrete ceiling to get a
  simple drop ceiling.
- AE: full-width black-framed sliding door to balcony; split AC
  indoor unit already installed with exposed flex duct.
- AW: kitchen 一字型配置 (sink + IH + hood + dishwasher) already
  in; upper cabinet above sink will be rebuilt; green X marks
  are 驗屋 flags for the builder to address.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><span class="cl-tag">圖片 ×3</span></div>
</div>

<div class="cl-commit" id="e856589" data-hash="e856589">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#e856589" title="複製此變更的永久連結">e856589</a> · 2026-04-18 23:02</div>
  <div class="cl-subj">Add design references across rooms and walls</div>
  <div class="cl-body">- AS (客廳主牆): wall-anchored suspension training — RC + embedded
  anchors for chains, dark mineral paint finish.
- DN (衛浴門框): wooden peg-board door frame with removable bars
  for pull-ups, dips, leg raises. Must survive bathroom humidity.
- BW (主臥西牆): modular white-track + wood-shelf storage system
  (IKEA Boaxel / Elfa style); doors required to hide contents.
- C 房: loft sleeping platform + study bookshelf ambience ref.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><span class="cl-tag">圖片 ×4</span></div>
</div>

<div class="cl-commit" id="5e74012" data-hash="5e74012">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#5e74012" title="複製此變更的永久連結">5e74012</a> · 2026-04-18 23:00</div>
  <div class="cl-subj">Log purchased Murphy beds — KL Board (CW) and LD002 (B)</div>
  <div class="cl-body">- KL Board (Hefeng, NT$147k/154k): wall-mounted flip bed for CW.
  Converts to desk; 106 cm depth clearance needed for rotation.
  CW partition behind is storage-only, to be bright, non-oppressive,
  with door fronts hiding clutter.
- LD002 (Hefeng, NT$407k): double Murphy bed with integrated
  shelving for B room. Wall assignment (BW or BE) still pending —
  BW now has modular shelving planned, so BE is the likely home.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><span class="cl-tag">圖片 ×2</span></div>
</div>

<div class="cl-commit" id="6beb94c" data-hash="6beb94c">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#6beb94c" title="複製此變更的永久連結">6beb94c</a> · 2026-04-18 22:52</div>
  <div class="cl-subj">Replace ASCII floor plan with inline SVG</div>
  <div class="cl-body">- Proper proportions: A width = D + B, C sticks out west, D is
  shorter N-S than C/B with an alley above it connecting C to B.
- Balcony (陽台) shown outside AE wall with same N-S extent as A.
- Wall labels (AN/AE/…) placed inside their respective rooms
  (BW inside B, DE/DW inside D, CE inside C) instead of floating
  into neighbours.
- Single 陽台 label (user has one balcony, not 前/後).</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a></div>
</div>

<div class="cl-commit" id="2ac7392" data-hash="2ac7392">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#2ac7392" title="複製此變更的永久連結">2ac7392</a> · 2026-04-18 22:46</div>
  <div class="cl-subj">Switch to plain Jekyll for local dev + add preview helper</div>
  <div class="cl-body">- Gemfile: drop github-pages gem (pins to Ruby 3.x) in favour of
  jekyll 4.3 + webrick so it installs on modern Ruby. Prod still
  uses github-pages&#x27; environment; the local Gemfile is dev-only.
- _config.yml: add jekyll-relative-links plugin so relative image
  paths like ../assets/… get rewritten to baseurl-aware URLs.
- scripts/preview: one-shot clean rebuild + serve. jekyll-relative-links
  caches its static-file index at startup, so images added mid-session
  don&#x27;t get rewritten without a fresh build.
- .gitignore: exclude docs/contract/private/ — folder for scans
  containing PII (e.g. national ID on technician cert).</div>
</div>

<div class="cl-commit" id="9be7d4a" data-hash="9be7d4a">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#9be7d4a" title="複製此變更的永久連結">9be7d4a</a> · 2026-04-18 21:35</div>
  <div class="cl-subj">Fix asset paths for project-site baseurl</div>
  <div class="cl-body">Setting baseurl: /new-house so Jekyll/jekyll-relative-links prepends
the GitHub Pages subpath to every generated link. Image references
in active pages and templates switched from root-absolute (/assets/…)
to page-relative (../assets/…) so they resolve correctly in both
localhost and https://bater.github.io/new-house/.

Also adds .hover-lightbox-trigger to template placeholders so copies
inherit the hover-preview behaviour.</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a><a class="cl-tag cl-tag-link" href="{{ '/references/' | relative_url }}">參考</a><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/walls/_template/' | relative_url }}">牆 _template</a></div>
</div>

<div class="cl-commit" id="defc462" data-hash="defc462">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#defc462" title="複製此變更的永久連結">defc462</a> · 2026-04-18 21:29</div>
  <div class="cl-subj">Link aux_links and README to the real repo + Pages URL</div>
</div>

<div class="cl-commit" id="7fa26ce" data-hash="7fa26ce">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#7fa26ce" title="複製此變更的永久連結">7fa26ce</a> · 2026-04-18 21:27</div>
  <div class="cl-subj">Polish index layout and add hover-lightbox for product thumbnails</div>
  <div class="cl-body">- index.md: replace ASCII plan with inline SVG (L-shape, coloured
  rooms, wall labels, alley strip above D, 前陽台 outside AE)
- rooms/A.md: list → table with thumbnail column; link uses
  absolute path to survive pretty permalinks
- _includes/head_custom.html: site-wide hover lightbox for any
  .hover-lightbox-trigger image
- _config.yml: site title → 永豐泰雲川2C
- .gitignore: exclude local Claude Code settings</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a></div>
</div>

<div class="cl-commit" id="f54e2e9" data-hash="f54e2e9">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#f54e2e9" title="複製此變更的永久連結">f54e2e9</a> · 2026-04-18 21:16</div>
  <div class="cl-subj">Scaffold Jekyll renovation workspace under docs/</div>
  <div class="cl-body">Repurposes the repo from a 3D viewer into a markdown-first workspace
for managing renovation details with the designer, published via
GitHub Pages.

- docs/ uses just-the-docs remote theme, no build step on CI
- Floor plan labelled A/B/C/D × N/E/S/W — 16 wall pages, 4 room pages
- Contract source drawings (DWG/PDF) live under docs/contract/source
- First purchase logged: TA-175 升降茶几/餐桌 under references/products
- CLAUDE.md, README.md, and .gitignore updated for the new shape</div>
  <div class="cl-tags"><a class="cl-tag cl-tag-link" href="{{ '/contract/' | relative_url }}">合約</a><a class="cl-tag cl-tag-link" href="{{ '/' | relative_url }}">首頁</a><a class="cl-tag cl-tag-link" href="{{ '/references/' | relative_url }}">參考</a><a class="cl-tag cl-tag-link" href="{{ '/references/products/' | relative_url }}">產品</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/A/' | relative_url }}">房間 A</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/B/' | relative_url }}">房間 B</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/C/' | relative_url }}">房間 C</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/D/' | relative_url }}">房間 D</a><a class="cl-tag cl-tag-link" href="{{ '/rooms/' | relative_url }}">房間目錄</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AE/' | relative_url }}">牆 AE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AN/' | relative_url }}">牆 AN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AS/' | relative_url }}">牆 AS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/AW/' | relative_url }}">牆 AW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BE/' | relative_url }}">牆 BE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BN/' | relative_url }}">牆 BN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BS/' | relative_url }}">牆 BS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/BW/' | relative_url }}">牆 BW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CE/' | relative_url }}">牆 CE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CN/' | relative_url }}">牆 CN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CS/' | relative_url }}">牆 CS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/CW/' | relative_url }}">牆 CW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DE/' | relative_url }}">牆 DE</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DN/' | relative_url }}">牆 DN</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DS/' | relative_url }}">牆 DS</a><a class="cl-tag cl-tag-link" href="{{ '/walls/DW/' | relative_url }}">牆 DW</a><a class="cl-tag cl-tag-link" href="{{ '/walls/_template/' | relative_url }}">牆 _template</a><a class="cl-tag cl-tag-link" href="{{ '/walls/' | relative_url }}">牆面總表</a><span class="cl-tag">圖片 ×2</span></div>
</div>

<div class="cl-commit" id="e4d3d4d" data-hash="e4d3d4d">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#e4d3d4d" title="複製此變更的永久連結">e4d3d4d</a> · 2026-04-18 21:16</div>
  <div class="cl-subj">Archive 3D floor-plan viewer approach</div>
  <div class="cl-body">Moves the Vite + Three.js viewer, Python extraction scripts,
Dockerfile/ODA converter attempts, and APPROACH_LOG.md into archive/.
Designer already provides 3D renders, so the in-house viewer is
retired — kept (not deleted) so the documented dead-ends for
AutoCAD AEC entity extraction on macOS stay discoverable.</div>
</div>


<h2 class="cl-day" markdown="0">2026-03-21</h2>

<div class="cl-commit" id="1e2d8cd" data-hash="1e2d8cd">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#1e2d8cd" title="複製此變更的永久連結">1e2d8cd</a> · 2026-03-21 15:55</div>
  <div class="cl-subj">Fix mirrored X axis — flip left/right to match PDF orientation</div>
  <div class="cl-body">- Flip X coordinates in extract_floorplan_v2.py (max_x - x instead of x - min_x)
- Update room labels to match corrected layout
- Kitchen now on left, balcony on right, matching the architectural drawing</div>
</div>

<div class="cl-commit" id="b53014d" data-hash="b53014d">
  <button type="button" class="cl-toggle" aria-label="切換已讀/未讀"></button>
  <div class="cl-meta"><a class="cl-perma" href="#b53014d" title="複製此變更的永久連結">b53014d</a> · 2026-03-21 15:45</div>
  <div class="cl-subj">Initial version: 3D floor plan viewer for 2F/C戶 apartment</div>
  <div class="cl-body">- Three.js viewer (Vite) with orbit controls, multiple camera views, wireframe mode
- PDF vector extraction (extract_floorplan_v2.py) using PyMuPDF: 293 walls, 7.5m × 7.4m
- Data-driven rendering (floorplan_from_data.js) from extracted JSON
- DWG/DXF parsing scripts (parse_dxf.py, parse_svg.py) as alternative approaches
- Docker configs for ODA File Converter and libredwg
- APPROACH_LOG.md documenting 12 extraction methods tried</div>
</div>


<script>
(function () {
  var COOKIE = 'cl_read';
  function read() {
    var m = document.cookie.match(/(?:^|; )cl_read=([^;]*)/);
    return m ? decodeURIComponent(m[1]).split(',').filter(Boolean) : [];
  }
  function write(arr) {
    var d = new Date(); d.setTime(d.getTime() + 365 * 864e5);
    document.cookie = 'cl_read=' + encodeURIComponent(arr.join(',')) +
      '; expires=' + d.toUTCString() + '; path=/; SameSite=Lax';
  }
  function refresh() {
    var set = {}; read().forEach(function (h) { set[h] = 1; });
    var items = document.querySelectorAll('.cl-commit');
    var n = 0;
    items.forEach(function (el) {
      var isRead = !!set[el.dataset.hash];
      if (isRead) el.classList.remove('new');
      else { el.classList.add('new'); n++; }
      var btn = el.querySelector('.cl-toggle');
      if (btn) btn.textContent = isRead ? '已讀 ✓' : '標為已讀';
    });
    document.getElementById('cl-new-count').textContent = n;
    document.getElementById('cl-total-count').textContent = items.length;
  }
  function toggle(hash) {
    var cur = read();
    var idx = cur.indexOf(hash);
    if (idx >= 0) cur.splice(idx, 1);
    else cur.push(hash);
    write(cur);
    refresh();
  }
  document.addEventListener('DOMContentLoaded', function () {
    refresh();
    document.querySelectorAll('.cl-commit').forEach(function (el) {
      var btn = el.querySelector('.cl-toggle');
      if (!btn) return;
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggle(el.dataset.hash);
      });
    });
    document.getElementById('cl-mark-all').addEventListener('click', function () {
      var all = Array.prototype.map.call(document.querySelectorAll('.cl-commit'),
        function (e) { return e.dataset.hash; });
      write(all); refresh();
    });
    document.getElementById('cl-unmark-all').addEventListener('click', function () {
      write([]); refresh();
    });
  });
})();
</script>
