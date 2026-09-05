# ============================================================
# NIGHTFALL VILLAGE v0.12.1 — MANUAL MAP + SEATED AYA MENU
# ============================================================
# - restores the earlier seated-Aya menu artwork
# - keeps only the requested main-menu options
# - the world map is an in-game overlay opened ONLY with MAPA
# ============================================================


init 10000 python:
    # Make the in-game HUD available during normal interactions/choices.
    # Keep the guard so older visual layers cannot append it twice.
    if "hud" not in config.overlay_screens:
        config.overlay_screens.append("hud")


style nv121_menu_button is button:
    background Solid("#02090ed0")
    hover_background Solid("#063b4de8")
    xsize 300
    ysize 44
    xpadding 16
    ypadding 7

style nv121_menu_button_text is button_text:
    size 18
    color "#c4d4da"
    hover_color "#ffffff"
    xalign 0.0

style nv121_menu_primary is nv121_menu_button:
    background Solid("#047e9be8")
    hover_background Solid("#08a4c6f2")

style nv121_menu_primary_text is nv121_menu_button_text:
    bold True
    color "#ffffff"

style nv121_map_button is button:
    background Solid("#06141ceb")
    hover_background Solid("#0a4054f2")
    insensitive_background Solid("#04090ccc")
    xpadding 14
    ypadding 10

style nv121_map_button_text is button_text:
    size 15
    color "#d7e6eb"
    hover_color "#ffffff"
    insensitive_color "#53646b"

style nv121_hud_button is button:
    background Solid("#061720e8")
    hover_background Solid("#0a455ae8")
    xpadding 11
    ypadding 7

style nv121_hud_button_text is button_text:
    size 13
    bold True
    color "#c9dbe2"
    hover_color "#ffffff"

style nv121_map_primary is nv121_hud_button:
    background Solid("#057f9de8")
    hover_background Solid("#08a8c9f2")

style nv121_map_primary_text is nv121_hud_button_text:
    color "#ffffff"


# ------------------------------------------------------------
# MAIN MENU — SEATED AYA ARTWORK
# ------------------------------------------------------------

screen main_menu():
    tag menu

    # The repository already contains the original v0.5 showcase.
    # Crop away its old baked sidebar/top HUD/dialogue and keep the
    # seated Aya + moonlit village illustration.
    add im.Scale(
        im.Crop("images/ui/hos_menu_showcase.png", (268, 77, 857, 482)),
        1280,
        720
    )

    add Solid("#01060a22")
    add SnowBlossom("images/ui/polish/petal.png", count=9, border=55, xspeed=(-12, 13), yspeed=(15, 31), start=2)

    # Right-side navigation leaves Aya fully visible.
    frame:
        xpos 895
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


# ------------------------------------------------------------
# MAP — NEVER AUTOMATIC. OPENED ONLY FROM HUD > MAPA.
# ------------------------------------------------------------

screen world_map():
    modal True
    zorder 320

    key "game_menu" action Hide("world_map")

    add Solid("#000000b0")

    frame:
        xpos 70
        ypos 45
        xsize 1140
        ysize 630
        background Solid("#02080df5")
        padding (26, 22)

        fixed:
            xfill True
            yfill True

            text "MAPA":
                xpos 0
                ypos 0
                size 34
                bold True
                color "#ffffff"

            text "Elige un destino. El mapa solo aparece cuando tú lo abres.":
                xpos 0
                ypos 44
                size 13
                color "#7e9aa5"

            text "DAY [day] • [period_name()] • $[coins] • ENERGY [energy]/4":
                xpos 630
                ypos 14
                size 13
                color "#d4e1e5"

            textbutton "CERRAR  ✕":
                xpos 950
                ypos 0
                action Hide("world_map")
                style "nv121_hud_button"

            grid 2 4:
                xpos 0
                ypos 92
                spacing 14

                for _location_id in LOCATION_ORDER:
                    $ _loc = LOCATION_DATA[_location_id]
                    $ _unlocked = is_location_unlocked(_location_id)
                    $ _event_ready = location_has_event(_location_id) if _unlocked else False
                    $ _residents = residents_at(_location_id) if _unlocked else ""
                    $ _visual = v09_visual(_location_id)

                    button:
                        xsize 535
                        ysize 108
                        background Solid("#06141deb" if _unlocked else "#03070acc")
                        hover_background Solid("#0a3545f0")
                        insensitive_background Solid("#03070acc")
                        sensitive _unlocked
                        action [
                            SetVariable("current_location_id", _location_id),
                            Hide("world_map"),
                            Jump(_loc["label"])
                        ]

                        fixed:
                            xfill True
                            yfill True

                            add Solid(_visual["accent"]):
                                xpos 0
                                ypos 0
                                xsize 3
                                ysize 108

                            text _loc["name"]:
                                xpos 16
                                ypos 15
                                size 20
                                bold True
                                color ("#ffffff" if _unlocked else "#56656b")

                            if _unlocked:
                                text ("EVENTO DISPONIBLE" if _event_ready else (_residents if _residents else "Disponible")):
                                    xpos 16
                                    ypos 48
                                    size 12
                                    bold _event_ready
                                    color ("#e4bd68" if _event_ready else ("#59e6a1" if _residents else "#7f97a1"))

                                text "IR  →":
                                    xpos 455
                                    ypos 72
                                    size 11
                                    bold True
                                    color "#62dff8"
                            else:
                                text "BLOQUEADO":
                                    xpos 16
                                    ypos 48
                                    size 12
                                    color "#536168"


# ------------------------------------------------------------
# HUD — MAP BUTTON IN THE TOP-LEFT
# ------------------------------------------------------------

screen hud():
    zorder 110

    if renpy.get_screen("main_menu") is None and renpy.get_screen("developer_tools") is None and renpy.get_screen("world_map") is None:

        frame:
            xpos 12
            ypos 10
            xsize 1256
            ysize 54
            background Solid("#02080de9")
            padding (9, 7)

            hbox:
                xfill True
                spacing 10

                textbutton "MAPA":
                    action Show("world_map")
                    style "nv121_map_primary"

                text "DAY [day]" size 13 bold True color "#e4bd68" yalign 0.5
                text period_name().upper() size 13 bold True color "#ffffff" yalign 0.5
                text "$[coins]" size 13 bold True color "#e4bd68" yalign 0.5
                text "ENERGY [energy]/4" size 12 color "#63dcf5" yalign 0.5
                text "STR [strength]" size 12 color "#d7e3e7" yalign 0.5
                text "REP [reputation]" size 12 color "#d7e3e7" yalign 0.5

                null width 55

                textbutton "OBJETOS" action Show("inventory_screen") style "nv121_hud_button"
                textbutton "PERSONAS" action Show("characters_screen") style "nv121_hud_button"
                textbutton "GUARDAR" action ShowMenu("save") style "nv121_hud_button"
