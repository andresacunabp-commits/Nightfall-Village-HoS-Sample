# Candidate Architecture — v0.15.0

Nightfall Village evolved through multiple vertical slices. The v0.15.0 candidate intentionally keeps a small number of versioned compatibility modules that are already stable rather than performing a risky last-minute merge before presentation.

Obsolete CI workflows, empty placeholders, and stale version-marker files were removed for the candidate. The active layers below are the ones a reviewer should focus on.

## Core gameplay

### `game/systems.rpy`
Reusable state and rules: time, NPC schedules, relationships, inventory, progression helpers, event eligibility, and save-safe defaults.

### `game/events.rpy`
Narrative event definitions and branching content.

### `game/script.rpy`
Primary labels, action routing, and the persistent sandbox playthrough flow.

## Current exploration stack

### `..._v130_interactive_world.rpy`
Defines the scene/zone model and the interactive exploration screen used throughout the current world.

### `..._v131_visual_assets.rpy`
Routes scene IDs to the multi-room visual set and fallback assets.

### `..._v140_master_art_pipeline.rpy`
Selects the final v0.14 1920×1080 master environment artwork when present, with safe fallback behavior.

### `..._v140_home_master_hotspots.rpy` and `..._v142_master_world_hotspots.rpy`
Align interaction regions to the final master artwork.

### `..._v145_direct_hover_navigation.rpy`
Implements the current low-noise interaction rule: no permanent hotspot labels, hover reveals the target name, click immediately moves or interacts.

### `..._v147_map_png_mask_fix.rpy`
Final world map screen: Morning/Day/Evening/Night artwork, circular real-image location nodes, exact PNG mask sizing, hover names, and direct travel.

### `..._v147_restore_polished_hud.rpy`
Keeps the polished icon-based top HUD as the only gameplay HUD and routes MAP to the current map implementation.

### `..._v148_hos_location_dock.rpy`
Contextual bottom location dock with line icons, hover-only labels, direct movement, current-location state, and green availability markers.

## Presentation/menu stack

The current main menu, load screen, and unified menu family are late overrides built on the same save data and are intentionally separated from core gameplay rules.

## Why the filenames are versioned

The project was built incrementally while being continuously playable. Versioned modules made it possible to add a presentation pass or navigation behavior without rewriting stable event/state code and breaking save compatibility.

For a production handoff, the next refactor would consolidate the active layers into semantic modules such as `navigation.rpy`, `world_map.rpy`, `hud.rpy`, and `scene_interactions.rpy` **after** a regression-test baseline is established. For this portfolio candidate, preserving proven runtime behavior is more valuable than a cosmetic file rename.

## Automated candidate checks

`tools/portfolio_audit.py` verifies the candidate version, required final runtime modules, v0.14 master-art inventory and dimensions, the exact circular map mask size, documentation disclosure, and known regression strings.

`.github/workflows/portfolio-candidate.yml` runs the audit and can build a Windows distribution with Ren'Py 8.3.7.