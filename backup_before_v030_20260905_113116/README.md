# Nightfall Village — Sandbox Systems Demo

An original Ren'Py/Python portfolio project built to demonstrate systems commonly used in non-linear sandbox visual novels.

## Why this demo exists

The goal is not to imitate another game's characters, art, dialogue, or story.  
The goal is to demonstrate that I can understand and implement the *technical structure* behind a sandbox visual novel:

- free location navigation;
- day / time progression;
- NPC schedules;
- relationship variables;
- route branching;
- stat-gated events;
- quest flags;
- inventory requirements;
- location unlocks;
- repeatable multi-stage interactions;
- spoiler-light objective tracking;
- save/load compatible state.

## Project structure

```text
game/
├── script.rpy      # Main navigation and repeatable location interactions
├── events.rpy      # Self-contained story event labels
├── systems.rpy     # State, event rules, schedules, requirements and helpers
├── screens.rpy     # Map, HUD, guide, inventory and relationship UI
├── options.rpy
└── gui.rpy
```

## Architectural idea

Story content is separated from gameplay rules.

`EVENT_DATA` in `systems.rpy` defines where and when an event can happen, its minimum day,
required quest state, relationship threshold, item requirement and priority.

`next_event_for(location_id)` evaluates those requirements and returns the highest-priority
eligible event. This avoids putting every condition directly inside the map screen.

This is deliberately small enough that I can explain and extend every part of it.

## Implemented examples

### Time-dependent NPC schedules
Aya and Ren appear in different locations depending on the current period.

### Relationship branches
Aya has two independent values:

- Bond
- Rivalry

At higher values, the dominant route changes dialogue and can later gate entire event chains.

### Quest-gated location
Completing Aya's first quest and raising Bond unlocks her household as a new map location.

### Multi-stage repeatable content
Returning to Aya's household changes the interaction stage instead of replaying exactly the same scene.

### Interactive guide
The guide generates spoiler-light objectives from the current save state.

## Next improvements

- visual illustrated map;
- proper character sprites;
- reusable quest/event classes;
- story log;
- developer debug screen;
- localization;
- automated event-condition tests;
- audio and transitions.
