# ============================================================
# NIGHTFALL VILLAGE v0.9 — VISUAL WORLD OVERHAUL
# ============================================================
# Portfolio-focused presentation pass:
# - cinematic world hub
# - destination cards with live state
# - location atmosphere/chrome
# - stronger hierarchy and readability
# - current objective + character/event presence
# ============================================================


default current_location_id = None


init python:

    V09_LOCATION_VISUALS = {
        "home": {
            "tag": "SAFEHOUSE",
            "thumb": "images/ui/home_bg.png",
            "accent": "#78d9ff",
            "mood": "Rest, plan and review your progress.",
        },
        "square": {
            "tag": "SOCIAL HUB",
            "thumb": "images/ui/square_bg.png",
            "accent": "#00d7ff",
            "mood": "Stories cross here as schedules change.",
        },
        "training": {
            "tag": "TRAINING",
            "thumb": "images/ui/training_bg.png",
            "accent": "#63e8ac",
            "mood": "Raise Strength and meet Ren during the day.",
        },
        "market": {
            "tag": "COMMERCE",
            "thumb": "images/ui/market_bg.png",
            "accent": "#e7bd68",
            "mood": "Supplies by day. Secrets after dark.",
        },
        "riverside": {
            "tag": "QUIET DISTRICT",
            "thumb": "images/ui/riverside_bg.png",
            "accent": "#7edcff",
            "mood": "Private conversations and hidden discoveries.",
        },
        "aya_house": {
            "tag": "HOUSEHOLD",
            "thumb": "images/ui/aya_house_bg.png",
            "accent": "#ff7ea7",
            "mood": "Relationship-gated scenes with Aya.",
        },
        "old_shrine": {
            "tag": "OUTSKIRTS",
            "thumb": "images/ui/old_shrine_bg.png",
            "accent": "#c48cff",
            "mood": "A forgotten path with late-game clues.",
        },
        "archive": {
            "tag": "SECRET AREA",
            "thumb": "images/ui/archive_bg.png",
            "accent": "#a98cff",
            "mood": "Route-reactive secrets beneath the village.",
        },
    }

    V09_OUTDOOR_LOCATIONS = (
        "square", "training", "market", "riverside", "old_shrine"
    )

    def v09_visual(location_id):
        return V09_LOCATION_VISUALS.get(location_id, {
            "tag": "DISTRICT",
            "thumb": "images/ui/village_night_bg.png",
            "accent": "#00c8ff",
            "mood": "Explore Nightfall Village.",
        })

    def v09_location_accent(location_id):
        return v09_visual(location_id)["accent"]

    def v09_location_thumb(location_id):
        return v09_visual(location_id)["thumb"]

    def v09_location_tag(location_id):
        return v09_visual(location_id)["tag"]

    def v09_location_mood(location_id):
        return v09_visual(location_id)["mood"]

    def v09_period_tint():
        p = period_name()
        if p == "Morning":
            return "#08233616"
        if p == "Afternoon":
            return "#0b253016"
        if p == "Evening":
            return "#160f3022"
        return "#0107102e"

    def v09_primary_objective():
        rows = guide_objectives()
        if not rows:
            return ("FREE ROAM", "Explore the village and discover new events.")
        return rows[0]

    def v09_location_status(location_id):
        if not is_location_unlocked(location_id):
            return ("LOCKED", "#687880")
        if location_has_event(location_id):
            return ("NEW EVENT", "#e7bd68")
        residents = residents_at(location_id)
        if residents:
            return ("CHARACTER HERE", "#59e6a1")
        return ("OPEN", "#00c8ff")


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------

style v09_nav_button is button:
    background None
    hover_background Solid("#0a3546e8")
    xsize 282
    yminimum 43
    xpadding 16
    ypadding 7

style v09_nav_button_text is button_text:
    size 18
    color "#aebfc6"
    hover_color "#ffffff"

style v09_hub_card is button:
    background Solid("#040b10e9")
    hover_background Solid("#092b39f2")
    insensitive_background Solid("#03070acb")
    xpadding 0
    ypadding 0

style v09_hub_card_text is button_text:
    color "#ffffff"

style v09_small_button is button:
    background Solid("#071922ef")
    hover_background Solid("#0a4055ef")
    xpadding 14
    ypadding 8

style v09_small_button_text is button_text:
    size 13
    color "#d1e5eb"
    hover_color "#ffffff"


# ------------------------------------------------------------
# Disable older floating menu additions.
# ------------------------------------------------------------

screen v07_main_menu_addon():
    pass


# ------------------------------------------------------------
# v0.9 MAIN MENU
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#01060a62")
    add SnowBlossom("images/ui/polish/petal.png", count=15, border=65, xspeed=(-18, 18), yspeed=(20, 45), start=3)

    # LEFT NAVIGATION
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
                xpos 33
                ypos 154
                size 10
                bold True
                color "#00d4ff"

            vbox:
                xpos 0
                ypos 188
                spacing 2

                textbutton "▶   Continue":
                    action ShowMenu("load")
                    style "v09_nav_button"

                textbutton "▣   New Game":
                    action Start()
                    style "v09_nav_button"

                textbutton "◆   World Hub":
                    action Start()
                    style "v09_nav_button"

                textbutton "✦   Household Demo":
                    action Start("v07_house_demo_start")
                    style "v09_nav_button"

                textbutton "◇   Mission Control":
                    action Start("v08_mission_control_start")
                    style "v09_nav_button"

                textbutton "♥   Aya Story Demo":
                    action Start("v06_aya_demo_start")
                    style "v09_nav_button"

                textbutton "▤   Guide / Events":
                    action Show("guide_screen")
                    style "v09_nav_button"

                textbutton "⌘   Developer Tools":
                    action Show("developer_tools")
                    style "v09_nav_button"

                textbutton "⚙   Settings":
                    action ShowMenu("preferences")
                    style "v09_nav_button"

                textbutton "⏻   Exit":
                    action Quit(confirm=False)
                    style "v09_nav_button"

            add Solid("#00c8ff55"):
                xpos 9
                ypos 626
                xsize 270
                ysize 1

            text "v0.9.0 • Visual World Overhaul":
                xpos 13
                ypos 642
                size 12
                color "#93abb5"

            text "World hub • atmosphere • live state":
                xpos 13
                ypos 663
                size 11
                color "#5f7b86"

    add Solid("#00c8ff"):
        xpos 334
        ypos 0
        xsize 2
        ysize 720

    # TOP FEATURE STRIP
    frame:
        xpos 358
        ypos 18
        xsize 892
        ysize 64
        background Solid("#02090ed9")
        padding (18, 8)

        hbox:
            spacing 34
            xalign 0.5

            vbox:
                text "WORLD HUB" size 12 bold True color "#00c8ff" xalign 0.5
                text "Visual destinations" size 11 color "#c4d2d7"

            vbox:
                text "LIVE STATE" size 12 bold True color "#00c8ff" xalign 0.5
                text "NPCs + events" size 11 color "#c4d2d7"

            vbox:
                text "ATMOSPHERE" size 12 bold True color "#00c8ff" xalign 0.5
                text "Particles + chrome" size 11 color "#c4d2d7"

            vbox:
                text "SYSTEMS" size 12 bold True color "#00c8ff" xalign 0.5
                text "Time + routes" size 11 color "#c4d2d7"

            vbox:
                text "TOOLING" size 12 bold True color "#00c8ff" xalign 0.5
                text "F2 inspector" size 11 color "#c4d2d7"

    add "images/characters/aya/aya_smile.png":
        xpos 385
        ypos 78
        zoom 0.68
        at v06_float

    # RIGHT FEATURE CARD
    frame:
        xpos 820
        ypos 125
        xsize 405
        ysize 470
        background Solid("#02080ce5")
        padding (26, 22)
        at v06_panel_in

        vbox:
            spacing 10

            text "NEW IN v0.9" size 12 bold True color "#e4bd68"
            text "Visual World Overhaul" size 30 bold True color "#ffffff"
            text "The sandbox now presents locations as a living village instead of a flat prototype map." size 15 color "#bdcbd1" line_spacing 3

            null height 2
            text "◆ Cinematic destination hub" size 14 color "#dbeaf0"
            text "◆ Live character availability" size 14 color "#dbeaf0"
            text "◆ Event badges and lock states" size 14 color "#dbeaf0"
            text "◆ Current objective at a glance" size 14 color "#dbeaf0"
            text "◆ Per-location atmosphere layer" size 14 color "#dbeaf0"
            text "◆ Improved scene readability" size 14 color "#dbeaf0"

            null height 8

            textbutton "ENTER WORLD HUB  →":
                action Start()
                style "v09_small_button"

            textbutton "MISSION CONTROL":
                action Start("v08_mission_control_start")
                style "v09_small_button"

    frame:
        xpos 782
        ypos 610
        background Solid("#020609d8")
        padding (18, 9)

        text "Nightfall Village • Ren'Py + Python • Portfolio Build 0.9.0":
            size 13
            color "#8aa6b1"


# ------------------------------------------------------------
# v0.9 WORLD HUB
# ------------------------------------------------------------

screen world_map():
    tag menu
    modal True
    on "show" action SetVariable("current_location_id", None)

    add "images/ui/village_night_bg.png"
    add Solid("#01070b70")
    add SnowBlossom("images/ui/polish/petal.png", count=11, border=55, xspeed=(-14, 16), yspeed=(17, 34), start=2)

    # HEADER
    frame:
        xpos 18
        ypos 16
        xsize 1244
        ysize 68
        background Solid("#02080de9")
        padding (19, 9)

        hbox:
            xfill True

            vbox:
                text "NIGHTFALL VILLAGE" size 25 bold True color "#ffffff"
                text "WORLD HUB • choose a district" size 11 bold True color "#00d4ff"

            hbox:
                spacing 28
                xalign 1.0
                yalign 0.5

                vbox:
                    text "[period_name()]" size 15 bold True color "#ffffff" xalign 0.5
                    text "DAY [day]" size 10 color "#7f99a4" xalign 0.5

                vbox:
                    text "$[coins]" size 16 bold True color "#e5bd68" xalign 0.5
                    text "COINS" size 10 color "#7f99a4" xalign 0.5

                vbox:
                    text "[energy]/4" size 16 bold True color "#4adfff" xalign 0.5
                    text "ENERGY" size 10 color "#7f99a4" xalign 0.5

                vbox:
                    text "[reputation]" size 16 bold True color "#59e6a1" xalign 0.5
                    text "REPUTATION" size 10 color "#7f99a4" xalign 0.5

    # LEFT OBJECTIVE RAIL
    frame:
        xpos 18
        ypos 98
        xsize 292
        ysize 568
        background Solid("#02080de5")
        padding (20, 18)

        vbox:
            spacing 13

            text "CURRENT OBJECTIVE" size 11 bold True color "#e4bd68"

            $ _cat, _obj = v09_primary_objective()
            text _cat size 20 bold True color "#ffffff"
            text _obj size 14 color "#aebfc6" line_spacing 3

            add Solid("#00c8ff44") xsize 250 ysize 1

            text "VILLAGE STATUS" size 11 bold True color "#00c8ff"
            text "Characters move with the time cycle. Gold badges mark story events that can trigger now." size 13 color "#8fa6af" line_spacing 3

            null height 5

            frame:
                xfill True
                background Solid("#06131ad8")
                padding (12, 10)

                vbox:
                    spacing 5
                    text "AYA" size 12 bold True color "#ff7ea7"
                    text ("Available at " + (LOCATION_DATA[npc_location('aya')]['name'] if npc_location('aya') else 'another time')) size 12 color "#c7d5da"

            frame:
                xfill True
                background Solid("#06131ad8")
                padding (12, 10)

                vbox:
                    spacing 5
                    text "REN" size 12 bold True color "#63e8ac"
                    text ("Available at " + (LOCATION_DATA[npc_location('ren')]['name'] if npc_location('ren') else 'another time')) size 12 color "#c7d5da"

            null height 2

            textbutton "CHARACTERS":
                action Show("characters_screen")
                style "v09_small_button"

            textbutton "EVENT LOG":
                action Show("gallery_screen")
                style "v09_small_button"

            textbutton "DEVELOPER INSPECTOR • F2":
                action Show("developer_tools")
                style "v09_small_button"

            textbutton "MAIN MENU":
                action MainMenu(confirm=False)
                style "v09_small_button"

    # DESTINATION GRID
    grid 2 4:
        xpos 330
        ypos 99
        spacing 12

        for _location_id in LOCATION_ORDER:
            $ _loc = LOCATION_DATA[_location_id]
            $ _visual = v09_visual(_location_id)
            $ _unlocked = is_location_unlocked(_location_id)
            $ _residents = residents_at(_location_id)
            $ _status, _status_color = v09_location_status(_location_id)

            button:
                style "v09_hub_card"
                xsize 450
                ysize 132
                sensitive _unlocked
                action [SetVariable("current_location_id", _location_id), Jump(_loc["label"])]

                fixed:
                    xfill True
                    yfill True

                    add im.Scale(_visual["thumb"], 450, 132)
                    add Solid("#02070a9e")

                    # left accent
                    add Solid(_visual["accent"]):
                        xpos 0
                        ypos 0
                        xsize 3
                        ysize 132

                    text _visual["tag"]:
                        xpos 16
                        ypos 12
                        size 9
                        bold True
                        color _visual["accent"]

                    text _loc["name"]:
                        xpos 16
                        ypos 31
                        size 21
                        bold True
                        color ("#ffffff" if _unlocked else "#6f7e84")

                    text _visual["mood"]:
                        xpos 16
                        ypos 64
                        xmaximum 295
                        size 11
                        color ("#b4c4ca" if _unlocked else "#59676d")

                    frame:
                        xpos 324
                        ypos 11
                        background Solid(_status_color + "22")
                        padding (8, 4)
                        text _status size 9 bold True color _status_color

                    if _unlocked:
                        if _residents:
                            hbox:
                                xpos 326
                                ypos 51
                                spacing 5
                                text "●" size 16 color "#59e6a1"
                                text _residents size 11 bold True color "#dff8ea" yalign 0.5
                        else:
                            hbox:
                                xpos 326
                                ypos 51
                                spacing 5
                                text "●" size 16 color "#576970"
                                text "No one here" size 10 color "#87989f" yalign 0.5

                        text "ENTER  →":
                            xpos 350
                            ypos 101
                            size 11
                            bold True
                            color _visual["accent"]
                    else:
                        text "STORY LOCKED":
                            xpos 326
                            ypos 55
                            size 10
                            bold True
                            color "#6d7b81"

    frame:
        xpos 930
        ypos 672
        background Solid("#02070ac8")
        padding (12, 5)
        text "v0.9 WORLD HUB • live schedules • event-aware navigation" size 10 color "#6e8a95"


# ------------------------------------------------------------
# LOCATION ATMOSPHERE / SCENE CHROME
# ------------------------------------------------------------

screen v09_scene_chrome():
    zorder 105

    if current_location_id and current_location_id in LOCATION_DATA:
        if renpy.get_screen("main_menu") is None and renpy.get_screen("world_map") is None and renpy.get_screen("developer_tools") is None:

            $ _loc = LOCATION_DATA[current_location_id]
            $ _visual = v09_visual(current_location_id)
            $ _residents = residents_at(current_location_id)
            $ _event_ready = location_has_event(current_location_id)
            $ _cat, _obj = v09_primary_objective()

            # cinematic grade over the simple base backgrounds
            add Solid(v09_period_tint())

            if current_location_id in V09_OUTDOOR_LOCATIONS:
                add SnowBlossom("images/ui/polish/petal.png", count=6, border=45, xspeed=(-10, 12), yspeed=(12, 26), start=1)

            # location identity card
            frame:
                xpos 18
                ypos 91
                xsize 360
                ysize 110
                background Solid("#02080ddc")
                padding (17, 12)

                fixed:
                    xfill True
                    yfill True

                    add Solid(_visual["accent"]):
                        xpos 0
                        ypos 0
                        xsize 3
                        ysize 86

                    text _visual["tag"]:
                        xpos 15
                        ypos 2
                        size 9
                        bold True
                        color _visual["accent"]

                    text _loc["name"]:
                        xpos 15
                        ypos 19
                        size 23
                        bold True
                        color "#ffffff"

                    text "[period_name()] • Day [day]":
                        xpos 15
                        ypos 52
                        size 11
                        color "#93a9b2"

                    if _residents:
                        hbox:
                            xpos 192
                            ypos 50
                            spacing 5
                            text "●" size 16 color "#59e6a1"
                            text _residents size 11 bold True color "#e0f8ea" yalign 0.5
                    else:
                        hbox:
                            xpos 192
                            ypos 50
                            spacing 5
                            text "●" size 16 color "#5a6b72"
                            text "Quiet" size 11 color "#8da0a7" yalign 0.5

                    if _event_ready:
                        frame:
                            xpos 230
                            ypos 2
                            background Solid("#e4bd6826")
                            padding (7, 3)
                            text "EVENT READY" size 9 bold True color "#e4bd68"

            # objective card on the right
            frame:
                xpos 900
                ypos 91
                xsize 360
                ysize 110
                background Solid("#02080ddc")
                padding (17, 12)

                vbox:
                    spacing 4
                    text "ACTIVE OBJECTIVE • [_cat]" size 9 bold True color "#e4bd68"
                    text _obj size 12 color "#c5d3d8" xmaximum 320 line_spacing 2

            # subtle lower cinematic plate behind the dialogue area
            add Solid("#01060a22"):
                xpos 0
                ypos 490
                xsize 1280
                ysize 230


init 2600 python:
    if "v09_scene_chrome" not in config.overlay_screens:
        config.overlay_screens.append("v09_scene_chrome")
