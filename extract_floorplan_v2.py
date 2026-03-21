"""
Extract ALL wall geometry from the architectural PDF (page 1: 建築平面圖)
using PyMuPDF get_drawings(). Improved version that captures thin lines (0.12pt+).

Outputs JSON for Three.js 3D wall extrusion.
"""
import json
import math
import fitz  # PyMuPDF

PDF_PATH = "2F_C戶- 雲川- 建築水電圖115.03.02.pdf"
OUTPUT_PATH = "viewer/public/floorplan_data_improved.json"

# Minimum line length in pts to skip noise
MIN_LINE_LENGTH = 3.0

# Maximum distance between parallel lines to consider them a wall pair
MAX_PAIR_DISTANCE = 15.0
MIN_PAIR_DISTANCE = 1.0

# Angle tolerance for classifying lines as horizontal/vertical (radians)
ANGLE_TOL = 0.1


def is_black(color, threshold=0.3):
    """Check if a color is black (all channels below threshold)."""
    if color is None:
        return True  # no color info -> treat as black
    if isinstance(color, (int, float)):
        return color < threshold
    try:
        return all(c < threshold for c in color)
    except TypeError:
        return True


def extract_segments(page):
    """Extract ALL black line segments from page drawings."""
    paths = page.get_drawings()
    segments = []

    for path in paths:
        width = path.get("width", 0)
        if width is None:
            width = 0
        width = round(width, 4)

        stroke_color = path.get("color", None)
        fill_color = path.get("fill", None)

        # Skip non-black strokes (gray backgrounds, colored elements)
        if stroke_color is not None and not is_black(stroke_color):
            continue

        # Skip fill-only paths with no stroke (filled rectangles / backgrounds)
        if stroke_color is None and fill_color is not None:
            continue

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
            elif item[0] == "re":  # rectangle - extract as 4 line segments
                rect = item[1]
                x0, y0, x1, y1 = rect.x0, rect.y0, rect.x1, rect.y1
                w = abs(x1 - x0)
                h = abs(y1 - y0)
                # Only include rectangles that look like wall segments
                # (long and thin, or reasonably sized)
                if max(w, h) < MIN_LINE_LENGTH:
                    continue
                # Add four edges
                edges = [
                    (x0, y0, x1, y0),  # top
                    (x1, y0, x1, y1),  # right
                    (x1, y1, x0, y1),  # bottom
                    (x0, y1, x0, y0),  # left
                ]
                for ex1, ey1, ex2, ey2 in edges:
                    seg_len = math.hypot(ex2 - ex1, ey2 - ey1)
                    if seg_len < MIN_LINE_LENGTH:
                        continue
                    segments.append({
                        "x1": ex1, "y1": ey1,
                        "x2": ex2, "y2": ey2,
                        "width": width,
                        "length": seg_len,
                    })

    return segments


def find_drawing_bounds(segments):
    """Find the bounding box of segments."""
    all_x = [s["x1"] for s in segments] + [s["x2"] for s in segments]
    all_y = [s["y1"] for s in segments] + [s["y2"] for s in segments]
    return min(all_x), min(all_y), max(all_x), max(all_y)


def classify_direction(s):
    """Classify a segment as horizontal, vertical, or diagonal."""
    dx = abs(s["x2"] - s["x1"])
    dy = abs(s["y2"] - s["y1"])
    angle = math.atan2(dy, dx)
    if angle < ANGLE_TOL:
        return "h"
    elif angle > math.pi / 2 - ANGLE_TOL:
        return "v"
    else:
        return "d"


def normalize_segment(s):
    """Ensure segment goes left-to-right (horizontal) or top-to-bottom (vertical)."""
    d = classify_direction(s)
    if d == "h":
        if s["x1"] > s["x2"]:
            return {**s, "x1": s["x2"], "y1": s["y2"], "x2": s["x1"], "y2": s["y1"]}
    elif d == "v":
        if s["y1"] > s["y2"]:
            return {**s, "x1": s["x2"], "y1": s["y2"], "x2": s["x1"], "y2": s["y1"]}
    return s


def overlap_1d(a_min, a_max, b_min, b_max):
    """Return the overlap length of two 1D intervals."""
    return max(0, min(a_max, b_max) - max(a_min, b_min))


def merge_parallel_pairs(segments):
    """
    Group parallel line pairs that are close together (< MAX_PAIR_DISTANCE apart)
    to detect wall thickness. Merge wall pairs into single center-line walls.
    """
    h_lines = []
    v_lines = []
    diag_lines = []

    for s in segments:
        s = normalize_segment(s)
        d = classify_direction(s)
        if d == "h":
            h_lines.append(s)
        elif d == "v":
            v_lines.append(s)
        else:
            diag_lines.append(s)

    walls = []

    # --- Merge horizontal line pairs ---
    # Sort by y coordinate, then by x start
    h_lines.sort(key=lambda s: (s["y1"], s["x1"]))
    h_used = [False] * len(h_lines)

    for i in range(len(h_lines)):
        if h_used[i]:
            continue
        a = h_lines[i]
        best_j = -1
        best_dist = MAX_PAIR_DISTANCE + 1

        for j in range(i + 1, len(h_lines)):
            if h_used[j]:
                continue
            b = h_lines[j]
            y_dist = abs(a["y1"] - b["y1"])
            if y_dist > MAX_PAIR_DISTANCE:
                # Since sorted by y, no more candidates
                break
            if y_dist < MIN_PAIR_DISTANCE:
                continue

            # Check x overlap
            a_x1, a_x2 = min(a["x1"], a["x2"]), max(a["x1"], a["x2"])
            b_x1, b_x2 = min(b["x1"], b["x2"]), max(b["x1"], b["x2"])
            ov = overlap_1d(a_x1, a_x2, b_x1, b_x2)
            min_len = min(a_x2 - a_x1, b_x2 - b_x1)
            if min_len > 0 and ov > min_len * 0.5:
                if y_dist < best_dist:
                    best_dist = y_dist
                    best_j = j

        if best_j >= 0:
            b = h_lines[best_j]
            a_x1, a_x2 = min(a["x1"], a["x2"]), max(a["x1"], a["x2"])
            b_x1, b_x2 = min(b["x1"], b["x2"]), max(b["x1"], b["x2"])
            center_y = (a["y1"] + b["y1"]) / 2
            # Use the union of both lines' x extents for wall length
            x_start = min(a_x1, b_x1)
            x_end = max(a_x2, b_x2)
            walls.append({
                "x1": x_start, "y1": center_y,
                "x2": x_end, "y2": center_y,
                "measured_thickness": best_dist,
                "width": max(a["width"], b["width"]),
                "direction": "h",
            })
            h_used[i] = True
            h_used[best_j] = True
        else:
            # Unpaired horizontal line
            walls.append({
                "x1": a["x1"], "y1": a["y1"],
                "x2": a["x2"], "y2": a["y2"],
                "measured_thickness": 0,
                "width": a["width"],
                "direction": "h",
            })
            h_used[i] = True

    # --- Merge vertical line pairs ---
    v_lines.sort(key=lambda s: (s["x1"], s["y1"]))
    v_used = [False] * len(v_lines)

    for i in range(len(v_lines)):
        if v_used[i]:
            continue
        a = v_lines[i]
        best_j = -1
        best_dist = MAX_PAIR_DISTANCE + 1

        for j in range(i + 1, len(v_lines)):
            if v_used[j]:
                continue
            b = v_lines[j]
            x_dist = abs(a["x1"] - b["x1"])
            if x_dist > MAX_PAIR_DISTANCE:
                break
            if x_dist < MIN_PAIR_DISTANCE:
                continue

            a_y1, a_y2 = min(a["y1"], a["y2"]), max(a["y1"], a["y2"])
            b_y1, b_y2 = min(b["y1"], b["y2"]), max(b["y1"], b["y2"])
            ov = overlap_1d(a_y1, a_y2, b_y1, b_y2)
            min_len = min(a_y2 - a_y1, b_y2 - b_y1)
            if min_len > 0 and ov > min_len * 0.5:
                if x_dist < best_dist:
                    best_dist = x_dist
                    best_j = j

        if best_j >= 0:
            b = v_lines[best_j]
            a_y1, a_y2 = min(a["y1"], a["y2"]), max(a["y1"], a["y2"])
            b_y1, b_y2 = min(b["y1"], b["y2"]), max(b["y1"], b["y2"])
            center_x = (a["x1"] + b["x1"]) / 2
            y_start = min(a_y1, b_y1)
            y_end = max(a_y2, b_y2)
            walls.append({
                "x1": center_x, "y1": y_start,
                "x2": center_x, "y2": y_end,
                "measured_thickness": best_dist,
                "width": max(a["width"], b["width"]),
                "direction": "v",
            })
            v_used[i] = True
            v_used[best_j] = True
        else:
            walls.append({
                "x1": a["x1"], "y1": a["y1"],
                "x2": a["x2"], "y2": a["y2"],
                "measured_thickness": 0,
                "width": a["width"],
                "direction": "v",
            })
            v_used[i] = True

    # --- Diagonal lines (unpaired) ---
    for s in diag_lines:
        walls.append({
            "x1": s["x1"], "y1": s["y1"],
            "x2": s["x2"], "y2": s["y2"],
            "measured_thickness": 0,
            "width": s["width"],
            "direction": "d",
        })

    return walls


def classify_wall_type(width):
    """Classify wall type by stroke width in pts."""
    if width >= 0.7:
        return "rc", 0.15
    elif width >= 0.4:
        return "brick", 0.10
    else:
        return "partition", 0.06


def to_meters(walls, bounds):
    """Convert PDF pts to meters, with Y-axis flip."""
    min_x, min_y, max_x, max_y = bounds
    draw_w = max_x - min_x
    draw_h = max_y - min_y

    # Scale: target ~7.5m width
    scale = 7.5 / draw_w

    print(f"  Scale: {scale:.6f} m/pt")
    print(f"  Drawing: {draw_w:.1f} x {draw_h:.1f} pts")
    print(f"  Model:   {draw_w * scale:.2f} x {draw_h * scale:.2f} m")

    result = []
    for w in walls:
        wall_type, default_thickness = classify_wall_type(w["width"])

        # Use measured thickness if we detected a parallel pair
        if w["measured_thickness"] > 0:
            thickness = round(w["measured_thickness"] * scale, 3)
        else:
            thickness = default_thickness

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

    print("=== Floor Plan Vector Extraction v2 ===\n")
    print(f"PDF: {PDF_PATH}")
    print(f"Page 1 size: {page.rect.width:.1f} x {page.rect.height:.1f} pts\n")

    # Step 1: Extract all black line segments (no stroke width filter)
    segments = extract_segments(page)
    print(f"Step 1: Extracted {len(segments)} black line segments (>= {MIN_LINE_LENGTH}pt)")

    if not segments:
        print("ERROR: No segments found!")
        doc.close()
        return

    # Show stroke width distribution
    width_counts = {}
    for s in segments:
        w = round(s["width"], 2)
        width_counts[w] = width_counts.get(w, 0) + 1
    print("\n  Stroke width distribution:")
    for w in sorted(width_counts.keys()):
        print(f"    {w:.2f}pt: {width_counts[w]} segments")

    # Step 2: Find bounds
    bounds = find_drawing_bounds(segments)
    print(f"\n  Bounds: ({bounds[0]:.1f}, {bounds[1]:.1f}) -> ({bounds[2]:.1f}, {bounds[3]:.1f})")

    # Step 3: Merge parallel pairs into walls
    walls = merge_parallel_pairs(segments)
    print(f"\nStep 2: Merged into {len(walls)} wall segments")

    paired = sum(1 for w in walls if w["measured_thickness"] > 0)
    unpaired = len(walls) - paired
    print(f"  Paired (with measured thickness): {paired}")
    print(f"  Unpaired (using default thickness): {unpaired}")

    # Step 4: Convert to meters
    print(f"\nStep 3: Converting to meters...")
    meter_walls, width_m, depth_m = to_meters(walls, bounds)

    # Wall type breakdown
    by_type = {}
    for w in meter_walls:
        t = w["type"]
        by_type[t] = by_type.get(t, 0) + 1
    print(f"\n  Wall type breakdown:")
    for t in sorted(by_type.keys()):
        print(f"    {t}: {by_type[t]} walls")

    # Step 5: Output JSON
    output = {
        "floor_height": 3.6,
        "width": round(width_m, 3),
        "depth": round(depth_m, 3),
        "walls": meter_walls,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n=== Result ===")
    print(f"  Output: {OUTPUT_PATH}")
    print(f"  Model: {width_m:.2f}m x {depth_m:.2f}m")
    print(f"  Total walls: {len(meter_walls)}")

    doc.close()


if __name__ == "__main__":
    main()
