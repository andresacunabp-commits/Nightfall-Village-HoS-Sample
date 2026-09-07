# Nightfall Village — Directly Relevant Sandbox VN Sample

Nightfall Village was built specifically as a portfolio sample for work on a large nonlinear shinobi sandbox visual novel.

It does **not** reuse House of Shinobi source code, proprietary art, characters, dialogue, story content, logos, or extracted assets. Instead, it demonstrates development categories that are directly relevant to that kind of project:

- Ren'Py + Python scripting;
- persistent sandbox playthroughs;
- free location navigation;
- room-by-room household movement;
- hover/click interactive hotspots;
- image-based world travel;
- Morning / Day / Evening / Night state;
- NPC schedules;
- Love / Hatred relationship routes;
- stat-, item-, relationship-, quest-, and time-gated events;
- event priority and prerequisite chains;
- unlockable locations;
- repeatable multi-stage interactions;
- save/load presentation and save-safe defaults;
- event discovery / replay / guide UI;
- developer event inspection and fast condition testing.

## Current UX sample

The current candidate uses a polished icon HUD, a contextual bottom navigation dock, direct hover interactions, and a manually opened dynamic world map with circular destination previews. These are implemented as original Ren'Py screens and Python helpers using original project data.

## Portfolio talking point

> I built this sample around the workflow problems of a large Ren'Py sandbox VN: persistent state, schedules, conditional event gating, relationship branches, location navigation, debugging blocked content, and iterating UI without breaking saves. I kept the implementation and narrative content original while making the interaction flow directly relevant to the type of project I want to contribute to.

## Useful files to discuss

- `game/systems.rpy` — reusable rules and persistent systems.
- `game/events.rpy` — narrative/event content.
- `game/script.rpy` — main sandbox/action flow.
- `game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v130_interactive_world.rpy` — scene model and exploration.
- `game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v145_direct_hover_navigation.rpy` — direct interaction UX.
- `game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v147_map_png_mask_fix.rpy` — dynamic circular map.
- `game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v147_restore_polished_hud.rpy` — polished HUD.
- `game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v148_hos_location_dock.rpy` — contextual location dock.

## Asset disclosure

Some environment and character presentation artwork is AI-assisted prototype art. The sample is presented primarily as a programming, systems, UX-integration, and debugging portfolio piece.