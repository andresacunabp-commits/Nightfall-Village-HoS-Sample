# ============================================================
# NIGHTFALL VILLAGE v0.12.6 — UNIFIED MENU SCREENS
# ============================================================
# Matches the v0.12.5 load-screen language across Save, Gallery,
# Replay, Preferences, About and Help.
# ============================================================

style nv126_nav is button:
    background None
    hover_background Solid("#07354ae8")
    xsize 235
    ysize 40
    xpadding 10
    ypadding 6

style nv126_nav_text is button_text:
    size 18
    color "#8f9aa0"
    hover_color "#ffffff"
    xalign 0.0

style nv126_nav_active is nv126_nav:
    background Solid("#075f77dd")

style nv126_nav_active_text is nv126_nav_text:
    color "#ffffff"
    bold True

style nv126_page_button is button:
    background None
    hover_background Solid("#07354ae8")
    selected_background Solid("#075f77dd")
    xminimum 32
    yminimum 32
    xpadding 6
    ypadding 3

style nv126_page_button_text is button_text:
    size 18
    color "#8d989e"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5

style nv126_card is button:
    background Solid("#064e64df")
    hover_background Solid("#08738fee")
    insensitive_background Solid("#082531cc")
    xpadding 0
    ypadding 0

style nv126_card_text is button_text:
    color "#ffffff"

style nv126_small is button:
    background Solid("#06364ae5")
    hover_background Solid("#087a98ee")
    insensitive_background Solid("#09242dcc")
    xpadding 14
    ypadding 8

style nv126_small_text is button_text:
    size 14
    color "#d9e8ed"
    hover_color "#ffffff"
    insensitive_color "#53666d"

style nv126_toggle is button:
    background Solid("#07131bdc")
    hover_background Solid("#08455be8")
    selected_background Solid("#087b97e8")
    xminimum 180
    yminimum 42
    xpadding 14
    ypadding 8

style nv126_toggle_text is button_text:
    size 16
    color "#9fadb3"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5


# ------------------------------------------------------------
# SHARED LEFT NAVIGATION
# ------------------------------------------------------------

screen nv126_sidebar(page_title, active):
    frame:
        xpos 0
        ypos 0
        xsize 330
        ysize 720
        background Solid("#02080dcc")
        padding (34, 18)

        fixed:
            xfill True
            yfill True

            text page_title:
                xpos 12
                ypos 0
                size 46
                color "#08bfe9"

            vbox:
                xpos 0
                ypos 90
                spacing 1

                textbutton "Comenzar":
                    action Start("nv12_start")
                    style ("nv126_nav_active" if active == "start" else "nv126_nav")

                textbutton "Cargar":
                    action ShowMenu("load")
                    style ("nv126_nav_active" if active == "load" else "nv126_nav")

                textbutton "Galería":
                    action ShowMenu("nv12_gallery")
                    style ("nv126_nav_active" if active == "gallery" else "nv126_nav")

                textbutton "Repetir escenas":
                    action ShowMenu("nv12_replay")
                    style ("nv126_nav_active" if active == "replay" else "nv126_nav")

                textbutton "Preferencias":
                    action ShowMenu("preferences")
                    style ("nv126_nav_active" if active == "preferences" else "nv126_nav")

                textbutton "Acerca de":
                    action ShowMenu("nv12_about")
                    style ("nv126_nav_active" if active == "about" else "nv126_nav")

                textbutton "Ayuda":
                    action ShowMenu("nv12_help")
                    style ("nv126_nav_active" if active == "help" else "nv126_nav")

                textbutton "Salir":
                    action Quit(confirm=False)
                    style "nv126_nav"

            add Solid("#00c8ff"):
                xpos 292
                ypos 80
                xsize 2
                ysize 550

            textbutton "Regresar":
                xpos 0
                ypos 625
                action Return()
                style "nv126_nav"


# ------------------------------------------------------------
# SAVE — SAME 3x2 / PAGE STRUCTURE AS LOAD
# ------------------------------------------------------------

screen save():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070aa8")
    use nv126_sidebar("Guardar", "save")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Página {}".format(FilePageName(auto="A", quick="Q")):
            xpos 0
            ypos 88
            xsize 900
            text_align 0.5
            size 24
            color "#11c7ee"

        grid 3 2:
            xpos 35
            ypos 160
            spacing 28

            for slot in range(1, 7):
                $ _has_save = FileTime(slot, empty="") != ""

                button:
                    xsize 245
                    ysize 170
                    style "nv126_card"
                    action FileSave(slot)

                    fixed:
                        xfill True
                        yfill True

                        if _has_save:
                            add FileScreenshot(slot):
                                xysize (245, 138)

                            add Solid("#00000088"):
                                ypos 112
                                xsize 245
                                ysize 26

                            text FileTime(slot, format="%d/%m/%Y  %H:%M", empty=""):
                                xpos 8
                                ypos 116
                                size 11
                                color "#ffffff"

                            text FileSaveName(slot):
                                xpos 8
                                ypos 143
                                xmaximum 225
                                size 11
                                color "#b8cbd2"
                        else:
                            text "espacio vacío":
                                xpos 0
                                ypos 143
                                xsize 245
                                text_align 0.5
                                size 12
                                color "#65767d"

        hbox:
            xpos 165
            ypos 585
            spacing 2

            textbutton "<" action FilePagePrevious() style "nv126_page_button"

            textbutton "A":
                action FilePage("auto")
                selected FilePageName(auto="A", quick="Q") == "A"
                style "nv126_page_button"

            textbutton "Q":
                action FilePage("quick")
                selected FilePageName(auto="A", quick="Q") == "Q"
                style "nv126_page_button"

            for _page in range(1, 10):
                textbutton str(_page):
                    action FilePage(_page)
                    selected FilePageName(auto="A", quick="Q") == str(_page)
                    style "nv126_page_button"

            textbutton ">" action FilePageNext(max=9) style "nv126_page_button"

        text "Selecciona un espacio para guardar tu progreso.":
            xpos 0
            ypos 640
            xsize 900
            text_align 0.5
            size 14
            color "#7d898f"


# ------------------------------------------------------------
# GALLERY — 3x2 CARD GRID
# ------------------------------------------------------------

screen nv12_gallery():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070ab5")
    use nv126_sidebar("Galería", "gallery")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Imágenes desbloqueadas":
            xpos 0
            ypos 88
            xsize 900
            text_align 0.5
            size 24
            color "#11c7ee"

        grid 3 2:
            xpos 35
            ypos 160
            spacing 28

            for _title, _path, _event_id in NV12_GALLERY_ITEMS:
                $ _unlocked = nv12_unlocked(_event_id)

                frame:
                    xsize 245
                    ysize 170
                    background Solid("#064e64e8" if _unlocked else "#082531dd")
                    padding (0, 0)

                    fixed:
                        xfill True
                        yfill True

                        if _unlocked:
                            add _path:
                                xysize (245, 138)

                            add Solid("#00000088"):
                                ypos 112
                                xsize 245
                                ysize 26

                            text _title:
                                xpos 8
                                ypos 116
                                xmaximum 228
                                size 12
                                bold True
                                color "#ffffff"
                        else:
                            text "BLOQUEADO":
                                xpos 0
                                ypos 67
                                xsize 245
                                text_align 0.5
                                size 15
                                bold True
                                color "#51666e"

                            text "???":
                                xpos 0
                                ypos 143
                                xsize 245
                                text_align 0.5
                                size 12
                                color "#5a6b72"

        text "La galería se desbloquea automáticamente al descubrir escenas.":
            xpos 0
            ypos 640
            xsize 900
            text_align 0.5
            size 14
            color "#7d898f"


# ------------------------------------------------------------
# REPLAY — 2x2 SCENE CARDS
# ------------------------------------------------------------

screen nv12_replay():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070ab5")
    use nv126_sidebar("Escenas", "replay")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Repetir escenas":
            xpos 0
            ypos 88
            xsize 900
            text_align 0.5
            size 24
            color "#11c7ee"

        text "Las repeticiones no modifican tu partida guardada.":
            xpos 0
            ypos 124
            xsize 900
            text_align 0.5
            size 13
            color "#7d898f"

        grid 2 2:
            xpos 80
            ypos 180
            spacing 24

            for _title, _character, _event_id, _replay_label in NV12_REPLAY_ITEMS:
                $ _unlocked = nv12_unlocked(_event_id)

                frame:
                    xsize 355
                    ysize 165
                    background Solid("#064e64df" if _unlocked else "#082531dd")
                    padding (18, 15)

                    fixed:
                        xfill True
                        yfill True

                        text _title:
                            xpos 0
                            ypos 0
                            xmaximum 310
                            size 20
                            bold True
                            color ("#ffffff" if _unlocked else "#52666d")

                        text _character.upper():
                            xpos 0
                            ypos 38
                            size 12
                            bold True
                            color ("#11c7ee" if _unlocked else "#46575d")

                        if _unlocked:
                            textbutton "REPETIR  ▶":
                                xpos 0
                                ypos 92
                                action Replay(_replay_label)
                                style "nv126_small"
                        else:
                            text "BLOQUEADO":
                                xpos 0
                                ypos 103
                                size 13
                                bold True
                                color "#53656c"


# ------------------------------------------------------------
# PREFERENCES
# ------------------------------------------------------------

screen preferences():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070ab5")
    use nv126_sidebar("Preferencias", "preferences")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Preferencias":
            xpos 0
            ypos 70
            xsize 900
            text_align 0.5
            size 28
            color "#11c7ee"

        frame:
            xpos 70
            ypos 125
            xsize 760
            ysize 500
            background Solid("#02080dc9")
            padding (28, 24)

            vbox:
                spacing 18

                text "PANTALLA" size 13 bold True color "#11c7ee"

                hbox:
                    spacing 12
                    textbutton "VENTANA":
                        action Preference("display", "window")
                        selected not preferences.fullscreen
                        style "nv126_toggle"
                    textbutton "PANTALLA COMPLETA":
                        action Preference("display", "fullscreen")
                        selected preferences.fullscreen
                        style "nv126_toggle"

                add Solid("#00c8ff44") xsize 700 ysize 1

                text "VELOCIDAD DEL TEXTO" size 13 bold True color "#11c7ee"
                bar value Preference("text speed") xmaximum 700

                text "AVANCE AUTOMÁTICO" size 13 bold True color "#11c7ee"
                bar value Preference("auto-forward time") xmaximum 700

                add Solid("#00c8ff44") xsize 700 ysize 1

                text "MÚSICA" size 13 bold True color "#11c7ee"
                bar value Preference("music volume") xmaximum 700

                text "SONIDO" size 13 bold True color "#11c7ee"
                bar value Preference("sound volume") xmaximum 700

                text "VOZ" size 13 bold True color "#11c7ee"
                bar value Preference("voice volume") xmaximum 700


# ------------------------------------------------------------
# ABOUT
# ------------------------------------------------------------

screen nv12_about():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070ab5")
    use nv126_sidebar("Acerca de", "about")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Nightfall Village":
            xpos 0
            ypos 88
            xsize 900
            text_align 0.5
            size 30
            bold True
            color "#11c7ee"

        frame:
            xpos 90
            ypos 155
            xsize 720
            ysize 415
            background Solid("#02080dd8")
            padding (34, 30)

            vbox:
                spacing 18

                text "SHINOBI SANDBOX" size 13 bold True color "#11c7ee" xalign 0.5
                text "Una novela visual sandbox centrada en una partida persistente." size 22 bold True color "#ffffff" xalign 0.5 text_align 0.5

                add Solid("#00c8ff44") xsize 650 ysize 1

                text "Eliges dónde ir, qué hacer y cómo relacionarte con los personajes mientras el tiempo, sus horarios y los eventos avanzan." size 16 color "#c2d0d5" text_align 0.5 xalign 0.5 line_spacing 4

                text "Proyecto original construido con Ren'Py + Python como muestra de sistemas narrativos, eventos condicionales, relaciones, guardado persistente y exploración libre." size 15 color "#93a8b1" text_align 0.5 xalign 0.5 line_spacing 4

                null height 8
                text "Versión [config.version]" size 13 color "#e4bd68" xalign 0.5


# ------------------------------------------------------------
# HELP
# ------------------------------------------------------------

screen nv12_help():
    tag menu

    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070ab5")
    use nv126_sidebar("Ayuda", "help")

    fixed:
        xpos 360
        ypos 0
        xsize 920
        ysize 720

        text "Ayuda":
            xpos 0
            ypos 75
            xsize 900
            text_align 0.5
            size 30
            color "#11c7ee"

        frame:
            xpos 70
            ypos 135
            xsize 760
            ysize 500
            background Solid("#02080dd8")
            padding (30, 26)

            hbox:
                spacing 45

                vbox:
                    xsize 300
                    spacing 14

                    text "CONTROLES" size 14 bold True color "#11c7ee"
                    text "Clic izquierdo" size 16 bold True color "#ffffff"
                    text "Avanzar / seleccionar" size 13 color "#8fa4ad"
                    text "Clic derecho" size 16 bold True color "#ffffff"
                    text "Volver" size 13 color "#8fa4ad"
                    text "Rueda del ratón" size 16 bold True color "#ffffff"
                    text "Historial" size 13 color "#8fa4ad"
                    text "Ctrl" size 16 bold True color "#ffffff"
                    text "Omitir texto" size 13 color "#8fa4ad"
                    text "Esc" size 16 bold True color "#ffffff"
                    text "Menú de juego" size 13 color "#8fa4ad"

                add Solid("#00c8ff44") xsize 1 ysize 420

                vbox:
                    xsize 330
                    spacing 14

                    text "CÓMO SE JUEGA" size 14 bold True color "#11c7ee"
                    text "Explora libremente" size 18 bold True color "#ffffff"
                    text "Dentro de tu partida decides adónde ir usando MAPA." size 14 color "#aabcc3" line_spacing 3

                    text "El tiempo importa" size 18 bold True color "#ffffff"
                    text "Las acciones pueden avanzar la hora y cambiar dónde se encuentran los personajes." size 14 color "#aabcc3" line_spacing 3

                    text "Los eventos reaccionan" size 18 bold True color "#ffffff"
                    text "Algunas escenas requieren un día, horario, objeto, estadística o relación determinados." size 14 color "#aabcc3" line_spacing 3

                    text "Guarda tu progreso" size 18 bold True color "#ffffff"
                    text "Puedes continuar cualquier partida desde Cargar." size 14 color "#aabcc3" line_spacing 3
