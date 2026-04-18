# Archive — 舊方案

此資料夾保留最初嘗試「DWG/PDF → Three.js 3D 檢視器」的所有工具與程式碼。

**狀態：已停用**（設計師已提供完善的 3D 視圖，工作重心改為 markdown 細節管理 — 見專案根目錄）。

## 內容

- `viewer/` — Three.js + Vite 3D 檢視器前端
- `extract_floorplan.py` / `extract_floorplan_v2.py` — PyMuPDF 從 PDF 抽取牆線
- `parse_dxf.py` / `parse_svg.py` — DXF / SVG 解析實驗
- `convert_dwg_oda.sh` / `Dockerfile.oda` — ODA File Converter 的 Docker 嘗試（未完成）
- `APPROACH_LOG.md` — 8 種嘗試方法的完整結果紀錄
- `2F_C戶-雲川-建築水電圖-115.03.02.dxf` — libredwg 輸出（AEC 實體遺失的版本）

## 為什麼不刪掉

記錄了一堆 macOS 上處理 AutoCAD Architecture (AEC entities) 的死路，未來若要再嘗試可以省下重踩的時間。
