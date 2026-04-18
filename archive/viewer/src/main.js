import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
import { buildFloorPlanFromData } from './floorplan_from_data.js';

// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a1a2e);

const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(12, 10, 12);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.getElementById('app').appendChild(renderer.domElement);

// CSS2D label renderer
const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize(window.innerWidth, window.innerHeight);
labelRenderer.domElement.style.position = 'absolute';
labelRenderer.domElement.style.top = '0';
labelRenderer.domElement.style.pointerEvents = 'none';
document.getElementById('app').appendChild(labelRenderer.domElement);

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.target.set(3.75, 1.5, 4.0);
controls.update();

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const dirLight = new THREE.DirectionalLight(0xffffff, 1.0);
dirLight.position.set(10, 15, 10);
dirLight.castShadow = true;
dirLight.shadow.mapSize.set(2048, 2048);
dirLight.shadow.camera.left = -15;
dirLight.shadow.camera.right = 15;
dirLight.shadow.camera.top = 15;
dirLight.shadow.camera.bottom = -15;
scene.add(dirLight);

const fillLight = new THREE.DirectionalLight(0x8888ff, 0.3);
fillLight.position.set(-5, 8, -5);
scene.add(fillLight);

// Grid helper
const grid = new THREE.GridHelper(20, 20, 0x444466, 0x333355);
grid.position.y = -0.01;
scene.add(grid);

// Build the floor plan from extracted PDF data
let house;
buildFloorPlanFromData().then(result => {
  house = result.house;
  scene.add(house);
  result.labels.forEach(l => scene.add(l));

  // Update camera target to center of model
  controls.target.set(3.75, 1.5, 3.8);
  controls.update();
});

// Wireframe toggle state
let wireframeMode = false;

// View buttons
const btn3d = document.getElementById('btn-3d');
const btnTop = document.getElementById('btn-top');
const btnFront = document.getElementById('btn-front');
const btnWireframe = document.getElementById('btn-wireframe');

function clearActive() {
  [btn3d, btnTop, btnFront].forEach(b => b.classList.remove('active'));
}

function animateCamera(pos, target, up, duration = 800) {
  const startPos = camera.position.clone();
  const startTarget = controls.target.clone();
  const startUp = camera.up.clone();
  const endPos = new THREE.Vector3(...pos);
  const endTarget = new THREE.Vector3(...target);
  const endUp = new THREE.Vector3(...(up || [0, 1, 0]));
  const startTime = performance.now();

  function step(now) {
    const t = Math.min((now - startTime) / duration, 1);
    const ease = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    camera.position.lerpVectors(startPos, endPos, ease);
    controls.target.lerpVectors(startTarget, endTarget, ease);
    camera.up.lerpVectors(startUp, endUp, ease).normalize();
    controls.update();
    if (t < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

btn3d.addEventListener('click', () => {
  clearActive(); btn3d.classList.add('active');
  animateCamera([12, 10, 12], [3.75, 1.5, 3.8], [0, 1, 0]);
});

btnTop.addEventListener('click', () => {
  clearActive(); btnTop.classList.add('active');
  animateCamera([3.75, 18, 3.8], [3.75, 0, 3.8], [0, 1, 0]);
});

btnFront.addEventListener('click', () => {
  clearActive(); btnFront.classList.add('active');
  animateCamera([3.75, 3, -6], [3.75, 1.5, 3.8], [0, 1, 0]);
});

btnWireframe.addEventListener('click', () => {
  wireframeMode = !wireframeMode;
  btnWireframe.classList.toggle('active', wireframeMode);
  if (!house) return;
  house.traverse(child => {
    if (child.isMesh && child.material) {
      const mats = Array.isArray(child.material) ? child.material : [child.material];
      mats.forEach(m => {
        m.wireframe = wireframeMode;
        m.transparent = wireframeMode ? true : m.userData.originalTransparent ?? m.transparent;
        m.opacity = wireframeMode ? 1 : m.userData.originalOpacity ?? m.opacity;
      });
    }
  });
});

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
}
animate();

// Resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  labelRenderer.setSize(window.innerWidth, window.innerHeight);
});
