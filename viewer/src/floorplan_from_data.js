import * as THREE from 'three';
import { CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

/**
 * Build a 3D floor plan from extracted PDF vector data.
 * Each wall segment is extruded into a 3D box based on:
 * - Start/end coordinates (x1,z1)→(x2,z2)
 * - Thickness (measured from parallel line pairs or default by type)
 * - Type (rc/brick/light) determines material
 */

const MATERIALS = {
  rc: new THREE.MeshStandardMaterial({ color: 0xd4cfc4, roughness: 0.85, side: THREE.DoubleSide }),
  brick: new THREE.MeshStandardMaterial({ color: 0xe8d5c4, roughness: 0.9, side: THREE.DoubleSide }),
  light: new THREE.MeshStandardMaterial({ color: 0xc0c0c0, roughness: 0.8, side: THREE.DoubleSide }),
  floor: new THREE.MeshStandardMaterial({ color: 0xc8b898, roughness: 0.7, side: THREE.DoubleSide }),
  ceil: new THREE.MeshStandardMaterial({ color: 0xf0ece4, roughness: 0.5, side: THREE.DoubleSide, transparent: true, opacity: 0.15 }),
};

Object.values(MATERIALS).forEach(m => {
  m.userData = { originalTransparent: m.transparent, originalOpacity: m.opacity };
});

function label(text, x, y, z) {
  const div = document.createElement('div');
  div.textContent = text;
  div.style.cssText = 'color:#fff;font-size:13px;background:rgba(0,0,0,0.55);padding:3px 8px;border-radius:4px;white-space:nowrap;';
  const l = new CSS2DObject(div);
  l.position.set(x, y, z);
  return l;
}

export async function buildFloorPlanFromData() {
  const resp = await fetch('/floorplan_data.json');
  const data = await resp.json();

  const house = new THREE.Group();
  const labels = [];

  const H = data.floor_height;
  const W = data.width;
  const D = data.depth;

  // ---- Floor ----
  const fl = new THREE.Mesh(new THREE.BoxGeometry(W, 0.08, D), MATERIALS.floor);
  fl.position.set(W / 2, -0.04, D / 2);
  fl.receiveShadow = true;
  house.add(fl);

  // ---- Ceiling ----
  const ce = new THREE.Mesh(new THREE.PlaneGeometry(W, D), MATERIALS.ceil);
  ce.rotation.x = Math.PI / 2;
  ce.position.set(W / 2, H, D / 2);
  house.add(ce);

  // ---- Walls from data ----
  for (const wall of data.walls) {
    const { x1, z1, x2, z2, thickness, type } = wall;
    const mat = MATERIALS[type] || MATERIALS.brick;

    const dx = x2 - x1;
    const dz = z2 - z1;
    const length = Math.hypot(dx, dz);

    if (length < 0.05) continue; // skip tiny segments

    // Create wall as a box
    const geo = new THREE.BoxGeometry(length, H, thickness);
    const mesh = new THREE.Mesh(geo, mat);

    // Position at center of the line segment
    const cx = (x1 + x2) / 2;
    const cz = (z1 + z2) / 2;
    mesh.position.set(cx, H / 2, cz);

    // Rotate to align with the line direction
    const angle = Math.atan2(dz, dx);
    mesh.rotation.y = -angle;

    mesh.castShadow = true;
    mesh.receiveShadow = true;
    house.add(mesh);
  }

  // ---- Labels (approximate room positions based on model bounds) ----
  // These are rough estimates - you can fine-tune
  labels.push(label('廚房 Kitchen', W * 0.18, 1.5, D * 0.7));
  labels.push(label('客廳 Living Room', W * 0.6, 1.5, D * 0.7));
  labels.push(label('臥室 Bedroom 1', W * 0.18, 1.5, D * 0.35));
  labels.push(label('臥室 Bedroom 2', W * 0.7, 1.5, D * 0.35));
  labels.push(label('浴廁 Bathroom', W * 0.45, 1.5, D * 0.25));
  labels.push(label('陽台 Balcony', W * 0.92, 1.0, D * 0.65));

  return { house, labels };
}
