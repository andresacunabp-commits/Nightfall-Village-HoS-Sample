# ============================================================
# NIGHTFALL v0.10.2 HOTFIX
# Visual cleanup for world/scene panels.
# ============================================================

init -50 python:

    def nv102_first_loadable(candidates, fallback=None):
        for c in candidates:
            try:
                if renpy.loadable(c):
                    return c
            except Exception:
                pass
        return fallback

    def nv102_safe_call(fn_name, default=None):
        try:
            fn = globals().get(fn_name, None)
            if callable(fn):
                return fn()
        except Exception:
            pass
        return default

    def nv102_pick(*values):
        for v in values:
            if v not in (None, "", False):
                return v
        return ""

style nv102_side_button is button:
    background Solid("#07141bcc")
    hover_background Solid("#0a4055ee")
    xpadding 16
    ypadding 9

style nv102_side_button_text is button_text:
    size 14
    color "#c2d1d7"
    hover_color "#ffffff"

style nv102_card is button:
    background Solid("#041018cc")
    hover_background Solid("#0b3445e8")
    insensitive_background Solid("#05090dad")
    xpadding 18
    ypadding 14

style nv102_card_text is button_text:
    color "#eef8fb"
    hover_color "#ffffff"

style nv102_chip_text:
    size 11
    bold True
    color "#001118"

screen world_map():

    tag menu
    modal True

    $ _map_bg = nv102_first_loadable([
        "images/backgrounds/world_hub.jpg",
        "images/backgrounds/world_hub.png",
        "images/ui/village_night_bg.png",
    ], "images/ui/village_night_bg.png")

    python:
        try:
            _objs = guide_objectives()
        except Exception:
            _objs = []

    add _map_bg
    add Solid("#02070a68")

    frame:
        xpos 28
        ypos 20
        xsize 1224
        ysize 78
        background Solid("#021018e6")
        padding (20, 10)

        hbox:
            xfill True

            vbox:
                text "NIGHTFALL VILLAGE" size 28 bold True color "#ffffff"
                text "WORLD HUB • choose a district" size 13 color "#00c8ff"

            vbox:
                xalign 1.0
                text "[period_name()] • Day [day]" size 15 color "#ffffff" xalign 1.0
                text "Energy [energy]/4" size 12 color "#9db4be" xalign 1.0

    frame:
        xpos 28
        ypos 112
        xsize 300
        ysize 560
        background Solid("#021018df")
        padding (18, 16)

        vbox:
            spacing 12

            text "CURRENT OBJECTIVE" size 12 bold True color "#e4bd68"

            if _objs and len(_objs) > 0:
                $ _cat, _goal = _objs[0]
                text _cat size 17 bold True color "#ffffff"
                text _goal size 14 color "#adc0c8" line_spacing 3
            else:
                text "Explore" size 17 bold True color "#ffffff"
                text "Move through the village and inspect the available scenes." size 14 color "#adc0c8" line_spacing 3

            null height 6

            text "LEGEND" size 12 bold True color "#00c8ff"

            hbox:
                spacing 8
                text "●" size 18 color "#54e89a"
                text "Character or event available" size 12 color "#c6d2d7"

            hbox:
                spacing 8
                text "●" size 18 color "#56666f"
                text "No current interaction" size 12 color "#81949c"

            hbox:
                spacing 8
                text "◆" size 16 color "#00c8ff"
                text "New event ready" size 12 color "#c6d2d7"

            null height 10

            textbutton "CHARACTERS":
                action Show("characters_screen")
                style "nv102_side_button"

            textbutton "GUIDE":
                action Show("guide_screen")
                style "nv102_side_button"

            textbutton "MAIN MENU":
                action MainMenu(confirm=False)
                style "nv102_side_button"

    grid 2 4:
        xpos 356
        ypos 122
        spacing 16

        for location_id in LOCATION_ORDER:

            $ loc = LOCATION_DATA[location_id]
            $ unlocked = is_location_unlocked(location_id)
            $ residents = residents_at(location_id)
            $ event_ready = location_has_event(location_id)
            $ desc = loc.get("description", "Explore this district.")

            button:
                style "nv102_card"
                xsize 430
                ysize 122
                sensitive unlocked
                action Jump(loc["label"])

                fixed:
                    xfill True
                    yfill True

                    text loc["icon"]:
                        xpos 4
                        ypos 7
                        size 36
                        color ("#00c8ff" if unlocked else "#43535b")

                    text loc["name"]:
                        xpos 58
                        ypos 8
                        size 22
                        bold True
                        color ("#ffffff" if unlocked else "#67777f")

                    text desc:
                        xpos 58
                        ypos 39
                        xmaximum 300
                        size 12
                        color ("#9eb4bd" if unlocked else "#66757d")

                    if unlocked:
                        if residents:
                            hbox:
                                xpos 58
                                ypos 84
                                spacing 7
                                text "●" size 18 color "#54e89a"
                                text residents size 13 bold True color "#dcf8e6"
                        else:
                            hbox:
                                xpos 58
                                ypos 84
                                spacing 7
                                text "●" size 18 color "#56666f"
                                text "No one here" size 12 color "#82939a"

                        text "ENTER  →":
                            xpos 320
                            ypos 88
                            size 12
                            bold True
                            color "#00c8ff"
                    else:
                        text "LOCKED":
                            xpos 58
                            ypos 82
                            size 12
                            bold True
                            color "#687980"

                    if event_ready and unlocked:
                        frame:
                            xpos 320
                            ypos 6
                            background Solid("#00c8ff")
                            padding (8, 3)
                            text "EVENT" style "nv102_chip_text"

screen nv102_clean_location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    zorder 130

    $ _title = nv102_pick(location_name, location_title, area_name, "LOCATION")
    $ _district = nv102_pick(district, district_name, area_type, "DISTRICT")
    $ _present = nv102_pick(present_character, character_name, npc_present, "No one here")
    $ _objective = nv102_pick(objective, objective_text, "")

    frame:
        xpos 28
        ypos 92
        xsize 360
        ysize 110
        background Solid("#021018dc")
        padding (16, 12)

        vbox:
            spacing 3
            text _district.upper() size 11 bold True color "#00c8ff"
            text _title size 28 bold True color "#ffffff"
            hbox:
                spacing 7
                text "●" size 18 color ("#54e89a" if _present != "No one here" else "#56666f")
                text _present size 12 color "#c5d4da"

    if _objective != "":
        frame:
            xpos 905
            ypos 92
            xsize 325
            ysize 110
            background Solid("#021018dc")
            padding (15, 12)

            vbox:
                spacing 4
                text "OBJECTIVE" size 11 bold True color "#e4bd68"
                text _objective size 13 color "#c1d0d6" line_spacing 3

                if event_ready:
                    text "EVENT READY" size 12 bold True color "#00d6ff"

screen location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    use nv102_clean_location_overlay(
        location_name=location_name,
        location_title=location_title,
        district=district,
        district_name=district_name,
        area_type=area_type,
        area_name=area_name,
        present_character=present_character,
        character_name=character_name,
        npc_present=npc_present,
        objective=objective,
        objective_text=objective_text,
        event_ready=event_ready
    )

screen current_location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    use location_overlay(
        location_name=location_name,
        location_title=location_title,
        district=district,
        district_name=district_name,
        area_type=area_type,
        area_name=area_name,
        present_character=present_character,
        character_name=character_name,
        npc_present=npc_present,
        objective=objective,
        objective_text=objective_text,
        event_ready=event_ready
    )

screen scene_location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    use location_overlay(
        location_name=location_name,
        location_title=location_title,
        district=district,
        district_name=district_name,
        area_type=area_type,
        area_name=area_name,
        present_character=present_character,
        character_name=character_name,
        npc_present=npc_present,
        objective=objective,
        objective_text=objective_text,
        event_ready=event_ready
    )

screen v09_location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    use location_overlay(
        location_name=location_name,
        location_title=location_title,
        district=district,
        district_name=district_name,
        area_type=area_type,
        area_name=area_name,
        present_character=present_character,
        character_name=character_name,
        npc_present=npc_present,
        objective=objective,
        objective_text=objective_text,
        event_ready=event_ready
    )

screen v10_location_overlay(
    location_name=None,
    location_title=None,
    district=None,
    district_name=None,
    area_type=None,
    area_name=None,
    present_character=None,
    character_name=None,
    npc_present=None,
    objective=None,
    objective_text=None,
    event_ready=False
):
    use location_overlay(
        location_name=location_name,
        location_title=location_title,
        district=district,
        district_name=district_name,
        area_type=area_type,
        area_name=area_name,
        present_character=present_character,
        character_name=character_name,
        npc_present=npc_present,
        objective=objective,
        objective_text=objective_text,
        event_ready=event_ready
    )
