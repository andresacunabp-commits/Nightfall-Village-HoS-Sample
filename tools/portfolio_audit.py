#!/usr/bin/env python3
"""Static presentation audit for Nightfall Village v0.15.0.

Uses only the Python standard library so it can run on GitHub Actions without
installing project dependencies.
"""

from __future__ import annotations

import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "0.15.0"
EXPECTED_SIZE = (1920, 1080)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def jpeg_size(path: Path) -> tuple[int, int]:
    sof = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}
    with path.open("rb") as f:
        if f.read(2) != b"\xff\xd8":
            raise ValueError("not a JPEG")
        while True:
            byte = f.read(1)
            if not byte:
                raise ValueError("SOF marker not found")
            if byte != b"\xff":
                continue
            while byte == b"\xff":
                byte = f.read(1)
            marker = byte[0]
            if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                continue
            raw_len = f.read(2)
            if len(raw_len) != 2:
                raise ValueError("truncated JPEG")
            seg_len = int.from_bytes(raw_len, "big")
            if marker in sof:
                precision = f.read(1)
                if not precision:
                    raise ValueError("truncated SOF")
                height = int.from_bytes(f.read(2), "big")
                width = int.from_bytes(f.read(2), "big")
                return width, height
            f.seek(seg_len - 2, 1)


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    errors: list[str] = []

    required_runtime = [
        "game/systems.rpy",
        "game/events.rpy",
        "game/script.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v130_interactive_world.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v132_hotspot_polish.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v140_master_art_pipeline.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v142_master_world_hotspots.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v145_direct_hover_navigation.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v147_map_png_mask_fix.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v147_restore_polished_hud.rpy",
        "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v148_hos_location_dock.rpy",
        "game/portfolio_candidate.rpy",
    ]
    for rel in required_runtime:
        if (ROOT / rel).is_file():
            ok(f"runtime file: {rel}")
        else:
            fail(f"missing runtime file: {rel}", errors)

    options = (ROOT / "game/options.rpy").read_text(encoding="utf-8")
    if f'define config.version = "{EXPECTED_VERSION}"' in options:
        ok(f"options version is {EXPECTED_VERSION}")
    else:
        fail(f"game/options.rpy does not define version {EXPECTED_VERSION}", errors)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if EXPECTED_VERSION in readme:
        ok("README candidate version")
    else:
        fail("README does not mention candidate version", errors)
    if "AI-assisted prototype art" in readme:
        ok("README asset disclosure")
    else:
        fail("README is missing AI-assisted art disclosure", errors)

    master_root = ROOT / "game/images/backgrounds/v140/master"
    required_masters = [
        *[f"home/{n}.jpg" for n in ("bedroom", "hallway", "kitchen", "living_room", "bathroom", "exterior")],
        *[f"aya_house/{n}.jpg" for n in ("exterior", "hallway", "living_room", "kitchen", "bathroom", "aya_room")],
        "village/village_square.jpg", "village/residential_street.jpg",
        "market/market_entrance.jpg", "market/market_street.jpg", "market/night_stall.jpg",
        "training/training_gate.jpg", "training/training_yard.jpg", "training/dojo_interior.jpg",
        "riverside/river_path.jpg", "riverside/old_bridge.jpg", "riverside/riverbank.jpg",
        "shrine/shrine_path.jpg", "shrine/old_shrine.jpg", "shrine/hidden_passage.jpg", "shrine/archive.jpg",
        "map/map_morning.jpg", "map/map_day.jpg", "map/map_evening.jpg", "map/map_night.jpg",
    ]

    for rel in required_masters:
        path = master_root / rel
        if not path.is_file():
            fail(f"missing master art: {rel}", errors)
            continue
        try:
            size = jpeg_size(path)
        except Exception as exc:
            fail(f"cannot read {rel}: {exc}", errors)
            continue
        if size == EXPECTED_SIZE:
            ok(f"master {rel}: {size[0]}x{size[1]}")
        else:
            fail(f"master {rel} is {size}, expected {EXPECTED_SIZE}", errors)

    mask = ROOT / "game/gui/map_circle_mask_116.png"
    try:
        size = png_size(mask)
        if size == (116, 116):
            ok("map alpha mask is exactly 116x116")
        else:
            fail(f"map alpha mask is {size}, expected (116, 116)", errors)
    except Exception as exc:
        fail(f"map alpha mask unreadable: {exc}", errors)

    all_rpy = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in (ROOT / "game").rglob("*.rpy"))
    if "use file_slots" in all_rpy:
        fail("regression string present: obsolete load-screen helper reference", errors)
    else:
        ok("regression absent: obsolete load-screen helper reference")

    # Check the actual presentation overlay definition, not harmless historical
    # comments/strings elsewhere in compatibility modules.
    stability = (ROOT / "game/zzzzzzz_v061_stability.rpy").read_text(encoding="utf-8")
    visible_footer_statement = 'text "F2 DEV • F3 PORTFOLIO"'
    if visible_footer_statement in stability:
        fail("visible developer footer is still rendered by the active stability overlay", errors)
    else:
        ok("visible developer footer removed from active stability overlay")

    final_map = (ROOT / "game/zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz_v147_map_png_mask_fix.rpy").read_text(encoding="utf-8")
    if "map_circle_mask_116.png" in final_map and "im.Scale(_thumb, 116, 116)" in final_map:
        ok("final map uses exact-size PNG mask")
    else:
        fail("final map mask implementation is not the expected exact-size PNG path", errors)

    print("\n" + ("Candidate audit PASSED." if not errors else f"Candidate audit FAILED with {len(errors)} issue(s)."))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
