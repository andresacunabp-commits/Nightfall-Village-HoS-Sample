# ============================================================
# NIGHTFALL VILLAGE v0.7 — HOUSEHOLD VERTICAL SLICE
# A directly relevant sandbox-VN sample: room navigation,
# character availability, chained events and route reactions.
# ============================================================

# ------------------------------------------------------------
# Save-compatible demo state
# ------------------------------------------------------------

default v07_house_stage = 0
default v07_house_visits = {}
default v07_last_choice = "none"
default v07_demo_complete = False


init python:

    V07_ROOM_DATA = {
        "entrance": {
            "name": "Entrance",
            "subtitle": "Front hall and mission board",
            "label": "v07_room_entrance",
            "icon": "◇",
        },
        "hallway": {
            "name": "Hallway",
            "subtitle": "Connects the private rooms",
            "label": "v07_room_hallway",
            "icon": "▤",
        },
        "kitchen": {
            "name": "Kitchen",
            "subtitle": "A quieter place to talk",
            "label": "v07_room_kitchen",
            "icon": "◫",
        },
        "aya_room": {
            "name": "Aya's Room",
            "subtitle": "Relationship-gated story space",
            "label": "v07_room_aya",
            "icon": "✦",
        },
    }

    def v07_demo_route():
        love = relation("aya", "love")
        hatred = relation("aya", "hatred")
        if love > hatred:
            return "Love"
        if hatred > love:
            return "Hatred"
        return "Undecided"

    def v07_room_unlocked(room_id):
        if room_id == "entrance":
            return True
        if room_id in ("hallway", "kitchen"):
            return store.v07_house_stage >= 1
        if room_id == "aya_room":
            return store.v07_house_stage >= 2
        return False

    def v07_room_occupant(room_id):
        stage = store.v07_house_stage
        if room_id == "entrance" and stage <= 1:
            return "Aya"
        if room_id == "kitchen" and stage == 1:
            return "Aya"
        if room_id == "hallway" and stage == 3:
            return "Aya"
        if room_id == "aya_room" and stage >= 2:
            return "Aya"
        return ""

    def v07_room_event(room_id):
        stage = store.v07_house_stage
        return (
            (room_id == "entrance" and stage == 0) or
            (room_id == "kitchen" and stage == 1) or
            (room_id == "aya_room" and stage == 2) or
            (room_id == "hallway" and stage == 3) or
            (room_id == "aya_room" and stage == 4)
        )

    def v07_house_hint():
        stage = store.v07_house_stage
        if stage == 0:
            return "Enter the household and speak with Aya."
        if stage == 1:
            return "Aya moved to the Kitchen. Follow the green availability marker."
        if stage == 2:
            return "Aya's Room is now accessible. A private conversation is available."
        if stage == 3:
            return "Check the Hallway. Your earlier choices will change the scene."
        if stage == 4:
            return "Return to Aya's Room for the route-reactive finale."
        return "Vertical slice complete. Use Reset Demo to test the other route."

    def v07_stage_title():
        titles = {
            0: "Arrival",
            1: "Tea After Midnight",
            2: "Mission Notes",
            3: "The Hallway Choice",
            4: "Route Finale",
            5: "Complete",
        }
        return titles.get(store.v07_house_stage, "Complete")


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------

style v07_room_button is button:
    background Solid("#061017e8")
    hover_background Solid("#0a3446f2")
    insensitive_background Solid("#05090dc7")
    xpadding 18
    ypadding 14

style v07_room_button_text is button_text:
    color "#eaf8fc"
    hover_color "#ffffff"

style v07_nav_button is button:
    background Solid("#07141bcc")
    hover_background Solid("#0a4055ee")
    xpadding 16
    ypadding 9

style v07_nav_button_text is button_text:
    size 14
    color "#b8cbd3"
    hover_color "#ffffff"


# ------------------------------------------------------------
# Main-menu callout. We do not replace the v0.6 menu; this sits
# on top of it and makes the new vertical slice obvious.
# ------------------------------------------------------------

screen v07_main_menu_addon():
    zorder 500

    if renpy.get_screen("main_menu") is not None:
        frame:
            xpos 840
            ypos 530
            xsize 370
            ysize 118
            background Solid("#02090edb")
            padding (18, 13)

            vbox:
                spacing 6
                text "NEW • v0.7 HOUSEHOLD SLICE" size 12 bold True color "#00d5ff"
                text "Room navigation + chained Aya events" size 15 color "#ffffff"

                textbutton "PLAY HOUSEHOLD DEMO  →":
                    action Start("v07_house_demo_start")
                    style "v07_nav_button"


# ------------------------------------------------------------
# House hub — intentionally similar to the interaction pattern
# of a large sandbox VN: visual rooms, occupant markers, event
# badges and a compact progression panel.
# ------------------------------------------------------------

screen v07_house_hub():
    tag menu
    modal True

    add "images/ui/aya_house_bg.png"
    add Solid("#0106098f")

    # Header
    frame:
        xpos 30
        ypos 20
        xsize 1220
        ysize 74
        background Solid("#02090ee8")
        padding (20, 10)

        hbox:
            xfill True

            vbox:
                text "AYA'S HOUSEHOLD" size 28 bold True color "#ffffff"
                text "Nightfall Village • [period_name()] • Day [day]" size 13 color "#00c8ff"

            vbox:
                xalign 1.0
                text "STORY [v07_house_stage] / 5" size 14 bold True color "#e4bd68" xalign 1.0
                text "Route: [v07_demo_route()]" size 13 color "#c5d3d8" xalign 1.0

    # Left character / objective rail
    frame:
        xpos 30
        ypos 108
        xsize 315
        ysize 565
        background Solid("#02090ee8")
        padding (18, 16)

        fixed:
            xfill True
            yfill True

            add "images/characters/aya/aya_portrait.png":
                xpos 18
                ypos 4
                zoom 0.78

            text "AYA":
                xpos 160
                ypos 18
                size 24
                bold True
                color "#00d7ff"

            text "Love [relation('aya','love')]":
                xpos 160
                ypos 52
                size 13
                color "#ff6c9d"

            text "Hatred [relation('aya','hatred')]":
                xpos 160
                ypos 76
                size 13
                color "#c98cff"

            add Solid("#00c8ff44"):
                xpos 0
                ypos 145
                xsize 279
                ysize 2

            text "CURRENT EVENT":
                xpos 0
                ypos 169
                size 11
                bold True
                color "#e4bd68"

            text v07_stage_title():
                xpos 0
                ypos 193
                size 20
                bold True
                color "#ffffff"

            text v07_house_hint():
                xpos 0
                ypos 229
                xmaximum 275
                size 14
                color "#a9bbc3"
                line_spacing 3

            text "AVAILABILITY":
                xpos 0
                ypos 328
                size 11
                bold True
                color "#00c8ff"

            hbox:
                xpos 0
                ypos 354
                spacing 8
                text "●" size 19 color "#54e89a"
                text "Green = character/event available" size 12 color "#bdcbd1" yalign 0.5

            hbox:
                xpos 0
                ypos 382
                spacing 8
                text "●" size 19 color "#53626a"
                text "Gray = no current interaction" size 12 color "#7f929a" yalign 0.5

            vbox:
                xpos 0
                ypos 445
                spacing 7

                textbutton "RESET DEMO":
                    action Jump("v07_house_demo_reset")
                    style "v07_nav_button"

                textbutton "WORLD MAP":
                    action Jump("map")
                    style "v07_nav_button"

                textbutton "MAIN MENU":
                    action MainMenu(confirm=False)
                    style "v07_nav_button"

    # Room cards
    grid 2 2:
        xpos 370
        ypos 122
        spacing 18

        for _room_id in ("entrance", "hallway", "kitchen", "aya_room"):
            $ _room = V07_ROOM_DATA[_room_id]
            $ _unlocked = v07_room_unlocked(_room_id)
            $ _occupant = v07_room_occupant(_room_id)
            $ _event = v07_room_event(_room_id)

            button:
                style "v07_room_button"
                xsize 420
                ysize 225
                sensitive _unlocked
                action Jump(_room["label"])

                fixed:
                    xfill True
                    yfill True

                    text _room["icon"]:
                        xpos 4
                        ypos 6
                        size 42
                        color ("#00c8ff" if _unlocked else "#41515a")

                    text _room["name"]:
                        xpos 67
                        ypos 8
                        size 24
                        bold True
                        color ("#ffffff" if _unlocked else "#586970")

                    text _room["subtitle"]:
                        xpos 67
                        ypos 45
                        size 13
                        color ("#9fb3bc" if _unlocked else "#56636a")

                    if not _unlocked:
                        text "LOCKED":
                            xpos 67
                            ypos 84
                            size 13
                            bold True
                            color "#6f7a80"

                    else:
                        if _occupant:
                            hbox:
                                xpos 67
                                ypos 91
                                spacing 7
                                text "●" size 20 color "#54e89a"
                                text _occupant size 15 bold True color "#dff9ea" yalign 0.5
                        else:
                            hbox:
                                xpos 67
                                ypos 91
                                spacing 7
                                text "●" size 20 color "#53626a"
                                text "No character here" size 13 color "#7e9199" yalign 0.5

                    if _event and _unlocked:
                        frame:
                            xpos 284
                            ypos 6
                            background Solid("#00c8ff")
                            padding (8, 3)
                            text "NEW EVENT" size 10 bold True color "#001017"

                    if _unlocked:
                        text "ENTER  →":
                            xpos 296
                            ypos 172
                            size 13
                            bold True
                            color "#00c8ff"

    # tiny portfolio note
    frame:
        xpos 900
        ypos 645
        background Solid("#02070ab8")
        padding (11, 5)
        text "v0.7 • room schedules • event chain • route reaction" size 10 color "#6f8b96"


# ------------------------------------------------------------
# Demo flow
# ------------------------------------------------------------

label v07_house_demo_start:
    $ day = max(day, 3)
    $ period_index = 3
    $ unlocked_locations["aya_house"] = True
    $ flags["v07_house_demo_started"] = True

    scene bg_aya_house
    with fade

    if v07_house_stage == 0:
        show expression "images/characters/aya/aya_neutral.png" as v07_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        aya "You found the place."
        mc "You sound surprised."
        aya "I was deciding whether inviting you was a mistake."

        hide v07_aya
        with dissolve

    jump v07_house_hub_label


label v07_house_hub_label:
    call screen v07_house_hub
    jump v07_house_hub_label


label v07_house_demo_reset:
    $ v07_house_stage = 0
    $ v07_house_visits = {}
    $ v07_last_choice = "none"
    $ v07_demo_complete = False
    $ relationships["aya"]["love"] = 0
    $ relationships["aya"]["hatred"] = 0
    $ flags["v07_house_demo_started"] = True
    $ period_index = 3
    $ day = max(day, 3)
    $ renpy.notify("Household demo reset")
    jump v07_house_hub_label


# ------------------------------------------------------------
# Entrance event
# ------------------------------------------------------------

label v07_room_entrance:
    scene bg_aya_house
    with dissolve

    if v07_house_stage == 0:
        show expression "images/characters/aya/aya_serious.png" as v07_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        aya "One rule: don't wander into rooms just because a door is open."

        menu:
            "Respect the boundary":
                $ change_relation("aya", "love", 1)
                $ v07_last_choice = "respect"

                show expression "images/characters/aya/aya_smile.png" as v07_aya:
                    xalign 0.72
                    yalign 1.02
                    zoom 0.56

                mc "Your house, your rules."
                aya "Good answer."

            "Tease her about being nervous":
                $ change_relation("aya", "hatred", 1)
                $ v07_last_choice = "tease"

                show expression "images/characters/aya/aya_serious.png" as v07_aya:
                    xalign 0.72
                    yalign 1.02
                    zoom 0.56

                mc "You rehearsed that speech, didn't you?"
                aya "Keep testing me and you'll find out."

        $ v07_house_stage = 1
        $ v07_house_visits["entrance"] = True
        $ renpy.notify("New event: Tea After Midnight")

        hide v07_aya
        with dissolve

    else:
        "The entrance is quiet. Aya has moved deeper into the house."

    jump v07_house_hub_label


# ------------------------------------------------------------
# Kitchen event
# ------------------------------------------------------------

label v07_room_kitchen:
    scene bg_aya_house
    with dissolve

    if v07_house_stage == 1:
        show expression "images/characters/aya/aya_neutral.png" as v07_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        aya "Tea?"
        mc "Is that an offer or an order?"
        aya "Depends on your answer."

        menu:
            "Help prepare it":
                $ change_relation("aya", "love", 1)
                $ v07_last_choice = "help_tea"

                show expression "images/characters/aya/aya_smile.png" as v07_aya:
                    xalign 0.72
                    yalign 1.02
                    zoom 0.56

                "You work side by side in comfortable silence."
                aya "You're less distracting when you're useful."

            "Turn it into a competition":
                $ change_relation("aya", "hatred", 1)
                $ v07_last_choice = "tea_race"

                show expression "images/characters/aya/aya_surprised.png" as v07_aya:
                    xalign 0.72
                    yalign 1.02
                    zoom 0.56

                mc "First one to finish setting everything wins."
                aya "You turned tea into a contest? Fine."

        $ v07_house_stage = 2
        $ v07_house_visits["kitchen"] = True
        $ renpy.notify("Aya's Room unlocked")

        hide v07_aya
        with dissolve

    else:
        "The kitchen is empty, but two cups are still warm."

    jump v07_house_hub_label


# ------------------------------------------------------------
# Aya room — private event / finale
# ------------------------------------------------------------

label v07_room_aya:
    scene bg_aya_house
    with dissolve

    if v07_house_stage == 2:
        show expression "images/characters/aya/aya_neutral.png" as v07_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        "Mission reports cover the desk. Aya closes one folder when you enter."

        aya "This is why I invited you. I need another opinion on tomorrow's route."

        menu:
            "Study the reports seriously":
                $ change_relation("aya", "love", 1)
                $ change_stat("reputation", 1)
                $ v07_last_choice = "reports_help"

                mc "The eastern checkpoint creates a blind spot. I'd move the handoff."
                aya "...That's actually useful."

            "Challenge her plan":
                $ change_relation("aya", "hatred", 1)
                $ v07_last_choice = "reports_challenge"

                mc "Your route is too predictable. I could intercept it twice."
                aya "Then prove it."

        $ v07_house_stage = 3
        $ v07_house_visits["aya_room_1"] = True
        $ renpy.notify("Your earlier choices will affect the next scene")

        hide v07_aya
        with dissolve

    elif v07_house_stage == 4:
        $ _route = v07_demo_route()

        if _route == "Love":
            show expression "images/characters/aya/aya_smile.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "You've been irritatingly reliable tonight."
            mc "I'll take that as a compliment."
            aya "Don't get used to it."

            "LOVE ROUTE PREVIEW UNLOCKED"
            "Future events can now require Aya Love and react to the choices you made in earlier rooms."

        elif _route == "Hatred":
            show expression "images/characters/aya/aya_serious.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "You challenged every decision I made tonight."
            mc "And you're still talking to me."
            aya "Because beating you properly will take more than one night."

            "HATRED ROUTE PREVIEW UNLOCKED"
            "Future events can now require Aya Hatred and turn rivalry into a separate event chain."

        else:
            show expression "images/characters/aya/aya_neutral.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "I still can't decide what you're trying to do."
            "NEUTRAL ROUTE"
            "A larger sandbox can keep the route undecided until later thresholds are reached."

        $ v07_house_stage = 5
        $ v07_demo_complete = True
        $ flags["v07_house_demo_complete"] = True
        $ renpy.notify("Household vertical slice complete")

        hide v07_aya
        with dissolve

    else:
        "Aya's room is available, but there is no new event here right now."

    jump v07_house_hub_label


# ------------------------------------------------------------
# Hallway route reaction
# ------------------------------------------------------------

label v07_room_hallway:
    scene bg_aya_house
    with dissolve

    if v07_house_stage == 3:
        $ _route = v07_demo_route()

        if _route == "Love":
            show expression "images/characters/aya/aya_smile.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "You know, most people leave when the work is done."
            mc "Maybe I wasn't here only for the work."
            aya "I noticed."
            $ change_relation("aya", "love", 1)

        elif _route == "Hatred":
            show expression "images/characters/aya/aya_serious.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "Still here?"
            mc "You haven't won yet."
            aya "Good. I hate easy victories."
            $ change_relation("aya", "hatred", 1)

        else:
            show expression "images/characters/aya/aya_surprised.png" as v07_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56

            aya "You're impossible to predict."
            mc "That can be useful."
            aya "Or exhausting."

        $ v07_house_stage = 4
        $ v07_house_visits["hallway_route"] = True
        $ renpy.notify("Route-reactive finale available in Aya's Room")

        hide v07_aya
        with dissolve

    else:
        "The hallway connects the household's rooms. Nothing new happens here."

    jump v07_house_hub_label


# ------------------------------------------------------------
# Register the main-menu callout after the older UI layers.
# ------------------------------------------------------------

init 2000 python:
    if "v07_main_menu_addon" not in config.overlay_screens:
        config.overlay_screens.append("v07_main_menu_addon")
