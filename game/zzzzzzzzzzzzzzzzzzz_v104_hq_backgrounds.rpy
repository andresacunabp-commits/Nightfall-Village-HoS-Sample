# ============================================================
# NIGHTFALL VILLAGE v0.10.4 — EDSR DETAIL RESTORATION
# ============================================================
# Final scene-image authority. Uses EDSR x4 restored masters generated
# by GitHub Actions and committed under images/backgrounds/v104/.
# ============================================================

init 7000 python:

    NV104_BG_DIR = "images/backgrounds/v104/"
    NV104_FILES = {
        "home": "aya_house_hallway.jpg",
        "square": "village_square.jpg",
        "training": "training_ground.jpg",
        "market": "market_alley.jpg",
        "riverside": "riverside.jpg",
        "aya_house": "aya_house_hallway.jpg",
        "aya_house_ext": "aya_house_ext.jpg",
        "old_shrine": "shrine_path.jpg",
        "archive": "aya_house_hallway.jpg",
    }

    def nv104_bg(filename):
        return NV104_BG_DIR + filename

    def nv104_ready():
        required = (
            "village_square.jpg",
            "market_alley.jpg",
            "training_ground.jpg",
            "riverside.jpg",
            "shrine_path.jpg",
            "aya_house_ext.jpg",
            "aya_house_hallway.jpg",
        )
        try:
            return all(renpy.loadable(nv104_bg(filename)) for filename in required)
        except Exception:
            return False

    NV104_BACKGROUNDS_READY = nv104_ready()

    if NV104_BACKGROUNDS_READY:
        # These files are already 1280x720. Do not scale them again in Ren'Py.
        renpy.image("bg_home", nv104_bg(NV104_FILES["home"]))
        renpy.image("bg_square", nv104_bg(NV104_FILES["square"]))
        renpy.image("bg_training", nv104_bg(NV104_FILES["training"]))
        renpy.image("bg_market", nv104_bg(NV104_FILES["market"]))
        renpy.image("bg_riverside", nv104_bg(NV104_FILES["riverside"]))
        renpy.image("bg_aya_house", nv104_bg(NV104_FILES["aya_house"]))
        renpy.image("bg_aya_house_ext", nv104_bg(NV104_FILES["aya_house_ext"]))
        renpy.image("bg_old_shrine", nv104_bg(NV104_FILES["old_shrine"]))
        renpy.image("bg_archive", nv104_bg(NV104_FILES["archive"]))

        if "V09_LOCATION_VISUALS" in globals():
            V09_LOCATION_VISUALS["home"]["thumb"] = nv104_bg(NV104_FILES["home"])
            V09_LOCATION_VISUALS["square"]["thumb"] = nv104_bg(NV104_FILES["square"])
            V09_LOCATION_VISUALS["training"]["thumb"] = nv104_bg(NV104_FILES["training"])
            V09_LOCATION_VISUALS["market"]["thumb"] = nv104_bg(NV104_FILES["market"])
            V09_LOCATION_VISUALS["riverside"]["thumb"] = nv104_bg(NV104_FILES["riverside"])
            V09_LOCATION_VISUALS["aya_house"]["thumb"] = nv104_bg(NV104_FILES["aya_house_ext"])
            V09_LOCATION_VISUALS["old_shrine"]["thumb"] = nv104_bg(NV104_FILES["old_shrine"])
            V09_LOCATION_VISUALS["archive"]["thumb"] = nv104_bg(NV104_FILES["archive"])

        renpy.log("Nightfall v0.10.4: EDSR restored scenario art active.")
    else:
        renpy.log("Nightfall v0.10.4: restored art missing; v0.10.3 fallback active.")


# Disable the old v0.10.3 presentation overlay so it cannot show a stale
# version or cover the current main menu.
screen nv103_presentation_overlay():
    pass


screen nv10_art_status():
    zorder 7400

    if renpy.get_screen("developer_tools") is not None:
        frame:
            xpos 835
            ypos 626
            xsize 420
            background Solid("#02080df4")
            padding (12, 8)

            vbox:
                spacing 3
                hbox:
                    spacing 8
                    text "●" size 16 color ("#55e49a" if NV104_BACKGROUNDS_READY else "#ff6c7d")
                    text ("EDSR SCENARIO ART READY • v[config.version]" if NV104_BACKGROUNDS_READY else "EDSR SCENARIO ART MISSING") size 12 bold True color "#dce9ed"
                text "1280×720 • EDSR x4 • JPEG 98 • edge/detail restoration" size 9 color "#76909a"


screen nv104_presentation_overlay():
    zorder 7350

    if renpy.get_screen("world_map") is not None:
        frame:
            xpos 875
            ypos 665
            xsize 385
            background Solid("#02070af4")
            padding (12, 5)
            text "v[config.version] • EDSR restored world art • native 1280×720" size 10 color "#8eb8c6"


init 7500 python:
    if "nv104_presentation_overlay" not in config.overlay_screens:
        config.overlay_screens.append("nv104_presentation_overlay")
