# ============================================================
# NIGHTFALL VILLAGE — PRESENTATION/UI v0.3
# Original visual identity. No third-party game assets are used.
# ============================================================

# ------------------------------------------------------------
# STYLES
# ------------------------------------------------------------

style nv_panel:
    background Solid("#071018ee")
    xpadding 24
    ypadding 20

style nv_title:
    size 42
    bold True
    color "#f2f6f8"

style nv_subtitle:
    size 18
    color "#91a7b5"

style nv_accent:
    color "#e1b86a"

style nv_button is button:
    background Solid("#0f1c27e8")
    hover_background Solid("#17364be8")
    selected_background Solid("#1f4d63e8")
    xpadding 20
    ypadding 13
    xminimum 220

style nv_button_text is button_text:
    size 20
    color "#dce9ef"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5

style nv_primary_button is button:
    background Solid("#b78b3ce8")
    hover_background Solid("#d0a85be8")
    xpadding 22
    ypadding 14
    xminimum 300

style nv_primary_button_text is button_text:
    size 21
    bold True
    color "#081018"
    xalign 0.5

style nv_small_button is button:
    background Solid("#102330e8")
    hover_background Solid("#1b455be8")
    xpadding 12
    ypadding 8

style nv_small_button_text is button_text:
    size 16
    color "#d7e5eb"
    hover_color "#ffffff"

style nv_card is button:
    background Solid("#08141ddd")
    hover_background Solid("#112d3bdd")
    insensitive_background Solid("#080c10bb")
    xpadding 18
    ypadding 14

style nv_card_text is button_text:
    color "#eef7fa"
    hover_color "#ffffff"

style bar:
    ysize 12
    left_bar Solid("#e1b86a")
    right_bar Solid("#20303a")

style vbar:
    xsize 12
    top_bar Solid("#e1b86a")
    bottom_bar Solid("#20303a")

# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/ui/main_menu_bg.png"
    add Solid("#02070b33")

    frame:
        background Solid("#050d14e8")
        xalign 0.075
        yalign 0.5
        xsize 470
        ysize 600
        padding (38, 34)

        vbox:
            spacing 12

            text "NIGHTFALL" size 58 bold True color "#f6f8fa"
            text "VILLAGE" size 34 bold True color "#e1b86a"
            text "SHINOBI SANDBOX SYSTEMS DEMO" size 15 color "#8fb8c8"

            null height 16

            text "A Ren'Py + Python portfolio build focused on nonlinear events, schedules, relationship routes and developer tooling.":
                size 18
                color "#b9c8cf"
                xmaximum 380

            null height 16

            textbutton "NEW GAME" action Start() style "nv_primary_button"
            textbutton "CONTINUE / LOAD" action ShowMenu("load") style "nv_button"
            textbutton "SETTINGS" action ShowMenu("preferences") style "nv_button"
            textbutton "QUIT" action Quit(confirm=False) style "nv_button"

            null height 12

            text "BUILD 0.3.0  •  ORIGINAL PORTFOLIO DEMO" size 13 color "#718894"

    frame:
        background Solid("#071018bb")
        xalign 0.96
        yalign 0.95
        padding (16, 10)

        text "SANDBOX • LOVE / HATRED • LIVING WORLD • EVENT INSPECTOR" size 13 color "#d8c08c"

# ------------------------------------------------------------
# SAY / CHOICE — dialogue stays at the bottom
# ------------------------------------------------------------

screen say(who, what):
    window:
        id "window"
        style "nv_say_window"

        vbox:
            spacing 8

            if who:
                frame:
                    background Solid("#b78b3cee")
                    xpadding 16
                    ypadding 5

                    text who:
                        id "who"
                        style "nv_say_who"

            text what:
                id "what"
                style "nv_say_what"

style nv_say_window:
    xalign 0.5
    yalign 0.985
    xsize 1200
    yminimum 158
    background Solid("#050c12f2")
    xpadding 28
    ypadding 17

style nv_say_who:
    size 23
    bold True
    color "#071018"

style nv_say_what:
    size 24
    color "#edf4f7"
    xmaximum 1120
    line_spacing 4

screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.62
        spacing 9

        for i in items:
            textbutton i.caption:
                action i.action
                style "nv_choice_button"

style nv_choice_button is button:
    xsize 760
    yminimum 52
    background Solid("#091722ee")
    hover_background Solid("#17445aee")
    xpadding 22
    ypadding 11

style nv_choice_button_text is button_text:
    xalign 0.5
    size 20
    color "#e7f1f5"
    hover_color "#ffffff"

screen notify(message):
    zorder 350

    frame at slow_float:
        background Solid("#0a1a24f2")
        xalign 0.98
        yalign 0.11
        xmaximum 420
        padding (18, 12)

        text message size 17 color "#e9f2f5"

    timer 2.8 action Hide("notify")

screen confirm(message, yes_action, no_action):
    modal True
    zorder 400

    add Solid("#000b")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 620
        ysize 280

        vbox:
            spacing 22
            text message size 23 xalign 0.5 text_align 0.5

            hbox:
                xalign 0.5
                spacing 18
                textbutton "YES" action yes_action style "nv_primary_button"
                textbutton "NO" action no_action style "nv_button"

screen skip_indicator():
    zorder 360

    frame:
        background Solid("#071018dd")
        xalign 0.02
        yalign 0.11
        padding (12, 7)

        text "SKIPPING »" size 15 color "#e1b86a"

# ------------------------------------------------------------
# HUD
# ------------------------------------------------------------

screen hud():
    zorder 100

    if renpy.get_screen("main_menu") is None and renpy.get_screen("developer_tools") is None:
        frame:
            background Solid("#050d14e8")
            xalign 0.5
            yalign 0.012
            xsize 1220
            ysize 58
            padding (16, 9)

            hbox:
                xfill True
                spacing 20

                text "DAY [day]" size 17 color "#e1b86a"
                text period_name().upper() size 17 color "#f2f6f8"
                text "ENERGY [energy]/4" size 16 color "#98cfe4"
                text "STR [strength]" size 16
                text "REP [reputation]" size 16
                text "COINS [coins]" size 16 color "#e1b86a"

                null width 50

                textbutton "GUIDE" action Show("guide_screen") style "nv_small_button"
                textbutton "RELATIONS" action Show("characters_screen") style "nv_small_button"
                textbutton "BAG" action Show("inventory_screen") style "nv_small_button"
                textbutton "DEV • F2" action Show("developer_tools") style "nv_small_button"

# ------------------------------------------------------------
# WORLD MAP
# ------------------------------------------------------------

screen world_map():
    tag menu
    modal True

    add "images/ui/map_bg.png"
    add Solid("#02080d66")

    frame:
        background Solid("#050d14ea")
        xalign 0.5
        yalign 0.08
        xsize 1180
        ysize 88
        padding (24, 14)

        hbox:
            xfill True

            vbox:
                spacing 2
                text "NIGHTFALL VILLAGE" size 31 bold True
                text "Choose a location. Time advances when you perform an action." size 15 color "#8fa7b3"

            null width 100

            vbox:
                xalign 1.0
                text "DAY {} • {}".format(day, period_name().upper()) size 18 color "#e1b86a" xalign 1.0
                text "Energy [energy]/4   •   Coins [coins]" size 15 xalign 1.0

    grid 2 4:
        xalign 0.5
        yalign 0.54
        spacing 16

        for location_id in LOCATION_ORDER:
            $ loc = LOCATION_DATA[location_id]
            $ unlocked = is_location_unlocked(location_id)
            $ residents = residents_at(location_id)
            $ event_ready = location_has_event(location_id)

            button:
                style "nv_card"
                xsize 565
                ysize 112
                sensitive unlocked
                action Jump(loc["label"])

                hbox:
                    spacing 16
                    yalign 0.5

                    frame:
                        background Solid("#b78b3cdd" if unlocked else "#26323acc")
                        xsize 62
                        ysize 62
                        xalign 0.5
                        yalign 0.5

                        text loc["icon"]:
                            size 31
                            color ("#071018" if unlocked else "#66757d")
                            xalign 0.5
                            yalign 0.5

                    vbox:
                        spacing 4
                        xsize 430

                        hbox:
                            spacing 10
                            text loc["name"] size 23 bold True color ("#f3f7f9" if unlocked else "#65727a")

                            if event_ready and unlocked:
                                text "EVENT" size 13 bold True color "#e1b86a"

                        if unlocked:
                            text loc["description"] size 14 color "#9fb2bc"
                            if residents:
                                text "Available now: [residents]" size 13 color "#7fd0e8"
                        else:
                            text "LOCKED — progress another storyline to discover this area." size 14 color "#68747b"

    frame:
        background Solid("#050d14e8")
        xalign 0.5
        yalign 0.955
        xsize 1180
        ysize 62
        padding (16, 9)

        hbox:
            xalign 0.5
            spacing 12

            textbutton "INTERACTIVE GUIDE" action Show("guide_screen") style "nv_small_button"
            textbutton "RELATIONSHIPS" action Show("characters_screen") style "nv_small_button"
            textbutton "INVENTORY" action Show("inventory_screen") style "nv_small_button"
            textbutton "EVENT LOG" action Show("gallery_screen") style "nv_small_button"
            textbutton "SAVE" action ShowMenu("save") style "nv_small_button"
            textbutton "LOAD" action ShowMenu("load") style "nv_small_button"
            textbutton "DEV TOOLS" action Show("developer_tools") style "nv_small_button"

# ------------------------------------------------------------
# MODAL PANELS
# ------------------------------------------------------------

screen guide_screen(close_action=Hide("guide_screen")):
    modal True
    zorder 220

    add Solid("#000a")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 590

        vbox:
            spacing 14

            hbox:
                xfill True
                text "INTERACTIVE GUIDE" style "nv_title"
                textbutton "CLOSE" action close_action style "nv_small_button" xalign 1.0

            text "Spoiler-light objectives generated from your current save state." style "nv_subtitle"

            frame:
                background Solid("#0d1a23cc")
                xfill True
                padding (18, 14)

                hbox:
                    spacing 18
                    text "EVENT PROGRESS" size 16 color "#e1b86a"
                    bar value completion_count() range len(EVENT_DATA) xmaximum 420
                    text "{}%".format(completion_percent()) size 16

            viewport:
                ymaximum 390
                mousewheel True
                draggable True

                vbox:
                    spacing 12

                    for category, objective in guide_objectives():
                        frame:
                            background Solid("#0b1720dd")
                            xfill True
                            padding (16, 12)

                            vbox:
                                spacing 4
                                text category size 16 bold True color "#e1b86a"
                                text objective size 18 color "#e4edf1"

screen characters_screen():
    modal True
    zorder 220

    add Solid("#000a")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 920
        ysize 610

        vbox:
            spacing 14

            hbox:
                xfill True
                text "RELATIONSHIPS" style "nv_title"
                textbutton "CLOSE" action Hide("characters_screen") style "nv_small_button" xalign 1.0

            text "Route values influence dialogue, event requirements, and later story branches." style "nv_subtitle"

            for cid in ("aya", "ren"):
                $ data = CHARACTER_DATA[cid]
                $ current_loc = npc_location(cid)
                $ current_loc_name = LOCATION_DATA[current_loc]["name"] if current_loc else "Unavailable"
                $ love_value = relation(cid, "love")
                $ hatred_value = relation(cid, "hatred")
                $ route_name = dominant_route(cid).upper()

                frame:
                    background Solid("#0b1720dd")
                    xfill True
                    padding (18, 14)

                    vbox:
                        spacing 8

                        hbox:
                            xfill True
                            text data["name"] size 27 bold True
                            text "ROUTE: [route_name]" size 16 color "#e1b86a" xalign 1.0

                        text data["description"] size 15 color "#9fb1ba"

                        hbox:
                            spacing 12
                            text "LOVE [love_value]/10" size 15 color "#ff9db6"
                            bar value love_value range 10 xmaximum 260

                        hbox:
                            spacing 12
                            text "HATRED [hatred_value]/10" size 15 color "#8fcfff"
                            bar value hatred_value range 10 xmaximum 260

                        text "Current schedule: [current_loc_name]" size 14 color "#82c7df"

            frame:
                background Solid("#0b1720dd")
                xfill True
                padding (18, 12)

                text "Sora Trust: [sora_trust]/3   •   Appears in Market Alley at Night after introduction." size 16

screen inventory_screen():
    modal True
    zorder 220

    add Solid("#000a")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 720
        ysize 520

        vbox:
            spacing 14

            hbox:
                xfill True
                text "INVENTORY" style "nv_title"
                textbutton "CLOSE" action Hide("inventory_screen") style "nv_small_button" xalign 1.0

            text "Coins: [coins]" size 20 color "#e1b86a"

            viewport:
                ymaximum 340
                mousewheel True
                draggable True

                vbox:
                    spacing 9

                    for line in inventory_lines():
                        frame:
                            background Solid("#0b1720dd")
                            xfill True
                            padding (15, 10)
                            text line size 19

screen gallery_screen(close_action=Hide("gallery_screen")):
    modal True
    zorder 220

    add Solid("#000a")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 920
        ysize 610

        vbox:
            spacing 12

            hbox:
                xfill True
                text "EVENT LOG" style "nv_title"
                textbutton "CLOSE" action close_action style "nv_small_button" xalign 1.0

            $ _done_count = completion_count()
            $ _total_count = len(EVENT_DATA)
            $ _done_percent = completion_percent()
            text "[_done_count] / [_total_count] story events discovered — [_done_percent]% complete." style "nv_subtitle"

            viewport:
                ymaximum 440
                mousewheel True
                draggable True

                vbox:
                    spacing 8

                    for ev in EVENT_DATA:
                        $ done = seen_events.get(ev["id"], False)

                        frame:
                            background Solid("#10251ddd" if done else "#0b141bdd")
                            xfill True
                            padding (15, 10)

                            hbox:
                                xfill True
                                text ("✓" if done else "•") size 19 color ("#8fe3b1" if done else "#657681")
                                text ev["title"] size 18 color ("#eef4f6" if done else "#85939a")
                                text LOCATION_DATA[ev["location"]]["name"] size 14 color "#e1b86a" xalign 1.0

# ------------------------------------------------------------
# SAVE / LOAD / SETTINGS
# ------------------------------------------------------------

screen save():
    tag menu
    use file_panel("SAVE GAME", "save")

screen load():
    tag menu
    use file_panel("LOAD GAME", "load")

screen file_panel(title, mode):
    add "images/ui/main_menu_bg.png"
    add Solid("#02070bcc")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 980
        ysize 620

        vbox:
            spacing 16

            hbox:
                xfill True
                text title style "nv_title"
                textbutton "BACK" action Return() style "nv_small_button" xalign 1.0

            grid 2 3:
                spacing 14

                for slot in range(1, 7):
                    frame:
                        background Solid("#08141ddd")
                        xsize 450
                        ysize 125
                        padding (16, 12)

                        vbox:
                            spacing 7

                            hbox:
                                xfill True
                                text "SLOT [slot]" size 20 bold True color "#e1b86a"

                                if mode == "save":
                                    textbutton "SAVE" action FileSave(slot) style "nv_small_button" xalign 1.0
                                else:
                                    textbutton "LOAD" action FileLoad(slot) style "nv_small_button" xalign 1.0

                            text FileTime(slot, format="%d/%m/%Y  %H:%M", empty="EMPTY SLOT") size 15 color "#aebfc7"

                            if FileTime(slot, empty="") != "":
                                textbutton "DELETE SLOT" action FileDelete(slot) style "nv_small_button"

screen preferences():
    tag menu

    add "images/ui/main_menu_bg.png"
    add Solid("#02070bcc")

    frame:
        style "nv_panel"
        xalign 0.5
        yalign 0.5
        xsize 820
        ysize 580

        vbox:
            spacing 18

            hbox:
                xfill True
                text "SETTINGS" style "nv_title"
                textbutton "BACK" action Return() style "nv_small_button" xalign 1.0

            text "DISPLAY" size 16 color "#e1b86a"
            hbox:
                spacing 12
                textbutton "WINDOW" action Preference("display", "window") style "nv_button"
                textbutton "FULLSCREEN" action Preference("display", "fullscreen") style "nv_button"

            null height 8
            text "TEXT SPEED" size 16 color "#e1b86a"
            bar value Preference("text speed") xmaximum 600

            text "AUTO-FORWARD" size 16 color "#e1b86a"
            bar value Preference("auto-forward time") xmaximum 600

            text "MUSIC VOLUME" size 16 color "#e1b86a"
            bar value Preference("music volume") xmaximum 600

            text "SOUND VOLUME" size 16 color "#e1b86a"
            bar value Preference("sound volume") xmaximum 600

# ------------------------------------------------------------
# DEVELOPER TOOLS / EVENT INSPECTOR
# ------------------------------------------------------------

screen developer_tools():
    modal True
    zorder 300

    add Solid("#000c")

    frame:
        background Solid("#050d14f8")
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 660
        padding (24, 20)

        vbox:
            spacing 12

            hbox:
                xfill True

                vbox:
                    spacing 2
                    text "DEVELOPER TOOLS" size 36 bold True color "#f3f7f9"
                    text "Live progression controls + event requirement inspector" size 15 color "#88a6b3"

                textbutton "CLOSE • F2" action Hide("developer_tools") style "nv_small_button" xalign 1.0

            hbox:
                spacing 18

                frame:
                    background Solid("#0b1720dd")
                    xsize 420
                    ysize 520
                    padding (18, 15)

                    viewport:
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 12

                            text "WORLD STATE" size 18 bold True color "#e1b86a"

                            hbox:
                                spacing 8
                                text "Day [day]" xminimum 145
                                textbutton "-1" action Function(debug_change_day, -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_day, 1) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Time {}".format(period_name()) xminimum 145
                                textbutton "◀" action Function(debug_change_period, -1) style "nv_small_button"
                                textbutton "▶" action Function(debug_change_period, 1) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Energy [energy]" xminimum 145
                                textbutton "-1" action Function(debug_change_energy, -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_energy, 1) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Coins [coins]" xminimum 145
                                textbutton "-10" action Function(debug_change_coins, -10) style "nv_small_button"
                                textbutton "+10" action Function(debug_change_coins, 10) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Strength [strength]" xminimum 145
                                textbutton "-1" action Function(debug_change_stat, "strength", -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_stat, "strength", 1) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Reputation [reputation]" xminimum 145
                                textbutton "-1" action Function(debug_change_stat, "reputation", -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_stat, "reputation", 1) style "nv_small_button"

                            text "AYA ROUTE" size 18 bold True color "#e1b86a"

                            hbox:
                                spacing 8
                                text "Love {}".format(relation("aya", "love")) xminimum 145
                                textbutton "-1" action Function(debug_change_relation, "aya", "love", -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_relation, "aya", "love", 1) style "nv_small_button"

                            hbox:
                                spacing 8
                                text "Hatred {}".format(relation("aya", "hatred")) xminimum 145
                                textbutton "-1" action Function(debug_change_relation, "aya", "hatred", -1) style "nv_small_button"
                                textbutton "+1" action Function(debug_change_relation, "aya", "hatred", 1) style "nv_small_button"

                            text "TOOLS" size 18 bold True color "#e1b86a"

                            textbutton "+ Silver Charm" action Function(debug_add_item, "Silver Charm") style "nv_button"
                            textbutton "+ Moon Token" action Function(debug_add_item, "Moon Token") style "nv_button"
                            textbutton "Toggle Aya House" action Function(debug_toggle_location, "aya_house") style "nv_button"
                            textbutton "Toggle Old Shrine" action Function(debug_toggle_location, "old_shrine") style "nv_button"
                            textbutton "Toggle Archive" action Function(debug_toggle_location, "archive") style "nv_button"

                frame:
                    background Solid("#0b1720dd")
                    xsize 680
                    ysize 520
                    padding (18, 15)

                    vbox:
                        spacing 10
                        text "EVENT INSPECTOR" size 18 bold True color "#e1b86a"
                        text "Shows why every story event is available or blocked right now." size 14 color "#8fa8b4"

                        viewport:
                            ymaximum 440
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 8

                                for title, location, reason, event_label in event_debug_rows():
                                    $ available = reason == "AVAILABLE"

                                    frame:
                                        background Solid("#123322dd" if available else "#111a20dd")
                                        xfill True
                                        padding (12, 9)

                                        vbox:
                                            spacing 3
                                            hbox:
                                                xfill True
                                                text title size 16 bold True color "#eef5f7"
                                                text ("READY" if available else "BLOCKED") size 12 bold True color ("#8fe3b1" if available else "#e29393") xalign 1.0
                                            text "[location] • [reason]" size 13 color "#9fb0b8"
                                            if available:
                                                textbutton "JUMP TO EVENT" action [Hide("developer_tools"), Jump(event_label)] style "nv_small_button"

screen debug_hotkey():
    key "K_F2" action Show("developer_tools")

init python:
    for overlay in ("hud", "debug_hotkey"):
        if overlay not in config.overlay_screens:
            config.overlay_screens.append(overlay)
