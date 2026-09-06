# ============================================================
# NIGHTFALL VILLAGE v0.13.2 — HOTSPOT / SCENE POLISH
# ============================================================
# Aligns navigation labels and interactables with the dedicated v131 art.
# Walking remains free; only meaningful activities advance time.
# ============================================================

init 15000 python:

    def nv132_layout(scene_id, moves=None, actions=None):
        if scene_id not in NV130_SCENES:
            return
        if moves is not None:
            NV130_SCENES[scene_id]["moves"] = moves
        if actions is not None:
            NV130_SCENES[scene_id]["actions"] = actions

    # --------------------------------------------------------
    # PROTAGONIST HOME
    # --------------------------------------------------------
    nv132_layout("home_bedroom",
        moves=[
            ("PASILLO  →", "home_hallway", 1045, 520, "always"),
        ],
        actions=[
            ("CAMA", "sleep", 465, 525, "always"),
            ("REVISAR NOTAS", "notes", 990, 430, "always"),
        ])

    nv132_layout("home_hallway",
        moves=[
            ("DORMITORIO", "home_bedroom", 135, 430, "always"),
            ("BAÑO", "home_bathroom", 360, 315, "always"),
            ("SALIR", "home_exterior", 570, 390, "always"),
            ("SALA", "home_living", 790, 315, "always"),
            ("COCINA", "home_kitchen", 1010, 430, "always"),
        ],
        actions=[])

    nv132_layout("home_kitchen",
        moves=[
            ("←  PASILLO", "home_hallway", 35, 565, "always"),
        ],
        actions=[
            ("DESAYUNAR", "eat", 610, 485, "always"),
        ])

    nv132_layout("home_living",
        moves=[
            ("←  PASILLO", "home_hallway", 35, 565, "always"),
        ],
        actions=[
            ("MESA / CORREO", "notes", 525, 500, "always"),
        ])

    nv132_layout("home_bathroom",
        moves=[
            ("←  PASILLO", "home_hallway", 35, 565, "always"),
        ],
        actions=[
            ("ASEARSE", "wash", 720, 470, "always"),
        ])

    nv132_layout("home_exterior",
        moves=[
            ("ENTRAR", "home_hallway", 550, 355, "always"),
            ("CALLE RESIDENCIAL  →", "residential_street", 1010, 540, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # VILLAGE CENTER
    # --------------------------------------------------------
    nv132_layout("residential_street",
        moves=[
            ("←  TU CASA", "home_exterior", 30, 535, "always"),
            ("CASA DE AYA", "aya_exterior", 845, 285, "aya_house"),
            ("PLAZA  →", "village_square", 1040, 500, "always"),
        ],
        actions=[])

    nv132_layout("village_square",
        moves=[
            ("←  RESIDENCIAL", "residential_street", 30, 500, "always"),
            ("MERCADO", "market_entrance", 115, 275, "always"),
            ("ENTRENAMIENTO  →", "training_gate", 1010, 305, "always"),
            ("RÍO  ↓", "riverside_path", 555, 595, "always"),
        ],
        actions=[
            ("ESCUCHAR RUMORES", "rumors", 520, 405, "shrine_rumor"),
        ])

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------
    nv132_layout("market_entrance",
        moves=[
            ("←  PLAZA", "village_square", 30, 540, "always"),
            ("ENTRAR AL MERCADO", "market_street", 535, 410, "always"),
        ],
        actions=[])

    nv132_layout("market_street",
        moves=[
            ("←  ENTRADA", "market_entrance", 30, 540, "always"),
            ("PUESTO NOCTURNO  →", "market_night_stall", 1000, 455, "night"),
        ],
        actions=[
            ("TIENDA GENERAL", "shop", 875, 330, "day_shop"),
        ])

    # Sora is represented by the scheduled NPC hotspot; avoid a second
    # duplicated 'talk' button in the same scene.
    nv132_layout("market_night_stall",
        moves=[
            ("←  MERCADO", "market_street", 30, 540, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # TRAINING DISTRICT
    # --------------------------------------------------------
    nv132_layout("training_gate",
        moves=[
            ("←  PLAZA", "village_square", 30, 540, "always"),
            ("ENTRAR AL PATIO", "training_yard", 535, 390, "always"),
        ],
        actions=[])

    nv132_layout("training_yard",
        moves=[
            ("←  ENTRADA", "training_gate", 30, 540, "always"),
            ("DOJO", "training_dojo", 545, 285, "always"),
        ],
        actions=[
            ("ENTRENAR", "train", 300, 445, "energy"),
        ])

    nv132_layout("training_dojo",
        moves=[
            ("←  PATIO", "training_yard", 30, 540, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # RIVERSIDE
    # --------------------------------------------------------
    nv132_layout("riverside_path",
        moves=[
            ("←  PLAZA", "village_square", 30, 550, "always"),
            ("PUENTE VIEJO  →", "riverside_bridge", 995, 390, "always"),
        ],
        actions=[])

    nv132_layout("riverside_bridge",
        moves=[
            ("←  SENDERO", "riverside_path", 30, 540, "always"),
            ("ORILLA  ↓", "riverside_bank", 1010, 565, "always"),
        ],
        actions=[])

    nv132_layout("riverside_bank",
        moves=[
            ("←  PUENTE", "riverside_bridge", 30, 540, "always"),
            ("SANTUARIO  →", "shrine_path", 1010, 390, "old_shrine"),
        ],
        actions=[
            ("BUSCAR ENTRE LAS PIEDRAS", "search_river", 500, 515, "charm_search"),
        ])

    # --------------------------------------------------------
    # AYA HOUSE
    # --------------------------------------------------------
    nv132_layout("aya_exterior",
        moves=[
            ("←  CALLE", "residential_street", 30, 540, "always"),
            ("ENTRAR", "aya_hallway", 550, 375, "aya_house"),
        ],
        actions=[])

    nv132_layout("aya_hallway",
        moves=[
            ("SALA", "aya_living", 135, 430, "always"),
            ("BAÑO", "aya_bathroom", 350, 315, "always"),
            ("SALIR", "aya_exterior", 570, 390, "always"),
            ("HABITACIÓN DE AYA", "aya_room", 770, 315, "aya_room"),
            ("COCINA", "aya_kitchen", 1010, 430, "always"),
        ],
        actions=[])

    nv132_layout("aya_living",
        moves=[
            ("PASILLO  →", "aya_hallway", 1015, 565, "always"),
        ],
        actions=[
            ("REPORTES DE MISIÓN", "aya_reports", 510, 485, "always"),
        ])

    nv132_layout("aya_kitchen",
        moves=[
            ("←  PASILLO", "aya_hallway", 30, 565, "always"),
        ],
        actions=[])

    nv132_layout("aya_bathroom",
        moves=[
            ("←  PASILLO", "aya_hallway", 30, 565, "always"),
        ],
        actions=[])

    # Aya herself is the clickable target when her schedule places her here.
    nv132_layout("aya_room",
        moves=[
            ("←  PASILLO", "aya_hallway", 30, 565, "always"),
        ],
        actions=[])

    # --------------------------------------------------------
    # SHRINE / ARCHIVE
    # --------------------------------------------------------
    nv132_layout("shrine_path",
        moves=[
            ("←  RÍO", "riverside_bank", 30, 540, "always"),
            ("SUBIR AL SANTUARIO", "old_shrine", 535, 305, "always"),
        ],
        actions=[])

    nv132_layout("old_shrine",
        moves=[
            ("←  SENDERO", "shrine_path", 30, 540, "always"),
            ("PASAJE OCULTO  ↓", "hidden_passage", 535, 575, "archive"),
        ],
        actions=[
            # Always inspectable: without the Moon Token the interaction
            # itself explains that a circular key/item is missing.
            ("EXAMINAR MURO", "open_archive", 925, 430, "always"),
            ("BUSCAR ALREDEDOR", "shrine_search", 245, 485, "always"),
        ])

    nv132_layout("hidden_passage",
        moves=[
            ("←  SANTUARIO", "old_shrine", 30, 540, "always"),
            ("AVANZAR AL ARCHIVO", "archive", 535, 390, "archive"),
        ],
        actions=[])

    nv132_layout("archive",
        moves=[
            ("←  PASAJE", "hidden_passage", 30, 540, "always"),
        ],
        actions=[
            ("LEER REGISTROS", "archive_read", 525, 480, "always"),
        ])


# Compact markers keep the artwork visible while remaining easy to read.
style nv130_hotspot is button:
    background Solid("#031016c7")
    hover_background Solid("#0786a9e8")
    xpadding 11
    ypadding 7

style nv130_hotspot_text is button_text:
    size 13
    bold True
    color "#edf9fc"
    hover_color "#ffffff"
    outlines [(1, "#000000dd", 0, 0)]

style nv130_action_hotspot is nv130_hotspot:
    background Solid("#4b350bc9")
    hover_background Solid("#a77a18eb")

style nv130_action_hotspot_text is nv130_hotspot_text:
    color "#ffe8a5"
    hover_color "#fff5d5"

style nv130_locked_hotspot is button:
    background Solid("#05090cb8")
    xpadding 11
    ypadding 7

style nv130_locked_hotspot_text is button_text:
    size 12
    bold True
    color "#718087"
    outlines [(1, "#000000cc", 0, 0)]
