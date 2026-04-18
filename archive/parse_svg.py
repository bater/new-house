"""
Parse SVG exported from DWG (via dwg2SVG) to extract wall geometry.
The SVG contains all block references resolved to actual vector paths.
"""
import json
import math
import re
import xml.etree.ElementTree as ET
from collections import Counter

SVG_PATH = "floorplan.svg"
OUTPUT_PATH = "viewer/public/floorplan_data.json"

NS = {'svg': 'http://www.w3.org/2000/svg'}


def parse_svg_paths(filepath):
    """Parse SVG file and extract all path/line/circle elements with styles."""
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Get viewBox for coordinate reference
    vb = root.get('viewBox', '0 0 1000 1000')
    vb_parts = [float(x) for x in vb.split()]
    print(f"ViewBox: {vb_parts}")

    segments = []
    stroke_widths = Counter()

    def parse_style(style_str):
        """Parse CSS style string."""
        props = {}
        if style_str:
            for part in style_str.split(';'):
                if ':' in part:
                    k, v = part.split(':', 1)
                    props[k.strip()] = v.strip()
        return props

    def process_element(elem, parent_transform=None):
        """Recursively process SVG elements."""
        tag = elem.tag.replace('{http://www.w3.org/2000/svg}', '')

        style = parse_style(elem.get('style', ''))
        stroke = style.get('stroke', elem.get('stroke', 'black'))
        stroke_width_str = style.get('stroke-width', elem.get('stroke-width', '0.1px'))
        stroke_width = float(re.sub(r'[a-zA-Z%]+', '', stroke_width_str) or '0.1')

        if tag == 'path':
            d = elem.get('d', '')
            # Parse simple M/L/Z path commands
            points = parse_path_d(d)
            if len(points) >= 2:
                for i in range(len(points) - 1):
                    segments.append({
                        'x1': points[i][0], 'y1': points[i][1],
                        'x2': points[i+1][0], 'y2': points[i+1][1],
                        'stroke_width': stroke_width,
                        'stroke': stroke,
                    })
                    stroke_widths[stroke_width] += 1

        elif tag == 'line':
            x1 = float(elem.get('x1', 0))
            y1 = float(elem.get('y1', 0))
            x2 = float(elem.get('x2', 0))
            y2 = float(elem.get('y2', 0))
            segments.append({
                'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                'stroke_width': stroke_width, 'stroke': stroke,
            })
            stroke_widths[stroke_width] += 1

        # Recurse into groups (resolves block references)
        for child in elem:
            process_element(child, parent_transform)

    process_element(root)

    print(f"Extracted {len(segments)} line segments")
    print(f"Stroke width distribution:")
    for w, c in stroke_widths.most_common(15):
        print(f"  {w}: {c}")

    return segments, vb_parts


def parse_path_d(d):
    """Parse SVG path d attribute into coordinate points."""
    points = []
    # Handle M (moveto) and L (lineto) commands
    parts = re.findall(r'[MLHVZmlhvz]|[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', d)

    x, y = 0, 0
    cmd = 'M'
    i = 0

    while i < len(parts):
        if parts[i] in 'MLHVZmlhvz':
            cmd = parts[i]
            i += 1
            if cmd in 'Zz':
                if points:
                    points.append(points[0])  # close
                continue

        if i >= len(parts):
            break

        if cmd == 'M' or cmd == 'L':
            x = float(parts[i])
            i += 1
            if i < len(parts) and parts[i] not in 'MLHVZmlhvz':
                # Check if next is a comma or number
                val = parts[i].replace(',', '')
                if val:
                    y = float(val)
                    i += 1
            points.append((x, y))
            if cmd == 'M':
                cmd = 'L'  # implicit lineto after moveto

        elif cmd == 'm' or cmd == 'l':
            dx = float(parts[i])
            i += 1
            if i < len(parts) and parts[i] not in 'MLHVZmlhvz':
                dy = float(parts[i])
                i += 1
                x += dx
                y += dy
                points.append((x, y))
            if cmd == 'm':
                cmd = 'l'

        elif cmd == 'H':
            x = float(parts[i]); i += 1
            points.append((x, y))
        elif cmd == 'h':
            x += float(parts[i]); i += 1
            points.append((x, y))
        elif cmd == 'V':
            y = float(parts[i]); i += 1
            points.append((x, y))
        elif cmd == 'v':
            y += float(parts[i]); i += 1
            points.append((x, y))
        else:
            i += 1  # skip unknown

    return points


def filter_wall_segments(segments, viewbox):
    """
    Filter segments to keep only wall-like ones.
    Walls are characterized by:
    - Being straight (horizontal or vertical)
    - Having consistent stroke widths
    - Being within certain length ranges
    """
    vb_x, vb_y, vb_w, vb_h = viewbox

    # Note: SVG Y coordinates from dwg2SVG use inverted Y from DWG
    # The viewBox already accounts for this

    # Compute bounds of all segments
    all_x = [s['x1'] for s in segments] + [s['x2'] for s in segments]
    all_y = [s['y1'] for s in segments] + [s['y2'] for s in segments]

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    draw_w = max_x - min_x
    draw_h = max_y - min_y

    print(f"\nSegment bounds: ({min_x:.1f},{min_y:.1f}) → ({max_x:.1f},{max_y:.1f})")
    print(f"Size: {draw_w:.1f} × {draw_h:.1f}")

    # Filter: keep meaningful segments
    filtered = []
    for s in segments:
        length = math.hypot(s['x2'] - s['x1'], s['y2'] - s['y1'])
        # Skip very short (< 2 units) or very long (> 2000 units)
        if length < 2 or length > 2000:
            continue
        # Skip if outside main drawing area
        if s['x1'] < min_x + draw_w * 0.01 and s['x2'] < min_x + draw_w * 0.01:
            continue
        filtered.append(s)

    print(f"After filtering: {len(filtered)} segments")
    return filtered, (min_x, min_y, max_x, max_y)


def identify_floor_plan_region(segments, bounds):
    """
    The DWG has multiple pages. Identify which region is the floor plan.
    The floor plan (page 1) should be roughly square and in the leftmost position.
    """
    min_x, min_y, max_x, max_y = bounds
    total_w = max_x - min_x

    # Divide into 4 regions (4 PDF pages)
    page_w = total_w / 4

    # Group segments by page region
    pages = [[] for _ in range(4)]
    for s in segments:
        cx = (s['x1'] + s['x2']) / 2
        page_idx = min(3, int((cx - min_x) / page_w))
        pages[page_idx].append(s)

    for i, page in enumerate(pages):
        if page:
            xs = [s['x1'] for s in page] + [s['x2'] for s in page]
            ys = [s['y1'] for s in page] + [s['y2'] for s in page]
            pw = max(xs) - min(xs)
            ph = max(ys) - min(ys)
            print(f"  Page {i}: {len(page)} segs, size {pw:.0f} × {ph:.0f}")

    # Return page 0 (first page = architectural floor plan)
    # Actually, find the page with the most segments that has a reasonable aspect ratio
    best_page = max(range(4), key=lambda i: len(pages[i]))
    print(f"\nUsing page {best_page} ({len(pages[best_page])} segments)")
    return pages[best_page]


def convert_to_3d(segments):
    """Convert filtered segments to 3D wall data."""
    if not segments:
        return [], 0, 0

    all_x = [s['x1'] for s in segments] + [s['x2'] for s in segments]
    all_y = [s['y1'] for s in segments] + [s['y2'] for s in segments]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    draw_w = max_x - min_x
    draw_h = max_y - min_y

    # Convert to meters - DWG units are mm
    scale = 1.0 / 1000.0

    # Classify by stroke width
    walls = []
    for s in segments:
        length = math.hypot(s['x2'] - s['x1'], s['y2'] - s['y1']) * scale
        if length < 0.03:
            continue

        sw = s['stroke_width']
        if sw >= 1.0:
            wall_type = 'rc'
            thickness = 0.15
        elif sw >= 0.3:
            wall_type = 'brick'
            thickness = 0.10
        else:
            wall_type = 'other'
            thickness = 0.06

        walls.append({
            'x1': round((s['x1'] - min_x) * scale, 4),
            'z1': round((max_y - s['y1']) * scale, 4),  # flip Y
            'x2': round((s['x2'] - min_x) * scale, 4),
            'z2': round((max_y - s['y2']) * scale, 4),
            'thickness': thickness,
            'type': wall_type,
        })

    width_m = draw_w * scale
    depth_m = draw_h * scale

    return walls, width_m, depth_m


def main():
    print("=== Parsing SVG from DWG (dwg2SVG output) ===\n")

    segments, viewbox = parse_svg_paths(SVG_PATH)

    filtered, bounds = filter_wall_segments(segments, viewbox)

    page_segments = identify_floor_plan_region(filtered, bounds)

    walls, width_m, depth_m = convert_to_3d(page_segments)

    type_counts = Counter(w['type'] for w in walls)
    print(f"\nModel: {width_m:.2f}m × {depth_m:.2f}m")
    print(f"Walls: {len(walls)} ({dict(type_counts)})")

    output = {
        "floor_height": 3.6,
        "width": round(width_m, 3),
        "depth": round(depth_m, 3),
        "walls": walls,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
