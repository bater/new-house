# 3D Floor Plan Viewer — Approach Log

## Goal
Display the 2F/C戶 architectural floor plan as an interactive 3D model in the browser using Three.js.

## Source Files
- `2F_C戶- 雲川- 建築水電圖115.03.02.dwg` — AutoCAD Architecture (ACA) file, AC1032 format (2018+)
- `2F_C戶- 雲川- 建築水電圖115.03.02.pdf` — 4-page PDF exported from AutoCAD (建築平面圖, 電氣弱電, 給排水)

## Key Discovery
The DWG uses **AEC (Architecture, Engineering, Construction) entities** — proprietary objects (AEC_WALL, AEC_OPENING, AEC_DOOR) from AutoCAD Architecture. These store the actual wall geometry but are NOT standard LINE/POLYLINE. Open-source tools cannot fully extract them.

---

## Approaches Tried

### 1. Manual wall placement by eyeballing PDF ❌
- Created `floorplan.js` with hand-coded wall coordinates
- **Result**: Very inaccurate. Required 5+ correction rounds. User rejected.
- **Lesson**: Never manually guess coordinates.

### 2. PDF vector extraction with PyMuPDF ⚠️ (partial)
- Script: `extract_floorplan.py`
- Used `page.get_drawings()` to extract vector paths from page 1
- Found wall lines at stroke widths: 0.84pt (RC), 0.54pt (partitions), 0.36pt (secondary)
- **Result**: Got 46 wall segments after merging parallel lines. Model: 7.50m × 7.66m
- **Issue**: Only thick lines captured. Many details missing. Output messy.
- **Lesson**: PDF has ALL geometry but needs better filtering and wall-pair detection.

### 3. libdxfrw (dwg2dxf) from source ❌
- Built from `github.com/LibreCAD/libdxfrw`
- **Result**: Can't read AC1032 format. Error: "format 18 error 9"
- Tool location: `/tmp/libdxfrw/build/dwg2dxf/dwg2dxf`

### 4. GNU libredwg (dwg2dxf + dwg2SVG) from source ⚠️ (partial)
- Built from `github.com/LibreDWG/libredwg`
- Required: cmake, memmem shim for macOS, git submodule init for jsmn
- **DWG→DXF**: Converted successfully (24MB DXF), but:
  - ezdxf crashes on it (SORTENTSTABLE invalid handle code 331)
  - Even recovery mode fails
  - Stripping SORTENTSTABLE → ENDBLK structure error
- **DWG→SVG**: Converted (14MB SVG, 73K paths), but coordinates distorted by nested block transforms
- Tool location: `/tmp/libredwg/build/dwg2dxf`, `/tmp/libredwg/build/dwg2SVG`

### 5. Raw DXF parser (custom Python) ⚠️ (partial)
- Script: `parse_dxf.py`
- Parsed BLOCKS + ENTITIES sections, resolved INSERT references
- **Result**: 11,465 entities → 9,418 line segments across 38 real layers
- **Layers found**: WALL (192), G-IMPT (3996), 裝修-CON2-輕隔間 (69), 木門 (540), A-DOOR (123), 模板-窗開口 (555), etc.
- **Issue**: WALL layer spans 5861mm × 1076mm — only partial geometry. AEC wall data NOT in standard entities.
- **Lesson**: Standard LINE/POLYLINE only contain annotation/block elements, not the AEC wall geometry.

### 6. SVG parser (custom Python) ❌
- Script: `parse_svg.py`
- Parsed dwg2SVG output
- **Result**: 101K segments but coordinates scattered (bounds: -48K to 1.1M) due to block transform accumulation
- All strokes same width (0.1px) — no classification possible.

### 7. Python packages for DWG ❌
- `ezdxf`: DXF only, can't read DWG directly
- `pydwg`: Windows-only (requires COM/pyautocad)
- `aspose-cad`: No Python 3.13 support
- `dwgread`, `dwg`: Not found on PyPI

### 8. ODA File Converter via Docker (fn9170/dwg2dxf-api) ❌
- Docker image `fn9170/dwg2dxf-api` contains ODA File Converter
- **Result**: Crashes under amd64 emulation on Apple Silicon (exit code 134 SIGABRT)
- Would work on native x86_64 Linux/Mac

### 9. aspose-cad + uv + Python 3.12 ❌
- `uv venv .venv312 --python 3.12` + `uv pip install aspose-cad`
- Installed aspose-cad 25.12.0 successfully
- **Result**: `RuntimeError: Drawing loading failed: TypeInitializationException` on this AEC DWG file
- aspose-cad may not support AutoCAD Architecture AEC entities either

### 10. Docker arm64 libredwg ⚠️ (same as #4)
- Built native arm64 Docker image from GNU libredwg source
- `docker build -t libredwg-arm64` — successful
- DWG→DXF conversion works but same AEC entity limitation

### 11. Node.js dxf-parser ⚠️ (same data as #5)
- `npm install dxf-parser` in viewer/
- Parsed the libredwg DXF: 241 entities, 1046 blocks, 11349 resolved entities
- Same limitation: AEC wall data missing, model only 33.75m × 1.33m

### 12. Improved PDF extraction v2 ✅ (BEST RESULT)
- Script: `extract_floorplan_v2.py`
- Includes ALL stroke widths (0.12pt included), merges parallel line pairs
- **Result**: 293 wall segments, model 7.50m × 7.39m
- Breakdown: 236 partition, 33 brick, 24 RC walls
- Much better than v1 (46 walls) — room structure clearly visible

---

## Current State
- Viewer project at `viewer/` (Vite + Three.js) works
- `floorplan_from_data.js` renders wall data from JSON
- **Best extraction: `extract_floorplan_v2.py`** — 293 walls, 7.50m × 7.39m
- Active data: `viewer/public/floorplan_data.json` (copied from `floorplan_data_improved.json`)

## Next Steps (Priority Order)

### 1. uv + Python 3.12 + aspose-cad ⭐ (easiest to try)
`aspose-cad` supports Python <3.13. Use `uv` to create a venv with Python 3.12:
```bash
uv venv .venv312 --python 3.12
uv pip install aspose-cad --python .venv312
```
Then use aspose-cad to read the DWG directly and export to DXF/JSON/SVG. aspose-cad is a commercial library with a free tier that should handle AEC entities properly since it uses the ODA engine internally.

### 2. Docker + ODA File Converter
ODA File Converter (free, Linux version) properly handles AEC entities:
```bash
docker run --rm -v $(pwd):/data oda-converter /data/input.dwg /data/output.dxf
```
Convert DWG → clean DXF → parse with ezdxf → JSON → Three.js.

### 3. Improved PDF extraction (fallback)
Current `extract_floorplan.py` only captures thick lines (46 walls). Improve by:
- Include 0.12pt lines (standard drawing width — majority of geometry)
- Better parallel-line pair detection for wall thickness
- Spatial clustering to isolate page 1 from other pages
- Use line color in addition to width for classification

### 4. FreeCAD Python bindings in Docker
FreeCAD has Python bindings that can import DWG/DXF. Run in Docker:
```bash
docker run --rm -v $(pwd):/data freecad-python python3 /data/convert.py
```

## Installed Tools
- Python venv: `.venv/` (ezdxf, pymupdf)
- GNU libredwg: `/tmp/libredwg/build/` (dwg2dxf, dwg2SVG, dwgread)
- LibreCAD: `/Applications/LibreCAD.app` (GUI only)
- Docker: installed but daemon not running
- poppler: installed (pdftoppm for PDF rendering)
