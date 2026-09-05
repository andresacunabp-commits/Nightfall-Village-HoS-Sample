# ============================================================
# NIGHTFALL VILLAGE v0.12.7 — DYNAMIC WORLD MAP
# ============================================================
# Final authority for the in-game map/HUD.
# - fixes the MAPA button by using a unique screen name
# - map never opens automatically
# - floating destination nodes instead of a grid/list
# - visual state changes with Morning / Afternoon / Evening / Night
# ============================================================

init 12000 python:

    NV127_MAP_NAMES = {
        "home": "CASA",
        "square": "PLAZA",
        "training": "ENTRENAMIENTO",
        "market": "MERCADO",
        "riverside": "RÍO",
        "aya_house": "CASA DE AYA",
        "old_shrine": "SANTUARIO",
        "archive": "ARCHIVO",
    }

    NV127_MAP_THUMBS = {
        "home": "images/backgrounds/v110/aya_house_hallway.jpg",
        "square": "images/backgrounds/v110/village_square.jpg",
        "training": "images/backgrounds/v110/training_ground.jpg",
        "market": "images/backgrounds/v110/market_alley.jpg",
        "riverside": "images/backgrounds/v110/riverside.jpg",
        "aya_house": "images/backgrounds/v110/aya_house_ext.jpg",
        "old_shrine": "images/backgrounds/v110/shrine_path.jpg",
        "archive": "images/backgrounds/v110/aya_house_hallway.jpg",
    }

    # Deliberately scattered across the village image so the screen reads
    # like a real map instead of another menu/grid.
    NV127_MAP_NODES = (
        ("aya_house", 68, 278),
        ("market", 286, 174),
        ("training", 660, 122),
        ("square", 500, 315),
        ("home", 195, 505),
        ("riverside", 785, 455),
        ("old_shrine", 1010, 220),
        ("archive", 1015, 490),
    )

    def nv127_period_label():
        labels = ("MAÑANA", "DÍA", "TARDE", "NOCHE")
        try:
            return labels[max(0, min(3, int(store.period_index)))]
        except Exception:
            return "MAÑANA"

    def nv127_period_subtitle():
        subtitles = (
            "La aldea despierta",
            "La aldea está en movimiento",
            "Las calles empiezan a vaciarse",
            "La noche cambia quién está disponible",
        )
        try:
            return subtitles[max(0, min(3, int(store.period_index)))]
        except Exception:
            return subtitles[0]


style nv127_map_node is button:
    background None
    hover_background Solid("#0bd4ff26")
    insensitive_background None
    xpadding 0
    ypadding 0

style nv127_map_node_text is button_text:
    color "#ffffff"

style nv127_close is button:
    background Solid("#e64b42f2")
    hover_background Solid("#ff675df8")
    xsize 70
    ysize 70
    xpadding 0
    ypadding 0

style nv127_close_text is button_text:
    size 39
    bold True
    color "#ffffff"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style nv127_hud_map is button:
    background Solid("#087e9de9")
    hover_background Solid("#0db2d6f2")
    xpadding 14
    ypadding 7

style nv127_hud_map_text is button_text:
    size 13
    bold True
    color "#ffffff"
    hover_color "#ffffff"

style nv127_hud_button is button:
    background Solid("#061720e8")
    hover_background Solid("#0a455ae8")
    xpadding 11
    ypadding 7

style nv127_hud_button_text is button_text:
    size 13
    bold True
    color "#c9dbe2"
    hover_color "#ffffff"


# ------------------------------------------------------------
# DYNAMIC MAP — UNIQUE NAME PREVENTS OLD WORLD_MAP COLLISIONS
# ------------------------------------------------------------

screen nv127_world_map():
    modal True
    zorder 500

    key "game_menu" action Hide("nv127_world_map")

    # Same village composition, four clearly different time states.
    # This keeps every destination in the same physical place while the
    # lighting changes as time advances.
    if period_index == 0:
        add Transform(im.Scale("images/backgrounds/v110/village_square.jpg", 1280, 720), matrixcolor=BrightnessMatrix(0.22))
        add Solid("#ffe0a919")
    elif period_index == 1:
        add Transform(im.Scale("images/backgrounds/v110/village_square.jpg", 1280, 720), matrixcolor=BrightnessMatrix(0.11))
        add Solid("#fff4dc0d")
    elif period_index == 2:
        add Transform(im.Scale("images/backgrounds/v110/village_square.jpg", 1280, 720), matrixcolor=BrightnessMatrix(0.01))
        add Solid("#c858262d")
    else:
        add Transform(im.Scale("images/backgrounds/v110/village_square.jpg", 1280, 720), matrixcolor=BrightnessMatrix(-0.18))
        add Solid("#04152f58")

    # Subtle contrast layer so map nodes remain readable.
    add Solid("#00000016")

    # Header / current time.
    frame:
        xpos 930
        ypos 18
        xsize 315
        ysize 76
        background Solid("#02080dd9")
        padding (16, 10)

        vbox:
            xalign 0.5
            spacing 1
            text nv127_period_label() size 22 bold True color "#ffffff" xalign 0.5
            text "DÍA [day]" size 11 bold True color "#65ddf7" xalign 0.5
            text nv127_period_subtitle() size 10 color "#9db0b8" xalign 0.5

    # Big close button in the same visual spirit as the reference.
    textbutton "✕":
        xpos 24
        ypos 22
        action Hide("nv127_world_map")
        style "nv127_close"

    # Destination nodes.
    for _location_id, _node_x, _node_y in NV127_MAP_NODES:
        $ _loc = LOCATION_DATA[_location_id]
        $ _unlocked = is_location_unlocked(_location_id)
        $ _thumb = NV127_MAP_THUMBS[_location_id]
        $ _here = current_location_id == _location_id
        $ _event_ready = location_has_event(_location_id) if _unlocked else False
        $ _people = residents_at(_location_id) if _unlocked else ""

        button:
            xpos _node_x
            ypos _node_y
            xsize 168
            ysize 106
            style "nv127_map_node"
            sensitive _unlocked
            action [
                SetVariable("current_location_id", _location_id),
                Hide("nv127_world_map"),
                Jump(_loc["label"]),
            ]

            fixed:
                xfill True
                yfill True

                # Thick dark outer frame + scene thumbnail gives the node
                # the floating destination-bubble feeling of the reference.
                add Solid("#020507f3"):
                    xpos 0
                    ypos 0
                    xsize 168
                    ysize 106

                if _unlocked:
                    add Transform(_thumb, xysize=(158, 96)):
                        xpos 5
                        ypos 5
                else:
                    add Solid("#10171bdc"):
                        xpos 5
                        ypos 5
                        xsize 158
                        ysize 96

                add Solid("#00000070"):
                    xpos 5
                    ypos 5
                    xsize 158
                    ysize 96

                # Current location gets a cyan frame marker.
                if _here:
                    add Solid("#00d7ff"):
                        xpos 0
                        ypos 0
                        xsize 168
                        ysize 4
                    add Solid("#00d7ff"):
                        xpos 0
                        ypos 102
                        xsize 168
                        ysize 4

                text NV127_MAP_NAMES[_location_id]:
                    xpos 0
                    ypos 30
                    xsize 168
                    text_align 0.5
                    size (17 if len(NV127_MAP_NAMES[_location_id]) < 12 else 13)
                    bold True
                    color ("#ffffff" if _unlocked else "#56646a")
                    outlines [(2, "#000000cc", 0, 0)]

                if not _unlocked:
                    text "BLOQUEADO":
                        xpos 0
                        ypos 61
                        xsize 168
                        text_align 0.5
                        size 9
                        bold True
                        color "#68777d"
                elif _event_ready:
                    text "◆ EVENTO":
                        xpos 0
                        ypos 65
                        xsize 168
                        text_align 0.5
                        size 9
                        bold True
                        color "#f0c86d"
                elif _people:
                    text _people:
                        xpos 0
                        ypos 65
                        xsize 168
                        text_align 0.5
                        size 9
                        bold True
                        color "#72edb2"
                elif _here:
                    text "ESTÁS AQUÍ":
                        xpos 0
                        ypos 65
                        xsize 168
                        text_align 0.5
                        size 9
                        bold True
                        color "#61e7ff"

    # Bottom hint/status strip.
    frame:
        xpos 310
        ypos 655
        xsize 660
        ysize 46
        background Solid("#02080de3")
        padding (14, 8)

        hbox:
            xalign 0.5
            spacing 24
            text "$[coins]" size 13 bold True color "#e4bd68"
            text "ENERGÍA [energy]/4" size 13 color "#63dcf5"
            text "Selecciona un lugar para viajar" size 12 color "#aebfc6"


# Legacy safety alias. Anything old that still asks for `world_map`
# receives the new map instead of an obsolete household/demo screen.
screen world_map():
    use nv127_world_map


# ------------------------------------------------------------
# FINAL IN-GAME HUD — MAPA OPENS ONLY THE UNIQUE MAP SCREEN
# ------------------------------------------------------------

screen hud():
    zorder 120

    if renpy.get_screen("main_menu") is None and renpy.get_screen("developer_tools") is None and renpy.get_screen("nv127_world_map") is None:
        frame:
            xpos 12
            ypos 10
            xsize 1256
            ysize 54
            background Solid("#02080de9")
            padding (9, 7)

            hbox:
                xfill True
                spacing 10

                textbutton "MAPA":
                    action Show("nv127_world_map")
                    style "nv127_hud_map"

                text "DÍA [day]" size 13 bold True color "#e4bd68" yalign 0.5
                text nv127_period_label() size 13 bold True color "#ffffff" yalign 0.5
                text "$[coins]" size 13 bold True color "#e4bd68" yalign 0.5
                text "ENERGÍA [energy]/4" size 12 color "#63dcf5" yalign 0.5
                text "STR [strength]" size 12 color "#d7e3e7" yalign 0.5
                text "REP [reputation]" size 12 color "#d7e3e7" yalign 0.5

                null width 42

                textbutton "OBJETOS" action Show("inventory_screen") style "nv127_hud_button"
                textbutton "PERSONAS" action Show("characters_screen") style "nv127_hud_button"
                textbutton "GUARDAR" action ShowMenu("save") style "nv127_hud_button"
