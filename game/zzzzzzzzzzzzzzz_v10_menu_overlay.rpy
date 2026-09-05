# ============================================================
# NIGHTFALL VILLAGE v0.10.1 — MAIN MENU PRESENTATION OVERLAY
# Keeps the v0.9 navigation layout while presenting the scenario art pass.
# ============================================================

screen nv10_main_menu_overlay():
    zorder 1800

    if renpy.get_screen("main_menu") is not None:

        frame:
            xpos 18
            ypos 630
            xsize 292
            ysize 67
            background Solid("#02080df8")
            padding (10, 8)

            vbox:
                spacing 3
                text ("v0.10.1 • Scenario Art READY" if NV10_BACKGROUNDS_READY else "v0.10.1 • Scenario Art ERROR") size 13 bold True color ("#9edfec" if NV10_BACKGROUNDS_READY else "#ff7f8f")
                text ("7 cinematic backgrounds • validated" if NV10_BACKGROUNDS_READY else "Press F2 to view the art diagnostic") size 10 color "#607d88"

        frame:
            xpos 820
            ypos 125
            xsize 405
            ysize 470
            background Solid("#02080cf4")
            padding (26, 22)

            vbox:
                spacing 10

                text "NEW IN v0.10.1" size 12 bold True color "#e4bd68"
                text "Scenario Art Pass" size 30 bold True color "#ffffff"
                text "The flat prototype scenery has been replaced by original cinematic shinobi-village backgrounds integrated directly into the game." size 15 color "#bdcbd1" line_spacing 3

                null height 2
                text "◆ Detailed Village Square" size 14 color "#dbeaf0"
                text "◆ Lantern-lit Market Alley" size 14 color "#dbeaf0"
                text "◆ Dedicated Training Ground" size 14 color "#dbeaf0"
                text "◆ Moonlit Riverside" size 14 color "#dbeaf0"
                text "◆ Shrine Path + torii gates" size 14 color "#dbeaf0"
                text "◆ Aya residence exterior + hallway" size 14 color "#dbeaf0"

                null height 8

                textbutton "ENTER WORLD HUB  →":
                    action Start()
                    style "v09_small_button"

                textbutton "HOUSEHOLD DEMO":
                    action Start("v07_house_demo_start")
                    style "v09_small_button"

        frame:
            xpos 770
            ypos 605
            xsize 475
            background Solid("#020609ef")
            padding (15, 8)

            text "Nightfall Village • Ren'Py + Python • Portfolio Build 0.10.1":
                size 12
                color "#8aa6b1"


init 2200 python:
    if "nv10_main_menu_overlay" not in config.overlay_screens:
        config.overlay_screens.append("nv10_main_menu_overlay")
