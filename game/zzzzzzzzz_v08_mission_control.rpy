# ============================================================
# NIGHTFALL VILLAGE v0.8 — MISSION CONTROL / SCHEDULE DEMO
# Original portfolio vertical slice for a large sandbox VN.
# Demonstrates mission gating, NPC schedules, route-aware events,
# persistent state and a cleaner portfolio-first main menu.
# ============================================================

# ------------------------------------------------------------
# Save-compatible state
# ------------------------------------------------------------

default v08_selected_mission = "silent_route"
default v08_mission_states = {}
default v08_demo_started = False
default v08_demo_complete = False


init python:

    V08_MISSIONS = {
        "silent_route": {
            "title": "Silent Route",
            "rank": "D-RANK",
            "location": "Training Ground",
            "summary": "Scout a guarded route before the evening handoff.",
            "reward": 18,
            "label": "v08_mission_silent_route",
        },
        "coded_scroll": {
            "title": "Coded Scroll",
            "rank": "C-RANK",
            "location": "Market Alley",
            "summary": "Recover a message without drawing attention to Aya's courier network.",
            "reward": 24,
            "label": "v08_mission_coded_scroll",
        },
        "river_signal": {
            "title": "River Signal",
            "rank": "C-RANK",
            "location": "Riverside",
            "summary": "Investigate a night signal. Aya's route changes the tone of the event.",
            "reward": 30,
            "label": "v08_mission_river_signal",
        },
        "joint_patrol": {
            "title": "Joint Patrol",
            "rank": "B-RANK",
            "location": "Village Square",
            "summary": "Final mission unlocked by completing the two prerequisite assignments.",
            "reward": 45,
            "label": "v08_mission_joint_patrol",
        },
    }

    V08_MISSION_ORDER = (
        "silent_route",
        "coded_scroll",
        "river_signal",
        "joint_patrol",
    )

    V08_SCHEDULES = {
        "aya": {
            "Morning": "Village Square",
            "Afternoon": "Village Square",
            "Evening": "Riverside",
            "Night": "Aya's Household",
        },
        "ren": {
            "Morning": "Training Ground",
            "Afternoon": "Training Ground",
            "Evening": "Village Square",
            "Night": "Unavailable",
        },
        "sora": {
            "Morning": "Unavailable",
            "Afternoon": "Unavailable",
            "Evening": "Unavailable",
            "Night": "Market Alley",
        },
    }

    def v08_route_name():
        love = relation("aya", "love")
        hatred = relation("aya", "hatred")
        if love >= 2 and love > hatred:
            return "Love"
        if hatred >= 2 and hatred > love:
            return "Hatred"
        return "Undecided"

    def v08_state(mid):
        return store.v08_mission_states.get(mid, "open")

    def v08_requirement_reason(mid):
        state = v08_state(mid)
        if state == "done":
            return "COMPLETED"
        if state == "active":
            return "ACTIVE"

        if mid == "silent_route":
            if store.day < 4:
                return "Requires Day 4+"
            if period_name() not in ("Afternoon", "Evening"):
                return "Available Afternoon / Evening"
            if store.strength < 1:
                return "Requires Strength 1+"
            return "READY"

        if mid == "coded_scroll":
            if store.reputation < 1:
                return "Requires Reputation 1+"
            if period_name() == "Night":
                return "Return before Night"
            return "READY"

        if mid == "river_signal":
            if period_name() != "Night":
                return "Night-only mission"
            if max(relation("aya", "love"), relation("aya", "hatred")) < 2:
                return "Requires Aya Love 2+ or Hatred 2+"
            return "READY"

        if mid == "joint_patrol":
            if v08_state("silent_route") != "done":
                return "Complete Silent Route"
            if v08_state("coded_scroll") != "done":
                return "Complete Coded Scroll"
            if store.reputation < 2:
                return "Requires Reputation 2+"
            return "READY"

        return "LOCKED"

    def v08_status(mid):
        reason = v08_requirement_reason(mid)
        if reason == "READY":
            return "READY"
        if reason == "COMPLETED":
            return "DONE"
        if reason == "ACTIVE":
            return "ACTIVE"
        return "LOCKED"

    def v08_status_color(mid):
        status = v08_status(mid)
        if status == "READY":
            return "#55e49a"
        if status == "DONE":
            return "#00c8ff"
        if status == "ACTIVE":
            return "#e6bd68"
        return "#66767e"

    def v08_schedule_for(cid, period=None):
        if period is None:
            period = period_name()
        return V08_SCHEDULES.get(cid, {}).get(period, "Unavailable")

    def v08_complete(mid, reward):
        store.v08_mission_states[mid] = "done"
        store.coins += reward
        store.reputation += 1
        store.flags["v08_{}_done".format(mid)] = True
        renpy.notify("Mission complete • +{} coins • Reputation +1".format(reward))

        if all(store.v08_mission_states.get(m) == "done" for m in V08_MISSION_ORDER):
            store.v08_demo_complete = True
            store.flags["v08_mission_demo_complete"] = True

    def v08_advance_period():
        spend_time(0)

    def v08_demo_train():
        store.strength += 1
        renpy.notify("Strength +1")

    def v08_demo_errand():
        store.reputation += 1
        renpy.notify("Reputation +1")

    def v08_demo_relation(route):
        change_relation("aya", route, 1)

    def v08_done_count():
        return sum(1 for m in V08_MISSION_ORDER if v08_state(m) == "done")


# ------------------------------------------------------------
# Styles
# ------------------------------------------------------------

style v08_menu_button is button:
    background None
    hover_background Solid("#0a3446e6")
    xsize 286
    yminimum 44
    xpadding 17
    ypadding 7

style v08_menu_button_text is button_text:
    size 18
    color "#afbec5"
    hover_color "#ffffff"

style v08_action_button is button:
    background Solid("#071922ef")
    hover_background Solid("#0a4055ef")
    insensitive_background Solid("#050b0fc7")
    xpadding 14
    ypadding 8

style v08_action_button_text is button_text:
    size 13
    color "#cfe2e8"
    hover_color "#ffffff"
    insensitive_color "#53646c"

style v08_mission_card is button:
    background Solid("#061017e8")
    hover_background Solid("#0a2c3be8")
    selected_background Solid("#0b3445f2")
    xpadding 15
    ypadding 12

style v08_mission_card_text is button_text:
    color "#ffffff"


# ------------------------------------------------------------
# Disable the older v0.7 menu callout. v0.8 replaces the entire
# main menu with one coherent presentation.
# ------------------------------------------------------------

screen v07_main_menu_addon():
    pass


# ------------------------------------------------------------
# v0.8 Main Menu
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/ui/village_night_bg.png"
    add Solid("#01060966")
    add SnowBlossom("images/ui/polish/petal.png", count=14, border=60, xspeed=(-18, 18), yspeed=(22, 48), start=4)

    # Sidebar
    frame:
        xpos 0
        ypos 0
        xsize 336
        ysize 720
        background Solid("#02080dec")
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
                    style "v08_menu_button"

                textbutton "▣   New Game":
                    action Start()
                    style "v08_menu_button"

                textbutton "✦   Household Demo":
                    action Start("v07_house_demo_start")
                    style "v08_menu_button"

                textbutton "◆   Mission Control":
                    action Start("v08_mission_control_start")
                    style "v08_menu_button"

                textbutton "♥   Aya Story Demo":
                    action Start("v06_aya_demo_start")
                    style "v08_menu_button"

                textbutton "◫   Gallery / Events":
                    action Show("gallery_screen")
                    style "v08_menu_button"

                textbutton "▤   Guide":
                    action Show("guide_screen")
                    style "v08_menu_button"

                textbutton "⌘   Developer Tools":
                    action Show("developer_tools")
                    style "v08_menu_button"

                textbutton "⚙   Settings":
                    action ShowMenu("preferences")
                    style "v08_menu_button"

                textbutton "⏻   Exit":
                    action Quit(confirm=False)
                    style "v08_menu_button"

            add Solid("#00c8ff55"):
                xpos 9
                ypos 626
                xsize 270
                ysize 1

            text "v0.8.0 • Mission Control Build":
                xpos 13
                ypos 642
                size 12
                color "#8ba4ae"

            text "Ren'Py • Python • systems • UI":
                xpos 13
                ypos 663
                size 11
                color "#58727d"

    add Solid("#00c8ff"):
        xpos 334
        ypos 0
        xsize 2
        ysize 720

    # Top strip
    frame:
        xpos 358
        ypos 18
        xsize 892
        ysize 63
        background Solid("#02090ed7")
        padding (18, 8)

        hbox:
            spacing 32
            xalign 0.5

            vbox:
                text "SANDBOX" size 12 color "#00c8ff" xalign 0.5
                text "Time + navigation" size 11 color "#c3d1d7"

            vbox:
                text "SCHEDULES" size 12 color "#00c8ff" xalign 0.5
                text "NPC availability" size 11 color "#c3d1d7"

            vbox:
                text "MISSIONS" size 12 color "#00c8ff" xalign 0.5
                text "Conditional gates" size 11 color "#c3d1d7"

            vbox:
                text "ROUTES" size 12 color "#00c8ff" xalign 0.5
                text "Love / Hatred" size 11 color "#c3d1d7"

            vbox:
                text "TOOLING" size 12 color "#00c8ff" xalign 0.5
                text "F2 inspector" size 11 color "#c3d1d7"

    # Character showcase
    add "images/characters/aya/aya_neutral.png":
        xpos 380
        ypos 78
        zoom 0.67
        at v06_float

    # Portfolio panel
    frame:
        xpos 820
        ypos 125
        xsize 405
        ysize 470
        background Solid("#02080ce0")
        padding (26, 22)
        at v06_panel_in

        vbox:
            spacing 10

            text "NEW IN v0.8" size 12 bold True color "#e4bd68"
            text "Mission Control" size 31 bold True color "#ffffff"
            text "A stronger systems sample built around the kinds of dependencies a nonlinear sandbox needs." size 15 color "#b8c8cf" line_spacing 3

            null height 2
            text "◆ Mission requirements + lock reasons" size 14 color "#d8e8ed"
            text "◆ NPC schedule table by time period" size 14 color "#d8e8ed"
            text "◆ Route-aware Aya mission" size 14 color "#d8e8ed"
            text "◆ Persistent completion + rewards" size 14 color "#d8e8ed"
            text "◆ Live progression controls" size 14 color "#d8e8ed"
            text "◆ Multi-mission prerequisite chain" size 14 color "#d8e8ed"

            null height 8

            textbutton "PLAY MISSION CONTROL  →":
                action Start("v08_mission_control_start")
                style "v08_action_button"

            textbutton "PLAY HOUSEHOLD SLICE  →":
                action Start("v07_house_demo_start")
                style "v08_action_button"

            null height 4
            text "Original project • no copied characters, code or game assets" size 10 color "#607882"


# ------------------------------------------------------------
# Mission Control screen
# ------------------------------------------------------------

screen v08_mission_control():
    tag menu
    modal True

    add "images/ui/village_night_bg.png"
    add Solid("#010609b5")

    # Header
    frame:
        xpos 24
        ypos 18
        xsize 1232
        ysize 72
        background Solid("#02090ef2")
        padding (18, 9)

        hbox:
            xfill True

            vbox:
                text "MISSION CONTROL" size 29 bold True color "#ffffff"
                text "Conditional assignments • schedule intelligence • route state" size 12 color "#00c8ff"

            vbox:
                xalign 1.0
                text "[period_name()] • DAY [day]" size 16 bold True color "#ffffff" xalign 1.0
                text "Completed [v08_done_count()] / 4" size 12 color "#e4bd68" xalign 1.0

    # Left mission list
    frame:
        xpos 24
        ypos 104
        xsize 420
        ysize 518
        background Solid("#02090ee8")
        padding (15, 14)

        vbox:
            spacing 9
            text "ASSIGNMENTS" size 13 bold True color "#00c8ff"

            for _mid in V08_MISSION_ORDER:
                $ _m = V08_MISSIONS[_mid]
                $ _status = v08_status(_mid)
                $ _reason = v08_requirement_reason(_mid)

                button:
                    style "v08_mission_card"
                    xsize 388
                    ysize 94
                    selected (v08_selected_mission == _mid)
                    action SetVariable("v08_selected_mission", _mid)

                    fixed:
                        text _m["rank"]:
                            xpos 0
                            ypos 0
                            size 10
                            bold True
                            color "#e4bd68"

                        text _m["title"]:
                            xpos 0
                            ypos 19
                            size 20
                            bold True
                            color "#ffffff"

                        text _m["location"]:
                            xpos 0
                            ypos 52
                            size 11
                            color "#8299a3"

                        text _status:
                            xpos 303
                            ypos 5
                            size 11
                            bold True
                            color v08_status_color(_mid)

                        if _status == "LOCKED":
                            text _reason:
                                xpos 178
                                ypos 52
                                xmaximum 195
                                size 10
                                color "#7b8a91"
                                text_align 1.0

    # Detail panel
    frame:
        xpos 462
        ypos 104
        xsize 480
        ysize 342
        background Solid("#02090ee8")
        padding (22, 18)

        $ _sel = V08_MISSIONS[v08_selected_mission]
        $ _sel_reason = v08_requirement_reason(v08_selected_mission)
        $ _sel_status = v08_status(v08_selected_mission)

        vbox:
            spacing 10
            hbox:
                xfill True
                text _sel["rank"] size 11 bold True color "#e4bd68"
                text _sel_status size 12 bold True color v08_status_color(v08_selected_mission) xalign 1.0

            text _sel["title"] size 29 bold True color "#ffffff"
            text _sel["summary"] size 15 color "#b7c8cf" line_spacing 3
            add Solid("#00c8ff44") xsize 430 ysize 1

            text "LOCATION" size 10 bold True color "#6f8e9a"
            text _sel["location"] size 15 color "#ffffff"

            text "CURRENT REQUIREMENT" size 10 bold True color "#6f8e9a"
            text _sel_reason size 14 bold True color ("#55e49a" if _sel_reason == "READY" else "#c6d2d7")

            text "REWARD  {} COINS + REPUTATION".format(_sel["reward"]) size 11 color "#e4bd68"

            if _sel_status == "READY":
                textbutton "START MISSION  →":
                    action Jump(_sel["label"])
                    style "v08_action_button"
            elif _sel_status == "DONE":
                text "MISSION COMPLETED" size 13 bold True color "#00c8ff"
            else:
                text "Adjust time, stats, relationship or prerequisites below." size 11 color "#758b94"

    # Schedule panel
    frame:
        xpos 462
        ypos 462
        xsize 480
        ysize 160
        background Solid("#02090ee8")
        padding (18, 13)

        vbox:
            spacing 7
            text "LIVE NPC SCHEDULE" size 12 bold True color "#00c8ff"

            grid 3 2:
                spacing 12

                for _cid, _name in (("aya", "AYA"), ("ren", "REN"), ("sora", "SORA")):
                    vbox:
                        xsize 135
                        text _name size 12 bold True color "#ffffff"
                        text v08_schedule_for(_cid) size 11 color ("#55e49a" if v08_schedule_for(_cid) != "Unavailable" else "#65747b")

                for _cid, _name in (("aya", "ROUTE"), ("ren", "STRENGTH"), ("sora", "REPUTATION")):
                    vbox:
                        xsize 135
                        text _name size 10 color "#6f8e9a"
                        if _cid == "aya":
                            text v08_route_name() size 12 bold True color "#ff83ad"
                        elif _cid == "ren":
                            text "[strength]" size 12 bold True color "#d9e4e8"
                        else:
                            text "[reputation]" size 12 bold True color "#d9e4e8"

    # Progression controls
    frame:
        xpos 960
        ypos 104
        xsize 296
        ysize 518
        background Solid("#02090ee8")
        padding (17, 15)

        vbox:
            spacing 9
            text "PROGRESSION LAB" size 13 bold True color "#e4bd68"
            text "Use these controls to prove that mission locks react live to persistent game state." size 12 color "#9db1ba" line_spacing 3

            add Solid("#00c8ff44") xsize 260 ysize 1

            text "TIME" size 10 bold True color "#6f8e9a"
            text "[period_name()] • Day [day]" size 15 color "#ffffff"
            textbutton "ADVANCE TIME":
                action Function(v08_advance_period)
                style "v08_action_button"

            text "PLAYER STATS" size 10 bold True color "#6f8e9a"
            hbox:
                spacing 6
                textbutton "STR +1":
                    action Function(v08_demo_train)
                    style "v08_action_button"
                textbutton "REP +1":
                    action Function(v08_demo_errand)
                    style "v08_action_button"

            text "AYA ROUTE" size 10 bold True color "#6f8e9a"
            text "Love [relation('aya','love')]  •  Hatred [relation('aya','hatred')]" size 12 color "#ffffff"

            hbox:
                spacing 6
                textbutton "LOVE +1":
                    action Function(v08_demo_relation, "love")
                    style "v08_action_button"
                textbutton "HATE +1":
                    action Function(v08_demo_relation, "hatred")
                    style "v08_action_button"

            add Solid("#00c8ff44") xsize 260 ysize 1

            text "QUICK LINKS" size 10 bold True color "#6f8e9a"
            textbutton "HOUSEHOLD DEMO":
                action Jump("v07_house_demo_start")
                style "v08_action_button"
            textbutton "WORLD MAP":
                action Jump("map")
                style "v08_action_button"
            textbutton "RESET MISSION DEMO":
                action Jump("v08_mission_control_reset")
                style "v08_action_button"
            textbutton "MAIN MENU":
                action MainMenu(confirm=False)
                style "v08_action_button"

    frame:
        xpos 24
        ypos 640
        xsize 1232
        ysize 48
        background Solid("#02090ed9")
        padding (14, 8)

        hbox:
            xfill True
            text "PORTFOLIO SIGNAL: every lock explains exactly which state is missing." size 11 color "#78919b"
            text "F2 DEV • F3 PORTFOLIO" size 11 color "#00c8ff" xalign 1.0


# ------------------------------------------------------------
# Demo entry / reset
# ------------------------------------------------------------

label v08_mission_control_start:
    $ v08_demo_started = True
    $ day = max(day, 4)
    $ period_index = 1
    $ strength = max(strength, 1)
    $ flags["v08_mission_demo_started"] = True

    scene bg_square
    with fade

    mc "The mission board updates throughout the day."
    mc "Assignments can depend on time, stats, relationships and earlier missions."
    mc "If something is locked, Mission Control tells you exactly why."

    jump v08_mission_control_hub


label v08_mission_control_hub:
    call screen v08_mission_control
    jump v08_mission_control_hub


label v08_mission_control_reset:
    $ v08_mission_states = {}
    $ v08_selected_mission = "silent_route"
    $ v08_demo_complete = False
    $ day = max(day, 4)
    $ period_index = 1
    $ strength = 1
    $ reputation = 0
    $ relationships["aya"]["love"] = 0
    $ relationships["aya"]["hatred"] = 0
    $ renpy.notify("Mission Control reset")
    jump v08_mission_control_hub


# ------------------------------------------------------------
# Mission 1 — stat + time gate
# ------------------------------------------------------------

label v08_mission_silent_route:
    if not v08_requirement_reason("silent_route") == "READY":
        jump v08_mission_control_hub

    $ v08_mission_states["silent_route"] = "active"

    scene bg_training
    with dissolve

    "MISSION • SILENT ROUTE"
    "You follow the edge of the training district toward an exposed courier path."

    menu:
        "Move slowly and map every guard rotation":
            mc "Speed doesn't matter if they never know I was here."
            $ change_stat("reputation", 1)
            "You return with a clean patrol map and no witnesses."

        "Test the route with a fast run":
            mc "If I can cross before the patrol turns, the route is usable."
            $ change_stat("strength", 1)
            "The run is risky, but your timing proves the opening exists."

    $ v08_complete("silent_route", V08_MISSIONS["silent_route"]["reward"])
    jump v08_mission_control_hub


# ------------------------------------------------------------
# Mission 2 — reputation gate + Aya relationship choice
# ------------------------------------------------------------

label v08_mission_coded_scroll:
    if not v08_requirement_reason("coded_scroll") == "READY":
        jump v08_mission_control_hub

    $ v08_mission_states["coded_scroll"] = "active"

    scene bg_market
    with dissolve

    show expression "images/characters/aya/aya_neutral.png" as v08_aya:
        xalign 0.72
        yalign 1.02
        zoom 0.56

    aya "The scroll isn't valuable. The route written inside it is."
    mc "So nobody can know we recovered it."
    aya "Exactly."

    menu:
        "Follow Aya's plan exactly":
            $ change_relation("aya", "love", 1)
            mc "Lead. I'll cover the exit."
            show expression "images/characters/aya/aya_smile.png" as v08_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56
            aya "You listen better than I expected."

        "Change the plan at the last second":
            $ change_relation("aya", "hatred", 1)
            mc "Your exit is watched. We're taking the roofline."
            show expression "images/characters/aya/aya_serious.png" as v08_aya:
                xalign 0.72
                yalign 1.02
                zoom 0.56
            aya "Next time, warn me before improvising."

    hide v08_aya
    with dissolve

    $ v08_complete("coded_scroll", V08_MISSIONS["coded_scroll"]["reward"])
    jump v08_mission_control_hub


# ------------------------------------------------------------
# Mission 3 — night + relationship gate, route-reactive scene
# ------------------------------------------------------------

label v08_mission_river_signal:
    if not v08_requirement_reason("river_signal") == "READY":
        jump v08_mission_control_hub

    $ v08_mission_states["river_signal"] = "active"
    $ _route = v08_route_name()

    scene bg_riverside
    with dissolve

    if _route == "Love":
        show expression "images/characters/aya/aya_smile.png" as v08_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        aya "Stay close. The signal repeats every thirty seconds."
        mc "You worried about me?"
        aya "I'm worried you'll ruin a perfectly good mission."
        "Her tone is softer than the words. Your Love route changes the scene context."
        $ change_relation("aya", "love", 1)

    elif _route == "Hatred":
        show expression "images/characters/aya/aya_serious.png" as v08_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56

        aya "Try to keep up."
        mc "I was about to tell you the same thing."
        aya "Good. First to identify the signal source wins."
        "The same mission becomes a rivalry challenge on the Hatred route."
        $ change_relation("aya", "hatred", 1)

    else:
        show expression "images/characters/aya/aya_neutral.png" as v08_aya:
            xalign 0.72
            yalign 1.02
            zoom 0.56
        aya "Keep your eyes on the far bank."

    "A reflected lantern code reveals a hidden handoff point near the bridge."

    hide v08_aya
    with dissolve

    $ v08_complete("river_signal", V08_MISSIONS["river_signal"]["reward"])
    jump v08_mission_control_hub


# ------------------------------------------------------------
# Mission 4 — prerequisite chain finale
# ------------------------------------------------------------

label v08_mission_joint_patrol:
    if not v08_requirement_reason("joint_patrol") == "READY":
        jump v08_mission_control_hub

    $ v08_mission_states["joint_patrol"] = "active"

    scene bg_square
    with dissolve

    "MISSION • JOINT PATROL"
    "Your earlier reconnaissance and recovered route data are combined into one final patrol plan."

    if v08_route_name() == "Love":
        aya "You take the east side. I'll meet you at the tower."
        mc "No competition this time?"
        aya "Maybe I trust you with half the village now. Half."
    elif v08_route_name() == "Hatred":
        aya "East side is mine. Try not to finish last."
        mc "You really can't do anything without making it a contest."
        aya "And yet you keep showing up."
    else:
        aya "Stay on the route and signal if anything changes."

    "The patrol finishes without a breach. The board marks the assignment complete."

    $ v08_complete("joint_patrol", V08_MISSIONS["joint_patrol"]["reward"])

    if v08_demo_complete:
        "MISSION CONTROL VERTICAL SLICE COMPLETE"
        "The demo has now exercised time gates, stat gates, relationship gates, prerequisite chains and persistent rewards."

    jump v08_mission_control_hub
