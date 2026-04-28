## Documentation

### `README.md`

This file serves as the main README for the EasyCAD software. It describes the application's purpose: a minimalistic CAD software intended to provide makers with the necessary tools and resources to transform conceptual ideas into tangible realities.

### `index.html`

This file structures the main user interface for the EasyCAD application. It sets up the viewport, the toolbar containing tools (Move, Scale, Rotate), primitives (Cube, Sphere, Cylinder), and modifiers (Merge, Subtract, Intersect).

Key structural elements include:
*   **Header:** Contains the logo, tool selection buttons, and an export button for STL files.
*   **Viewport:** Houses the `<canvas>` element where the 3D scene is rendered.
*   **Footer:** Displays selection status, a checkbox for toggling camera type (Orthographic/Perspective), and the application copyright notice.
*   **Script Inclusion:** Imports the main application logic from `main.js`.

### `style.css`

This file provides the visual styling for the EasyCAD interface. It defines the layout using CSS Flexbox, setting a full-screen, dark, and professional aesthetic.

Styling details include:
*   Global resets for colors and fonts.
*   Layout rules for `#main`, `#header`, `#viewport`, and `#footer`.
*   Specific styling for control buttons (`.tool`, `.primitive`, `.modifier`) to differentiate their functions.
*   Styles for the selection overlay elements (`.overlay`) used for property editing.

### `main.js`

This module contains the core application logic, utilizing Three.js for 3D rendering and interactive controls.

**Key Components and Functionality:**

*   **Setup:** Initializes the scene, renderer, and a post-processing `EffectComposer` pipeline, including `RenderPass`, `OutlinePass`, and `GammaCorrectionShader`.
*   **Camera Management:** Defines and manages two cameras: `orthoCamera` and `perspCamera`. It implements the `setCameraType` function to switch between them based on the UI toggle, ensuring the `OrbitControls` and renderer are updated accordingly.
*   **Resizing:** The `handleResize` function recalculates and updates camera aspect ratios and renderer/composer sizes when the window dimensions change.
*   **Orbit Controls:** Implements a custom `orbitControls` class allowing mouse interactions for orbiting, panning (middle-click), and zooming.
*   **Transform Controls:** Integrates `THREE.TransformControls` to allow manipulation of selected objects (Move, Scale, Rotate). Event listeners are set up to synchronize transform control settings (snaps) with the UI inputs.
*   **Primitives & Selection:**
    *   `createPrimitive`: Creates standard 3D meshes (Box, Sphere, Cylinder) and adds them to the scene and internal object registry.
    *   `selectObject`: Manages the active selection state, updating both the `OutlinePass` and the UI feedback.
*   **Interaction:** Implements `onMouseClick` and `raycast` to detect clicks on objects in the 3D scene when no tool is actively selected.
*   **Tool Functionality:** The `setTool` function manages the UI panel (`#editor-controls`) based on the selected tool (Move, Scale, Rotate). It populates controls with the selected object's current properties and attaches the `TransformControls` helper.
*   **Boolean Operations:** Functions like `booleanToSelection` and `booleanOperation` utilize `three-bvh-csg` to perform geometric set operations (Addition, Subtraction, Intersection) on two selected meshes, removing the originals and adding the result.
*   **Event Handling:** Global event listeners handle keyboard shortcuts (Escape, Delete, hotkeys for tools), window resizing, and UI form submissions to apply transformations or clear tool states.
*   **Export:** Attaches an event listener to the export button to serialize selected meshes into individual STL files.

### `vite.config.js`

This configuration file configures the Vite build tool.

*   It sets the `base` path for the application build to `/EasyCAD/`, ensuring correct asset resolution when deployed.