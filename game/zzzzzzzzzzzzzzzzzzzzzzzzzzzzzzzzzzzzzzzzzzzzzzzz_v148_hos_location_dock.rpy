# ============================================================
# NIGHTFALL VILLAGE v0.14.7 — HoS-STYLE LOCATION DOCK
# ============================================================
# Contextual bottom navigation for multi-room houses.
# Inspired by the interaction pattern the portfolio is targeting:
# circular room icons, hover-only names, direct travel and green
# availability dots. The polished v0.6 top HUD remains untouched.
# ============================================================


default nv147_dock_hover = None


init 28000 python:
    config.version = "0.14.7"

    NV147_DOCK_ROOT = "images/ui/room_icons"

    NV147_LOCATION_DOCKS = {
        "home": (
            ("home_bedroom",  "DORMITORIO", NV147_DOCK_ROOT + "/bed.svg",      "always"),
            ("home_bathroom", "BAÑO",       NV147_DOCK_ROOT + "/bath.svg",     "always"),
            ("home_living",   "SALA",       NV147_DOCK_ROOT + "/living.svg",   "always"),
            ("home_kitchen",  "COCINA",     NV147_DOCK_ROOT + "/kitchen.svg",  "always"),
            ("home_hallway",  "PASILLO",    NV147_DOCK_ROOT + "/hallway.svg",  "always"),
            ("home_exterior", "EXTERIOR",   NV147_DOCK_ROOT + "/exterior.svg", "always"),
        ),

        "aya_house": (
            ("aya_room",      "HABITACIÓN DE AYA", NV147_DOCK_ROOT + "/bed.svg",      "aya_room"),
            ("aya_bathroom",  "BAÑO",              NV147_DOCK_ROOT + "/bath.svg",     "always"),
            ("aya_living",    "SALA",              NV147_DOCK_ROOT + "/living.svg",   "always"),
            ("aya_kitchen",   "COCINA",            NV147_DOCK_ROOT + "/kitchen.svg",  "always"),
            ("aya_hallway",   "PASILLO",           NV147_DOCK_ROOT + "/hallway.svg",  "always"),
            ("aya_exterior",  "EXTERIOR",          NV147_DOCK_ROOT + "/exterior.svg", "always"),
        ),
    }

    def nv147_dock_items(scene_id):
        data = NV130_SCENES.get(scene_id)
        if not data:
            return ()
        return NV147_LOCATION_DOCKS.get(data.get("zone"), ())

    def nv147_dock_attention(scene_id):
        try:
            if nv130_here_aya(scene_id):
                return True
            if nv130_here_ren(scene_id):
                return True
            if scene_id == "market_night_stall" and store.period_index == 3:
                return True
        except Exception:
            pass
        return False

    if "nv147_location_dock" not in config.overlay_screens:
        config.overlay_screens.append("nv147_location_dock")


style nv147_dock_button is button:
    background None
    hover_background None
    insensitive_background None
    xpadding 0
    ypadding 0

style nv147_dock_utility is button:
    background None
    hover_background Solid("#0a405466")
    xpadding 5
    ypadding 2

style nv147_dock_utility_text is button_text:
    size 9
    color "#7f929a"
    hover_color "#ffffff"


screen nv147_location_dock():
    zorder 118

    if (renpy.get_screen("nv130_scene") is not None and
        renpy.get_screen("nv127_world_map") is None and
        renpy.get_screen("inventory_screen") is None and
        renpy.get_screen("characters_screen") is None and
        renpy.get_screen("gallery_screen") is None and
        renpy.get_screen("guide_screen") is None and
        renpy.get_screen("developer_tools") is None):

        $ _dock_items = nv147_dock_items(nv130_scene_id)

        if _dock_items:
            frame:
                xpos 8
                ypos 625
                xsize 790
                ysize 89
                background Solid("#02070aae")
                padding (7, 4)

                fixed:
                    xfill True
                    yfill True

                    hbox:
                        xpos 0
                        ypos 0
                        spacing 6

                        for _target, _label, _icon, _gate in _dock_items:
                            $ _current = nv130_scene_id == _target
                            $ _open = _current or nv130_gate(_gate)
                            $ _hovered = nv147_dock_hover == _target
                            $ _attention = nv147_dock_attention(_target)

                            button:
                                xsize 61
                                ysize 61
                                style "nv147_dock_button"
                                hovered SetVariable("nv147_dock_hover", _target)
                                unhovered SetVariable("nv147_dock_hover", None)
                                action ([SetVariable("nv147_dock_hover", None), Return(("move", _target))] if (_open and not _current) else NullAction())

                                fixed:
                                    xfill True
                                    yfill True

                                    if _hovered:
                                        text "●":
                                            size 67
                                            color "#18d9ff38"
                                            xalign 0.5
                                            yalign 0.48
                                    elif _current:
                                        text "●":
                                            size 67
                                            color "#16bddd25"
                                            xalign 0.5
                                            yalign 0.48

                                    add _icon:
                                        xalign 0.5
                                        yalign 0.5
                                        zoom 0.58
                                        alpha (1.0 if _open else 0.30)

                                    if _attention:
                                        text "●":
                                            xpos 48
                                            ypos -5
                                            size 16
                                            color "#38f06d"
                                            outlines [(1, "#00150acc", 0, 0)]

                    add Solid("#b7d6df35"):
                        xpos 0
                        ypos 64
                        xsize 775
                        ysize 1

                    hbox:
                        xpos 150
                        ypos 66
                        spacing 4

                        textbutton "Atrás" action Rollback() style "nv147_dock_utility"
                        textbutton "Historial" action ShowMenu("history") style "nv147_dock_utility"
                        textbutton "Omitir" action Skip() style "nv147_dock_utility"
                        textbutton "Automático" action Preference("auto-forward", "toggle") style "nv147_dock_utility"
                        textbutton "Guardar" action ShowMenu("save") style "nv147_dock_utility"
                        textbutton "Guard. rápido" action QuickSave() style "nv147_dock_utility"
                        textbutton "Preferencias" action ShowMenu("preferences") style "nv147_dock_utility"

            if nv147_dock_hover is not None:
                $ _hover_label = ""
                $ _hover_open = True
                for _target, _label, _icon, _gate in _dock_items:
                    if _target == nv147_dock_hover:
                        $ _hover_label = _label
                        $ _hover_open = (_target == nv130_scene_id) or nv130_gate(_gate)

                frame:
                    xpos 20
                    ypos 596
                    background Solid("#02090ddc")
                    padding (12, 5)

                    text (_hover_label if _hover_open else _hover_label + " • BLOQUEADO"):
                        size 13
                        bold True
                        color ("#ffffff" if _hover_open else "#7f8c92")
                        outlines [(1, "#000000cc", 0, 0)]
