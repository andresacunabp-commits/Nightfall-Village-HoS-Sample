# v0.15.0 Portfolio Candidate — Manual QA Checklist

The repository audit and CI build catch structural/compile problems. This checklist is the final human gameplay pass before sharing the link.

## Clean start

- [ ] `git pull` completes cleanly.
- [ ] Delete `.rpyc` and `game/cache`, then launch with Ren'Py 8.3.7.
- [ ] No traceback or parse error before the main menu.
- [ ] Main menu background is clean; no baked dialogue or duplicated UI.
- [ ] Menu contains only the intended presentation options.

## New game / persistent sandbox

- [ ] COMENZAR starts a normal persistent playthrough.
- [ ] The game does not throw the player into a portfolio/world-hub selector.
- [ ] The player can remain in a location and decide what to do next.

## Top HUD

- [ ] Only the polished icon HUD is visible; no text-only HUD is superimposed.
- [ ] MAP opens the current dynamic circular map.
- [ ] PEOPLE / ITEMS / EVENTS / GUIDE open their intended screens.
- [ ] No visible `F2 DEV • F3 PORTFOLIO` footer is present in normal gameplay.

## Contextual bottom dock

- [ ] Home shows room icons for Bedroom / Bathroom / Living / Kitchen / Hallway / Exterior.
- [ ] Aya House shows the correct equivalent room icons.
- [ ] Village / Market / Training / Riverside / Shrine / Archive show contextual sublocation icons.
- [ ] Hover shows the location name without permanent text clutter.
- [ ] Click moves directly without asking for confirmation.
- [ ] Current location is visually distinct.
- [ ] Green availability dots appear only where a character/event is actually available.
- [ ] Locked locations remain visibly disabled and cannot be entered.

## Scene hotspots

- [ ] Hotspots do not display permanent labels.
- [ ] Hover illumination aligns with the actual object/door/path.
- [ ] Hover name appears cleanly.
- [ ] Click performs the action/movement directly.
- [ ] No dead clickable areas cover unrelated artwork.

## World map

- [ ] Morning uses the morning master image.
- [ ] Day uses the day master image.
- [ ] Evening uses the evening master image.
- [ ] Night uses the night master image.
- [ ] Every destination is circular.
- [ ] Every unlocked destination shows a real location preview image.
- [ ] No `AlphaMask surfaces must be the same size` text appears.
- [ ] Hover shows only the destination name.
- [ ] Click travels directly.
- [ ] Locked destinations cannot be entered.

## Location route

- [ ] Home → Village Square.
- [ ] Village Square → Market.
- [ ] Market → Training.
- [ ] Training → Riverside.
- [ ] Riverside → Aya House.
- [ ] Aya House → Shrine when unlocked.
- [ ] Shrine → Hidden Passage / Archive when unlocked.
- [ ] No transition unexpectedly opens the map automatically.

## Systems

- [ ] Energy changes when intended and never displays invalid values.
- [ ] Time advances when intended.
- [ ] NPC schedule changes are reflected after time changes.
- [ ] Relationship choices persist.
- [ ] Inventory changes persist.
- [ ] Unlock flags persist.

## Save/load

- [ ] Manual save works.
- [ ] Load screen displays six slots cleanly.
- [ ] Saved screenshot/name/time render correctly.
- [ ] Loading restores room, day/period, stats, relationships, inventory, and flags.
- [ ] Quick Save works.
- [ ] Closing and reopening the game still loads the same save.

## Presentation finish

- [ ] No debug text, placeholder labels, test rectangles, or visual warnings appear.
- [ ] No obviously blurry legacy background appears during the five-minute reviewer route.
- [ ] Main menu, map, Home, Aya House, Market, and one story event are screenshot-ready.
- [ ] Windows candidate build opens on a machine/session without the Ren'Py launcher.

When all items above pass, the candidate is ready to send.