# Nightfall Village — Scenario Art Pass v0.10.1

This pass replaces the flat prototype scenery with seven original cinematic location backgrounds generated specifically for the portfolio demo.

Integrated locations:
- Village Square
- Market Alley
- Training Ground
- Riverside
- Old Shrine / Shrine Path
- Aya Household exterior
- Aya Household interior hallway

## Git-friendly asset pipeline

The artwork is stored as validated base64 chunks in `game/assets/v10_parts/`. On first launch, `game/zzzzzzzzzzzzzz_v10_scenario_art.rpy` concatenates the required chunks, decodes the archive, checks its SHA-256 digest, validates the ZIP contents and extracts the seven images into `game/images/backgrounds/v10/`.

The generated background directory and runtime ZIP are intentionally ignored by Git. Existing story labels keep using names such as `bg_square` and `bg_market`; v0.10.1 overrides those image definitions after the assets pass validation.

## Test workflow

`git pull` → Launch Project → check the main-menu footer for `Scenario Art READY` → enter World Hub and visit locations.

If installation fails, press **F2**. Developer Tools displays the exact scenario-art diagnostic instead of silently falling back.
