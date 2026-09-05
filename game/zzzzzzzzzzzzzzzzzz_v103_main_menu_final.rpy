# ============================================================
# NIGHTFALL VILLAGE — v0.10.3 FINAL MAIN MENU OVERRIDE
# ============================================================
# Keeps the proven v0.10.2 layout, but makes the displayed build
# version dynamic so future releases cannot show a stale number.
# ============================================================

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#01060a58")
    add SnowBlossom("images/ui/polish/petal.png", count=13, border=60, xspeed=(-15, 16), yspeed=(18, 40), start=3)

    frame:
        xpos 0
        ypos 0
        xsize 336
        ysize 720
        background Solid("#02080df2")
        padding (24, 18)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 9
                ypos 0
                zoom 0.47

            text "SHINOBI SANDBOX PORTFOLIO":
                xpos 32
                ypos 154
                size 10
                bold True
                color "#00d4ff"

            vbox:
                xpos 0
                ypos 188
                spacing 2

                textbutton "▶   Continue" action ShowMenu("load") style "nv102_nav"
                textbutton "▣   New Game" action Start() style "nv102_nav"
                textbutton "◆   World Hub" action Start() style "nv102_nav"
                textbutton "✦   Household Demo" action Start("v07_house_demo_start") style "nv102_nav"
                textbutton "◇   Mission Control" action Start("v08_mission_control_start") style "nv102_nav"
                textbutton "♥   Aya Story Demo" action Start("v06_aya_demo_start") style "nv102_nav"
                textbutton "▤   Guide / Events" action Show("guide_screen") style "nv102_nav"
                textbutton "⌘   Developer Tools" action Show("developer_tools") style "nv102_nav"
                textbutton "⚙   Settings" action ShowMenu("preferences") style "nv102_nav"
                textbutton "⏻   Exit" action Quit(confirm=False) style "nv102_nav"

            add Solid("#00c8ff55"):
                xpos 9
                ypos 626
                xsize 270
                ysize 1

            text "v[config.version] • HQ Background Upgrade":
                xpos 13
                ypos 642
                size 12
                bold True
                color "#9edfec"

            text "Native 1280×720 • sharper scene masters":
                xpos 13
                ypos 663
                size 10
                color "#607d88"

    add Solid("#00c8ff"):
        xpos 334
        ypos 0
        xsize 2
        ysize 720

    frame:
        xpos 358
        ypos 18
        xsize 892
        ysize 64
        background Solid("#02090ed9")
        padding (18, 8)

        hbox:
            spacing 36
            xalign 0.5

            vbox:
                text "SCENES" size 12 bold True color "#00c8ff" xalign 0.5
                text "HQ cinematic art" size 11 color "#c4d2d7"
            vbox:
                text "SANDBOX" size 12 bold True color "#00c8ff" xalign 0.5
                text "World navigation" size 11 color "#c4d2d7"
            vbox:
                text "ROUTES" size 12 bold True color "#00c8ff" xalign 0.5
                text "Love / Hatred" size 11 color "#c4d2d7"
            vbox:
                text "EVENTS" size 12 bold True color "#00c8ff" xalign 0.5
                text "Persistent state" size 11 color "#c4d2d7"
            vbox:
                text "TOOLING" size 12 bold True color "#00c8ff" xalign 0.5
                text "F2 inspector" size 11 color "#c4d2d7"

    add "images/characters/aya/aya_smile.png":
        xpos 390
        ypos 80
        zoom 0.68
        at v06_float

    frame:
        xpos 820
        ypos 130
        xsize 405
        ysize 455
        background Solid("#02080ce8")
        padding (26, 22)

        vbox:
            spacing 11
            text "NEW IN v[config.version]" size 12 bold True color "#e4bd68"
            text "HQ Background Upgrade" size 30 bold True color "#ffffff"
            text "Seven gameplay locations now use native-resolution 1280×720 masters instead of stretching the compact fallback art." size 15 color "#bdcbd1" line_spacing 3

            null height 4
            text "◆ 1280×720 gameplay backgrounds" size 14 color "#dbeaf0"
            text "◆ Super-resolution reconstruction" size 14 color "#dbeaf0"
            text "◆ High-quality JPEG export" size 14 color "#dbeaf0"
            text "◆ Detail + local-contrast recovery" size 14 color "#dbeaf0"
            text "◆ HQ thumbnails in World Hub" size 14 color "#dbeaf0"
            text "◆ No prototype geometry overlays" size 14 color "#dbeaf0"

            null height 10
            textbutton "ENTER WORLD HUB  →" action Start() style "v09_small_button"
            textbutton "HOUSEHOLD DEMO" action Start("v07_house_demo_start") style "v09_small_button"

    frame:
        xpos 785
        ypos 610
        background Solid("#020609e8")
        padding (16, 8)
        text "Nightfall Village • Ren'Py + Python • Portfolio Build [config.version]" size 12 color "#8aa6b1"
