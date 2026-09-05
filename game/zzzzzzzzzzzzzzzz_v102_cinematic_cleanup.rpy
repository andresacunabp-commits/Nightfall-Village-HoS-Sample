# ============================================================
# NIGHTFALL VILLAGE v0.10.2 — CINEMATIC CLEANUP
# ============================================================
# Final authority for the current presentation layer.
# - forces the generated cinematic backgrounds over prototype art
# - restores/centralizes the v0.9 helper API used by later modules
# - replaces the world hub with clean image-led destination cards
# - keeps scene chrome minimal so the artwork stays visible
# - suppresses obsolete menu overlays
# ============================================================


default current_location_id = None


init python:

    V09_LOCATION_VISUALS = {
        "home": {
            "tag": "SAFEHOUSE",
            "thumb": "images/backgrounds/v10/aya_house_hallway.jpg",
            "accent": "#78d9ff",
            "mood": "Rest, plan and review your progress.",
        },
        "square": {
            "tag": "SOCIAL HUB",
            "thumb": "images/backgrounds/v10/village_square.jpg",
            "accent": "#00d7ff",
            "mood": "Stories cross here as schedules change.",
        },
        "training": {
            "tag": "TRAINING",
            "thumb": "images/backgrounds/v10/training_ground.jpg",
            "accent": "#63e8ac",
            "mood": "Raise Strength and meet Ren during the day.",
        },
        "market": {
            "tag": "COMMERCE",
            "thumb": "images/backgrounds/v10/market_alley.jpg",
            "accent": "#e7bd68",
            "mood": "Supplies by day. Secrets after dark.",
        },
        "riverside": {
            "tag": "QUIET DISTRICT",
            "thumb": "images/backgrounds/v10/riverside.jpg",
            "accent": "#7edcff",
            "mood": "Private conversations and hidden discoveries.",
        },
        "aya_house": {
            "tag": "HOUSEHOLD",
            "thumb": "images/backgrounds/v10/aya_house_ext.jpg",
            "accent": "#ff7ea7",
            "mood": "Relationship-gated scenes with Aya.",
        },
        "old_shrine": {
            "tag": "OUTSKIRTS",
            "thumb": "images/backgrounds/v10/shrine_path.jpg",
            "accent": "#c48cff",
            "mood": "A forgotten path with late-game clues.",
        },
        "archive": {
            "tag": "SECRET AREA",
            "thumb": "images/backgrounds/v10/aya_house_hallway.jpg",
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

    def v09_primary_objective():
        try:
            rows = guide_objectives()
        except Exception:
            rows = []
        if not rows:
            return ("FREE ROAM", "Explore the village and discover new events.")
        return rows[0]

    def v09_location_status(location_id):
        if not is_location_unlocked(location_id):
            return ("LOCKED", "#687880")
        if location_has_event(location_id):
            return ("NEW EVENT", "#e7bd68")
        if residents_at(location_id):
            return ("CHARACTER HERE", "#59e6a1")
        return ("OPEN", "#00c8ff")

    def nv102_loadable_or(path, fallback="images/ui/village_night_bg.png"):
        try:
            if renpy.loadable(path):
                return path
        except Exception:
            pass
        return fallback

    def nv102_scene_path(location_id):
        mapping = {
            "home": "images/backgrounds/v10/aya_house_hallway.jpg",
            "square": "images/backgrounds/v10/village_square.jpg",
            "training": "images/backgrounds/v10/training_ground.jpg",
            "market": "images/backgrounds/v10/market_alley.jpg",
            "riverside": "images/backgrounds/v10/riverside.jpg",
            "aya_house": "images/backgrounds/v10/aya_house_hallway.jpg",
            "old_shrine": "images/backgrounds/v10/shrine_path.jpg",
            "archive": "images/backgrounds/v10/aya_house_hallway.jpg",
        }
        return nv102_loadable_or(mapping.get(location_id, "images/ui/village_night_bg.png"))


# ------------------------------------------------------------
# Force the final scene images AFTER the v0.10 asset installer.
# This intentionally replaces the old Composite() images from visuals.rpy.
# ------------------------------------------------------------

init 4000 python:

    def _nv102_define_scene(name, path, fallback="images/ui/village_night_bg.png"):
        chosen = nv102_loadable_or(path, fallback)
        renpy.image(name, im.Scale(chosen, 1280, 720))

    _nv102_define_scene("bg_home", "images/backgrounds/v10/aya_house_hallway.jpg")
    _nv102_define_scene("bg_square", "images/backgrounds/v10/village_square.jpg")
    _nv102_define_scene("bg_training", "images/backgrounds/v10/training_ground.jpg")
    _nv102_define_scene("bg_market", "images/backgrounds/v10/market_alley.jpg")
    _nv102_define_scene("bg_riverside", "images/backgrounds/v10/riverside.jpg")
    _nv102_define_scene("bg_aya_house", "images/backgrounds/v10/aya_house_hallway.jpg")
    _nv102_define_scene("bg_aya_house_ext", "images/backgrounds/v10/aya_house_ext.jpg")
    _nv102_define_scene("bg_old_shrine", "images/backgrounds/v10/shrine_path.jpg")
    _nv102_define_scene("bg_archive", "images/backgrounds/v10/aya_house_hallway.jpg")


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------

style v09_small_button is button:
    background Solid("#071922ef")
    hover_background Solid("#0a4055ef")
    insensitive_background Solid("#050a0dcc")
    xpadding 14
    ypadding 8

style v09_small_button_text is button_text:
    size 13
    color "#d1e5eb"
    hover_color "#ffffff"
    insensitive_color "#566870"

style nv102_nav is button:
    background None
    hover_background Solid("#0a3546e8")
    xsize 280
    yminimum 42
    xpadding 14
    ypadding 7

style nv102_nav_text is button_text:
    size 17
    color "#aebfc6"
    hover_color "#ffffff"

style nv102_card is button:
    background Solid("#040b10e8")
    hover_background Solid("#0a2c3be8")
    insensitive_background Solid("#03070ac9")
    xpadding 0
    ypadding 0

style nv102_card_text is button_text:
    color "#ffffff"


# ------------------------------------------------------------
# Disable superseded menu callouts / overlays.
# ------------------------------------------------------------

screen v07_main_menu_addon():
    pass

screen nv10_main_menu_overlay():
    pass


# ------------------------------------------------------------
# v0.10.2 MAIN MENU
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#01060a58")
    add SnowBlossom("images/ui/polish/petal.png", count=13, border=60, xspeed=(-15, 16), yspeed=(18, 40), start=3)

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
                xpos 32
                ypos 154
                size 10
                bold True
                color "#00d4ff"

            vbox:
                xpos 0
                ypos 188
                spacing 2

                textbutton "▶   Continue" action ShowMenu("load") style "nv102_nav"
                textbutton "▣   New Game" action Start() style "nv102_nav"
                textbutton "◆   World Hub" action Start() style "nv102_nav"
                textbutton "✦   Household Demo" action Start("v07_house_demo_start") style "nv102_nav"
                textbutton "◇   Mission Control" action Start("v08_mission_control_start") style "nv102_nav"
                textbutton "♥   Aya Story Demo" action Start("v06_aya_demo_start") style "nv102_nav"
                textbutton "▤   Guide / Events" action Show("guide_screen") style "nv102_nav"
                textbutton "⌘   Developer Tools" action Show("developer_tools") style "nv102_nav"
                textbutton "⚙   Settings" action ShowMenu("preferences") style "nv102_nav"
                textbutton "⏻   Exit" action Quit(confirm=False) style "nv102_nav"

            add Solid("#00c8ff55"):
                xpos 9
                ypos 626
                xsize 270
                ysize 1

            text "v0.10.2 • Cinematic Cleanup":
                xpos 13
                ypos 642
                size 12
                color "#9edfec"

            text "Clean scenes • no prototype geometry":
                xpos 13
                ypos 663
                size 10
                color "#607d88"

    add Solid("#00c8ff"):
        xpos 334
        ypos 0
        xsize 2
        ysize 720

    frame:
        xpos 358
        ypos 18
        xsize 892
        ysize 64
        background Solid("#02090ed9")
        padding (18, 8)

        hbox:
            spacing 36
            xalign 0.5

            vbox:
                text "SCENES" size 12 bold True color "#00c8ff" xalign 0.5
                text "Cinematic art" size 11 color "#c4d2d7"
            vbox:
                text "SANDBOX" size 12 bold True color "#00c8ff" xalign 0.5
                text "World navigation" size 11 color "#c4d2d7"
            vbox:
                text "ROUTES" size 12 bold True color "#00c8ff" xalign 0.5
                text "Love / Hatred" size 11 color "#c4d2d7"
            vbox:
                text "EVENTS" size 12 bold True color "#00c8ff" xalign 0.5
                text "Persistent state" size 11 color "#c4d2d7"
            vbox:
                text "TOOLING" size 12 bold True color "#00c8ff" xalign 0.5
                text "F2 inspector" size 11 color "#c4d2d7"

    add "images/characters/aya/aya_smile.png":
        xpos 390
        ypos 80
        zoom 0.68
        at v06_float

    frame:
        xpos 820
        ypos 130
        xsize 405
        ysize 455
        background Solid("#02080ce8")
        padding (26, 22)

        vbox:
            spacing 11
            text "v0.10.2" size 12 bold True color "#e4bd68"
            text "Cinematic Scene Pass" size 30 bold True color "#ffffff"
            text "Prototype geometry is removed from gameplay scenes so the environment art becomes the visual focus." size 15 color "#bdcbd1" line_spacing 3

            null height 4
            text "◆ Clean location backgrounds" size 14 color "#dbeaf0"
            text "◆ Image-led world hub" size 14 color "#dbeaf0"
            text "◆ Minimal scene chrome" size 14 color "#dbeaf0"
            text "◆ Live NPC + event status" size 14 color "#dbeaf0"
            text "◆ Existing sandbox logic preserved" size 14 color "#dbeaf0"

            null height 10
            textbutton "ENTER WORLD HUB  →" action Start() style "v09_small_button"
            textbutton "HOUSEHOLD DEMO" action Start("v07_house_demo_start") style "v09_small_button"

    frame:
        xpos 785
        ypos 610
        background Solid("#020609e8")
        padding (16, 8)
        text "Nightfall Village • Ren'Py + Python • Portfolio Build 0.10.2" size 12 color "#8aa6b1"


# ------------------------------------------------------------
# CLEAN WORLD HUB
# ------------------------------------------------------------

screen world_map():
    tag menu
    modal True
    on "show" action SetVariable("current_location_id", None)

    add "images/ui/village_night_bg.png"
    add Solid("#01070b72")
    add SnowBlossom("images/ui/polish/petal.png", count=8, border=50, xspeed=(-11, 12), yspeed=(14, 28), start=2)

    frame:
        xpos 18
        ypos 16
        xsize 1244
        ysize 68
        background Solid("#02080dee")
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
                    text "REP" size 10 color "#7f99a4" xalign 0.5

    frame:
        xpos 18
        ypos 98
        xsize 292
        ysize 568
        background Solid("#02080dea")
        padding (20, 18)

        vbox:
            spacing 13

            text "CURRENT OBJECTIVE" size 11 bold True color "#e4bd68"
            $ _cat, _obj = v09_primary_objective()
            text _cat size 20 bold True color "#ffffff"
            text _obj size 14 color "#aebfc6" line_spacing 3

            add Solid("#00c8ff44") xsize 250 ysize 1

            text "LIVE AVAILABILITY" size 11 bold True color "#00c8ff"

            $ _aya_loc = npc_location("aya")
            $ _ren_loc = npc_location("ren")

            frame:
                xfill True
                background Solid("#06131ad8")
                padding (12, 9)
                vbox:
                    text "AYA" size 12 bold True color "#ff7ea7"
                    text (LOCATION_DATA[_aya_loc]["name"] if _aya_loc else "Unavailable now") size 12 color "#c7d5da"

            frame:
                xfill True
                background Solid("#06131ad8")
                padding (12, 9)
                vbox:
                    text "REN" size 12 bold True color "#63e8ac"
                    text (LOCATION_DATA[_ren_loc]["name"] if _ren_loc else "Unavailable now") size 12 color "#c7d5da"

            null height 6
            textbutton "CHARACTERS" action Show("characters_screen") style "v09_small_button"
            textbutton "EVENT LOG" action Show("gallery_screen") style "v09_small_button"
            textbutton "DEVELOPER INSPECTOR • F2" action Show("developer_tools") style "v09_small_button"
            textbutton "MAIN MENU" action MainMenu(confirm=False) style "v09_small_button"

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
            $ _thumb = nv102_loadable_or(_visual["thumb"])

            button:
                style "nv102_card"
                xsize 450
                ysize 132
                sensitive _unlocked
                action [SetVariable("current_location_id", _location_id), Jump(_loc["label"])]

                fixed:
                    xfill True
                    yfill True

                    add im.Scale(_thumb, 450, 132)
                    add Solid("#01060982")

                    add Solid(_visual["accent"]):
                        xpos 0
                        ypos 0
                        xsize 3
                        ysize 132

                    text _visual["tag"]:
                        xpos 16
                        ypos 11
                        size 9
                        bold True
                        color _visual["accent"]

                    text _loc["name"]:
                        xpos 16
                        ypos 29
                        size 21
                        bold True
                        color ("#ffffff" if _unlocked else "#6f7e84")

                    text _visual["mood"]:
                        xpos 16
                        ypos 61
                        xmaximum 290
                        size 11
                        color ("#b4c4ca" if _unlocked else "#59676d")

                    frame:
                        xpos 324
                        ypos 10
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
        background Solid("#02070ad8")
        padding (12, 5)
        text "v0.10.2 • clean cinematic navigation" size 10 color "#6e8a95"


# ------------------------------------------------------------
# COMPACT GAMEPLAY HUD — no duplicate header on World Hub.
# ------------------------------------------------------------

screen v06_hud():
    zorder 120

    if (renpy.get_screen("main_menu") is None
        and renpy.get_screen("world_map") is None
        and renpy.get_screen("developer_tools") is None
        and renpy.get_screen("v08_mission_control") is None):

        frame:
            xpos 12
            ypos 10
            background Solid("#02070bd9")
            padding (6, 5)

            hbox:
                spacing 5
                use v06_hud_icon("images/ui/icons/icon_map.png", "MAP", Jump("map"))
                use v06_hud_icon("images/ui/icons/icon_characters.png", "PEOPLE", Show("characters_screen"))
                use v06_hud_icon("images/ui/icons/icon_inventory.png", "ITEMS", Show("inventory_screen"))
                use v06_hud_icon("images/ui/icons/icon_missions.png", "EVENTS", Show("gallery_screen"))
                use v06_hud_icon("images/ui/icons/icon_guide.png", "GUIDE", Show("guide_screen"))

        frame:
            xpos 502
            ypos 10
            xsize 285
            ysize 62
            background Solid("#02070be5")
            padding (13, 7)

            hbox:
                xfill True
                vbox:
                    text "◉  $[coins]" size 18 color "#e7ba58"
                    text "REP [reputation]  •  STR [strength]" size 10 color "#8aa0aa"
                vbox:
                    xalign 1.0
                    text "{} {}".format(weekday_name(day), period_name()) size 15 color "#ffffff" xalign 1.0
                    text "Day [day]" size 11 color "#9eb0b8" xalign 1.0

        frame:
            xpos 1030
            ypos 10
            xsize 238
            ysize 62
            background Solid("#02070be5")
            padding (10, 7)

            vbox:
                spacing 6
                hbox:
                    text "⚡" size 14 color "#29d9ff" xminimum 25
                    fixed:
                        xsize 140
                        ysize 8
                        yalign 0.5
                        add Solid("#16303a") xsize 140 ysize 8
                        add Solid("#20d7ff") xsize int(140 * min(energy, 4) / 4.0) ysize 8
                    text "[energy]/4" size 11 color "#d8e6eb" xoffset 6
                hbox:
                    text "♥" size 14 color "#ff4d82" xminimum 25
                    fixed:
                        xsize 140
                        ysize 8
                        yalign 0.5
                        add Solid("#351a26") xsize 140 ysize 8
                        add Solid("#ff4d82") xsize int(140 * relation("aya", "love") / 10.0) ysize 8
                    text "[relation('aya','love')]" size 11 color "#d8e6eb" xoffset 6


# ------------------------------------------------------------
# MINIMAL SCENE CHROME — artwork remains unobstructed.
# ------------------------------------------------------------

screen v09_scene_chrome():
    zorder 105

    if (current_location_id
        and current_location_id in LOCATION_DATA
        and renpy.get_screen("main_menu") is None
        and renpy.get_screen("world_map") is None
        and renpy.get_screen("developer_tools") is None):

        $ _loc = LOCATION_DATA[current_location_id]
        $ _visual = v09_visual(current_location_id)
        $ _residents = residents_at(current_location_id)
        $ _event_ready = location_has_event(current_location_id)
        $ _cat, _obj = v09_primary_objective()

        if current_location_id in V09_OUTDOOR_LOCATIONS:
            add SnowBlossom("images/ui/polish/petal.png", count=4, border=40, xspeed=(-8, 10), yspeed=(10, 22), start=1)

        frame:
            xpos 18
            ypos 86
            xsize 340
            ysize 94
            background Solid("#02080de7")
            padding (15, 10)

            fixed:
                xfill True
                yfill True

                add Solid(_visual["accent"]):
                    xpos 0
                    ypos 0
                    xsize 3
                    ysize 72

                text _visual["tag"]:
                    xpos 14
                    ypos 1
                    size 9
                    bold True
                    color _visual["accent"]

                text _loc["name"]:
                    xpos 14
                    ypos 18
                    size 22
                    bold True
                    color "#ffffff"

                text "[period_name()] • Day [day]":
                    xpos 14
                    ypos 50
                    size 10
                    color "#93a9b2"

                if _residents:
                    text "●  [_residents]":
                        xpos 180
                        ypos 49
                        size 10
                        bold True
                        color "#59e6a1"
                else:
                    text "●  Quiet":
                        xpos 180
                        ypos 49
                        size 10
                        color "#7f929a"

                if _event_ready:
                    text "EVENT READY":
                        xpos 230
                        ypos 2
                        size 9
                        bold True
                        color "#e4bd68"

        frame:
            xpos 930
            ypos 86
            xsize 338
            ysize 94
            background Solid("#02080de7")
            padding (15, 10)

            vbox:
                spacing 4
                text "ACTIVE OBJECTIVE • [_cat]" size 9 bold True color "#e4bd68"
                text _obj size 11 color "#c5d3d8" xmaximum 305 line_spacing 2


init 4300 python:
    if "v09_scene_chrome" not in config.overlay_screens:
        config.overlay_screens.append("v09_scene_chrome")
