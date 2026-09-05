# ============================================================
# NIGHTFALL VILLAGE — VISUAL POLISH v0.6
# Directly relevant sandbox-VN portfolio presentation.
# Original implementation/assets; familiar workflow, not copied code.
# ============================================================

transform v06_float:
    subpixel True
    yoffset 0
    ease 3.0 yoffset -5
    ease 3.0 yoffset 0
    repeat

transform v06_soft_in:
    alpha 0.0
    xoffset 25
    ease 0.35 alpha 1.0 xoffset 0

transform v06_panel_in:
    alpha 0.0
    yoffset 12
    ease 0.25 alpha 1.0 yoffset 0


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------

style v06_sidebar_button is button:
    background None
    hover_background Solid("#092b38d9")
    selected_background Solid("#083c4fe6")
    xsize 272
    yminimum 48
    xpadding 18
    ypadding 8

style v06_sidebar_button_text is button_text:
    size 20
    color "#aebbc4"
    hover_color "#e9fbff"
    selected_color "#ffffff"

style v06_small_button is button:
    background Solid("#08141bcc")
    hover_background Solid("#0a4054ee")
    xpadding 14
    ypadding 8

style v06_small_button_text is button_text:
    size 14
    color "#b9c9d0"
    hover_color "#ffffff"

style v06_choice is button:
    background Solid("#071016f2")
    hover_background Solid("#07394cec")
    xsize 690
    yminimum 54
    xpadding 24
    ypadding 10

style v06_choice_text is button_text:
    size 20
    color "#edf8fb"
    hover_color "#ffffff"
    xalign 0.5

style v06_card_button is button:
    background Solid("#071016d9")
    hover_background Solid("#0a3444ee")
    insensitive_background Solid("#070a0dbe")
    xpadding 16
    ypadding 13

style v06_card_button_text is button_text:
    color "#eaf7fb"
    hover_color "#ffffff"


# ------------------------------------------------------------
# Main Menu
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#02070a4f")
    add SnowBlossom("images/ui/polish/petal.png", count=14, border=60, xspeed=(-18, 18), yspeed=(22, 48), start=4)

    # LEFT SIDEBAR
    frame:
        xpos 0
        ypos 0
        xsize 330
        ysize 720
        background Solid("#02080ddf")
        padding (26, 20)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 10
                ypos 0
                zoom 0.47

            text "DIRECT HoS-RELATED SAMPLE":
                xpos 38
                ypos 156
                size 11
                color "#50d9ff"

            vbox:
                xpos 0
                ypos 205
                spacing 4

                textbutton "▶   Continue":
                    action ShowMenu("load")
                    style "v06_sidebar_button"

                textbutton "▣   New Game":
                    action Start()
                    style "v06_sidebar_button"

                textbutton "✦   Aya Story Demo":
                    action Start("v06_aya_demo_start")
                    style "v06_sidebar_button"

                textbutton "◫   Gallery / Events":
                    action Show("gallery_screen")
                    style "v06_sidebar_button"

                textbutton "♥   Characters":
                    action Show("characters_screen")
                    style "v06_sidebar_button"

                textbutton "▤   Guide":
                    action Show("guide_screen")
                    style "v06_sidebar_button"

                textbutton "⚙   Settings":
                    action ShowMenu("preferences")
                    style "v06_sidebar_button"

                textbutton "⌘   Developer Tools":
                    action Show("developer_tools")
                    style "v06_sidebar_button"

                textbutton "⏻   Exit":
                    action Quit(confirm=False)
                    style "v06_sidebar_button"

            add "images/ui/polish/separator.png":
                xpos 8
                ypos 610
                zoom 0.50

            text "v0.6 • Portfolio Build":
                xpos 16
                ypos 635
                size 13
                color "#718a95"

            text "Sandbox systems • UI • tooling":
                xpos 16
                ypos 657
                size 12
                color "#516b77"

    # cyan divider
    add Solid("#00c8ff"):
        xpos 328
        ypos 0
        xsize 2
        ysize 720

    # TOP FEATURE STRIP
    frame:
        xpos 360
        ypos 18
        xsize 880
        ysize 64
        background Solid("#03090eb8")
        padding (18, 9)

        hbox:
            spacing 38
            xalign 0.5

            vbox:
                text "SANDBOX" size 13 color "#00c8ff" xalign 0.5
                text "Free navigation" size 12 color "#c7d3d8"

            vbox:
                text "RELATIONSHIPS" size 13 color "#00c8ff" xalign 0.5
                text "Love / Hatred" size 12 color "#c7d3d8"

            vbox:
                text "EVENTS" size 13 color "#00c8ff" xalign 0.5
                text "Conditional chains" size 12 color "#c7d3d8"

            vbox:
                text "TOOLING" size 13 color "#00c8ff" xalign 0.5
                text "F2 Inspector" size 12 color "#c7d3d8"

    # AYA SHOWCASE CARD
    add "images/characters/aya/aya_smile.png":
        xpos 405
        ypos 80
        zoom 0.69
        at v06_float

    # Right-side pitch
    frame:
        xpos 840
        ypos 180
        xsize 370
        ysize 330
        background Solid("#02080cc4")
        padding (28, 24)
        at v06_panel_in

        vbox:
            spacing 13

            text "A DIRECTLY RELEVANT SAMPLE":
                size 14
                bold True
                color "#00c8ff"

            text "Nightfall Village":
                size 30
                bold True
                color "#ffffff"

            text "A compact Ren'Py sandbox demo focused on the same development problems a large branching VN needs.":
                size 17
                color "#becbd1"
                line_spacing 4

            null height 4

            text "◆ NPC schedules" size 16 color "#d9edf3"
            text "◆ Relationship routes" size 16 color "#d9edf3"
            text "◆ Event requirements" size 16 color "#d9edf3"
            text "◆ Progression + inventory" size 16 color "#d9edf3"
            text "◆ Developer event inspector" size 16 color "#d9edf3"

            null height 5

            textbutton "PLAY AYA DEMO  →":
                action Start("v06_aya_demo_start")
                style "v06_small_button"

    # footer tag
    frame:
        xpos 800
        ypos 625
        background Solid("#020609ce")
        padding (18, 10)

        text "Original art direction • Ren'Py + Python":
            size 14
            color "#8aa5b0"


# ------------------------------------------------------------
# HUD button
# ------------------------------------------------------------

screen v06_hud_icon(icon_path, label, act):
    vbox:
        spacing 2

        button:
            xsize 55
            ysize 55
            background Solid("#03080cdc")
            hover_background Solid("#073b4eee")
            action act

            add icon_path:
                xalign 0.5
                yalign 0.5
                zoom 0.50

        text label:
            size 10
            xalign 0.5
            color "#a7bac2"


# ------------------------------------------------------------
# HUD
# ------------------------------------------------------------

screen v06_hud():
    zorder 120

    if renpy.get_screen("main_menu") is None and renpy.get_screen("developer_tools") is None:
        frame:
            xpos 18
            ypos 12
            background Solid("#02070bc8")
            padding (8, 6)

            hbox:
                spacing 8
                use v06_hud_icon("images/ui/icons/icon_map.png", "MAP", Jump("map"))
                use v06_hud_icon("images/ui/icons/icon_characters.png", "PEOPLE", Show("characters_screen"))
                use v06_hud_icon("images/ui/icons/icon_inventory.png", "ITEMS", Show("inventory_screen"))
                use v06_hud_icon("images/ui/icons/icon_missions.png", "EVENTS", Show("gallery_screen"))
                use v06_hud_icon("images/ui/icons/icon_guide.png", "GUIDE", Show("guide_screen"))

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

        # compact status bars on the right
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
                        add Solid("#ff4d82") xsize int(150 * relation("aya","love") / 10.0) ysize 8
                    text "[relation('aya','love')]" size 12 color "#d8e6eb" xoffset 8


# ------------------------------------------------------------
# Dialogue: fixed bottom + character portrait + utility rail
# ------------------------------------------------------------

screen say(who, what):
    zorder 250

    # speaker portrait
    if who == "Aya":
        add "images/characters/aya/aya_portrait.png":
            xpos 32
            ypos 520
            zoom 0.72

    window:
        id "window"
        xpos 150
        ypos 536
        xsize 965
        ysize 154
        background Solid("#03070aef")

        fixed:
            xfill True
            yfill True

            add Solid("#00c8ff") xpos 0 ypos 0 xsize 965 ysize 2
            add Solid("#00c8ff55") xpos 0 ypos 2 xsize 2 ysize 152

            if who:
                text who:
                    id "who"
                    xpos 28
                    ypos 16
                    size 23
                    bold True
                    color "#00d8ff"

            text what:
                id "what"
                xpos 28
                ypos 51
                xmaximum 885
                size 23
                color "#f4f7f8"
                line_spacing 4

            text "⌄":
                xpos 915
                ypos 108
                size 24
                color "#8de9ff"

    # utility rail
    frame:
        xpos 1122
        ypos 536
        xsize 138
        ysize 154
        background Solid("#03070aef")
        padding (11, 8)

        vbox:
            spacing 2
            textbutton "AUTO" action Preference("auto-forward", "toggle") style "v06_small_button"
            textbutton "SKIP" action Skip() style "v06_small_button"
            textbutton "SAVE" action ShowMenu("save") style "v06_small_button"
            textbutton "Q.SAVE" action QuickSave() style "v06_small_button"
            textbutton "PREF." action ShowMenu("preferences") style "v06_small_button"


screen choice(items):
    zorder 260

    vbox:
        xalign 0.63
        yalign 0.50
        spacing 9

        for i in items:
            textbutton i.caption:
                action i.action
                style "v06_choice"


# ------------------------------------------------------------
# World map polish
# ------------------------------------------------------------

screen world_map():
    tag menu
    modal True

    add "images/ui/village_night_bg.png"
    add Solid("#02070a63")
    add SnowBlossom("images/ui/polish/petal.png", count=9, border=50, xspeed=(-12, 15), yspeed=(18, 36), start=2)

    # left navigation identity
    frame:
        xpos 18
        ypos 94
        xsize 300
        ysize 570
        background Solid("#02080dde")
        padding (22, 18)

        vbox:
            spacing 14
            text "VILLAGE MAP" size 28 bold True color "#ffffff"
            text "{} • Day {}".format(period_name(), day) size 15 color "#00c8ff"
            text "Choose a district. Character availability and events change with time." size 14 color "#9bb0b9" line_spacing 3

            null height 5
            text "CURRENT OBJECTIVE" size 12 bold True color "#e1b86a"

            $ _objectives = guide_objectives()
            if _objectives:
                $ _cat, _obj = _objectives[0]
                text _cat size 16 color "#ffffff"
                text _obj size 14 color "#aebdc4" line_spacing 3

            null height 8
            textbutton "RELATIONSHIPS" action Show("characters_screen") style "v06_small_button"
            textbutton "EVENT LOG" action Show("gallery_screen") style "v06_small_button"
            textbutton "DEV INSPECTOR • F2" action Show("developer_tools") style "v06_small_button"

    # map cards
    grid 2 4:
        xpos 345
        ypos 112
        spacing 12

        for location_id in LOCATION_ORDER:
            $ loc = LOCATION_DATA[location_id]
            $ unlocked = is_location_unlocked(location_id)
            $ residents = residents_at(location_id)
            $ event_ready = location_has_event(location_id)

            button:
                style "v06_card_button"
                xsize 435
                ysize 125
                sensitive unlocked
                action Jump(loc["label"])

                fixed:
                    xfill True
                    yfill True

                    text loc["icon"]:
                        xpos 4
                        ypos 15
                        size 34
                        color ("#00c8ff" if unlocked else "#3b4b52")

                    text loc["name"]:
                        xpos 62
                        ypos 8
                        size 21
                        bold True
                        color ("#ffffff" if unlocked else "#5e6b71")

                    if event_ready and unlocked:
                        frame:
                            xpos 322
                            ypos 5
                            background Solid("#00bfe8")
                            padding (7, 3)
                            text "EVENT" size 10 bold True color "#001018"

                    if unlocked:
                        text (residents if residents else "No known character here"):
                            xpos 62
                            ypos 42
                            size 13
                            color ("#7fe8ff" if residents else "#75878f")

                        text loc["description"]:
                            xpos 62
                            ypos 67
                            xmaximum 350
                            size 12
                            color "#9cabb2"
                    else:
                        text "LOCKED":
                            xpos 62
                            ypos 48
                            size 13
                            color "#68747a"


# ------------------------------------------------------------
# Relationship screen polish
# ------------------------------------------------------------

screen characters_screen(close_action=Hide("characters_screen")):
    modal True
    zorder 210

    add "images/ui/village_night_bg.png"
    add Solid("#010609d8")

    frame:
        xpos 80
        ypos 70
        xsize 1120
        ysize 590
        background Solid("#03090ef0")
        padding (28, 24)

        hbox:
            spacing 24

            # Aya visual panel
            frame:
                xsize 410
                ysize 535
                background Solid("#07131ad6")
                padding (12, 12)

                fixed:
                    add "images/characters/aya/aya_neutral.png":
                        xpos -25
                        ypos -40
                        zoom 0.63

                    frame:
                        xpos 14
                        ypos 390
                        xsize 355
                        ysize 115
                        background Solid("#02070ae8")
                        padding (15, 10)

                        vbox:
                            text "AYA" size 27 bold True color "#00d6ff"
                            text "Route: {}".format(dominant_route("aya")) size 15 color "#ffffff"
                            text "Love {}   •   Hatred {}".format(relation("aya","love"), relation("aya","hatred")) size 15 color "#b8c8cf"

            vbox:
                xsize 615
                spacing 16

                hbox:
                    xfill True
                    vbox:
                        text "RELATIONSHIPS" size 33 bold True color "#ffffff"
                        text "Current state, route direction and schedule." size 14 color "#8fa6b0"
                    textbutton "CLOSE" action close_action style "v06_small_button" xalign 1.0

                add "images/ui/polish/separator.png"

                text "AYA" size 22 bold True color "#00c8ff"
                text CHARACTER_DATA["aya"]["description"] size 16 color "#c1ced3" line_spacing 3

                $ _loc = npc_location("aya")
                $ _loc_name = LOCATION_DATA[_loc]["name"] if _loc else "Unavailable"
                text "Current schedule: {}".format(_loc_name) size 15 color "#ffffff"

                text "LOVE" size 12 bold True color "#ff5c8f"
                fixed:
                    xsize 560
                    ysize 12
                    add Solid("#311923") xsize 560 ysize 12
                    add Solid("#ff4d82") xsize int(560 * relation("aya","love") / 10.0) ysize 12

                text "HATRED" size 12 bold True color "#cf7cff"
                fixed:
                    xsize 560
                    ysize 12
                    add Solid("#24182d") xsize 560 ysize 12
                    add Solid("#a76bdf") xsize int(560 * relation("aya","hatred") / 10.0) ysize 12

                null height 6
                text "NEXT HINT" size 12 bold True color "#e1b86a"
                $ _goals = guide_objectives()
                for _cat, _goal in _goals[:2]:
                    text "• {}".format(_goal) size 14 color "#a9bac2"

                null height 10
                textbutton "PLAY AYA STORY DEMO":
                    action [Hide("characters_screen"), Start("v06_aya_demo_start")]
                    style "v06_small_button"


# ------------------------------------------------------------
# Save / load polish
# ------------------------------------------------------------

screen save():
    tag menu
    use v06_file_screen("SAVE GAME", "save")

screen load():
    tag menu
    use v06_file_screen("LOAD GAME", "load")

screen v06_file_screen(title, mode):
    add "images/ui/village_night_bg.png"
    add Solid("#020609c8")

    frame:
        xpos 60
        ypos 35
        xsize 1160
        ysize 650
        background Solid("#03090ef2")
        padding (28, 24)

        vbox:
            spacing 18

            hbox:
                xfill True
                vbox:
                    text title size 38 bold True color "#00c8ff"
                    text "Six clean portfolio demo slots" size 14 color "#859aa3"
                textbutton "BACK" action Return() style "v06_small_button" xalign 1.0

            grid 3 2:
                spacing 14

                for slot in range(1, 7):
                    button:
                        xsize 345
                        ysize 235
                        background Solid("#07141bdc")
                        hover_background Solid("#0a3444ec")
                        action (FileSave(slot) if mode == "save" else FileLoad(slot))

                        fixed:
                            xfill True
                            yfill True

                            add Solid("#00c8ff33"):
                                xpos 0
                                ypos 0
                                xsize 345
                                ysize 2

                            text "SLOT [slot]":
                                xpos 18
                                ypos 17
                                size 20
                                bold True
                                color "#ffffff"

                            text FileTime(slot, format="%d/%m/%Y • %H:%M", empty="EMPTY SLOT"):
                                xpos 18
                                ypos 50
                                size 13
                                color "#8eb2c0"

                            if FileTime(slot, empty="") != "":
                                text "Saved progression":
                                    xpos 18
                                    ypos 92
                                    size 13
                                    color "#c5d2d7"

                                text "Click to {}".format("overwrite" if mode == "save" else "continue"):
                                    xpos 18
                                    ypos 175
                                    size 13
                                    color "#00c8ff"
                            else:
                                text "No save data":
                                    xpos 18
                                    ypos 110
                                    size 14
                                    color "#5f747d"


# ------------------------------------------------------------
# Notification polish
# ------------------------------------------------------------

screen notify(message):
    zorder 420

    frame:
        xpos 895
        ypos 92
        xsize 335
        background Solid("#03090ef4")
        padding (16, 11)
        at v06_soft_in

        hbox:
            spacing 10
            text "◆" size 18 color "#00c8ff"
            vbox:
                text "PROGRESSION UPDATE" size 10 bold True color "#00c8ff"
                text message size 15 color "#ffffff"

    timer 3.0 action Hide("notify")


# ------------------------------------------------------------
# Overlay registration
# ------------------------------------------------------------

init 1000 python:
    for _old in ("hud", "hos_hud", "hos_quick_menu"):
        while _old in config.overlay_screens:
            config.overlay_screens.remove(_old)

    if "v06_hud" not in config.overlay_screens:
        config.overlay_screens.append("v06_hud")