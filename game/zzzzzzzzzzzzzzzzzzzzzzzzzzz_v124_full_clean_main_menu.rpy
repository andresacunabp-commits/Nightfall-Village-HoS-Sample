# ============================================================
# NIGHTFALL VILLAGE v0.12.4 — FULL CLEAN MAIN MENU ART
# ============================================================
# Uses the clean Aya artwork already added as load_bg.png.
# No crop: the whole illustration is shown across the 1280x720 menu.
# Player navigation stays on the LEFT.
# ============================================================

screen main_menu():
    tag menu

    # Show the complete clean illustration. Explicit scaling prevents
    # Ren'Py from displaying only a native-size portion of the image.
    add im.Scale("images/ui/load_bg.png", 1280, 720)

    # Gentle darkening only; the artwork remains the visual focus.
    add Solid("#01060a18")
    add SnowBlossom("images/ui/polish/petal.png", count=8, border=55, xspeed=(-12, 13), yspeed=(15, 31), start=2)

    # LEFT navigation panel.
    frame:
        xpos 0
        ypos 0
        xsize 385
        ysize 720
        background Solid("#02080dee")
        padding (38, 26)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 5
                ypos 2
                zoom 0.47

            text "SHINOBI SANDBOX":
                xpos 30
                ypos 150
                size 11
                bold True
                color "#59dffc"

            vbox:
                xpos 0
                ypos 190
                spacing 5

                textbutton "COMENZAR" action Start("nv12_start") style "nv121_menu_primary"
                textbutton "CARGAR" action ShowMenu("load") style "nv121_menu_button"
                textbutton "GALERÍA" action ShowMenu("nv12_gallery") style "nv121_menu_button"
                textbutton "REPETIR ESCENAS" action ShowMenu("nv12_replay") style "nv121_menu_button"
                textbutton "PREFERENCIAS" action ShowMenu("preferences") style "nv121_menu_button"
                textbutton "ACERCA DE" action ShowMenu("nv12_about") style "nv121_menu_button"
                textbutton "AYUDA" action ShowMenu("nv12_help") style "nv121_menu_button"
                textbutton "SALIR" action Quit(confirm=False) style "nv121_menu_button"

            add Solid("#00c8ff55"):
                xpos 0
                ypos 642
                xsize 300
                ysize 1

            text "v[config.version]":
                xpos 4
                ypos 657
                size 11
                color "#7fb8c6"

            text "Tu partida. Tus decisiones.":
                xpos 4
                ypos 678
                size 11
                color "#59737e"
