# ============================================================
# NIGHTFALL VILLAGE v0.12.3 — LOAD SCREEN
# ============================================================
# Uses the custom Aya background and the project's native six-slot
# save/load layout. No dependency on the default Ren'Py file_slots.
# ============================================================

screen load():
    tag menu

    add "images/ui/load_bg.png"
    add Solid("#0000004d")

    # Left title/navigation strip.
    frame:
        xpos 0
        ypos 0
        xsize 310
        ysize 720
        background Solid("#02080dea")
        padding (28, 28)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 0
                ypos 0
                zoom 0.40

            text "CARGAR":
                xpos 4
                ypos 150
                size 38
                bold True
                color "#39cfff"

            text "Continúa una partida guardada.":
                xpos 4
                ypos 198
                xmaximum 245
                size 13
                color "#9cb7c2"

            textbutton "← VOLVER":
                xpos 4
                ypos 620
                action Return()
                style "v06_small_button"

    # Save slots.
    frame:
        xpos 330
        ypos 32
        xsize 920
        ysize 656
        background Solid("#02080dba")
        padding (24, 22)

        vbox:
            spacing 15

            hbox:
                xfill True
                text "PARTIDAS GUARDADAS" size 24 bold True color "#ffffff"
                text "Selecciona una partida para continuar" size 12 color "#8ba3ad" xalign 1.0 yalign 0.5

            grid 3 2:
                spacing 14

                for slot in range(1, 7):
                    button:
                        xsize 278
                        ysize 268
                        background Solid("#06131cdd")
                        hover_background Solid("#0a3547ee")
                        action FileLoad(slot)

                        fixed:
                            xfill True
                            yfill True

                            add Solid("#00c8ff55"):
                                xpos 0
                                ypos 0
                                xsize 278
                                ysize 2

                            if FileTime(slot, empty="") != "":
                                add FileScreenshot(slot):
                                    xpos 12
                                    ypos 12
                                    xysize (254, 143)

                                add Solid("#00000055"):
                                    xpos 12
                                    ypos 112
                                    xsize 254
                                    ysize 43

                                text "SLOT [slot]":
                                    xpos 18
                                    ypos 120
                                    size 18
                                    bold True
                                    color "#ffffff"

                                text FileTime(slot, format="%d/%m/%Y  •  %H:%M", empty=""):
                                    xpos 16
                                    ypos 174
                                    size 12
                                    color "#8fc4d1"

                                text FileSaveName(slot):
                                    xpos 16
                                    ypos 198
                                    xmaximum 245
                                    size 12
                                    color "#c9d7dc"

                                text "CARGAR  →":
                                    xpos 184
                                    ypos 235
                                    size 11
                                    bold True
                                    color "#39cfff"

                            else:
                                text "SLOT [slot]":
                                    xpos 18
                                    ypos 18
                                    size 18
                                    bold True
                                    color "#667982"

                                text "VACÍO":
                                    xpos 0
                                    ypos 112
                                    xsize 278
                                    text_align 0.5
                                    size 16
                                    bold True
                                    color "#53656d"

                                text "No hay una partida guardada en este espacio.":
                                    xpos 28
                                    ypos 145
                                    xmaximum 220
                                    text_align 0.5
                                    size 11
                                    color "#52666e"
