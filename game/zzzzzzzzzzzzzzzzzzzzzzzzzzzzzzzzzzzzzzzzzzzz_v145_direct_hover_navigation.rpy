# ============================================================
# NIGHTFALL VILLAGE v0.14.4 — DIRECT HOVER NAVIGATION
# ============================================================
# HoS-style interaction pass:
# - no permanent labels on scene hotspots
# - hover only: light the interactive region and show its name at the top
# - click immediately performs the action / movement (no confirmation menu)
# - map nodes show circular destination images
# - map hover shows the destination name at the top
# - map click travels immediately
# ============================================================


default nv144_hover_name = None
default nv144_map_hover = None


style nv144_hover_name_frame is frame:
    background Solid("#02090dd8")
    padding (18, 8)

style nv144_scene_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#54ddff32")
    xpadding 0
    ypadding 0

style nv144_action_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#ffd86f30")
    xpadding 0
    ypadding 0

style nv144_locked_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#7b858b25")
    xpadding 0
    ypadding 0

style nv144_npc_hotspot is button:
    background Solid("#00000000")
    hover_background Solid("#58e5ff2c")
    xpadding 0
    ypadding 0

style nv144_map_node is button:
    background None
    hover_background None
    xpadding 0
    ypadding 0


# ============================================================
# EXPLORATION — HOVER NAME, DIRECT CLICK
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

    add Solid("#0000000e")

    # Movement hotspots. Nothing is written on the scene permanently.
    for _label, _target, _x, _y, _gate in _scene["moves"]:
        $ _open = nv130_gate(_gate)
        $ _clean = nv143_clean_label(_label)
        $ _hx, _hy, _hw, _hh = nv143_hitbox(scene_id, "move", _target, _x, _y)

        if _open:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv144_scene_hotspot"
                hovered SetVariable("nv144_hover_name", _clean)
                unhovered SetVariable("nv144_hover_name", None)
                action [
                    SetVariable("nv144_hover_name", None),
                    Return(("move", _target)),
                ]
        else:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv144_locked_hotspot"
                hovered SetVariable("nv144_hover_name", _clean + " • BLOQUEADO")
                unhovered SetVariable("nv144_hover_name", None)
                action NullAction()

    # Object/activity hotspots. Hover names the object; click performs it.
    for _label, _action_id, _x, _y, _gate in _scene["actions"]:
        $ _usable = nv130_gate(_gate)
        $ _clean = nv143_clean_label(_label)
        $ _hx, _hy, _hw, _hh = nv143_hitbox(scene_id, "action", _action_id, _x, _y)

        if _usable:
            button:
                xpos _hx
                ypos _hy
                xsize _hw
                ysize _hh
                style "nv144_action_hotspot"
                hovered SetVariable("nv144_hover_name", _clean)
                unhovered SetVariable("nv144_hover_name", None)
                action [
                    SetVariable("nv144_hover_name", None),
                    Return(("action", _action_id)),
                ]

    # Aya: sprite is the clickable area; no HABLAR text is painted on top.
    if nv130_here_aya(scene_id):
        button:
            xpos 735
            ypos 190
            xsize 270
            ysize 390
            style "nv144_npc_hotspot"
            hovered SetVariable("nv144_hover_name", "AYA")
            unhovered SetVariable("nv144_hover_name", None)
            action [
                SetVariable("nv144_hover_name", None),
                Return(("npc", "aya")),
            ]

            fixed:
                xfill True
                yfill True
                add "images/characters/aya/aya_neutral.png":
                    xalign 0.5
                    yalign 1.0
                    zoom 0.48

    # Temporary discovery markers for NPCs that do not yet have sprites.
    if nv130_here_ren(scene_id):
        button:
            xpos 835
            ypos 250
            xsize 190
            ysize 300
            style "nv144_npc_hotspot"
            hovered SetVariable("nv144_hover_name", "REN")
            unhovered SetVariable("nv144_hover_name", None)
            action [
                SetVariable("nv144_hover_name", None),
                Return(("npc", "ren")),
            ]

            fixed:
                xfill True
                yfill True
                text "◆" size 24 color "#bfefff70" xalign 0.5 yalign 0.55

    if scene_id == "market_night_stall" and period_index == 3:
        button:
            xpos 790
            ypos 275
            xsize 210
            ysize 300
            style "nv144_npc_hotspot"
            hovered SetVariable("nv144_hover_name", "SORA")
            unhovered SetVariable("nv144_hover_name", None)
            action [
                SetVariable("nv144_hover_name", None),
                Return(("npc", "sora")),
            ]

            fixed:
                xfill True
                yfill True
                text "◆" size 24 color "#e4c87170" xalign 0.5 yalign 0.55

    # Only the hovered hotspot name appears, centered near the top.
    if nv144_hover_name:
        frame:
            xalign 0.5
            ypos 78
            style "nv144_hover_name_frame"

            text nv144_hover_name:
                size 18
                bold True
                color "#ffffff"
                xalign 0.5
                outlines [(1, "#000000dd", 0, 0)]


# ============================================================
# WORLD MAP — CIRCULAR IMAGE NODES, DIRECT TRAVEL
# ============================================================

screen nv127_world_map():
    modal True
    zorder 500

    key "game_menu" action [
        SetVariable("nv144_map_hover", None),
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

    add Solid("#0000000b")

    # Close only. No travel confirmation panel exists anymore.
    textbutton "✕":
        xpos 24
        ypos 22
        action [
            SetVariable("nv144_map_hover", None),
            Hide("nv127_world_map"),
        ]
        style "nv127_close"

    # Current time remains tucked into the upper-right corner.
    frame:
        xpos 1010
        ypos 20
        xsize 235
        ysize 58
        background Solid("#02080dc8")
        padding (13, 8)

        hbox:
            xalign 0.5
            spacing 10
            text nv127_period_label() size 15 bold True color "#ffffff" yalign 0.5
            text "DÍA [day]" size 11 bold True color "#65ddf7" yalign 0.5

    for _location_id, _node_x, _node_y in NV127_MAP_NODES:
        $ _loc = LOCATION_DATA[_location_id]
        $ _unlocked = is_location_unlocked(_location_id)
        $ _here = current_location_id == _location_id
        $ _event_ready = location_has_event(_location_id) if _unlocked else False
        $ _thumb = NV127_MAP_THUMBS[_location_id]
        $ _hover = nv144_map_hover == _location_id
        $ _name = NV127_MAP_NAMES[_location_id]
        $ _ring_color = "#6bedffff" if _hover else ("#19d9f5ff" if _here else ("#0b879fef" if _unlocked else "#566066d0"))

        button:
            xpos _node_x
            ypos _node_y
            xsize 136
            ysize 136
            style "nv144_map_node"
            hovered SetVariable("nv144_map_hover", _location_id)
            unhovered SetVariable("nv144_map_hover", None)
            action (
                [
                    SetVariable("nv144_map_hover", None),
                    SetVariable("current_location_id", _location_id),
                    Hide("nv127_world_map"),
                    Jump(_loc["label"]),
                ] if _unlocked else NullAction()
            )

            fixed:
                xfill True
                yfill True

                # Circular frame.
                text "●":
                    size 140
                    color _ring_color
                    xalign 0.5
                    yalign 0.5

                # Destination artwork is clipped to a true circle.
                add im.AlphaMask(
                    im.Scale(_thumb, 116, 116),
                    im.Scale("gui/map_circle_alpha.svg", 116, 116)
                ):
                    xpos 10
                    ypos 10

                # Locked locations keep their image but are visibly dimmed.
                if not _unlocked:
                    text "●":
                        size 122
                        color "#071014a6"
                        xalign 0.5
                        yalign 0.5

                # Small state indicators only; no permanent destination names.
                if _event_ready:
                    text "◆":
                        xpos 103
                        ypos 10
                        size 16
                        color "#ffd66f"
                        outlines [(1, "#000000cc", 0, 0)]

                if _here:
                    text "•":
                        xpos 62
                        ypos 105
                        size 20
                        color "#62ecff"
                        outlines [(1, "#000000cc", 0, 0)]

    # Like scene hotspots, only the hovered destination name is shown.
    if nv144_map_hover is not None:
        $ _hovered_map_name = NV127_MAP_NAMES[nv144_map_hover]
        $ _hovered_open = is_location_unlocked(nv144_map_hover)

        frame:
            xalign 0.5
            ypos 82
            style "nv144_hover_name_frame"

            text (_hovered_map_name if _hovered_open else _hovered_map_name + " • BLOQUEADO"):
                size 19
                bold True
                color ("#ffffff" if _hovered_open else "#86949a")
                xalign 0.5
                outlines [(1, "#000000dd", 0, 0)]

    frame:
        xalign 0.5
        ypos 665
        background Solid("#02080dc8")
        padding (14, 7)

        text "Pasa el mouse sobre un destino y haz click para viajar" size 11 color "#b8c7cc"
