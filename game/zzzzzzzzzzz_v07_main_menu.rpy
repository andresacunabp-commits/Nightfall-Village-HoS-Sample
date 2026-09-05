# ============================================================
# NIGHTFALL VILLAGE v0.7 — MAIN MENU OVERRIDE
# Loaded after the v0.6 visual layer so the visible build is 0.7.
# ============================================================

style v07_main_button is button:
    background None
    hover_background Solid("#073548e8")
    selected_background Solid("#08445ae8")
    xsize 270
    yminimum 45
    xpadding 16
    ypadding 7

style v07_main_button_text is button_text:
    size 19
    color "#aebbc4"
    hover_color "#ffffff"
    selected_color "#00d8ff"

style v07_feature_button is button:
    background Solid("#06212ddb")
    hover_background Solid("#0a4a62f2")
    xpadding 18
    ypadding 10

style v07_feature_button_text is button_text:
    size 15
    bold True
    color "#dff8ff"
    hover_color "#ffffff"

# Disable the old floating v0.7 addon because the new menu includes it directly.
screen v07_main_menu_addon():
    pass

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#02070a55")
    add SnowBlossom("images/ui/polish/petal.png", count=14, border=60, xspeed=(-18, 18), yspeed=(22, 48), start=4)

    # --------------------------------------------------------
    # LEFT NAVIGATION
    # --------------------------------------------------------
    frame:
        xpos 0
        ypos 0
        xsize 335
        ysize 720
        background Solid("#02080de8")
        padding (26, 20)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 8
                ypos 0
                zoom 0.47

            text "DIRECT HoS-RELATED SAMPLE":
                xpos 36
                ypos 154
                size 11
                color "#50d9ff"

            vbox:
                xpos 0
                ypos 196
                spacing 3

                textbutton "▶   Continue":
                    action ShowMenu("load")
                    style "v07_main_button"

                textbutton "▣   New Game":
                    action Start()
                    style "v07_main_button"

                textbutton "✦   Household Demo":
                    action Start("v07_house_demo_start")
                    style "v07_main_button"

                textbutton "◫   Aya Story Demo":
                    action Start("v06_aya_demo_start")
                    style "v07_main_button"

                textbutton "♥   Characters":
                    action Show("characters_screen")
                    style "v07_main_button"

                textbutton "▤   Guide / Events":
                    action Show("guide_screen")
                    style "v07_main_button"

                textbutton "⚙   Settings":
                    action ShowMenu("preferences")
                    style "v07_main_button"

                textbutton "⌘   Developer Tools":
                    action Show("developer_tools")
                    style "v07_main_button"

                textbutton "⏻   Exit":
                    action Quit(confirm=False)
                    style "v07_main_button"

            add "images/ui/polish/separator.png":
                xpos 8
                ypos 612
                zoom 0.50

            text "v0.7.0 • Household Vertical Slice":
                xpos 14
                ypos 636
                size 13
                color "#8da6b0"

            text "Sandbox • relationships • event tooling":
                xpos 14
                ypos 658
                size 11
                color "#59737e"

    add Solid("#00c8ff"):
        xpos 333
        ypos 0
        xsize 2
        ysize 720

    # --------------------------------------------------------
    # TOP FEATURE BAR
    # --------------------------------------------------------
    frame:
        xpos 365
        ypos 18
        xsize 875
        ysize 64
        background Solid("#03090ec5")
        padding (18, 8)

        hbox:
            spacing 42
            xalign 0.5

            vbox:
                text "SANDBOX" size 12 bold True color "#00c8ff" xalign 0.5
                text "Room + world navigation" size 11 color "#c4d2d7"

            vbox:
                text "ROUTES" size 12 bold True color "#00c8ff" xalign 0.5
                text "Love / Hatred" size 11 color "#c4d2d7"

            vbox:
                text "EVENTS" size 12 bold True color "#00c8ff" xalign 0.5
                text "Persistent chain state" size 11 color "#c4d2d7"

            vbox:
                text "TOOLING" size 12 bold True color "#00c8ff" xalign 0.5
                text "F2 event inspector" size 11 color "#c4d2d7"

    # --------------------------------------------------------
    # CHARACTER SHOWCASE
    # --------------------------------------------------------
    add "images/characters/aya/aya_smile.png":
        xpos 390
        ypos 80
        zoom 0.68
        at v06_float

    # --------------------------------------------------------
    # v0.7 FEATURE CARD
    # --------------------------------------------------------
    frame:
        xpos 825
        ypos 155
        xsize 395
        ysize 390
        background Solid("#02090ed9")
        padding (26, 22)
        at v06_panel_in

        vbox:
            spacing 12

            text "NEW IN v0.7":
                size 13
                bold True
                color "#e7bd67"

            text "Aya's Household":
                size 31
                bold True
                color "#ffffff"

            text "A compact vertical slice built around room navigation, character availability and chained relationship events.":
                size 16
                color "#bccbd1"
                line_spacing 4

            null height 2

            text "● Room-by-room navigation" size 15 color "#dceaf0"
            text "● Green availability markers" size 15 color "#dceaf0"
            text "● Five-stage event chain" size 15 color "#dceaf0"
            text "● Love / Hatred reactions" size 15 color "#dceaf0"
            text "● Persistent save state" size 15 color "#dceaf0"

            null height 5

            textbutton "PLAY HOUSEHOLD DEMO  →":
                action Start("v07_house_demo_start")
                style "v07_feature_button"

    frame:
        xpos 785
        ypos 610
        background Solid("#020609ce")
        padding (18, 9)

        text "Nightfall Village • Ren'Py + Python • Portfolio Build 0.7.0":
            size 13
            color "#86a3af"
