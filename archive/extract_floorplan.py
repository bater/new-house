"""
Extract wall geometry from the architectural PDF (page 1: 建築平面圖)
and output JSON for Three.js 3D wall extrusion.
"""
import json
import math
import fitz  # PyMuPDF

PDF_PATH = "2F_C戶- 雲川- 建築水電圖115.03.02.pdf"
OUTPUT_PATH = "viewer/public/floorplan_data.json"

# Wall classification by stroke width (pts)
WALL_TYPES = {
    "rc":    {"min_width": 0.7, "thickness": 0.15, "color": "#d4cfc4"},    # RC walls
    "brick": {"min_width": 0.4, "thickness": 0.10, "color": "#e8d5c4"},    # Brick partition walls
    "light": {"min_width": 0.3, "thickness": 0.08, "color": "#c0c0c0"},    # Light walls / balcony
}

# Minimum line length to consider (in pts) - skip tiny segments
MIN_LINE_LENGTH = 8.0


def extract_walls(page):
    """Extract wall lines from PDF page, classified by type."""
    paths = page.get_drawings()

    # Collect all black line segments with their stroke width
    segments = []
    for path in paths:
        width = round(path.get("width", 0), 2)
        color = path.get("color", (0, 0, 0))

        # Only process black lines (walls are black in the drawing)
        if color and (color[0] > 0.3 or color[1] > 0.3 or color[2] > 0.3):
            continue  # Skip gray/colored lines

        if width < 0.3:
            continue  # Skip thin detail lines

        for item in path["items"]:
            if item[0] == "l":  # line segment
                p1, p2 = item[1], item[2]
                length = math.hypot(p2.x - p1.x, p2.y - p1.y)
                if length < MIN_LINE_LENGTH:
                    continue

                segments.append({
                    "x1": p1.x, "y1": p1.y,
                    "x2": p2.x, "y2": p2.y,
                    "width": width,
                    "length": length,
                })

    return segments


def find_drawing_bounds(segments):
    """Find the bounding box of wall segments."""
    all_x = [s["x1"] for s in segments] + [s["x2"] for s in segments]
    all_y = [s["y1"] for s in segments] + [s["y2"] for s in segments]
    return min(all_x), min(all_y), max(all_x), max(all_y)


def merge_parallel_lines(segments, tolerance=2.0):
    """
    Merge closely parallel lines that form wall pairs into single center lines.
    In AutoCAD drawings, walls are drawn as two parallel lines.
    We detect pairs and merge them into a single wall with proper thickness.
    """
    h_lines = []  # horizontal (or near-horizontal)
    v_lines = []  # vertical (or near-vertical)
    other = []

    for s in segments:
        dx = abs(s["x2"] - s["x1"])
        dy = abs(s["y2"] - s["y1"])
        angle = math.atan2(dy, dx)

        if angle < 0.1:  # near horizontal
            h_lines.append(s)
        elif angle > math.pi/2 - 0.1:  # near vertical
            v_lines.append(s)
        else:
            other.append(s)

    walls = []

    # Merge horizontal line pairs
    h_lines.sort(key=lambda s: (round(s["y1"], 0), min(s["x1"], s["x2"])))
    used = set()
    for i, a in enumerate(h_lines):
        if i in used:
            continue
        for j, b in enumerate(h_lines):
            if j <= i or j in used:
                continue
            # Check if b is a parallel partner of a
            y_dist = abs(a["y1"] - b["y1"])
            if y_dist < tolerance * 0.5 or y_dist > 20:
                continue
            # Check overlap in x
            a_x1, a_x2 = min(a["x1"], a["x2"]), max(a["x1"], a["x2"])
            b_x1, b_x2 = min(b["x1"], b["x2"]), max(b["x1"], b["x2"])
            overlap = min(a_x2, b_x2) - max(a_x1, b_x1)
            if overlap > min(a_x2 - a_x1, b_x2 - b_x1) * 0.5:
                # These form a wall pair
                center_y = (a["y1"] + b["y1"]) / 2
                x_start = max(a_x1, b_x1)
                x_end = min(a_x2, b_x2)
                measured_thickness = y_dist
                walls.append({
                    "x1": x_start, "y1": center_y,
                    "x2": x_end, "y2": center_y,
                    "measured_thickness": measured_thickness,
                    "width": max(a["width"], b["width"]),
                    "direction": "h",
                })
                used.add(i)
                used.add(j)
                break

    # Add unmerged horizontal lines as single walls
    for i, s in enumerate(h_lines):
        if i not in used:
            walls.append({
                "x1": min(s["x1"], s["x2"]), "y1": s["y1"],
                "x2": max(s["x1"], s["x2"]), "y2": s["y2"],
                "measured_thickness": 0,
                "width": s["width"],
                "direction": "h",
            })

    # Merge vertical line pairs
    v_lines.sort(key=lambda s: (round(s["x1"], 0), min(s["y1"], s["y2"])))
    used = set()
    for i, a in enumerate(v_lines):
        if i in used:
            continue
        for j, b in enumerate(v_lines):
            if j <= i or j in used:
                continue
            x_dist = abs(a["x1"] - b["x1"])
            if x_dist < tolerance * 0.5 or x_dist > 20:
                continue
            a_y1, a_y2 = min(a["y1"], a["y2"]), max(a["y1"], a["y2"])
            b_y1, b_y2 = min(b["y1"], b["y2"]), max(b["y1"], b["y2"])
            overlap = min(a_y2, b_y2) - max(a_y1, b_y1)
            if overlap > min(a_y2 - a_y1, b_y2 - b_y1) * 0.5:
                center_x = (a["x1"] + b["x1"]) / 2
                y_start = max(a_y1, b_y1)
                y_end = min(a_y2, b_y2)
                measured_thickness = x_dist
                walls.append({
                    "x1": center_x, "y1": y_start,
                    "x2": center_x, "y2": y_end,
                    "measured_thickness": measured_thickness,
                    "width": max(a["width"], b["width"]),
                    "direction": "v",
                })
                used.add(i)
                used.add(j)
                break

    for i, s in enumerate(v_lines):
        if i not in used:
            walls.append({
                "x1": s["x1"], "y1": min(s["y1"], s["y2"]),
                "x2": s["x2"], "y2": max(s["y1"], s["y2"]),
                "measured_thickness": 0,
                "width": s["width"],
                "direction": "v",
            })

    # Add diagonal/other lines
    for s in other:
        walls.append({
            "x1": s["x1"], "y1": s["y1"],
            "x2": s["x2"], "y2": s["y2"],
            "measured_thickness": 0,
            "width": s["width"],
            "direction": "d",
        })

    return walls


def to_meters(walls, bounds):
    """Convert PDF pts to meters, with coordinate transform (PDF Y is inverted)."""
    min_x, min_y, max_x, max_y = bounds
    draw_w = max_x - min_x
    draw_h = max_y - min_y

    # Use drawing dimensions to establish scale
    # We don't assume target dimensions - let the actual drawing determine scale
    # The PDF is from AutoCAD where 1 unit = some real-world unit
    # At ~508pt width for a ~7.5m floor plan: scale ≈ 0.0148 m/pt
    scale = 7.5 / draw_w  # approximate, adjust if needed

    print(f"Scale: {scale:.6f} m/pt")
    print(f"Drawing: {draw_w:.1f} x {draw_h:.1f} pts → {draw_w*scale:.2f} x {draw_h*scale:.2f} m")

    result = []
    for w in walls:
        # Classify wall type by stroke width
        if w["width"] >= 0.7:
            wall_type = "rc"
            thickness = 0.15
        elif w["width"] >= 0.4:
            wall_type = "brick"
            thickness = 0.10
        else:
            wall_type = "light"
            thickness = 0.08

        # Use measured thickness if available (from merged parallel lines)
        if w["measured_thickness"] > 0:
            thickness = round(w["measured_thickness"] * scale, 3)

        result.append({
            "x1": round((w["x1"] - min_x) * scale, 4),
            "z1": round((max_y - w["y1"]) * scale, 4),  # flip Y
            "x2": round((w["x2"] - min_x) * scale, 4),
            "z2": round((max_y - w["y2"]) * scale, 4),  # flip Y
            "thickness": thickness,
            "type": wall_type,
        })

    return result, draw_w * scale, draw_h * scale


def main():
    doc = fitz.open(PDF_PATH)
    page = doc[0]

    print("=== Extracting Floor Plan Geometry ===\n")

    segments = extract_walls(page)
    print(f"Found {len(segments)} wall line segments")

    if not segments:
        print("No wall segments found!")
        return

    bounds = find_drawing_bounds(segments)
    print(f"Drawing bounds: ({bounds[0]:.1f}, {bounds[1]:.1f}) → ({bounds[2]:.1f}, {bounds[3]:.1f})")

    walls = merge_parallel_lines(segments)
    print(f"After merging: {len(walls)} wall segments")

    meter_walls, width_m, depth_m = to_meters(walls, bounds)

    # Count by type
    by_type = {}
    for w in meter_walls:
        by_type[w["type"]] = by_type.get(w["type"], 0) + 1
    for t, n in by_type.items():
        print(f"  {t}: {n} segments")

    output = {
        "floor_height": 3.6,
        "width": round(width_m, 3),
        "depth": round(depth_m, 3),
        "walls": meter_walls,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput: {OUTPUT_PATH}")
    print(f"Model: {width_m:.2f}m x {depth_m:.2f}m, {len(meter_walls)} walls")

    doc.close()


if __name__ == "__main__":
    main()
