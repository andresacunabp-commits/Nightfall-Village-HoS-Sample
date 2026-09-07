# ============================================================
# NIGHTFALL VILLAGE v0.14.2 — MASTER WORLD HOTSPOTS
# ============================================================
# Final positioning pass for the remaining 21 high-resolution masters:
# Aya House, Village, Market, Training, Riverside, Shrine and Archive.
# Movement remains free; only meaningful actions/events advance time.
# ============================================================

init 19000 python:

    def nv142_layout(scene_id, moves=None, actions=None):
        if scene_id not in NV130_SCENES:
            return
        if moves is not None:
            NV130_SCENES[scene_id]["moves"] = moves
        if actions is not None:
            NV130_SCENES[scene_id]["actions"] = actions

    # --------------------------------------------------------
    # VILLAGE CENTER
    # --------------------------------------------------------
    nv142_layout("residential_street",
        moves=[
            ("←  TU CASA", "home_exterior", 85, 455, "always"),
            ("CASA DE AYA", "aya_exterior", 330, 300, "aya_house"),
            ("PLAZA  →", "village_square", 1040, 430, "always"),
        ],
        actions=[])

    nv142_layout("village_square",
        moves=[
            ("←  RESIDENCIAL", "residential_street", 45, 515, "always"),
            ("MERCADO", "market_entrance", 105, 275, "always"),
            ("ENTRENAMIENTO  →", "training_gate", 1015, 285, "always"),
            ("RÍO  ↓", "riverside_path", 600, 565, "always"),
        ],
        actions=[
            ("ESCUCHAR RUMORES", "rumors", 535, 390, "shrine_rumor"),
        ])

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------
    nv142_layout("market_entrance",
        moves=[
            ("←  PLAZA", "village_square", 40, 535, "always"),
            ("ENTRAR AL MERCADO", "market_street", 555, 405, "always"),
        ],
        actions=[])

    nv142_layout("market_street",
        moves=[
            ("←  ENTRADA", "market_entrance", 35, 545, "always"),
            ("PUESTO NOCTURNO  →", "market_night_stall", 1010, 425, "night"),
        ],
        actions=[
            ("TIENDA GENERAL", "shop", 245, 365, "day_shop"),
        ])

    # Sora is the scheduled clickable NPC when available at night.
    nv142_layout("market_night_stall",
        moves=[
            ("←  MERCADO", "market_street", 35, 545, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # TRAINING DISTRICT
    # --------------------------------------------------------
    nv142_layout("training_gate",
        moves=[
            ("←  PLAZA", "village_square", 35, 545, "always"),
            ("ENTRAR AL PATIO", "training_yard", 535, 360, "always"),
        ],
        actions=[])

    nv142_layout("training_yard",
        moves=[
            ("←  ENTRADA", "training_gate", 1035, 520, "always"),
            ("DOJO", "training_dojo", 170, 285, "always"),
        ],
        actions=[
            ("ENTRENAR", "train", 585, 455, "energy"),
        ])

    nv142_layout("training_dojo",
        moves=[
            ("PATIO  →", "training_yard", 1030, 385, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # RIVERSIDE
    # --------------------------------------------------------
    nv142_layout("riverside_path",
        moves=[
            ("←  PLAZA", "village_square", 35, 535, "always"),
            ("PUENTE VIEJO  →", "riverside_bridge", 975, 430, "always"),
        ],
        actions=[])

    nv142_layout("riverside_bridge",
        moves=[
            ("←  SENDERO", "riverside_path", 35, 535, "always"),
            ("ORILLA  →", "riverside_bank", 1025, 500, "always"),
        ],
        actions=[])

    nv142_layout("riverside_bank",
        moves=[
            ("←  PUENTE", "riverside_bridge", 35, 535, "always"),
            ("SANTUARIO  →", "shrine_path", 1020, 390, "old_shrine"),
        ],
        actions=[
            ("BUSCAR ENTRE LAS PIEDRAS", "search_river", 300, 515, "charm_search"),
        ])

    # --------------------------------------------------------
    # AYA HOUSE
    # --------------------------------------------------------
    nv142_layout("aya_exterior",
        moves=[
            ("ENTRAR", "aya_hallway", 245, 385, "aya_house"),
            ("CALLE  →", "residential_street", 1010, 515, "always"),
        ],
        actions=[])

    nv142_layout("aya_hallway",
        moves=[
            ("SALA", "aya_living", 105, 345, "always"),
            ("BAÑO", "aya_bathroom", 350, 315, "always"),
            ("SALIR", "aya_exterior", 590, 320, "always"),
            ("HABITACIÓN DE AYA", "aya_room", 825, 315, "aya_room"),
            ("COCINA", "aya_kitchen", 1045, 345, "always"),
        ],
        actions=[])

    nv142_layout("aya_living",
        moves=[
            ("PASILLO  →", "aya_hallway", 1030, 405, "always"),
        ],
        actions=[
            ("REPORTES DE MISIÓN", "aya_reports", 595, 485, "always"),
        ])

    nv142_layout("aya_kitchen",
        moves=[
            ("PASILLO  →", "aya_hallway", 1020, 405, "always"),
        ],
        actions=[])

    nv142_layout("aya_bathroom",
        moves=[
            ("PASILLO  →", "aya_hallway", 1025, 410, "always"),
        ],
        actions=[])

    # Aya herself remains the scheduled clickable target in her room.
    nv142_layout("aya_room",
        moves=[
            ("PASILLO  →", "aya_hallway", 1020, 415, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # SHRINE / ARCHIVE
    # --------------------------------------------------------
    nv142_layout("shrine_path",
        moves=[
            ("←  RÍO", "riverside_bank", 35, 540, "always"),
            ("SUBIR AL SANTUARIO", "old_shrine", 535, 320, "always"),
        ],
        actions=[])

    nv142_layout("old_shrine",
        moves=[
            ("←  SENDERO", "shrine_path", 35, 540, "always"),
            ("PASAJE OCULTO  ↓", "hidden_passage", 545, 565, "archive"),
        ],
        actions=[
            ("EXAMINAR MURO", "open_archive", 930, 420, "always"),
            ("BUSCAR ALREDEDOR", "shrine_search", 220, 475, "always"),
        ])

    nv142_layout("hidden_passage",
        moves=[
            ("←  SANTUARIO", "old_shrine", 35, 540, "always"),
            ("AVANZAR AL ARCHIVO", "archive", 900, 355, "archive"),
        ],
        actions=[])

    nv142_layout("archive",
        moves=[
            ("←  PASAJE", "hidden_passage", 45, 455, "always"),
        ],
        actions=[
            ("LEER REGISTROS", "archive_read", 625, 500, "always"),
        ])

    # --------------------------------------------------------
    # HIGH-RES MAP NODE THUMBNAILS
    # --------------------------------------------------------
    NV142_MASTER_THUMBS = {
        "home": NV140_ROOT + "/home/exterior.jpg",
        "square": NV140_ROOT + "/village/village_square.jpg",
        "training": NV140_ROOT + "/training/training_gate.jpg",
        "market": NV140_ROOT + "/market/market_entrance.jpg",
        "riverside": NV140_ROOT + "/riverside/river_path.jpg",
        "aya_house": NV140_ROOT + "/aya_house/exterior.jpg",
        "old_shrine": NV140_ROOT + "/shrine/shrine_path.jpg",
        "archive": NV140_ROOT + "/shrine/archive.jpg",
    }

    for _location_id, _asset_path in NV142_MASTER_THUMBS.items():
        if renpy.loadable(_asset_path):
            NV127_MAP_THUMBS[_location_id] = _asset_path
