"""
Parse DXF converted from DWG. Handles BLOCK definitions + INSERT references.
Outputs JSON with wall geometry for Three.js.
"""
import json
import math
from collections import Counter

DXF_PATH = "floorplan.dxf"
OUTPUT_PATH = "viewer/public/floorplan_data.json"


def read_group_codes(filepath):
    """Read DXF file as (code, value) pairs."""
    with open(filepath, 'r', errors='replace') as f:
        lines = f.readlines()
    pairs = []
    i = 0
    while i + 1 < len(lines):
        try:
            code = int(lines[i].strip())
        except ValueError:
            i += 1
            continue
        val = lines[i + 1].strip()
        pairs.append((code, val))
        i += 2
    return pairs


def parse_sections(pairs):
    """Split into sections: HEADER, CLASSES, TABLES, BLOCKS, ENTITIES, OBJECTS."""
    sections = {}
    current_section = None
    start = 0
    for i, (code, val) in enumerate(pairs):
        if code == 0 and val == 'SECTION':
            start = i
        elif code == 2 and i > 0 and pairs[i-1] == (0, 'SECTION'):
            current_section = val
        elif code == 0 and val == 'ENDSEC' and current_section:
            sections[current_section] = pairs[start:i+1]
            current_section = None
    return sections


def parse_blocks(pairs):
    """Parse BLOCK definitions, returning {block_name: [entities]}."""
    blocks = {}
    i = 0
    current_block = None
    current_entities = []

    while i < len(pairs):
        code, val = pairs[i]
        if code == 0 and val == 'BLOCK':
            current_entities = []
            # Find block name (group code 2)
            j = i + 1
            while j < len(pairs) and pairs[j][0] != 0:
                if pairs[j][0] == 2:
                    current_block = pairs[j][1]
                j += 1
            i = j
            continue
        elif code == 0 and val == 'ENDBLK':
            if current_block:
                blocks[current_block] = current_entities
            current_block = None
            current_entities = []
            i += 1
            continue

        if current_block is not None:
            # Parse entity within block
            if code == 0:
                entity = parse_entity(pairs, i)
                if entity:
                    current_entities.append(entity)

        i += 1

    return blocks


def parse_entity(pairs, start):
    """Parse a single entity starting at index start."""
    if start >= len(pairs):
        return None
    code, etype = pairs[start]
    if code != 0:
        return None

    entity = {'type': etype, 'layer': '0'}
    vertices = []
    current_v = {}
    i = start + 1

    while i < len(pairs) and pairs[i][0] != 0:
        c, v = pairs[i]

        if c == 8:
            entity['layer'] = v
        elif c == 62:
            entity['color'] = int(v)
        elif c == 2:
            entity['name'] = v  # for INSERT

        # LINE coords
        if etype == 'LINE':
            if c == 10: entity['x1'] = float(v)
            elif c == 20: entity['y1'] = float(v)
            elif c == 11: entity['x2'] = float(v)
            elif c == 21: entity['y2'] = float(v)

        # LWPOLYLINE coords
        elif etype == 'LWPOLYLINE':
            if c == 70:
                entity['closed'] = (int(v) & 1) == 1
            elif c == 10:
                if current_v and 'x' in current_v:
                    vertices.append(current_v)
                current_v = {'x': float(v)}
            elif c == 20:
                current_v['y'] = float(v)

        # INSERT (block reference)
        elif etype == 'INSERT':
            if c == 10: entity['x'] = float(v)
            elif c == 20: entity['y'] = float(v)
            elif c == 41: entity['sx'] = float(v)
            elif c == 42: entity['sy'] = float(v)
            elif c == 50: entity['rotation'] = float(v)

        # ARC
        elif etype == 'ARC' or etype == 'CIRCLE':
            if c == 10: entity['cx'] = float(v)
            elif c == 20: entity['cy'] = float(v)
            elif c == 40: entity['radius'] = float(v)

        i += 1

    if etype == 'LWPOLYLINE':
        if current_v and 'x' in current_v:
            vertices.append(current_v)
        entity['vertices'] = vertices

    return entity


def parse_entities_section(pairs):
    """Parse ENTITIES section for INSERT references and direct entities."""
    entities = []
    i = 0
    while i < len(pairs):
        code, val = pairs[i]
        if code == 0 and val in ('LINE', 'LWPOLYLINE', 'INSERT', 'ARC', 'CIRCLE', 'POLYLINE'):
            entity = parse_entity(pairs, i)
            if entity:
                entities.append(entity)
        i += 1
    return entities


def resolve_inserts(entities, blocks, depth=0):
    """Resolve INSERT references to actual geometry, applying transforms."""
    if depth > 5:
        return []

    result = []
    for e in entities:
        if e['type'] == 'INSERT':
            block_name = e.get('name', '')
            if block_name not in blocks:
                continue

            ox = e.get('x', 0)
            oy = e.get('y', 0)
            sx = e.get('sx', 1)
            sy = e.get('sy', 1)
            rot = math.radians(e.get('rotation', 0))

            block_entities = blocks[block_name]
            resolved = resolve_inserts(block_entities, blocks, depth + 1)

            for be in resolved:
                transformed = transform_entity(be, ox, oy, sx, sy, rot)
                if transformed:
                    result.append(transformed)
        else:
            result.append(e)

    return result


def transform_entity(entity, ox, oy, sx, sy, rot):
    """Apply INSERT transform (translate, scale, rotate) to an entity."""
    def xform(x, y):
        # Scale
        x2, y2 = x * sx, y * sy
        # Rotate
        cos_r, sin_r = math.cos(rot), math.sin(rot)
        x3 = x2 * cos_r - y2 * sin_r
        y3 = x2 * sin_r + y2 * cos_r
        # Translate
        return x3 + ox, y3 + oy

    e = dict(entity)
    if e['type'] == 'LINE' and 'x1' in e:
        e['x1'], e['y1'] = xform(e['x1'], e['y1'])
        e['x2'], e['y2'] = xform(e['x2'], e['y2'])
        return e
    elif e['type'] == 'LWPOLYLINE' and 'vertices' in e:
        e['vertices'] = []
        for v in entity['vertices']:
            if 'x' in v and 'y' in v:
                nx, ny = xform(v['x'], v['y'])
                e['vertices'].append({'x': nx, 'y': ny})
        return e
    return e


def to_segments(entities):
    """Convert entities to line segments."""
    segs = []
    for e in entities:
        layer = e.get('layer', '0')
        color = e.get('color', 0)

        if e['type'] == 'LINE' and 'x1' in e and 'x2' in e:
            segs.append({
                'x1': e['x1'], 'y1': e['y1'],
                'x2': e['x2'], 'y2': e['y2'],
                'layer': layer, 'color': color,
            })
        elif e['type'] == 'LWPOLYLINE' and 'vertices' in e:
            verts = e['vertices']
            for j in range(len(verts) - 1):
                segs.append({
                    'x1': verts[j]['x'], 'y1': verts[j]['y'],
                    'x2': verts[j+1]['x'], 'y2': verts[j+1]['y'],
                    'layer': layer, 'color': color,
                })
            if e.get('closed') and len(verts) >= 3:
                segs.append({
                    'x1': verts[-1]['x'], 'y1': verts[-1]['y'],
                    'x2': verts[0]['x'], 'y2': verts[0]['y'],
                    'layer': layer, 'color': color,
                })

    return segs


def classify_walls(segments):
    """Classify segments into wall types and convert to meters."""
    if not segments:
        return [], 0, 0

    # Filter by wall-related layers
    wall_layers = set()
    for s in segments:
        layer = s['layer']
        if any(kw in layer for kw in ['WALL', '牆', '壁', '隔間', 'RC', '模板', '女兒牆']):
            wall_layers.add(layer)
        elif any(kw in layer for kw in ['門', 'DOOR', '窗', 'WIND']):
            wall_layers.add(layer)

    # Also keep layers with many long segments (likely structural)
    layer_lengths = {}
    for s in segments:
        length = math.hypot(s['x2'] - s['x1'], s['y2'] - s['y1'])
        layer_lengths.setdefault(s['layer'], []).append(length)

    for layer, lengths in layer_lengths.items():
        avg_len = sum(lengths) / len(lengths)
        long_count = sum(1 for l in lengths if l > 50)  # > 50 units = > 5cm in mm scale
        if long_count > 3 and avg_len > 30:
            wall_layers.add(layer)

    print(f"\nWall-related layers: {wall_layers}")

    # Get only wall segments
    wall_segs = [s for s in segments if s['layer'] in wall_layers]

    if not wall_segs:
        print("No wall segments found, using ALL segments")
        wall_segs = segments

    # Find bounds of wall segments
    all_x = [s['x1'] for s in wall_segs] + [s['x2'] for s in wall_segs]
    all_y = [s['y1'] for s in wall_segs] + [s['y2'] for s in wall_segs]
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    draw_w = max_x - min_x
    draw_h = max_y - min_y

    # Determine scale - try mm first
    scale = 1.0 / 1000.0
    w_m = draw_w * scale
    h_m = draw_h * scale

    # If dimensions seem off, try other scales
    if w_m < 1 or w_m > 50:
        # Try cm
        scale = 1.0 / 100.0
        w_m = draw_w * scale
        h_m = draw_h * scale
    if w_m < 1 or w_m > 50:
        # Try raw units = meters
        scale = 1.0
        w_m = draw_w
        h_m = draw_h

    print(f"\nWall bounds: ({min_x:.1f}, {min_y:.1f}) → ({max_x:.1f}, {max_y:.1f})")
    print(f"Size: {draw_w:.1f} × {draw_h:.1f} units → {w_m:.2f} × {h_m:.2f} m (scale={scale})")

    walls = []
    for s in wall_segs:
        length = math.hypot(s['x2'] - s['x1'], s['y2'] - s['y1']) * scale
        if length < 0.03 or length > 20:
            continue

        layer = s['layer']
        if any(kw in layer for kw in ['WALL', '牆', 'RC', '模板']):
            wall_type = 'rc'
            thickness = 0.15
        elif any(kw in layer for kw in ['隔間', '輕', '磚']):
            wall_type = 'brick'
            thickness = 0.10
        elif any(kw in layer for kw in ['門', 'DOOR']):
            wall_type = 'door'
            thickness = 0.05
        else:
            wall_type = 'other'
            thickness = 0.08

        walls.append({
            'x1': round((s['x1'] - min_x) * scale, 4),
            'z1': round((max_y - s['y1']) * scale, 4),
            'x2': round((s['x2'] - min_x) * scale, 4),
            'z2': round((max_y - s['y2']) * scale, 4),
            'thickness': thickness,
            'type': wall_type,
            'layer': layer,
        })

    return walls, w_m, h_m


def main():
    print("=== Parsing DXF (DWG converted) with block resolution ===\n")

    pairs = read_group_codes(DXF_PATH)
    print(f"Read {len(pairs)} group code pairs")

    sections = parse_sections(pairs)
    print(f"Sections: {list(sections.keys())}")

    # Parse BLOCKS
    blocks = {}
    if 'BLOCKS' in sections:
        blocks = parse_blocks(sections['BLOCKS'])
        print(f"Parsed {len(blocks)} blocks")
        for name, ents in sorted(blocks.items(), key=lambda x: -len(x[1]))[:15]:
            types = Counter(e['type'] for e in ents)
            print(f"  {name}: {len(ents)} entities {dict(types)}")

    # Parse ENTITIES (mainly INSERTs)
    if 'ENTITIES' in sections:
        raw_entities = parse_entities_section(sections['ENTITIES'])
        print(f"\nENTITIES section: {len(raw_entities)} entities")
        types = Counter(e['type'] for e in raw_entities)
        print(f"  Types: {dict(types)}")

        # Resolve INSERT references
        resolved = resolve_inserts(raw_entities, blocks)
        print(f"After resolving inserts: {len(resolved)} entities")
    else:
        resolved = []

    # Convert to line segments
    segments = to_segments(resolved)
    print(f"Total line segments: {len(segments)}")

    # Layer analysis
    layer_counts = Counter(s['layer'] for s in segments)
    print(f"\nLayers ({len(layer_counts)}):")
    for layer, count in layer_counts.most_common(25):
        print(f"  {layer}: {count}")

    # Classify and output
    walls, width_m, depth_m = classify_walls(segments)

    output = {
        "floor_height": 3.6,
        "width": round(width_m, 3),
        "depth": round(depth_m, 3),
        "walls": walls,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    type_counts = Counter(w['type'] for w in walls)
    print(f"\n=== Output: {OUTPUT_PATH} ===")
    print(f"Size: {width_m:.2f}m × {depth_m:.2f}m")
    print(f"Walls: {len(walls)} ({dict(type_counts)})")


if __name__ == "__main__":
    main()
