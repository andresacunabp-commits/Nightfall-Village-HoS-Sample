# ============================================================
# NIGHTFALL VILLAGE v0.10.1 — SCENARIO ART PASS
# ============================================================
# The cinematic backgrounds are stored as Git-safe base64 chunks.
# On first launch Ren'Py rebuilds a validated ZIP, extracts the art,
# and transparently overrides the old prototype scene images.
# ============================================================

init -1000 python:
    import os
    import base64
    import hashlib
    import zipfile

    NV10_BG_VERSION = "0.10.1"
    NV10_ARCHIVE_SHA256 = "b8b1fbcee3e4bf26a8e7ec78feb9bdf52e70b6e50ef839eb82bc398ff816b147"

    NV10_BG_FILES = (
        "village_square.jpg",
        "market_alley.jpg",
        "training_ground.jpg",
        "riverside.jpg",
        "shrine_path.jpg",
        "aya_house_ext.jpg",
        "aya_house_hallway.jpg",
    )

    # Only these validated pieces are used. Older experimental parts remain
    # harmless and are deliberately ignored.
    NV10_PART_FILES = (
        "part00.txt",
        "part01.txt",
        "part02.txt",
        "part03a.txt",
        "part03b.txt",
        "part04a.txt",
        "part04b1.txt",
        "part04b2.txt",
        "part05a.txt",
        "part05b.txt",
        "part06a.txt",
        "part06b.txt",
        "part07a.txt",
        "part07b.txt",
    )

    NV10_ART_ERROR = ""

    def nv10_build_archive():
        global NV10_ART_ERROR

        parts_dir = os.path.join(config.gamedir, "assets", "v10_parts")
        runtime_zip = os.path.join(config.gamedir, "cache", "nightfall_v10_runtime.zip")

        try:
            encoded_parts = []

            for filename in NV10_PART_FILES:
                path = os.path.join(parts_dir, filename)
                if not os.path.exists(path):
                    NV10_ART_ERROR = "Missing art chunk: {}".format(filename)
                    renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                    return None

                with open(path, "r") as part_file:
                    encoded_parts.append(part_file.read().strip())

            encoded = "".join(encoded_parts)
            raw = base64.b64decode(encoded)

            if raw[:4] != b"PK\x03\x04":
                NV10_ART_ERROR = "Scenario art archive header is invalid."
                renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                return None

            digest = hashlib.sha256(raw).hexdigest()
            if digest != NV10_ARCHIVE_SHA256:
                NV10_ART_ERROR = "Scenario art checksum mismatch: {}".format(digest)
                renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                return None

            cache_dir = os.path.dirname(runtime_zip)
            if not os.path.isdir(cache_dir):
                os.makedirs(cache_dir)

            with open(runtime_zip, "wb") as archive_file:
                archive_file.write(raw)

            if not zipfile.is_zipfile(runtime_zip):
                NV10_ART_ERROR = "Rebuilt scenario art package is not a ZIP."
                renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                return None

            return runtime_zip

        except Exception as exc:
            NV10_ART_ERROR = "Could not rebuild scenario art: {}".format(exc)
            renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
            return None

    def nv10_install_backgrounds():
        global NV10_ART_ERROR

        target_dir = os.path.join(config.gamedir, "images", "backgrounds", "v10")
        stamp = os.path.join(target_dir, ".installed_" + NV10_BG_VERSION)

        complete = os.path.exists(stamp)
        if complete:
            for filename in NV10_BG_FILES:
                if not os.path.exists(os.path.join(target_dir, filename)):
                    complete = False
                    break

        if complete:
            return True

        runtime_zip = nv10_build_archive()
        if not runtime_zip:
            return False

        try:
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)

            with zipfile.ZipFile(runtime_zip, "r") as archive:
                corrupt_file = archive.testzip()
                if corrupt_file is not None:
                    NV10_ART_ERROR = "Corrupt file in scenario art package: {}".format(corrupt_file)
                    renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                    return False

                archive_names = set(archive.namelist())
                for filename in NV10_BG_FILES:
                    if filename not in archive_names:
                        NV10_ART_ERROR = "Scenario art package is missing {}".format(filename)
                        renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                        return False

                archive.extractall(target_dir)

            for filename in NV10_BG_FILES:
                if not os.path.exists(os.path.join(target_dir, filename)):
                    NV10_ART_ERROR = "Extracted background missing: {}".format(filename)
                    renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
                    return False

            with open(stamp, "w") as stamp_file:
                stamp_file.write(NV10_BG_VERSION)

            NV10_ART_ERROR = ""
            renpy.log("Nightfall v0.10.1: cinematic scenario art installed successfully.")
            return True

        except Exception as exc:
            NV10_ART_ERROR = "Background extraction failed: {}".format(exc)
            renpy.log("Nightfall v0.10: " + NV10_ART_ERROR)
            return False

    NV10_BACKGROUNDS_READY = nv10_install_backgrounds()


init 2000 python:
    if NV10_BACKGROUNDS_READY:
        # Replace old flat prototype scenery while keeping all story labels.
        renpy.image("bg_square", im.Scale("images/backgrounds/v10/village_square.jpg", 1280, 720))
        renpy.image("bg_market", im.Scale("images/backgrounds/v10/market_alley.jpg", 1280, 720))
        renpy.image("bg_training", im.Scale("images/backgrounds/v10/training_ground.jpg", 1280, 720))
        renpy.image("bg_riverside", im.Scale("images/backgrounds/v10/riverside.jpg", 1280, 720))
        renpy.image("bg_old_shrine", im.Scale("images/backgrounds/v10/shrine_path.jpg", 1280, 720))

        # Household gameplay happens inside the residence.
        renpy.image("bg_aya_house", im.Scale("images/backgrounds/v10/aya_house_hallway.jpg", 1280, 720))
        renpy.image("bg_aya_house_ext", im.Scale("images/backgrounds/v10/aya_house_ext.jpg", 1280, 720))

        # Temporary safehouse art until a dedicated player-home background is added.
        renpy.image("bg_home", im.Scale("images/backgrounds/v10/aya_house_hallway.jpg", 1280, 720))

        # World-hub cards use the same cinematic artwork as their destinations.
        if "V09_LOCATION_VISUALS" in globals():
            V09_LOCATION_VISUALS["home"]["thumb"] = "images/backgrounds/v10/aya_house_hallway.jpg"
            V09_LOCATION_VISUALS["square"]["thumb"] = "images/backgrounds/v10/village_square.jpg"
            V09_LOCATION_VISUALS["training"]["thumb"] = "images/backgrounds/v10/training_ground.jpg"
            V09_LOCATION_VISUALS["market"]["thumb"] = "images/backgrounds/v10/market_alley.jpg"
            V09_LOCATION_VISUALS["riverside"]["thumb"] = "images/backgrounds/v10/riverside.jpg"
            V09_LOCATION_VISUALS["aya_house"]["thumb"] = "images/backgrounds/v10/aya_house_ext.jpg"
            V09_LOCATION_VISUALS["old_shrine"]["thumb"] = "images/backgrounds/v10/shrine_path.jpg"


screen nv10_art_status():
    zorder 1400

    if renpy.get_screen("developer_tools") is not None:
        frame:
            xpos 880
            ypos 636
            xsize 370
            background Solid("#02080def")
            padding (12, 8)

            vbox:
                spacing 2

                hbox:
                    spacing 8
                    text "●" size 16 color ("#55e49a" if NV10_BACKGROUNDS_READY else "#ff6c7d")
                    text ("SCENARIO ART READY • v0.10.1" if NV10_BACKGROUNDS_READY else "SCENARIO ART ERROR") size 12 bold True color "#dce9ed"

                if (not NV10_BACKGROUNDS_READY) and NV10_ART_ERROR:
                    text NV10_ART_ERROR size 9 color "#ff9aa6" xmaximum 340


init 2100 python:
    if "nv10_art_status" not in config.overlay_screens:
        config.overlay_screens.append("nv10_art_status")
