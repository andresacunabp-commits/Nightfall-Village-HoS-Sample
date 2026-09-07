# ============================================================
# NIGHTFALL VILLAGE v0.14.3 — CONTEXTUAL INTERACTION REWORK
# ============================================================
# HoS-style presentation pass:
# - no permanent action/movement labels on exploration scenes
# - interactive areas glow only on mouse hover
# - clicking a hotspot opens a contextual action menu
# - map destinations are circular nodes instead of square cards
# - map travel also asks for confirmation before moving
# ============================================================


default nv143_scene_selected = None
default nv143_map_selected = None
default nv143_map_hover = None


init 20000 python:

    def nv143_clean_label(label):
        if label is None:
            return ""
        result = str(label)
        for token in ("←", "→", "↑", "↓", "↗", "↘", "↖", "↙", "🔒"):
            result = result.replace(token, "")
        return " ".join(result.split())

    def nv143_hitbox(scene_id, kind, key, x, y):
        # Existing v0.14.2 positions are already scene-aligned. Here they
        # become invisible interaction regions instead of visible buttons.
        if kind == "move":
            w, h = 220, 165
            px = int(x) - 24
            py = int(y) - 58
            if scene_id in ("home_hallway", "aya_hallway"):
                w, h = 180, 225
                px = int(x) - 14
                py = int(y) - 92
        elif kind == "action":
            w, h = 230, 145
            px = int(x) - 30
            py = int(y) - 48
        else:
            w, h = 230, 300
            px = int(x)
            py = int(y)

        px = max(0, min(1280 - w, px))
        py = max(72, min(720 - h, py))
        return px, py, w, h

    NV143_MAP_SHORT_NAMES = {
        "home": "CASA",
        "square": "PLAZA",
        "training": "ENTRENAMIENTO",
        "market": "MERCADO",
        "riverside": "RÍO",
        "aya_house": "CASA DE\nAYA",
        "old_shrine": "SANTUARIO",
        "archive": "ARCHIVO",
    }


style nv143_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#52dcff2c")
    xpadding 0
    ypadding 0

style nv143_action_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#ffd76a2b")
    xpadding 0
    ypadding 0

style nv143_locked_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#7c8b9126")
    xpadding 0
    ypadding 0

style nv143_npc_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#55e5ff25")
    xpadding 0
    ypadding 0

style nv143_context_button is button:
    background Solid("#092531e8")
    hover_background Solid("#0c7793f2")
    xfill True
    xpadding 14
    ypadding 9

style nv143_context_button_text is button_text:
    size 14
    bold True
    color "#eaf9fd"
    hover_color "#ffffff"

style nv143_cancel_button is nv143_context_button:
    background Solid("#11191de8")
    hover_background Solid("#3c4a50ef")

style nv143_map_circle is button:
    background None
    hover_background None
    xpadding 0
    ypadding 0


# ============================================================
# EXPLORATION SCENE — INVISIBLE HOTSPOTS + CLICK MENU
# ============================================================

screen nv130_scene(scene_id):
    zorder 20

    $ _scene = NV130_SCENES[scene_id]

    add Transform(_scene["bg"], xysize=(1280, 720))

    if period_index == 0:
        add Solid("#f7c77d10")
    elif period_index == 1:
        add Solid("#fff4d608")
    elif period_index == 2:
        add Solid("#b64e2425")
    else:
        add Solid("#03163055")

    add Solid("#00000010")

    # Scene/time information remains visible, but interaction labels do not.
    frame:
        xpos 965
        ypos 82
        xsize 280
        ysize 62
        background Solid("#02080dbf")
        padding (14, 8)

        vbox:
            text _scene["title"] size 18 bold True color "#ffffff" xalign 1.0
            text "DÍA {} • {}".format(day, nv127_period_label()) size 10 color "#66ddf6" xalign 1.0

    # Navigation areas: no text is rendered until the player clicks.
    for _label, _target, _x, _y, _gate in _scene["moves"]:
        $ _open = nv130_gate(_gate)
        $ _hb = nv143_hitbox(scene_id, "move", _target, _x, _y)
        $ _hx, _hy, _hw, _hh = _hb
        $ _clean = nv143_clean_label(_label)

        if _open:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv143_hotspot"
                action SetVariable("nv143_scene_selected", ("move", _clean, _target, _hx, _hy))
        else:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv143_locked_hotspot"
                action SetVariable("nv143_scene_selected", ("locked", _clean, _gate, _hx, _hy))

    # Object/activity areas: hover glow only, click opens choices.
    for _label, _action_id, _x, _y, _gate in _scene["actions"]:
        $ _usable = nv130_gate(_gate)
        $ _hb = nv143_hitbox(scene_id, "action", _action_id, _x, _y)
        $ _hx, _hy, _hw, _hh = _hb
        $ _clean = nv143_clean_label(_label)

        if _usable:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv143_action_hotspot"
                action SetVariable("nv143_scene_selected", ("action", _clean, _action_id, _hx, _hy))

    # Aya keeps her sprite but loses the permanent HABLAR label.
    if nv130_here_aya(scene_id):
        button:
            xpos 735
            ypos 190
            xsize 270
            ysize 390
            style "nv143_npc_hotspot"
            action SetVariable("nv143_scene_selected", ("npc", "AYA", "aya", 735, 190))

            fixed:
                xfill True
                yfill True
                add "images/characters/aya/aya_neutral.png":
                    xalign 0.5
                    yalign 1.0
                    zoom 0.48

    # Ren and Sora currently do not have full sprites in the portfolio build.
    # A tiny neutral marker keeps them discoverable without permanent words.
    if nv130_here_ren(scene_id):
        button:
            xpos 835
            ypos 250
            xsize 190
            ysize 300
            style "nv143_npc_hotspot"
            action SetVariable("nv143_scene_selected", ("npc", "REN", "ren", 835, 250))

            fixed:
                xfill True
                yfill True
                text "◆" size 24 color "#bfefff88" xalign 0.5 yalign 0.55

    if scene_id == "market_night_stall" and period_index == 3:
        button:
            xpos 790
            ypos 275
            xsize 210
            ysize 300
            style "nv143_npc_hotspot"
            action SetVariable("nv143_scene_selected", ("npc", "SORA", "sora", 790, 275))

            fixed:
                xfill True
                yfill True
                text "◆" size 24 color "#e4c87188" xalign 0.5 yalign 0.55

    # Clicking a hotspot opens the contextual menu instead of immediately
    # moving or performing the action.
    if nv143_scene_selected is not None:
        $ _kind, _title, _payload, _sx, _sy = nv143_scene_selected

        button:
            xpos 0
            ypos 0
            xsize 1280
            ysize 720
            background Solid("#00000018")
            action SetVariable("nv143_scene_selected", None)

        frame:
            xpos min(max(_sx + 35, 24), 940)
            ypos min(max(_sy + 45, 105), 515)
            xsize 310
            background Solid("#02090df0")
            padding (14, 13)

            vbox:
                spacing 9
                text _title size 18 bold True color "#ffffff"

                if _kind == "move":
                    textbutton "IR A " + _title:
                        action [
                            SetVariable("nv143_scene_selected", None),
                            Return(("move", _payload)),
                        ]
                        style "nv143_context_button"

                elif _kind == "action":
                    textbutton _title:
                        action [
                            SetVariable("nv143_scene_selected", None),
                            Return(("action", _payload)),
                        ]
                        style "nv143_context_button"

                elif _kind == "npc":
                    textbutton "HABLAR CON " + _title:
                        action [
                            SetVariable("nv143_scene_selected", None),
                            Return(("npc", _payload)),
                        ]
                        style "nv143_context_button"

                else:
                    text "Aún no está disponible." size 12 color "#84959c"

                textbutton "CANCELAR":
                    action SetVariable("nv143_scene_selected", None)
                    style "nv143_cancel_button"


# ============================================================
# WORLD MAP — CIRCULAR DESTINATION NODES
# ============================================================

screen nv127_world_map():
    modal True
    zorder 500

    key "game_menu" action [
        SetVariable("nv143_map_selected", None),
        SetVariable("nv143_map_hover", None),
        Hide("nv127_world_map"),
    ]

    add im.Scale(nv131_map_background(), 1280, 720)

    if period_index == 0:
        add Solid("#fff0c108")
    elif period_index == 1:
        add Solid("#ffffff04")
    elif period_index == 2:
        add Solid("#9e3d1710")
    else:
        add Solid("#02112618")

    add Solid("#0000000e")

    frame:
        xpos 930
        ypos 18
        xsize 315
        ysize 76
        background Solid("#02080dd0")
        padding (16, 10)

        vbox:
            xalign 0.5
            spacing 1
            text nv127_period_label() size 22 bold True color "#ffffff" xalign 0.5
            text "DÍA [day]" size 11 bold True color "#65ddf7" xalign 0.5
            text nv127_period_subtitle() size 10 color "#9db0b8" xalign 0.5

    textbutton "✕":
        xpos 24
        ypos 22
        action [
            SetVariable("nv143_map_selected", None),
            SetVariable("nv143_map_hover", None),
            Hide("nv127_world_map"),
        ]
        style "nv127_close"

    for _location_id, _node_x, _node_y in NV127_MAP_NODES:
        $ _loc = LOCATION_DATA[_location_id]
        $ _unlocked = is_location_unlocked(_location_id)
        $ _here = current_location_id == _location_id
        $ _event_ready = location_has_event(_location_id) if _unlocked else False
        $ _hover = nv143_map_hover == _location_id
        $ _short_name = NV143_MAP_SHORT_NAMES.get(_location_id, NV127_MAP_NAMES[_location_id])
        $ _outer = "#5de9ffff" if _hover else ("#18cfeeef" if _here else ("#0c7f99d9" if _unlocked else "#4c565bd0"))
        $ _inner = "#0b3340f5" if _hover else ("#06141bea" if _unlocked else "#101619ea")

        button:
            xpos _node_x
            ypos _node_y
            xsize 142
            ysize 142
            style "nv143_map_circle"
            hovered SetVariable("nv143_map_hover", _location_id)
            unhovered SetVariable("nv143_map_hover", None)
            action SetVariable("nv143_map_selected", _location_id)

            fixed:
                xfill True
                yfill True

                text "●":
                    size 145
                    color _outer
                    xalign 0.5
                    yalign 0.5

                text "●":
                    size 124
                    color _inner
                    xalign 0.5
                    yalign 0.5

                text _short_name:
                    xpos 14
                    ypos 50
                    xsize 114
                    text_align 0.5
                    size (11 if len(_short_name.replace("\n", "")) <= 11 else 9)
                    bold True
                    color ("#ffffff" if _unlocked else "#7b878c")
                    outlines [(1, "#000000cc", 0, 0)]

                if _event_ready:
                    text "◆":
                        xpos 101
                        ypos 18
                        size 15
                        color "#f0c86d"

                if _here:
                    text "•":
                        xpos 64
                        ypos 105
                        size 18
                        color "#62ecff"

    # Click a circle first; travel options appear only afterwards.
    if nv143_map_selected is not None:
        $ _selected_id = nv143_map_selected
        $ _selected_loc = LOCATION_DATA[_selected_id]
        $ _selected_open = is_location_unlocked(_selected_id)

        frame:
            xpos 455
            ypos 570
            xsize 370
            background Solid("#02090df2")
            padding (16, 12)

            vbox:
                spacing 8
                text _selected_loc["name"] size 19 bold True color "#ffffff" xalign 0.5

                if _selected_open:
                    textbutton "VIAJAR":
                        action [
                            SetVariable("nv143_map_selected", None),
                            SetVariable("nv143_map_hover", None),
                            SetVariable("current_location_id", _selected_id),
                            Hide("nv127_world_map"),
                            Jump(_selected_loc["label"]),
                        ]
                        style "nv143_context_button"
                else:
                    text "Aún no disponible." size 12 color "#84959c" xalign 0.5

                textbutton "CANCELAR":
                    action SetVariable("nv143_map_selected", None)
                    style "nv143_cancel_button"
