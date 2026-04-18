# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**2F/C戶 雲川集合住宅 裝修工作區** — a personal Jekyll site (deployed via GitHub Pages) for managing renovation details with the designer. Content: contract terms, per-wall decisions, reference products, inspiration imagery, meeting notes.

The earlier 3D-viewer approach (DWG/PDF → Three.js) has been **archived** — designer already provides 3D renders, so the workspace is now markdown-first.

## Structure

```
docs/                  # Jekyll site root (GitHub Pages serves from here)
├── _config.yml        # remote_theme: just-the-docs; baseurl: /new-house; jekyll-relative-links enabled
├── Gemfile            # jekyll 4.3 + webrick (local); prod is built by github-pages
├── index.md           # Home: SVG floor plan + architectural PDF embed
├── contract/          # Estimate, process, milestones, source drawings (DWG/PDF)
├── walls/             # 16 walls: AN/AE/AS/AW, BN/BE/..., DW
├── rooms/             # A/B/C/D per-room integration pages
├── references/        # products.md, inspiration, palette
├── budget.md          # Rollup of known spend
├── open-items.md      # Auto-aggregated TODO list across pages
├── _includes/         # head_custom (lightbox), open_items_body (aggregator)
└── assets/images/     # Photos & reference images (walls/<ID>/, rooms/<ID>/, products/, contract/)
scripts/preview        # Local hot-reload helper (port 4000 + livereload)
archive/               # Deprecated 3D viewer, Python extraction scripts
```

## Conventions

- **Wall pages**: filename is `<ROOM><DIR>.md` — room letter A/B/C/D + direction N/E/S/W (e.g. `AN.md`, `BE.md`). Copy `docs/walls/_template.md`.
- **Room pages**: `<ROOM>.md` (e.g. `A.md`). Copy `docs/rooms/_template.md`.
- **Contract changes**: copy `docs/contract/_change-template.md`, number sequentially.
- **Images**: save under `docs/assets/images/<topic>/<ID>/`. Reference with **relative** paths like `../assets/images/walls/AN/foo.png` — absolute `/assets/...` breaks on GitHub Pages because of `baseurl: /new-house`. The `jekyll-relative-links` plugin rewrites these to `/new-house/...` at build time.
- **Lightbox on images**: add `{: .hover-lightbox-trigger width="500" }` — `_includes/head_custom.html` wires up the preview-on-hover behaviour.
- **Open items**: any `- [ ]` task list line is auto-pulled into `/open-items/`. Walls get grouped under their room; product-page items keep a section tag. Lines containing `(待填)` are skipped.
- **Private files**: anything with PII (national ID, cert scans) goes under `docs/contract/private/` (gitignored).
- **Chinese-first content** — UI labels and page titles in 繁中.

## Local preview

Use the helper script (clean rebuild + livereload):
```bash
./scripts/preview
```
Then open `http://127.0.0.1:4000/new-house/`. Ruby 4.x + the Gemfile's jekyll 4.3 + webrick; don't mix in the `github-pages` gem (ffi incompat with Ruby 4).

## GitHub Pages setup

Repo: `bater/new-house`. Settings → Pages → Source: `Deploy from a branch` → Branch: `main` / folder: `/docs`. Live URL: `https://bater.github.io/new-house/`.

## Archive

`archive/` keeps the old DWG/DXF parsing attempts and Three.js viewer for reference. **Do not delete** — it documents approaches that didn't work for AEC entity extraction (see `archive/APPROACH_LOG.md`).
