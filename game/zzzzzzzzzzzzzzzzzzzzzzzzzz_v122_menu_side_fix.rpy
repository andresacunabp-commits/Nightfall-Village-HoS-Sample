# ============================================================
# NIGHTFALL VILLAGE v0.12.2 — MAIN MENU SIDE/FULL-ART FIX
# ============================================================
# Restores the full seated-Aya menu artwork with no crop and keeps
# the player-facing navigation on the LEFT side.
# ============================================================

screen main_menu():
    tag menu

    # Full original seated-Aya composition. No im.Crop(), so the art
    # is no longer enlarged from a partial slice or cut off.
    add im.Scale("images/ui/hos_menu_showcase.png", 1280, 720)

    # Soft treatment so the live Ren'Py menu reads clearly over the art.
    add Solid("#01060a18")
    add SnowBlossom("images/ui/polish/petal.png", count=8, border=55, xspeed=(-12, 13), yspeed=(15, 31), start=2)

    # LEFT navigation panel. This also covers the older baked sidebar
    # contained inside the original showcase image.
    frame:
        xpos 0
        ypos 0
        xsize 385
        ysize 720
        background Solid("#02080df2")
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
