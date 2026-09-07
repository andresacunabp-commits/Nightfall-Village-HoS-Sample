# ============================================================
# NIGHTFALL VILLAGE v0.14.5 — RESTORE POLISHED ICON HUD
# ============================================================
# Keep the older icon-based HUD as the only in-game top bar.
# The newer text-only `hud` overlay is removed.
# MAP now opens the latest circular-image world map directly.
# ============================================================

init 25000 python:
    # Remove the later text-only overlay that was being drawn on top.
    while "hud" in config.overlay_screens:
        config.overlay_screens.remove("hud")

    # Keep exactly one copy of the polished v0.6 icon HUD.
    while "v06_hud" in config.overlay_screens:
        config.overlay_screens.remove("v06_hud")
    config.overlay_screens.append("v06_hud")

    # Final version authority for this presentation pass.
    config.version = "0.14.5"


# Late override of the polished HUD so its MAP icon opens the current
# dynamic map instead of jumping to the obsolete legacy `map` label.
screen v06_hud():
    zorder 120

    if (
        renpy.get_screen("main_menu") is None and
        renpy.get_screen("developer_tools") is None and
        renpy.get_screen("nv127_world_map") is None and
        renpy.get_screen("world_map") is None
    ):
        # Left icon rail — this is the visual HUD the user chose to keep.
        frame:
            xpos 18
            ypos 12
            background Solid("#02070bc8")
            padding (8, 6)

            hbox:
                spacing 8
                use v06_hud_icon("images/ui/icons/icon_map.png", "MAP", Show("nv127_world_map"))
                use v06_hud_icon("images/ui/icons/icon_characters.png", "PEOPLE", Show("characters_screen"))
                use v06_hud_icon("images/ui/icons/icon_inventory.png", "ITEMS", Show("inventory_screen"))
                use v06_hud_icon("images/ui/icons/icon_missions.png", "EVENTS", Show("gallery_screen"))
                use v06_hud_icon("images/ui/icons/icon_guide.png", "GUIDE", Show("guide_screen"))

        # Center status panel.
        frame:
            xpos 500
            ypos 12
            xsize 285
            ysize 63
            background Solid("#02070bd9")
            padding (14, 7)

            hbox:
                xfill True

                vbox:
                    text "◉  $[coins]" size 19 color "#e7ba58"
                    text "REP [reputation]  •  STR [strength]" size 11 color "#8aa0aa"

                vbox:
                    xalign 1.0
                    $ _date = "{} {}".format(weekday_name(day), period_name())
                    text _date size 16 color "#ffffff" xalign 1.0
                    text "Day [day]" size 12 color "#9eb0b8" xalign 1.0

        # Right-side status bars.
        frame:
            xpos 1010
            ypos 12
            xsize 250
            ysize 63
            background Solid("#02070bd9")
            padding (12, 8)

            vbox:
                spacing 6

                hbox:
                    text "⚡" size 15 color "#29d9ff" xminimum 28
                    fixed:
                        xsize 150
                        ysize 8
                        yalign 0.5
                        add Solid("#16303a") xsize 150 ysize 8
                        add Solid("#20d7ff") xsize int(150 * min(energy, 4) / 4.0) ysize 8
                    text "[energy]/4" size 12 color "#d8e6eb" xoffset 8

                hbox:
                    text "♥" size 15 color "#ff4d82" xminimum 28
                    fixed:
                        xsize 150
                        ysize 8
                        yalign 0.5
                        add Solid("#351a26") xsize 150 ysize 8
                        add Solid("#ff4d82") xsize int(150 * relation("aya", "love") / 10.0) ysize 8
                    text "[relation('aya', 'love')]" size 12 color "#d8e6eb" xoffset 8
