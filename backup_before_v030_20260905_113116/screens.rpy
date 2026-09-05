# ============================================================
# USER INTERFACE
# ============================================================

screen hud():
    zorder 100

    if renpy.get_screen("main_menu") is None:
        frame:
            xalign 0.99
            yalign 0.02
            padding (14, 10)

            vbox:
                spacing 2
                text "Day [day] â€” [period_name()]" size 20
                text "Energy [energy]   Coins [coins]" size 18
                text "STR [strength]   REP [reputation]" size 18

screen world_map():
    tag menu
    modal True

    add Solid("#0a0d12")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 22

        text "NIGHTFALL VILLAGE" size 42 xalign 0.5
        text "Choose where to spend this part of the day." size 20 xalign 0.5

        grid 2 3:
            spacing 18

            for location_id in ("home", "square", "training", "market", "riverside", "aya_house"):
                $ loc = LOCATION_DATA[location_id]
                $ unlocked = is_location_unlocked(location_id)

                button:
                    xsize 430
                    ysize 115
                    sensitive unlocked
                    action Jump(loc["label"])

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 4

                        text loc["name"] size 27 xalign 0.5
                        if unlocked:
                            text loc["description"] size 15 xalign 0.5
                        else:
                            text "LOCKED â€” progress a storyline to discover this location." size 15 xalign 0.5

        hbox:
            xalign 0.5
            spacing 20
            textbutton "Guide" action Show("guide_screen")
            textbutton "Characters" action Show("characters_screen")
            textbutton "Inventory" action Show("inventory_screen")
            textbutton "Save" action ShowMenu("save")
            textbutton "Load" action ShowMenu("load")

screen guide_screen(close_action=Hide("guide_screen")):
    modal True
    zorder 200

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 780
        ysize 520
        padding (30, 25)

        vbox:
            spacing 15

            text "Interactive Guide" size 36
            text "Spoiler-light hints based on current flags, stats, quests and time." size 18

            viewport:
                ymaximum 330
                mousewheel True
                draggable True

                vbox:
                    spacing 16

                    for category, objective in guide_objectives():
                        vbox:
                            spacing 3
                            text category size 22
                            text "â€¢ [objective]" size 18

            textbutton "Close" action close_action xalign 1.0

screen characters_screen():
    modal True
    zorder 200

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        ysize 520
        padding (30, 25)

        vbox:
            spacing 18

            text "Relationships" size 36

            for cid in ("aya", "ren"):
                $ data = CHARACTER_DATA[cid]
                $ current_loc = npc_location(cid)
                $ current_loc_name = LOCATION_DATA[current_loc]["name"] if current_loc else "Unavailable"

                frame:
                    xfill True
                    padding (18, 12)

                    vbox:
                        spacing 4
                        text data["name"] size 26
                        text data["description"] size 16
                        text "Love: [relation(cid, 'love')]   Hatred: [relation(cid, 'hatred')]   Route: [dominant_route(cid)]" size 17
                        text "Current schedule: [current_loc_name]" size 16

            textbutton "Close" action Hide("characters_screen") xalign 1.0

screen inventory_screen():
    modal True
    zorder 200

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 430
        padding (30, 25)

        vbox:
            spacing 14

            text "Inventory" size 36

            for line in inventory_lines():
                text "â€¢ [line]" size 20

            null height 15
            text "Coins: [coins]" size 20

            textbutton "Close" action Hide("inventory_screen") xalign 1.0

init python:
    if "hud" not in config.overlay_screens:
        config.overlay_screens.append("hud")


