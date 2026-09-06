# ============================================================
# NIGHTFALL VILLAGE v0.13.1 — SCENE ART INTEGRATION
# ============================================================
# Connects the v131 background pack to the interactive navigation.
# Safe fallback: if an asset is missing, the previous v110 art remains.
# ============================================================

init 14000 python:

    NV131_ROOT = "images/backgrounds/v131"

    NV131_SCENE_BACKGROUNDS = {
        # Protagonist home
        "home_bedroom": NV131_ROOT + "/home/bedroom.jpg",
        "home_hallway": NV131_ROOT + "/home/hallway.jpg",
        "home_kitchen": NV131_ROOT + "/home/kitchen.jpg",
        "home_living": NV131_ROOT + "/home/living_room.jpg",
        "home_bathroom": NV131_ROOT + "/home/bathroom.jpg",
        "home_exterior": NV131_ROOT + "/home/exterior.jpg",

        # Village
        "residential_street": NV131_ROOT + "/village/residential_street.jpg",
        "village_square": NV131_ROOT + "/village/village_square.jpg",

        # Market
        "market_entrance": NV131_ROOT + "/market/market_entrance.jpg",
        "market_street": NV131_ROOT + "/market/market_street.jpg",
        "market_night_stall": NV131_ROOT + "/market/night_stall.jpg",

        # Training
        "training_gate": NV131_ROOT + "/training/training_gate.jpg",
        "training_yard": NV131_ROOT + "/training/training_yard.jpg",
        "training_dojo": NV131_ROOT + "/training/dojo_interior.jpg",

        # Riverside
        "riverside_path": NV131_ROOT + "/riverside/river_path.jpg",
        "riverside_bridge": NV131_ROOT + "/riverside/old_bridge.jpg",
        "riverside_bank": NV131_ROOT + "/riverside/riverbank.jpg",

        # Aya house
        "aya_exterior": NV131_ROOT + "/aya_house/exterior.jpg",
        "aya_hallway": NV131_ROOT + "/aya_house/hallway.jpg",
        "aya_living": NV131_ROOT + "/aya_house/living_room.jpg",
        "aya_kitchen": NV131_ROOT + "/aya_house/kitchen.jpg",
        "aya_bathroom": NV131_ROOT + "/aya_house/bathroom.jpg",
        "aya_room": NV131_ROOT + "/aya_house/aya_room.jpg",

        # Shrine / archive
        "shrine_path": NV131_ROOT + "/shrine/shrine_path.jpg",
        "old_shrine": NV131_ROOT + "/shrine/old_shrine.jpg",
        "hidden_passage": NV131_ROOT + "/shrine/hidden_passage.jpg",
        "archive": NV131_ROOT + "/shrine/archive.jpg",
    }

    # Apply only files that really exist. This keeps the branch bootable
    # even while the binary art pack is still being synchronized.
    for _scene_id, _asset_path in NV131_SCENE_BACKGROUNDS.items():
        if _scene_id in NV130_SCENES and renpy.loadable(_asset_path):
            NV130_SCENES[_scene_id]["bg"] = _asset_path

    # Representative thumbnails for the world map nodes.
    NV131_MAP_THUMBS = {
        "home": NV131_ROOT + "/home/exterior.jpg",
        "square": NV131_ROOT + "/village/village_square.jpg",
        "training": NV131_ROOT + "/training/training_gate.jpg",
        "market": NV131_ROOT + "/market/market_entrance.jpg",
        "riverside": NV131_ROOT + "/riverside/river_path.jpg",
        "aya_house": NV131_ROOT + "/aya_house/exterior.jpg",
        "old_shrine": NV131_ROOT + "/shrine/shrine_path.jpg",
        "archive": NV131_ROOT + "/shrine/archive.jpg",
    }

    for _location_id, _asset_path in NV131_MAP_THUMBS.items():
        if renpy.loadable(_asset_path):
            NV127_MAP_THUMBS[_location_id] = _asset_path

    NV131_MAP_BACKGROUNDS = (
        NV131_ROOT + "/map/map_morning.jpg",
        NV131_ROOT + "/map/map_day.jpg",
        NV131_ROOT + "/map/map_evening.jpg",
        NV131_ROOT + "/map/map_night.jpg",
    )

    def nv131_map_background():
        try:
            idx = max(0, min(3, int(store.period_index)))
        except Exception:
            idx = 0

        candidate = NV131_MAP_BACKGROUNDS[idx]
        if renpy.loadable(candidate):
            return candidate
        return "images/backgrounds/v110/village_square.jpg"

    def nv131_asset_count():
        count = 0
        for path in NV131_SCENE_BACKGROUNDS.values():
            if renpy.loadable(path):
                count += 1
        for path in NV131_MAP_BACKGROUNDS:
            if renpy.loadable(path):
                count += 1
        return count


# ------------------------------------------------------------
# WORLD MAP — ACTUAL MORNING / DAY / EVENING / NIGHT ART
# ------------------------------------------------------------
# This late screen definition intentionally supersedes v0.12.7 while
# keeping the same name, so the existing MAPA button needs no changes.

screen nv127_world_map():
    modal True
    zorder 500

    key "game_menu" action Hide("nv127_world_map")

    add im.Scale(nv131_map_background(), 1280, 720)

    # Each map already has its own lighting. Only a light readability
    # overlay is applied so the actual artwork remains visible.
    if period_index == 0:
        add Solid("#fff0c10a")
    elif period_index == 1:
        add Solid("#ffffff05")
    elif period_index == 2:
        add Solid("#9e3d1712")
    else:
        add Solid("#0211261e")

    add Solid("#00000012")

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

    textbutton "✕":
        xpos 24
        ypos 22
        action Hide("nv127_world_map")
        style "nv127_close"

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
