# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

3D floor plan viewer for a 2F/C戶 apartment (雲川 集合住宅). Converts AutoCAD architectural drawings into an interactive browser-based 3D model using Three.js.

## Commands

```bash
# Frontend dev server (Vite + Three.js, port 5173)
cd viewer && npm run dev

# Production build
cd viewer && npm run build

# Python extraction (activate venv first)
source .venv/bin/activate
python3 extract_floorplan.py    # PDF → floorplan_data.json (primary method)
python3 parse_dxf.py            # DXF fallback (limited — see below)
```

## Architecture

**Data pipeline:** DWG/PDF → Python extraction → `viewer/public/floorplan_data.json` → Three.js renderer

```
extract_floorplan.py (PyMuPDF)
  → viewer/public/floorplan_data.json
    → viewer/src/floorplan_from_data.js (async load, extrude walls to 3D)
      → viewer/src/main.js (scene, camera, controls, UI)
```

- `floorplan_from_data.js` — Reads JSON wall segments, creates BoxGeometry for each, extrudes to floor height (3.6m). Materials classified by wall type (rc/brick/light). Adds floor, ceiling, CSS2D room labels.
- `main.js` — Three.js scene with OrbitControls, shadow mapping, animated camera transitions. View buttons: 3D, top-down, front, wireframe.
- `floorplan.js` — Legacy hand-coded floor plan (deprecated, kept as reference).

**JSON format** (`floorplan_data.json`):
```json
{ "floor_height": 3.6, "width": 7.5, "depth": 7.66,
  "walls": [{ "x1", "z1", "x2", "z2", "thickness", "type", "layer" }] }
```

## DWG/DXF Parsing — Critical Constraints

The source DWG (AC1032 / AutoCAD 2018+) uses **AEC entities** (AutoCAD Architecture proprietary objects: AEC_WALL, AEC_OPENING, AEC_DOOR). No open-source tool fully extracts AEC geometry.

**What doesn't work** (don't retry these):
- `ezdxf` cannot read DWG directly; DXF from libredwg crashes it (SORTENTSTABLE error)
- `pydwg` / `pyautocad` — Windows-only (requires COM)
- `aspose-cad` — no Python 3.13 support
- `libdxfrw/dwg2dxf` — can't read AC1032 format
- GNU libredwg `dwg2dxf` — converts but AEC entities lost; only ~18% of wall data comes through as standard LINE/POLYLINE
- GNU libredwg `dwg2SVG` — coordinates distorted by nested block transforms

**What works:**
- **PDF extraction (PyMuPDF)** — the PDF is AutoCAD's rendered output with all AEC entities flattened to vector paths. Use `page.get_drawings()`. Classify walls by stroke width (0.84pt=RC, 0.54pt=partitions, 0.36pt=secondary).
- **Docker + ODA File Converter** — untried but most promising for proper AEC→standard geometry conversion.

See `APPROACH_LOG.md` for detailed results of all 8 approaches attempted.

## Coordinate System

- Three.js: X=east-west, Y=vertical, Z=north-south
- PDF Y-axis is inverted during extraction (flip Y→Z)
- DWG units appear to be mm; scale factor 1/1000 to meters
- Floor plan: ~7.5m wide × ~7m deep, floor height 3.6m

## Tools Installed

- Python venv: `.venv/` (Python 3.13.5, pymupdf, ezdxf)
- GNU libredwg: `/tmp/libredwg/build/{dwg2dxf,dwg2SVG}` (built from source)
- poppler: `pdftoppm` for PDF→PNG rendering
- Docker: installed (daemon may need starting)
