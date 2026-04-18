# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**2F/C戶 雲川集合住宅 裝修工作區** — a personal Jekyll site (deployed via GitHub Pages) for managing renovation details with the designer. Content: contract terms, per-wall decisions, reference products, inspiration imagery, meeting notes.

The earlier 3D-viewer approach (DWG/PDF → Three.js) has been **archived** — designer already provides 3D renders, so the workspace is now markdown-first.

## Structure

```
docs/                  # Jekyll site root (GitHub Pages serves from here)
├── _config.yml        # Jekyll config — remote_theme: just-the-docs
├── index.md           # Home: ASCII layout + nav
├── contract/          # Contract docs + source drawings (DWG/PDF)
├── walls/             # One page per wall: living-north.md, master-east.md, ...
├── rooms/             # Per-room integration: lighting, flooring, ceiling
├── references/        # Products, inspiration images, palette
└── assets/images/     # All uploaded photos & reference images
archive/               # Deprecated 3D viewer, Python extraction scripts
```

## Conventions

- **Wall pages**: file name `<room>-<direction>.md` (e.g. `living-north.md`). Copy `docs/walls/_template.md`.
- **Room pages**: copy `docs/rooms/_template.md`.
- **Contract changes**: copy `docs/contract/_change-template.md`, number sequentially.
- **Images**: save under `docs/assets/images/<topic>/`. Reference with `/assets/images/<topic>/file.jpg` (Jekyll permalink).
- **Chinese-first content** — UI labels and page titles in 繁中.

## Local preview (optional)

GitHub Pages builds automatically on push. For local preview:
```bash
cd docs
bundle init && bundle add jekyll webrick && bundle exec jekyll serve
```
(Not required — push and view on the Pages URL is simplest.)

## GitHub Pages setup

Repo Settings → Pages → Source: `Deploy from a branch` → Branch: `main` / folder: `/docs`.

## Archive

`archive/` keeps the old DWG/DXF parsing attempts and Three.js viewer for reference. **Do not delete** — it documents approaches that didn't work for AEC entity extraction (see `archive/APPROACH_LOG.md`).
