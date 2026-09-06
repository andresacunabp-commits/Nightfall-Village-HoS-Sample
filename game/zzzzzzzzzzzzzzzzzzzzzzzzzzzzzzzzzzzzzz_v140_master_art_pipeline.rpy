# ============================================================
# NIGHTFALL VILLAGE v0.14 — MASTER ART PIPELINE
# ============================================================
# High-quality art pass.
#
# v131 remains as a safe fallback. Whenever a true 1920x1080 master
# exists under images/backgrounds/v140/master, it automatically becomes
# the scene authority without changing navigation/event code.
# ============================================================

init 16000 python:

    NV140_ROOT = "images/backgrounds/v140/master"

    NV140_MASTER_SCENES = {
        # Protagonist home
        "home_bedroom": NV140_ROOT + "/home/bedroom.jpg",
        "home_hallway": NV140_ROOT + "/home/hallway.jpg",
        "home_kitchen": NV140_ROOT + "/home/kitchen.jpg",
        "home_living": NV140_ROOT + "/home/living_room.jpg",
        "home_bathroom": NV140_ROOT + "/home/bathroom.jpg",
        "home_exterior": NV140_ROOT + "/home/exterior.jpg",

        # Village
        "residential_street": NV140_ROOT + "/village/residential_street.jpg",
        "village_square": NV140_ROOT + "/village/village_square.jpg",

        # Market
        "market_entrance": NV140_ROOT + "/market/market_entrance.jpg",
        "market_street": NV140_ROOT + "/market/market_street.jpg",
        "market_night_stall": NV140_ROOT + "/market/night_stall.jpg",

        # Training
        "training_gate": NV140_ROOT + "/training/training_gate.jpg",
        "training_yard": NV140_ROOT + "/training/training_yard.jpg",
        "training_dojo": NV140_ROOT + "/training/dojo_interior.jpg",

        # Riverside
        "riverside_path": NV140_ROOT + "/riverside/river_path.jpg",
        "riverside_bridge": NV140_ROOT + "/riverside/old_bridge.jpg",
        "riverside_bank": NV140_ROOT + "/riverside/riverbank.jpg",

        # Aya house
        "aya_exterior": NV140_ROOT + "/aya_house/exterior.jpg",
        "aya_hallway": NV140_ROOT + "/aya_house/hallway.jpg",
        "aya_living": NV140_ROOT + "/aya_house/living_room.jpg",
        "aya_kitchen": NV140_ROOT + "/aya_house/kitchen.jpg",
        "aya_bathroom": NV140_ROOT + "/aya_house/bathroom.jpg",
        "aya_room": NV140_ROOT + "/aya_house/aya_room.jpg",

        # Shrine / archive
        "shrine_path": NV140_ROOT + "/shrine/shrine_path.jpg",
        "old_shrine": NV140_ROOT + "/shrine/old_shrine.jpg",
        "hidden_passage": NV140_ROOT + "/shrine/hidden_passage.jpg",
        "archive": NV140_ROOT + "/shrine/archive.jpg",
    }

    # True master files win; v131 stays untouched as fallback.
    for _scene_id, _master_path in NV140_MASTER_SCENES.items():
        if _scene_id in NV130_SCENES and renpy.loadable(_master_path):
            NV130_SCENES[_scene_id]["bg"] = _master_path

    NV140_MAP_BACKGROUNDS = (
        NV140_ROOT + "/map/map_morning.jpg",
        NV140_ROOT + "/map/map_day.jpg",
        NV140_ROOT + "/map/map_evening.jpg",
        NV140_ROOT + "/map/map_night.jpg",
    )

    def nv140_map_background():
        try:
            idx = max(0, min(3, int(store.period_index)))
        except Exception:
            idx = 0

        master = NV140_MAP_BACKGROUNDS[idx]
        if renpy.loadable(master):
            return master
        return nv131_map_background()

    # v131's map screen already calls nv131_map_background(). Replace that
    # resolver late so the screen itself does not need another duplicate.
    _nv131_original_map_background = nv131_map_background

    def nv131_map_background():
        try:
            idx = max(0, min(3, int(store.period_index)))
        except Exception:
            idx = 0

        master = NV140_MAP_BACKGROUNDS[idx]
        if renpy.loadable(master):
            return master
        return _nv131_original_map_background()

    def nv140_master_count():
        count = 0
        for _path in NV140_MASTER_SCENES.values():
            if renpy.loadable(_path):
                count += 1
        for _path in NV140_MAP_BACKGROUNDS:
            if renpy.loadable(_path):
                count += 1
        return count
