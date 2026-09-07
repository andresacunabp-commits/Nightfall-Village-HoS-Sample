# Portfolio / Interview Notes — v0.15.0

These are concise talking points for explaining Nightfall Village in a developer conversation.

## 1. What did you build?

A Ren'Py/Python sandbox visual-novel sample with a persistent playthrough, free location movement, time periods, NPC schedules, conditional events, relationship routes, inventory/progression, room-by-room exploration, a dynamic map, custom save/load UI, and developer inspection tools.

## 2. How does the event system work?

Events are data-driven. Each event can define requirements such as location, time of day, minimum day, prior quest state, items, stats, relationship values, and priority. The resolver checks current save state and selects the highest-priority valid event.

This lets content scale without turning every location into one giant chain of nested `if` statements.

## 3. Why separate `events.rpy` and `systems.rpy`?

`events.rpy` is narrative content. `systems.rpy` is reusable game logic: requirements, schedules, relationships, inventory, progression helpers, and event resolution.

That separation makes it easier to add or debug content without rewriting the underlying rules.

## 4. How does navigation work now?

The player remains inside one persistent save and chooses where to move. Small areas use a contextual bottom dock with icon-based direct movement. Scene objects use invisible/low-noise hotspots: hover reveals the name and click performs the action directly. Larger travel uses a manual world map with circular location previews.

## 5. How do relationships work?

Relationship values are persistent save state and can affect dialogue, event eligibility, room access, and later branches. The current Aya route demonstrates Love / Hatred-style branching rather than a single linear affection score.

## 6. How do schedules and time work?

The day is divided into Morning / Day / Evening / Night. NPC location and event availability can depend on the current period. The village map also switches artwork with the period so the visual state matches the simulation state.

## 7. How do you debug blocked content?

The developer tools inspect current event requirements and show why content is ready or blocked. This is useful in a sandbox because an event can depend on several dimensions at once: day, period, relationship, quest state, items, stats, or previous events.

## 8. What was the hardest part?

Keeping many iterative UI/navigation layers compatible while changing the game from a portfolio hub into a persistent sandbox. The final candidate keeps the stable versioned modules that are still active, removes obsolete build tooling/stubs, and documents the active runtime layers in `ARCHITECTURE.md` instead of doing a risky last-minute rewrite before presentation.

## 9. What is original and what is AI-assisted?

The Ren'Py/Python implementation, state systems, event logic, UI integration, navigation behavior, debugging workflow, and project structure are the portfolio focus. Some environment and character presentation artwork is AI-assisted prototype art. The repository does not contain House of Shinobi proprietary source, characters, dialogue, story, or extracted assets.

## 10. What would you improve in a production codebase?

- migrate the remaining versioned compatibility modules into a smaller production package after a regression-test pass;
- add automated event-graph validation for impossible requirement combinations;
- add localization from the beginning of new content production;
- add more unit-like tests around pure Python rule helpers;
- introduce content-authoring validation and editor tooling as the event catalog grows.

## 11. What can you contribute first on a real project?

Event/dialogue scripting, implementing location interactions, conditional content, testing and reproducing bugs, UI integration, save-safe state changes, and developer tooling. The sample is intended to show that I can learn a real project's conventions and work incrementally without needing to own the entire architecture on day one.