NIGHTFALL VILLAGE — v0.14 MASTER ART STANDARD

Goal
----
Replace the provisional v131 atlas-derived images with true independent
high-resolution scene masters.

Master resolution
-----------------
1920x1080 (16:9), full-frame environment art.
Runtime rendering remains 1280x720, so Ren'Py downsamples the master and
keeps much more detail than enlarging a small crop.

Rules
-----
- One scene per image.
- No baked UI, labels, logos, dialogue or hotspot text.
- No characters permanently baked into backgrounds.
- Doors, roads, furniture and interactable objects must be visually clear.
- Keep free negative space for NPC sprites and dialogue UI.
- Preserve a consistent Nightfall Village visual language across scenes.

Folder layout
-------------
master/home/
  bedroom.jpg
  hallway.jpg
  kitchen.jpg
  living_room.jpg
  bathroom.jpg
  exterior.jpg

master/village/
  residential_street.jpg
  village_square.jpg

master/market/
  market_entrance.jpg
  market_street.jpg
  night_stall.jpg

master/training/
  training_gate.jpg
  training_yard.jpg
  dojo_interior.jpg

master/riverside/
  river_path.jpg
  old_bridge.jpg
  riverbank.jpg

master/aya_house/
  exterior.jpg
  hallway.jpg
  living_room.jpg
  kitchen.jpg
  bathroom.jpg
  aya_room.jpg

master/shrine/
  shrine_path.jpg
  old_shrine.jpg
  hidden_passage.jpg
  archive.jpg

master/map/
  map_morning.jpg
  map_day.jpg
  map_evening.jpg
  map_night.jpg

Priority order
--------------
1. Protagonist home
2. Aya house
3. Village Square / residential street
4. Four map states
5. Market
6. Training
7. Riverside
8. Shrine / Archive

The v140 Ren'Py pipeline automatically uses a master whenever its exact
file exists. If it does not exist yet, v131 remains the fallback.
