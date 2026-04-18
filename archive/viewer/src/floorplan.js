import * as THREE from 'three';
import { CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

// ============================================================
// 2F/C戶 建築平面圖 - 樓高 H=360cm
//
// Coordinate: x=West→East, z=South→North, y=up
// Origin at southwest corner of the unit
//
// From the PDF, tracing walls carefully:
//
//  NORTH (z=D)
//  ┌───────────┬────────────────────────────┬───┐
//  │G5 window  │  玄關門 128x250            │col│
//  │           │                            │   │
//  │ Kitchen   │     客廳 Living Room       │   │
//  │ (applian- │                            │陽 │
//  │  ces on   │     SDW03 103.5x240       │台 │
//  │  east     │     (sliding door→balcony) │Bal│
//  │  wall)    │b6                          │   │
//  ├───────────┴──┬─────────────────────────┤   │
//  │              │                         │   │
//  │  Bedroom 1   │    Bedroom 2            │B6 │
//  │  臥室        │    臥室                 │   │
//  │        ┌─────┤                         │   │
//  │  B4    │Bath │                         │   │
//  │        │浴廁 │                         │   │
//  │        │W06  │                         │   │
//  └────W04─┴─────┴────────W04──────────────┘
//  SOUTH (z=0)
// ============================================================

const H = 3.6;       // floor height 360cm
const RC = 0.15;     // 15cm RC wall
const BRK = 0.10;    // brick partition wall

// Overall unit dimensions
const W = 7.5;       // width east-west
const D = 7.0;       // depth north-south

// Key layout lines
const VWALL_X = 2.6;   // center vertical RC wall (kitchen east / living west)
const DIV_Z = 3.8;     // horizontal divider (bedrooms south / kitchen+living north)

// Bathroom (compact, south-center, left of bedroom divider)
const BATH_W = 1.5;     // bathroom width
const BATH_D = 2.2;     // bathroom depth
const BATH_X1 = 2.3;    // bathroom west wall x
const BATH_X2 = BATH_X1 + BATH_W; // 3.8 - bathroom east wall x
const BATH_Z1 = RC;     // bathroom starts at south wall interior
const BATH_Z2 = BATH_Z1 + BATH_D; // bathroom north wall z

// Bedroom divider (continues from center wall down through bedroom area)
const BED_DIV_X = BATH_X2; // bedroom divider aligns with bathroom east wall

// Materials
const mat = {
  rc: new THREE.MeshStandardMaterial({ color: 0xd4cfc4, roughness: 0.85 }),
  brk: new THREE.MeshStandardMaterial({ color: 0xe8d5c4, roughness: 0.9 }),
  floor: new THREE.MeshStandardMaterial({ color: 0xc8b898, roughness: 0.7 }),
  ceil: new THREE.MeshStandardMaterial({ color: 0xf0ece4, roughness: 0.5, side: THREE.DoubleSide }),
  win: new THREE.MeshStandardMaterial({ color: 0x88bbee, roughness: 0.1, metalness: 0.3, transparent: true, opacity: 0.35 }),
  door: new THREE.MeshStandardMaterial({ color: 0x8B6914, roughness: 0.6, metalness: 0.1 }),
  balcony: new THREE.MeshStandardMaterial({ color: 0xa0a0a0, roughness: 0.8, metalness: 0.1 }),
  rail: new THREE.MeshStandardMaterial({ color: 0x666666, roughness: 0.3, metalness: 0.6, transparent: true, opacity: 0.7 }),
};

Object.values(mat).forEach(m => {
  m.userData = { originalTransparent: m.transparent, originalOpacity: m.opacity };
});

// ---- helpers ----

function wall(x, z, len, thick, h, dir, material) {
  const w = dir === 'x' ? len : thick;
  const d = dir === 'z' ? len : thick;
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  mesh.position.set(
    dir === 'x' ? x + len / 2 : x + thick / 2,
    h / 2,
    dir === 'z' ? z + len / 2 : z + thick / 2
  );
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  return mesh;
}

function wallWithOpenings(x, z, len, thick, h, dir, material, openings) {
  const g = new THREE.Group();
  openings.sort((a, b) => a.pos - b.pos);
  let cur = 0;
  for (const o of openings) {
    // solid before
    if (o.pos > cur) {
      g.add(wall(dir === 'x' ? x + cur : x, dir === 'z' ? z + cur : z, o.pos - cur, thick, h, dir, material));
    }
    // below sill
    if (o.sill > 0) {
      g.add(wall(dir === 'x' ? x + o.pos : x, dir === 'z' ? z + o.pos : z, o.width, thick, o.sill, dir, material));
    }
    // above opening
    const top = h - o.sill - o.height;
    if (top > 0) {
      const w2 = wall(dir === 'x' ? x + o.pos : x, dir === 'z' ? z + o.pos : z, o.width, thick, top, dir, material);
      w2.position.y = o.sill + o.height + top / 2;
      g.add(w2);
    }
    // fill (glass/door)
    if (o.fill) {
      const fw = dir === 'x' ? o.width : 0.02;
      const fd = dir === 'z' ? o.width : 0.02;
      const m = new THREE.Mesh(new THREE.BoxGeometry(fw, o.height, fd), o.fill);
      m.position.set(
        dir === 'x' ? x + o.pos + o.width / 2 : x + thick / 2,
        o.sill + o.height / 2,
        dir === 'z' ? z + o.pos + o.width / 2 : z + thick / 2
      );
      g.add(m);
    }
    cur = o.pos + o.width;
  }
  if (cur < len) {
    g.add(wall(dir === 'x' ? x + cur : x, dir === 'z' ? z + cur : z, len - cur, thick, h, dir, material));
  }
  return g;
}

function label(text, x, y, z) {
  const div = document.createElement('div');
  div.textContent = text;
  div.style.cssText = 'color:#fff;font-size:13px;background:rgba(0,0,0,0.55);padding:3px 8px;border-radius:4px;white-space:nowrap;';
  const l = new CSS2DObject(div);
  l.position.set(x, y, z);
  return l;
}

export function buildFloorPlan() {
  const house = new THREE.Group();
  const labels = [];

  // ---- Floor ----
  const fl = new THREE.Mesh(new THREE.BoxGeometry(W, 0.08, D), mat.floor);
  fl.position.set(W / 2, -0.04, D / 2);
  fl.receiveShadow = true;
  house.add(fl);

  // ---- Ceiling ----
  const cm = mat.ceil.clone();
  cm.transparent = true; cm.opacity = 0.15;
  cm.userData = { originalTransparent: true, originalOpacity: 0.15 };
  const ce = new THREE.Mesh(new THREE.PlaneGeometry(W, D), cm);
  ce.rotation.x = Math.PI / 2;
  ce.position.set(W / 2, H, D / 2);
  house.add(ce);

  // ================================================================
  // EXTERIOR WALLS (RC 15cm)
  // ================================================================

  // SOUTH wall (z=0): W04 | W06 | W04
  house.add(wallWithOpenings(0, 0, W, RC, H, 'x', mat.rc, [
    { pos: 0.4, width: 1.69, height: 1.85, sill: 0.58, fill: mat.win },    // W04 (bedroom 1)
    { pos: 2.65, width: 0.555, height: 1.89, sill: 0.58, fill: mat.win },   // W06 (bathroom)
    { pos: 4.3, width: 1.69, height: 1.85, sill: 0.58, fill: mat.win },     // W04 (bedroom 2)
  ]));

  // NORTH wall (z=D-RC): G5 window left, 玄關門 center-right
  house.add(wallWithOpenings(0, D - RC, W, RC, H, 'x', mat.rc, [
    { pos: 0.6, width: 0.50, height: 0.80, sill: 1.2, fill: mat.win },      // G5 50x80 (kitchen)
    { pos: 3.2, width: 1.28, height: 2.50, sill: 0, fill: mat.door },       // 玄關門 entrance 128x250
  ]));

  // WEST wall (x=0): B4 window in lower portion
  house.add(wallWithOpenings(0, 0, D, RC, H, 'z', mat.rc, [
    { pos: 1.6, width: 0.55, height: 0.80, sill: 1.2, fill: mat.win },      // B4 55x80
  ]));

  // EAST wall (x=W-RC): B6 window lower, SDW03 upper
  house.add(wallWithOpenings(W - RC, 0, D, RC, H, 'z', mat.rc, [
    { pos: 2.0, width: 0.70, height: 0.90, sill: 1.0, fill: mat.win },      // B6 70x90
    { pos: 4.5, width: 1.035, height: 2.40, sill: 0, fill: mat.win },       // SDW03 sliding door→balcony
  ]));

  // ================================================================
  // NO wall between kitchen and living room - open plan upper area
  // ================================================================

  // ================================================================
  // HORIZONTAL DIVIDER (brick, z=DIV_Z)
  // From west wall to east wall, with bedroom doors
  // ================================================================

  // Left section: west wall to bathroom area, with bedroom 1 door
  house.add(wallWithOpenings(RC, DIV_Z, BATH_X1 - RC, BRK, H, 'x', mat.brk, [
    { pos: 1.0, width: 0.85, height: 2.1, sill: 0, fill: mat.door },        // bedroom 1 door
  ]));

  // Center section: bathroom area, with door to living room (restroom↔living room)
  house.add(wallWithOpenings(BATH_X1, DIV_Z, BED_DIV_X - BATH_X1, BRK, H, 'x', mat.brk, [
    { pos: 0.3, width: 0.65, height: 2.1, sill: 0, fill: mat.door },        // door between bathroom corridor and living room
  ]));

  // Right section: bedroom divider to east wall, with bedroom 2 door (sliding)
  house.add(wallWithOpenings(BED_DIV_X, DIV_Z, W - RC - BED_DIV_X, BRK, H, 'x', mat.brk, [
    { pos: 0.2, width: 0.90, height: 2.1, sill: 0, fill: mat.door },        // bedroom 2 door
  ]));

  // ================================================================
  // BEDROOM DIVIDER (brick, from horizontal divider down to bathroom)
  // Aligns with bathroom east wall at x=BED_DIV_X
  // ================================================================
  // From divider south to bathroom north wall
  house.add(wall(BED_DIV_X, BATH_Z2, DIV_Z - BATH_Z2, BRK, H, 'z', mat.brk));

  // ================================================================
  // BATHROOM ENCLOSURE (brick walls)
  // ================================================================

  // Bathroom west wall (x=BATH_X1, from south interior to BATH_Z2)
  house.add(wall(BATH_X1, RC, BATH_Z2 - RC, BRK, H, 'z', mat.brk));

  // Bathroom east wall = BED_DIV_X wall continues to south
  // (from south interior to BATH_Z2 - already have divider above, now south portion)
  house.add(wall(BED_DIV_X, RC, BATH_Z2 - RC, BRK, H, 'z', mat.brk));

  // Bathroom north wall (z=BATH_Z2, from BATH_X1 to BED_DIV_X) with door
  house.add(wallWithOpenings(BATH_X1, BATH_Z2, BED_DIV_X - BATH_X1, BRK, H, 'x', mat.brk, [
    { pos: 0.3, width: 0.65, height: 2.1, sill: 0, fill: mat.door },        // bathroom door
  ]));

  // ================================================================
  // BALCONY (east side, upper portion)
  // ================================================================
  const balW = 1.5;
  const balD = 2.5;
  const balZ = 4.2;

  const bf = new THREE.Mesh(new THREE.BoxGeometry(balW, 0.1, balD), mat.balcony);
  bf.position.set(W + balW / 2, -0.05, balZ + balD / 2);
  bf.receiveShadow = true;
  house.add(bf);

  const rH = 1.1, rT = 0.05;
  // outer rail
  const r1 = new THREE.Mesh(new THREE.BoxGeometry(rT, rH, balD), mat.rail);
  r1.position.set(W + balW, rH / 2, balZ + balD / 2);
  house.add(r1);
  // north rail
  const r2 = new THREE.Mesh(new THREE.BoxGeometry(balW, rH, rT), mat.rail);
  r2.position.set(W + balW / 2, rH / 2, balZ + balD);
  house.add(r2);
  // south rail
  const r3 = new THREE.Mesh(new THREE.BoxGeometry(balW, rH, rT), mat.rail);
  r3.position.set(W + balW / 2, rH / 2, balZ);
  house.add(r3);

  // ================================================================
  // STRUCTURAL COLUMN (north-east corner, visible in drawing)
  // ================================================================
  const col = new THREE.Mesh(new THREE.BoxGeometry(0.4, H, 0.5), mat.rc);
  col.position.set(W - 0.2, H / 2, D - 0.25);
  house.add(col);

  // AC outdoor unit (gray square outside north-west)
  const ac = new THREE.Mesh(
    new THREE.BoxGeometry(0.8, 0.6, 0.3),
    new THREE.MeshStandardMaterial({ color: 0x888888, roughness: 0.5 })
  );
  ac.position.set(0.6, 0.3, D + 0.3);
  house.add(ac);

  // ================================================================
  // ROOM LABELS
  // ================================================================
  const ly = 1.5;
  labels.push(label('廚房 Kitchen', 1.3, ly, (DIV_Z + D) / 2));
  labels.push(label('客廳 Living Room', 5.0, ly, (DIV_Z + D) / 2));
  labels.push(label('臥室 Bedroom 1', BATH_X1 / 2, ly, DIV_Z * 0.55));
  labels.push(label('臥室 Bedroom 2', (BED_DIV_X + W) / 2, ly, DIV_Z * 0.5));
  labels.push(label('浴廁 Bathroom', (BATH_X1 + BED_DIV_X) / 2, ly, (BATH_Z1 + BATH_Z2) / 2));
  labels.push(label('陽台 Balcony', W + balW / 2, 1.0, balZ + balD / 2));
  labels.push(label('玄關 Entrance', 3.2 + 0.64, ly, D - 0.5));

  // ================================================================
  // FURNITURE (simple hints)
  // ================================================================
  const furnMat = new THREE.MeshStandardMaterial({ color: 0x7a9e7e, roughness: 0.8, transparent: true, opacity: 0.4 });
  furnMat.userData = { originalTransparent: true, originalOpacity: 0.4 };
  const whiteMat = new THREE.MeshStandardMaterial({ color: 0xeeeeee, roughness: 0.3 });
  whiteMat.userData = { originalTransparent: false, originalOpacity: 1 };
  const bedMat = new THREE.MeshStandardMaterial({ color: 0x6b8cae, roughness: 0.8, transparent: true, opacity: 0.5 });
  bedMat.userData = { originalTransparent: true, originalOpacity: 0.5 };

  // Kitchen: appliances along east wall (center RC wall)
  function addBox(geo, material, x, y, z) {
    const m = new THREE.Mesh(geo, material);
    m.position.set(x, y, z);
    house.add(m);
  }

  // Kitchen appliances along north wall (left side of upper area)
  addBox(new THREE.BoxGeometry(0.6, 0.05, 0.6), furnMat, 0.5, 0.9, D - 0.5);                 // Cooktop
  addBox(new THREE.BoxGeometry(0.5, 0.3, 0.5), whiteMat, 1.3, 0.85, D - 0.5);                // Sink
  addBox(new THREE.BoxGeometry(0.6, 0.85, 0.6), whiteMat, 2.1, 0.425, D - 0.5);              // Washer

  // Bathroom: toilet + sink
  addBox(new THREE.BoxGeometry(0.4, 0.4, 0.55), whiteMat, (BATH_X1 + BED_DIV_X) / 2 + 0.2, 0.2, 0.6);
  addBox(new THREE.BoxGeometry(0.45, 0.3, 0.35), whiteMat, BATH_X1 + 0.35, 0.85, BATH_Z2 - 0.3);

  // Beds
  addBox(new THREE.BoxGeometry(1.5, 0.4, 2.0), bedMat, 1.0, 0.2, 2.0);
  addBox(new THREE.BoxGeometry(1.8, 0.4, 2.0), bedMat, 5.5, 0.2, 1.8);

  // Sofa in living room
  const sofaMat = new THREE.MeshStandardMaterial({ color: 0x8b7355, roughness: 0.9, transparent: true, opacity: 0.5 });
  sofaMat.userData = { originalTransparent: true, originalOpacity: 0.5 };
  addBox(new THREE.BoxGeometry(1.8, 0.45, 0.8), sofaMat, 5.5, 0.225, 5.0);

  // Flip Z axis so that in top-down view, north (kitchen/living) is at TOP
  // matching the PDF orientation
  house.scale.z = -1;
  house.position.z = D; // re-center after flip

  // Fix face winding by setting all materials to DoubleSide
  house.traverse(child => {
    if (child.isMesh) {
      const mats = Array.isArray(child.material) ? child.material : [child.material];
      mats.forEach(m => { m.side = THREE.DoubleSide; });
    }
  });

  // Flip label z-positions to match
  labels.forEach(l => { l.position.z = D - l.position.z; });

  return { house, labels };
}
