# 2F/C戶 裝修工作區 · 雲川集合住宅

Personal renovation workspace — collects contract terms, per-wall decisions, reference products, and meeting notes with the designer. Published via GitHub Pages.

## Quick links

- **Live site**: <https://bater.github.io/new-house/>
- **Source**: [`docs/`](./docs) — Jekyll + `just-the-docs` theme
- **Archive**: [`archive/`](./archive) — earlier attempt at DWG/PDF → Three.js 3D viewer (abandoned in favour of designer-supplied renders)

## Structure

| Path | What |
|---|---|
| `docs/index.md` | Home — SVG floor plan + embedded architectural PDF |
| `docs/contract/` | 估價單、設計流程、里程碑、DWG/PDF 原檔 |
| `docs/walls/` | 16 面牆 (AN/AE/…/DW) 細節決策 |
| `docs/rooms/` | 房間 (A/B/C/D) 整合頁 |
| `docs/references/` | 產品、靈感、色彩 |
| `docs/budget.md` | 已知支出彙整（裝修 / 家具 / 驗屋） |
| `docs/open-items.md` | 自動彙整各頁 `- [ ]` 待辦 |
| `docs/assets/images/` | 所有上傳圖片 |

## Local preview

```bash
./scripts/preview   # clean rebuild + livereload on http://127.0.0.1:4000/new-house/
```

Needs Ruby 4.x and the Gemfile in `docs/` (jekyll 4.3 + webrick). GitHub Pages builds automatically on push — local preview optional.

## Enable GitHub Pages

Repo Settings → Pages → Source: *Deploy from a branch* → Branch: `main` / folder: `/docs`.
