# ============================================================
# NIGHTFALL VILLAGE v0.14.6 — SAFE CIRCULAR MAP THUMBNAILS
# ============================================================
# Fixes Ren'Py's "AlphaMask surfaces must be the same size" warning.
# The previous build scaled an SVG alpha mask at runtime. Ren'Py could
# rasterize that SVG at a different surface size than the location image.
# This pass uses one native 116x116 PNG mask, exactly matching every
# scaled destination thumbnail.
# ============================================================

init 27000 python:
    config.version = "0.14.6"
    NV146_MAP_MASK = "gui/map_circle_mask_116.png"


style nv146_map_node is button:
    background None
    hover_background None
    insensitive_background None
    xpadding 0
    ypadding 0


screen nv127_world_map():
    modal True
    zorder 500

    key "game_menu" action [
        SetVariable("nv144_map_hover", None),
        Hide("nv127_world_map"),
    ]

    # Dynamic morning / day / evening / night master artwork.
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

    textbutton "✕":
        xpos 24
        ypos 22
        action [
            SetVariable("nv144_map_hover", None),
            Hide("nv127_world_map"),
        ]
        style "nv127_close"

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
        $ _thumb = NV127_MAP_THUMBS.get(_location_id, None)
        $ _hover = nv144_map_hover == _location_id
        $ _name = NV127_MAP_NAMES[_location_id]
        $ _ring_color = "#70f1ffff" if _hover else ("#1bdcf7ff" if _here else ("#0a8199ee" if _unlocked else "#525d63dd"))

        button:
            xpos _node_x
            ypos _node_y
            xsize 136
            ysize 136
            style "nv146_map_node"
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

                # Outer cyan circle. The location image sits inside it.
                text "●":
                    size 142
                    color _ring_color
                    xalign 0.5
                    yalign 0.5

                # IMPORTANT: both surfaces are exactly 116x116.
                # No SVG runtime rasterization is involved anymore.
                if _thumb and renpy.loadable(_thumb):
                    add im.AlphaMask(
                        im.Scale(_thumb, 116, 116),
                        NV146_MAP_MASK
                    ):
                        xpos 10
                        ypos 10
                else:
                    text "●":
                        size 116
                        color "#07131add"
                        xpos 10
                        ypos 4

                if not _unlocked:
                    text "●":
                        size 116
                        color "#071014a8"
                        xpos 10
                        ypos 4

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

    # Only the hovered destination name is shown. Clicking travels directly.
    if nv144_map_hover is not None:
        $ _hovered_map_name = NV127_MAP_NAMES[nv144_map_hover]
        $ _hovered_open = is_location_unlocked(nv144_map_hover)

        frame:
            xalign 0.5
            ypos 82
            background Solid("#02090dd8")
            padding (18, 8)

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
