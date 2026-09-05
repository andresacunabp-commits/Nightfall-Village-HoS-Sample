# ============================================================
# NIGHTFALL VILLAGE v0.10 — SCENARIO ART PASS
# ============================================================
# Integrates seven cinematic location backgrounds directly into
# the Ren'Py project. Artwork ships inside the repository and is
# extracted automatically on first launch after git pull.
# ============================================================

init -1000 python:
    import os
    import zipfile

    NV10_BG_VERSION = "0.10.0"
    NV10_BG_FILES = (
        "village_square.jpg",
        "market_alley.jpg",
        "training_ground.jpg",
        "riverside.jpg",
        "shrine_path.jpg",
        "aya_house_ext.jpg",
        "aya_house_hallway.jpg",
    )

    def nv10_install_backgrounds():
        source_zip = os.path.join(config.gamedir, "assets", "nightfall_v10_backgrounds.zip")
        target_dir = os.path.join(config.gamedir, "images", "backgrounds", "v10")
        stamp = os.path.join(target_dir, ".installed_" + NV10_BG_VERSION)

        if not os.path.exists(source_zip):
            return False

        complete = os.path.exists(stamp)
        if complete:
            for filename in NV10_BG_FILES:
                if not os.path.exists(os.path.join(target_dir, filename)):
                    complete = False
                    break

        if complete:
            return True

        try:
            if not os.path.isdir(target_dir):
                os.makedirs(target_dir)

            with zipfile.ZipFile(source_zip, "r") as archive:
                archive.extractall(target_dir)

            with open(stamp, "w") as stamp_file:
                stamp_file.write(NV10_BG_VERSION)

            return True
        except Exception as exc:
            renpy.log("Nightfall v0.10 background install failed: {}".format(exc))
            return False

    NV10_BACKGROUNDS_READY = nv10_install_backgrounds()


init 2000 python:
    if NV10_BACKGROUNDS_READY:
        # Replace old prototype scenery while keeping existing story labels.
        renpy.image("bg_square", im.Scale("images/backgrounds/v10/village_square.jpg", 1280, 720))
        renpy.image("bg_market", im.Scale("images/backgrounds/v10/market_alley.jpg", 1280, 720))
        renpy.image("bg_training", im.Scale("images/backgrounds/v10/training_ground.jpg", 1280, 720))
        renpy.image("bg_riverside", im.Scale("images/backgrounds/v10/riverside.jpg", 1280, 720))
        renpy.image("bg_old_shrine", im.Scale("images/backgrounds/v10/shrine_path.jpg", 1280, 720))

        # Household gameplay happens inside the residence.
        renpy.image("bg_aya_house", im.Scale("images/backgrounds/v10/aya_house_hallway.jpg", 1280, 720))
        renpy.image("bg_aya_house_ext", im.Scale("images/backgrounds/v10/aya_house_ext.jpg", 1280, 720))

        # Temporary safehouse art until a dedicated player-home scene is added.
        renpy.image("bg_home", im.Scale("images/backgrounds/v10/aya_house_hallway.jpg", 1280, 720))

        # Upgrade v0.9 destination cards to matching cinematic artwork.
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
            xpos 930
            ypos 648
            xsize 320
            background Solid("#02080def")
            padding (12, 8)

            hbox:
                spacing 8
                text "●" size 16 color ("#55e49a" if NV10_BACKGROUNDS_READY else "#ff6c7d")
                text ("SCENARIO ART READY • v0.10" if NV10_BACKGROUNDS_READY else "SCENARIO ART MISSING") size 12 bold True color "#dce9ed"


init 2100 python:
    if "nv10_art_status" not in config.overlay_screens:
        config.overlay_screens.append("nv10_art_status")
