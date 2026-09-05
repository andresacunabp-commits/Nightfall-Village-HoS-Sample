# ============================================================
# NIGHTFALL VILLAGE v0.10.3 — HQ BACKGROUND UPGRADE
# ============================================================
# Generated 1280x720 background masters are committed directly to GitHub.
# This layer has the final init priority and replaces every lower-quality
# v0.10/v0.10.2 scene definition without changing story/event labels.
# ============================================================

init 6000 python:

    NV103_BG_DIR = "images/backgrounds/v103/"
    NV103_FILES = {
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

    def nv103_bg(filename):
        return NV103_BG_DIR + filename

    def nv103_ready():
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
            return all(renpy.loadable(nv103_bg(filename)) for filename in required)
        except Exception:
            return False

    NV103_BACKGROUNDS_READY = nv103_ready()

    if NV103_BACKGROUNDS_READY:
        # Native 1280x720 masters. They are no longer enlarged from the tiny
        # runtime v0.10 JPEG package, which caused the visible blur.
        renpy.image("bg_home", nv103_bg(NV103_FILES["home"]))
        renpy.image("bg_square", nv103_bg(NV103_FILES["square"]))
        renpy.image("bg_training", nv103_bg(NV103_FILES["training"]))
        renpy.image("bg_market", nv103_bg(NV103_FILES["market"]))
        renpy.image("bg_riverside", nv103_bg(NV103_FILES["riverside"]))
        renpy.image("bg_aya_house", nv103_bg(NV103_FILES["aya_house"]))
        renpy.image("bg_aya_house_ext", nv103_bg(NV103_FILES["aya_house_ext"]))
        renpy.image("bg_old_shrine", nv103_bg(NV103_FILES["old_shrine"]))
        renpy.image("bg_archive", nv103_bg(NV103_FILES["archive"]))

        # World Hub cards now use the same HQ masters as gameplay scenes.
        if "V09_LOCATION_VISUALS" in globals():
            V09_LOCATION_VISUALS["home"]["thumb"] = nv103_bg(NV103_FILES["home"])
            V09_LOCATION_VISUALS["square"]["thumb"] = nv103_bg(NV103_FILES["square"])
            V09_LOCATION_VISUALS["training"]["thumb"] = nv103_bg(NV103_FILES["training"])
            V09_LOCATION_VISUALS["market"]["thumb"] = nv103_bg(NV103_FILES["market"])
            V09_LOCATION_VISUALS["riverside"]["thumb"] = nv103_bg(NV103_FILES["riverside"])
            V09_LOCATION_VISUALS["aya_house"]["thumb"] = nv103_bg(NV103_FILES["aya_house_ext"])
            V09_LOCATION_VISUALS["old_shrine"]["thumb"] = nv103_bg(NV103_FILES["old_shrine"])
            V09_LOCATION_VISUALS["archive"]["thumb"] = nv103_bg(NV103_FILES["archive"])

        renpy.log("Nightfall v0.10.3: HQ 1280x720 scenario art active.")
    else:
        renpy.log("Nightfall v0.10.3: HQ scenario art missing; v0.10 fallback remains active.")


# ------------------------------------------------------------
# Replace the old v0.10.1 diagnostic with the current HQ status.
# ------------------------------------------------------------

screen nv10_art_status():
    zorder 6400

    if renpy.get_screen("developer_tools") is not None:
        frame:
            xpos 850
            ypos 628
            xsize 400
            background Solid("#02080df4")
            padding (12, 8)

            vbox:
                spacing 3
                hbox:
                    spacing 8
                    text "●" size 16 color ("#55e49a" if NV103_BACKGROUNDS_READY else "#ff6c7d")
                    text ("HQ SCENARIO ART READY • v0.10.3" if NV103_BACKGROUNDS_READY else "HQ SCENARIO ART MISSING") size 12 bold True color "#dce9ed"
                text "1280×720 • FSRCNN reconstruction • high-quality JPEG masters" size 9 color "#76909a"


# ------------------------------------------------------------
# Presentation overlay: covers the old v0.10.2 menu labels without
# duplicating or replacing navigation logic that already works.
# ------------------------------------------------------------

screen nv103_presentation_overlay():
    zorder 6300

    if renpy.get_screen("main_menu") is not None:

        # Left version footer.
        frame:
            xpos 8
            ypos 628
            xsize 315
            ysize 70
            background Solid("#02080dfd")
            padding (14, 8)

            vbox:
                spacing 3
                text "v0.10.3 • HQ Background Upgrade" size 12 bold True color "#9edfec"
                text "Native 1280×720 • sharper scene masters" size 10 color "#607d88"

        # Current feature card.
        frame:
            xpos 810
            ypos 120
            xsize 425
            ysize 475
            background Solid("#02080cf8")
            padding (26, 22)

            vbox:
                spacing 10
                text "NEW IN v0.10.3" size 12 bold True color "#e4bd68"
                text "HQ Background Upgrade" size 29 bold True color "#ffffff"
                text "The seven gameplay locations now use native-resolution masters instead of stretching the compact fallback art." size 15 color "#bdcbd1" line_spacing 3

                null height 2
                text "◆ 1280×720 gameplay backgrounds" size 14 color "#dbeaf0"
                text "◆ Super-resolution reconstruction" size 14 color "#dbeaf0"
                text "◆ High-quality JPEG export" size 14 color "#dbeaf0"
                text "◆ Detail + local-contrast recovery" size 14 color "#dbeaf0"
                text "◆ HQ thumbnails in World Hub" size 14 color "#dbeaf0"
                text "◆ No prototype geometry overlays" size 14 color "#dbeaf0"

                null height 8
                textbutton "ENTER WORLD HUB  →" action Start() style "v09_small_button"
                textbutton "HOUSEHOLD DEMO" action Start("v07_house_demo_start") style "v09_small_button"

        # Bottom-right build footer.
        frame:
            xpos 755
            ypos 606
            xsize 505
            background Solid("#020609f8")
            padding (16, 8)
            text "Nightfall Village • Ren'Py + Python • Portfolio Build 0.10.3" size 12 color "#8aa6b1"

    if renpy.get_screen("world_map") is not None:
        frame:
            xpos 905
            ypos 665
            xsize 355
            background Solid("#02070af4")
            padding (12, 5)
            text "v0.10.3 • HQ world art • native scene resolution" size 10 color "#7fa4b1"


init 6500 python:
    if "nv103_presentation_overlay" not in config.overlay_screens:
        config.overlay_screens.append("nv103_presentation_overlay")
