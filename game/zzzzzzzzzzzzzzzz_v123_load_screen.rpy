# ============================================================
# NIGHTFALL VILLAGE v0.12.5 — LOAD SCREEN REDESIGN
# ============================================================
# HoS-style structure: left navigation, page title, 3x2 save grid,
# and page controls along the bottom. Uses the project's own assets.
# ============================================================

style nv125_load_nav is button:
    background None
    hover_background Solid("#07354ae8")
    xsize 235
    ysize 40
    xpadding 10
    ypadding 6

style nv125_load_nav_text is button_text:
    size 18
    color "#8f9aa0"
    hover_color "#ffffff"
    xalign 0.0

style nv125_load_nav_active is nv125_load_nav:
    background Solid("#075f77dd")

style nv125_load_nav_active_text is nv125_load_nav_text:
    color "#ffffff"
    bold True

style nv125_page_button is button:
    background None
    hover_background Solid("#07354ae8")
    selected_background Solid("#075f77dd")
    xminimum 32
    yminimum 32
    xpadding 6
    ypadding 3

style nv125_page_button_text is button_text:
    size 18
    color "#8d989e"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5


screen load():
    tag menu

    # Full cinematic background.
    add im.Scale("images/ui/load_bg.png", 1280, 720)
    add Solid("#02070aa8")

    # --------------------------------------------------------
    # LEFT NAVIGATION
    # --------------------------------------------------------
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

            text "Cargar":
                xpos 12
                ypos 0
                size 46
                color "#08bfe9"

            vbox:
                xpos 0
                ypos 90
                spacing 1

                textbutton "Comenzar" action Start("nv12_start") style "nv125_load_nav"
                textbutton "Cargar" action NullAction() style "nv125_load_nav_active"
                textbutton "Galería" action ShowMenu("nv12_gallery") style "nv125_load_nav"
                textbutton "Repetir escenas" action ShowMenu("nv12_replay") style "nv125_load_nav"
                textbutton "Preferencias" action ShowMenu("preferences") style "nv125_load_nav"
                textbutton "Acerca de" action ShowMenu("nv12_about") style "nv125_load_nav"
                textbutton "Ayuda" action ShowMenu("nv12_help") style "nv125_load_nav"
                textbutton "Salir" action Quit(confirm=False) style "nv125_load_nav"

            add Solid("#00c8ff"):
                xpos 292
                ypos 80
                xsize 2
                ysize 550

            textbutton "Regresar":
                xpos 0
                ypos 625
                action Return()
                style "nv125_load_nav"

    # --------------------------------------------------------
    # RIGHT CONTENT
    # --------------------------------------------------------
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

        # 3 x 2 slots, deliberately wide and simple like the reference.
        grid 3 2:
            xpos 35
            ypos 160
            spacing 28

            for slot in range(1, 7):
                $ _has_save = FileTime(slot, empty="") != ""

                button:
                    xsize 245
                    ysize 170
                    background Solid("#064e64e8")
                    hover_background Solid("#08738fe8")
                    insensitive_background Solid("#064e64e8")
                    sensitive _has_save
                    action FileLoad(slot)

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

        # Page selector: < A Q 1 2 3 4 5 6 7 8 9 >
        hbox:
            xpos 165
            ypos 585
            spacing 2

            textbutton "<" action FilePagePrevious() style "nv125_page_button"

            textbutton "A":
                action FilePage("auto")
                selected FilePageName(auto="A", quick="Q") == "A"
                style "nv125_page_button"

            textbutton "Q":
                action FilePage("quick")
                selected FilePageName(auto="A", quick="Q") == "Q"
                style "nv125_page_button"

            for _page in range(1, 10):
                textbutton str(_page):
                    action FilePage(_page)
                    selected FilePageName(auto="A", quick="Q") == str(_page)
                    style "nv125_page_button"

            textbutton ">" action FilePageNext(max=9) style "nv125_page_button"

        text "Selecciona un espacio guardado para continuar.":
            xpos 0
            ypos 640
            xsize 900
            text_align 0.5
            size 14
            color "#7d898f"
