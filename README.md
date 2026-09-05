# Nightfall Village — Shinobi Sandbox Portfolio Demo v0.10.2

Original Ren'Py/Python portfolio project designed to demonstrate the systems and development workflow needed by a large nonlinear shinobi sandbox visual novel.

## Current vertical slices

### v0.7 — Aya Household
- Room-by-room navigation
- Character availability markers
- Multi-stage event chain
- Persistent Love / Hatred choices
- Route-reactive dialogue
- Relationship-gated rooms and follow-up scenes

### v0.8 — Mission Control
- Conditional mission board with live lock reasons
- Morning / Afternoon / Evening / Night mission gates
- NPC schedule table
- Strength and Reputation requirements
- Love / Hatred mission requirements
- Prerequisite mission chains
- Persistent completion state and rewards
- Route-aware mission scenes
- Live progression controls for testing conditions

### v0.9 — Visual World Overhaul
- Cinematic world hub instead of a flat prototype map
- Destination cards with live event / character / lock status
- Current objective surfaced directly in navigation
- Per-location accent identity and scene chrome
- Animated ambient particles on outdoor scenes

### v0.10.1 — Scenario Art Pass
- Seven original cinematic backgrounds integrated into the sandbox
- Dedicated art for Village Square, Market Alley, Training Ground, Riverside and Shrine Path
- Aya Household exterior and interior hallway artwork
- Scenario-art integrity validation and automatic installation

### v0.10.2 — Cinematic Cleanup
- Prototype geometric scenery is no longer composited over the finished backgrounds
- Gameplay scenes now force a single clean cinematic background layer
- World Hub cards are image-led and use matching destination art
- Scene chrome was reduced to compact location/objective panels
- The gameplay HUD no longer duplicates the World Hub header
- Existing schedules, events, routes, inventory and save state remain unchanged

## Core sandbox systems

- Original cinematic main menu and visual identity
- Bottom-anchored dialogue UI
- Cinematic world hub
- Morning / Afternoon / Evening / Night cycle
- NPC schedules
- Love / Hatred relationship routes
- Strength and Reputation progression
- Inventory and shop systems
- Night-only merchant
- Quest flags and event priorities
- Unlockable households and secret locations
- Multi-stage repeatable interactions
- Living-world dialogue reactions
- Interactive spoiler-light guide
- Event discovery log
- Custom save/load/settings UI
- Developer progression controls
- Live Event Inspector that explains why events are blocked

## Portfolio positioning

This project does **not** copy House of Shinobi characters, art, dialogue, CGs, story, or source code. It is an original sample created specifically to demonstrate relevant technical categories: sandbox navigation, schedules, time-sensitive events, relationship routes, progression gates, mission dependencies, persistent state, UI work, visual integration, and developer tooling.

## Recommended portfolio demos

Start with **World Hub** to see the visual sandbox navigation and live location state. Visit several districts to see the dedicated scenario art, then launch **Household Demo** for room-based relationship events and **Mission Control** for mission dependencies and schedule-driven gameplay.

## Developer shortcuts

- **F2** — Developer Tools / Event Inspector / scenario-art diagnostic
- **F3** — Portfolio Brief

The Event Inspector evaluates the current save and shows whether events are READY or BLOCKED, including the unmet requirement.
