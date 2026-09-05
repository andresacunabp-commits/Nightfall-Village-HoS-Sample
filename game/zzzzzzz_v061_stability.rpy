# ============================================================
# NIGHTFALL VILLAGE v0.6.1 — STABILITY / PORTFOLIO LAYER
# ============================================================

init -500 python:
    NIGHTFALL_WEEKDAYS = (
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    )

    def weekday_name(value):
        try:
            value = int(value)
        except Exception:
            value = 1
        value = max(1, value)
        return NIGHTFALL_WEEKDAYS[(value - 1) % 7]

    def nv_project_health():
        return [
            ("Time system", callable(globals().get("period_name", None))),
            ("Relationship system", callable(globals().get("relation", None))),
            ("Event resolver", callable(globals().get("next_event_for", None))),
            ("Guide system", callable(globals().get("guide_objectives", None))),
            ("NPC schedules", callable(globals().get("npc_location", None))),
            ("Inventory helpers", callable(globals().get("has_item", None))),
        ]

screen nv_global_controls():
    zorder 999
    key "K_F2" action Show("developer_tools")
    key "K_F3" action Show("nv_portfolio_screen")

    if renpy.get_screen("main_menu") is None:
        frame:
            xpos 1080
            ypos 690
            background Solid("#02070aa8")
            padding (9, 3)
            text "F2 DEV • F3 PORTFOLIO" size 10 color "#6b8d9a"

screen nv_portfolio_screen():
    modal True
    zorder 1000
    add Solid("#010407e8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1050
        ysize 610
        background Solid("#041018f5")
        padding (34, 28)

        vbox:
            spacing 16
            hbox:
                xfill True
                vbox:
                    text "NIGHTFALL VILLAGE" size 34 bold True color "#ffffff"
                    text "Directly Relevant Ren'Py Sandbox Sample" size 16 color "#00c8ff"
                textbutton "CLOSE" action Hide("nv_portfolio_screen") style "v06_small_button" xalign 1.0

            add Solid("#00c8ff55") xsize 980 ysize 2

            text "WHY THIS SAMPLE EXISTS" size 13 bold True color "#e3bd6b"
            text "This portfolio build was created specifically to demonstrate development work relevant to a large non-linear shinobi sandbox visual novel. It focuses on architecture, UI, branching state and developer tooling rather than reusing another game's code or assets." size 16 color "#c5d1d6" line_spacing 4

            grid 2 3:
                spacing 12

                for _title, _desc in (
                    ("SANDBOX FLOW", "Locations, time periods and NPC schedules."),
                    ("BRANCHING RELATIONSHIPS", "Persistent Love / Hatred routes and state."),
                    ("CONDITIONAL EVENTS", "Requirements, priorities, quests and items."),
                    ("VN PRESENTATION", "Bottom dialogue UI, character states and menus."),
                    ("SAVE-COMPATIBLE STATE", "Ren'Py defaults, flags and progression."),
                    ("DEVELOPER TOOLING", "F2 event testing and state inspection."),
                ):
                    frame:
                        xsize 475
                        ysize 105
                        background Solid("#071923cc")
                        padding (15, 12)
                        vbox:
                            text _title size 15 bold True color "#00c8ff"
                            text _desc size 14 color "#d2dde1"

screen nv_system_health():
    modal True
    zorder 1010
    add Solid("#010407e5")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        ysize 560
        background Solid("#041018f7")
        padding (30, 26)

        vbox:
            spacing 14
            hbox:
                xfill True
                vbox:
                    text "SYSTEM HEALTH" size 32 bold True color "#ffffff"
                    text "Quick architecture smoke test" size 14 color "#00c8ff"
                textbutton "CLOSE" action Hide("nv_system_health") style "v06_small_button" xalign 1.0

            add Solid("#00c8ff55") xsize 715 ysize 2

            for _name, _ok in nv_project_health():
                frame:
                    xfill True
                    ysize 55
                    background Solid("#07151ccc")
                    padding (14, 9)
                    hbox:
                        xfill True
                        text _name size 17 color "#dce9ed"
                        text ("READY" if _ok else "MISSING") size 15 bold True color ("#58e89a" if _ok else "#ff6c7d") xalign 1.0

screen nv_dev_launcher():
    zorder 998
    if renpy.get_screen("developer_tools") is not None:
        frame:
            xpos 18
            ypos 650
            background Solid("#02070ae8")
            padding (10, 7)
            hbox:
                spacing 8
                textbutton "SYSTEM HEALTH" action Show("nv_system_health") style "v06_small_button"
                textbutton "PORTFOLIO BRIEF" action Show("nv_portfolio_screen") style "v06_small_button"

init 1500 python:
    for _overlay in ("nv_global_controls", "nv_dev_launcher"):
        if _overlay not in config.overlay_screens:
            config.overlay_screens.append(_overlay)
