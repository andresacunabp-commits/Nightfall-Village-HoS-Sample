# Portfolio / Interview Notes

These notes are for explaining the project in a developer conversation.

## 1. How does the event system work?

Events are data-driven. Each event has rules such as location, time of day,
minimum day, required quest state, items, stats, relationship values and priority.

When the player enters a location, `next_event_for()` checks the rules and chooses
the highest-priority event that is currently valid.

## 2. Why separate `events.rpy` and `systems.rpy`?

`events.rpy` contains narrative content.
`systems.rpy` contains reusable gameplay rules.

This makes it easier to add new scenes without turning one file into a huge chain of conditions.

## 3. How do branching relationships work?

Each character can hold more than one relationship dimension.
Aya currently has `bond` and `rivalry`.

Choices modify these values independently. `dominant_route()` turns those values
into a higher-level route that other events can check.

## 4. How does the guide avoid spoilers?

It does not contain full walkthrough text.
It inspects current quest states and flags, then gives the next broad objective.

## 5. Why use dictionaries for this demo?

They are easy to inspect, save, debug, and explain while learning Ren'Py.
If the project became much larger, the next refactor would introduce reusable
data classes / managers and validation tools for event definitions.

## 6. What would I work on next?

- debug tools for changing day, stats and flags;
- event dependency visualizer;
- automated checks for impossible event requirements;
- reusable quest journal;
- localization;
- cleaner UI and assets.
