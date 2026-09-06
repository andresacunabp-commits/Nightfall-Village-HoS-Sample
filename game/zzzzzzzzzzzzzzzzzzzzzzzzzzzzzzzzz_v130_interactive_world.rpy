# ============================================================
# NIGHTFALL VILLAGE v0.13.0 — INTERACTIVE WORLD NAVIGATION
# ============================================================
# Navigation is scene-first: the player clicks doors, paths and
# buildings directly on the current background. Movement itself does
# NOT advance time. Only meaningful activities/events advance time.
# ============================================================


default nv130_scene_id = "home_bedroom"
default nv130_ate_day = 0
default nv130_washed_day = 0
default nv130_scene_visits = {}


init 13000 python:

    # Major-map destinations now land at an entry scene, not at the old
    # text-menu location labels.
    LOCATION_DATA["home"]["label"] = "nv130_map_home"
    LOCATION_DATA["square"]["label"] = "nv130_map_square"
    LOCATION_DATA["training"]["label"] = "nv130_map_training"
    LOCATION_DATA["market"]["label"] = "nv130_map_market"
    LOCATION_DATA["riverside"]["label"] = "nv130_map_riverside"
    LOCATION_DATA["aya_house"]["label"] = "nv130_map_aya_house"
    LOCATION_DATA["old_shrine"]["label"] = "nv130_map_shrine"
    LOCATION_DATA["archive"]["label"] = "nv130_map_archive"

    NV130_SCENES = {
        # ----------------------------------------------------
        # PROTAGONIST HOME
        # ----------------------------------------------------
        "home_bedroom": {
            "title": "Dormitorio",
            "zone": "home",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("PASILLO  →", "home_hallway", 1015, 425, "always"),
            ],
            "actions": [
                ("CAMA", "sleep", 120, 500, "always"),
                ("REVISAR NOTAS", "notes", 430, 520, "always"),
            ],
        },
        "home_hallway": {
            "title": "Pasillo de casa",
            "zone": "home",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  DORMITORIO", "home_bedroom", 55, 405, "always"),
                ("COCINA  →", "home_kitchen", 1010, 285, "always"),
                ("SALA  →", "home_living", 980, 475, "always"),
                ("BAÑO", "home_bathroom", 510, 265, "always"),
                ("SALIR  ↓", "home_exterior", 535, 580, "always"),
            ],
            "actions": [],
        },
        "home_kitchen": {
            "title": "Cocina",
            "zone": "home",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "home_hallway", 45, 545, "always"),
            ],
            "actions": [
                ("DESAYUNAR", "eat", 830, 480, "always"),
            ],
        },
        "home_living": {
            "title": "Sala",
            "zone": "home",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "home_hallway", 45, 545, "always"),
            ],
            "actions": [
                ("MESA / CORREO", "notes", 800, 470, "always"),
            ],
        },
        "home_bathroom": {
            "title": "Baño",
            "zone": "home",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "home_hallway", 45, 545, "always"),
            ],
            "actions": [
                ("ASEARSE", "wash", 780, 455, "always"),
            ],
        },
        "home_exterior": {
            "title": "Exterior de casa",
            "zone": "home",
            "bg": "images/backgrounds/v110/village_square.jpg",
            "moves": [
                ("ENTRAR  ↑", "home_hallway", 540, 120, "always"),
                ("CALLE RESIDENCIAL  →", "residential_street", 920, 430, "always"),
            ],
            "actions": [],
        },

        # ----------------------------------------------------
        # VILLAGE CENTER
        # ----------------------------------------------------
        "residential_street": {
            "title": "Calle residencial",
            "zone": "square",
            "bg": "images/backgrounds/v110/village_square.jpg",
            "moves": [
                ("←  TU CASA", "home_exterior", 45, 470, "always"),
                ("PLAZA  →", "village_square", 1000, 370, "always"),
                ("CASA DE AYA", "aya_exterior", 510, 210, "aya_house"),
            ],
            "actions": [],
        },
        "village_square": {
            "title": "Plaza de Nightfall",
            "zone": "square",
            "bg": "images/backgrounds/v110/village_square.jpg",
            "moves": [
                ("←  RESIDENCIAL", "residential_street", 45, 465, "always"),
                ("MERCADO  ↗", "market_entrance", 940, 205, "always"),
                ("ENTRENAMIENTO  →", "training_gate", 990, 405, "always"),
                ("RÍO  ↓", "riverside_path", 545, 590, "always"),
            ],
            "actions": [
                ("ESCUCHAR RUMORES", "rumors", 470, 355, "shrine_rumor"),
            ],
        },

        # ----------------------------------------------------
        # MARKET
        # ----------------------------------------------------
        "market_entrance": {
            "title": "Entrada del mercado",
            "zone": "market",
            "bg": "images/backgrounds/v110/market_alley.jpg",
            "moves": [
                ("←  PLAZA", "village_square", 45, 520, "always"),
                ("CALLE DEL MERCADO  →", "market_street", 920, 380, "always"),
            ],
            "actions": [],
        },
        "market_street": {
            "title": "Calle del mercado",
            "zone": "market",
            "bg": "images/backgrounds/v110/market_alley.jpg",
            "moves": [
                ("←  ENTRADA", "market_entrance", 45, 520, "always"),
                ("PUESTO NOCTURNO  →", "market_night_stall", 980, 450, "night"),
            ],
            "actions": [
                ("TIENDA GENERAL", "shop", 430, 355, "day_shop"),
            ],
        },
        "market_night_stall": {
            "title": "Puesto nocturno",
            "zone": "market",
            "bg": "images/backgrounds/v110/market_alley.jpg",
            "moves": [
                ("←  MERCADO", "market_street", 45, 520, "always"),
            ],
            "actions": [
                ("HABLAR CON SORA", "sora", 790, 405, "night"),
            ],
        },

        # ----------------------------------------------------
        # TRAINING DISTRICT
        # ----------------------------------------------------
        "training_gate": {
            "title": "Entrada de entrenamiento",
            "zone": "training",
            "bg": "images/backgrounds/v110/training_ground.jpg",
            "moves": [
                ("←  PLAZA", "village_square", 45, 520, "always"),
                ("PATIO  →", "training_yard", 970, 385, "always"),
            ],
            "actions": [],
        },
        "training_yard": {
            "title": "Patio de entrenamiento",
            "zone": "training",
            "bg": "images/backgrounds/v110/training_ground.jpg",
            "moves": [
                ("←  ENTRADA", "training_gate", 45, 520, "always"),
                ("DOJO  →", "training_dojo", 980, 265, "always"),
            ],
            "actions": [
                ("MUÑECO DE ENTRENAMIENTO", "train", 430, 455, "energy"),
            ],
        },
        "training_dojo": {
            "title": "Dojo",
            "zone": "training",
            "bg": "images/backgrounds/v110/training_ground.jpg",
            "moves": [
                ("←  PATIO", "training_yard", 45, 520, "always"),
            ],
            "actions": [],
        },

        # ----------------------------------------------------
        # RIVERSIDE
        # ----------------------------------------------------
        "riverside_path": {
            "title": "Sendero del río",
            "zone": "riverside",
            "bg": "images/backgrounds/v110/riverside.jpg",
            "moves": [
                ("↑  PLAZA", "village_square", 530, 105, "always"),
                ("PUENTE VIEJO  →", "riverside_bridge", 980, 420, "always"),
            ],
            "actions": [],
        },
        "riverside_bridge": {
            "title": "Puente viejo",
            "zone": "riverside",
            "bg": "images/backgrounds/v110/riverside.jpg",
            "moves": [
                ("←  SENDERO", "riverside_path", 45, 520, "always"),
                ("ORILLA  ↓", "riverside_bank", 560, 575, "always"),
            ],
            "actions": [],
        },
        "riverside_bank": {
            "title": "Orilla del río",
            "zone": "riverside",
            "bg": "images/backgrounds/v110/riverside.jpg",
            "moves": [
                ("↑  PUENTE", "riverside_bridge", 530, 105, "always"),
                ("SENDERO AL SANTUARIO  →", "shrine_path", 930, 430, "old_shrine"),
            ],
            "actions": [
                ("BUSCAR ENTRE LAS PIEDRAS", "search_river", 350, 505, "charm_search"),
            ],
        },

        # ----------------------------------------------------
        # AYA HOUSE — INCLUDING BATHROOM
        # ----------------------------------------------------
        "aya_exterior": {
            "title": "Casa de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_ext.jpg",
            "moves": [
                ("←  CALLE", "residential_street", 45, 520, "always"),
                ("ENTRAR  ↑", "aya_hallway", 550, 145, "aya_house"),
            ],
            "actions": [],
        },
        "aya_hallway": {
            "title": "Pasillo de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("SALIR  ↓", "aya_exterior", 520, 575, "always"),
                ("SALA  ←", "aya_living", 45, 355, "always"),
                ("COCINA  →", "aya_kitchen", 1010, 355, "always"),
                ("BAÑO", "aya_bathroom", 515, 250, "always"),
                ("HABITACIÓN DE AYA", "aya_room", 875, 190, "aya_room"),
            ],
            "actions": [],
        },
        "aya_living": {
            "title": "Sala de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("PASILLO  →", "aya_hallway", 1010, 520, "always"),
            ],
            "actions": [
                ("REPORTES DE MISIÓN", "aya_reports", 450, 445, "always"),
            ],
        },
        "aya_kitchen": {
            "title": "Cocina de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "aya_hallway", 45, 520, "always"),
            ],
            "actions": [],
        },
        "aya_bathroom": {
            "title": "Baño de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "aya_hallway", 45, 520, "always"),
            ],
            "actions": [],
        },
        "aya_room": {
            "title": "Habitación de Aya",
            "zone": "aya_house",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASILLO", "aya_hallway", 45, 520, "always"),
            ],
            "actions": [
                ("HABLAR CON AYA", "aya", 790, 405, "always"),
            ],
        },

        # ----------------------------------------------------
        # SHRINE / ARCHIVE
        # ----------------------------------------------------
        "shrine_path": {
            "title": "Sendero del santuario",
            "zone": "old_shrine",
            "bg": "images/backgrounds/v110/shrine_path.jpg",
            "moves": [
                ("←  RÍO", "riverside_bank", 45, 520, "always"),
                ("SANTUARIO  →", "old_shrine", 965, 390, "always"),
            ],
            "actions": [],
        },
        "old_shrine": {
            "title": "Santuario viejo",
            "zone": "old_shrine",
            "bg": "images/backgrounds/v110/shrine_path.jpg",
            "moves": [
                ("←  SENDERO", "shrine_path", 45, 520, "always"),
                ("PASAJE OCULTO  ↓", "hidden_passage", 535, 570, "archive"),
            ],
            "actions": [
                ("EXAMINAR MURO", "open_archive", 815, 420, "moon_token"),
                ("BUSCAR EN EL SANTUARIO", "shrine_search", 300, 450, "always"),
            ],
        },
        "hidden_passage": {
            "title": "Pasaje oculto",
            "zone": "archive",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("↑  SANTUARIO", "old_shrine", 520, 105, "always"),
                ("ARCHIVO  →", "archive", 980, 420, "archive"),
            ],
            "actions": [],
        },
        "archive": {
            "title": "Archivo oculto",
            "zone": "archive",
            "bg": "images/backgrounds/v110/aya_house_hallway.jpg",
            "moves": [
                ("←  PASAJE", "hidden_passage", 45, 520, "always"),
            ],
            "actions": [
                ("LEER REGISTROS", "archive_read", 530, 420, "always"),
            ],
        },
    }

    def nv130_gate(gate):
        if gate == "always":
            return True
        if gate == "energy":
            return store.energy > 0
        if gate == "night":
            return store.period_index == 3
        if gate == "day_shop":
            return store.period_index < 3
        if gate == "aya_house":
            return is_location_unlocked("aya_house")
        if gate == "aya_room":
            return (
                relation("aya", "love") + relation("aya", "hatred") >= 2 or
                store.flags.get("aya_charm_returned", False)
            )
        if gate == "old_shrine":
            return is_location_unlocked("old_shrine")
        if gate == "archive":
            return is_location_unlocked("archive")
        if gate == "moon_token":
            return has_item("Moon Token") and not is_location_unlocked("archive")
        if gate == "charm_search":
            return (
                store.quests.get("aya_charm") == "active" and
                not has_item("Silver Charm") and
                not store.seen_events.get("find_charm", False)
            )
        if gate == "shrine_rumor":
            return (
                not is_location_unlocked("old_shrine") and
                store.reputation >= 2 and
                store.period_index >= 2
            )
        return False

    def nv130_set_scene(scene_id):
        store.nv130_scene_id = scene_id
        data = NV130_SCENES.get(scene_id)
        if data:
            store.current_location_id = data["zone"]
            store.nv130_scene_visits[scene_id] = store.nv130_scene_visits.get(scene_id, 0) + 1

    def nv130_here_aya(scene_id):
        loc = npc_location("aya")
        if scene_id == "village_square" and loc == "square":
            return True
        if scene_id == "riverside_bank" and loc == "riverside":
            return True
        if scene_id in ("aya_hallway", "aya_living", "aya_room") and loc == "aya_house":
            return True
        return False

    def nv130_here_ren(scene_id):
        loc = npc_location("ren")
        return (
            (scene_id == "training_yard" and loc == "training") or
            (scene_id == "village_square" and loc == "square")
        )


style nv130_hotspot is button:
    background Solid("#02080dc4")
    hover_background Solid("#087c9bdd")
    xpadding 14
    ypadding 9

style nv130_hotspot_text is button_text:
    size 15
    bold True
    color "#edf8fb"
    hover_color "#ffffff"
    outlines [(1, "#000000cc", 0, 0)]

style nv130_action_hotspot is nv130_hotspot:
    background Solid("#3d2b0bc8")
    hover_background Solid("#9c731ae0")

style nv130_action_hotspot_text is nv130_hotspot_text:
    color "#ffe5a1"

style nv130_locked_hotspot is button:
    background Solid("#020608a8")
    xpadding 14
    ypadding 9

style nv130_locked_hotspot_text is button_text:
    size 14
    color "#66767d"

style nv130_npc_hotspot is button:
    background Solid("#06131cd9")
    hover_background Solid("#0a6079e8")
    xpadding 16
    ypadding 10

style nv130_npc_hotspot_text is button_text:
    size 16
    bold True
    color "#ffffff"
    hover_color "#ffffff"


screen nv130_scene(scene_id):
    zorder 20

    $ _scene = NV130_SCENES[scene_id]

    add Transform(_scene["bg"], xysize=(1280, 720))

    # Consistent world-time lighting. Dedicated scene art can replace
    # these reused master backgrounds without touching navigation logic.
    if period_index == 0:
        add Solid("#f7c77d10")
    elif period_index == 1:
        add Solid("#fff4d608")
    elif period_index == 2:
        add Solid("#b64e2425")
    else:
        add Solid("#03163055")

    add Solid("#00000016")

    # Scene identity card. No movement list/menu is shown.
    frame:
        xpos 875
        ypos 82
        xsize 370
        ysize 72
        background Solid("#02080dda")
        padding (16, 9)

        vbox:
            text _scene["title"] size 22 bold True color "#ffffff" xalign 1.0
            text "{} • DÍA {} • {}".format(LOCATION_DATA[_scene["zone"]]["name"], day, nv127_period_label()) size 11 color "#66ddf6" xalign 1.0

    # Doors, streets and paths are clickable directly on the scene.
    for _label, _target, _x, _y, _gate in _scene["moves"]:
        $ _open = nv130_gate(_gate)
        if _open:
            textbutton _label:
                xpos _x
                ypos _y
                action Return(("move", _target))
                style "nv130_hotspot"
        else:
            textbutton "🔒 " + _label:
                xpos _x
                ypos _y
                action NullAction()
                style "nv130_locked_hotspot"

    # Objects/activities. These may advance time; walking does not.
    for _label, _action_id, _x, _y, _gate in _scene["actions"]:
        $ _usable = nv130_gate(_gate)
        if _usable:
            textbutton _label:
                xpos _x
                ypos _y
                action Return(("action", _action_id))
                style "nv130_action_hotspot"

    # NPCs appear according to the existing schedule system.
    if nv130_here_aya(scene_id):
        button:
            xpos 735
            ypos 190
            xsize 270
            ysize 390
            background None
            hover_background Solid("#00c8ff12")
            action Return(("npc", "aya"))

            fixed:
                xfill True
                yfill True
                add "images/characters/aya/aya_neutral.png":
                    xalign 0.5
                    yalign 1.0
                    zoom 0.48
                text "AYA  •  HABLAR":
                    xpos 45
                    ypos 335
                    size 14
                    bold True
                    color "#ffffff"
                    outlines [(2, "#000000dd", 0, 0)]

    if nv130_here_ren(scene_id):
        textbutton "REN  •  HABLAR":
            xpos 850
            ypos 315
            action Return(("npc", "ren"))
            style "nv130_npc_hotspot"

    if scene_id == "market_night_stall" and period_index == 3:
        textbutton "SORA":
            xpos 805
            ypos 335
            action Return(("npc", "sora"))
            style "nv130_npc_hotspot"


# ============================================================
# NEW GAME / EXPLORATION LOOP
# ============================================================

label nv130_start:
    $ nv130_set_scene("home_bedroom")

    scene bg_home
    with fade

    centered "{size=50}{b}NIGHTFALL VILLAGE{/b}{/size}\n{size=20}Día 1 • Mañana{/size}"
    pause 0.5

    mc "Otra asignación en Nightfall Village."
    mc "Esta vez no hay una ruta marcada. Yo decido dónde ir y cómo gastar el día."

    jump nv130_explore


label nv130_explore:
    $ _scene_data = NV130_SCENES.get(nv130_scene_id)
    if not _scene_data:
        $ nv130_set_scene("home_bedroom")

    call screen nv130_scene(nv130_scene_id)

    if not _return:
        jump nv130_explore

    if _return[0] == "move":
        $ nv130_set_scene(_return[1])
        jump nv130_explore

    if _return[0] == "npc":
        if _return[1] == "aya":
            jump nv130_talk_aya
        elif _return[1] == "ren":
            jump nv130_talk_ren
        elif _return[1] == "sora":
            jump nv130_talk_sora

    if _return[0] == "action":
        if _return[1] == "sleep":
            jump nv130_sleep
        elif _return[1] == "notes":
            jump nv130_notes
        elif _return[1] == "eat":
            jump nv130_eat
        elif _return[1] == "wash":
            jump nv130_wash
        elif _return[1] == "train":
            jump nv130_train
        elif _return[1] == "shop":
            jump nv130_shop
        elif _return[1] == "search_river":
            jump nv130_search_river
        elif _return[1] == "rumors":
            jump nv130_rumors
        elif _return[1] == "open_archive":
            jump nv130_open_archive
        elif _return[1] == "shrine_search":
            jump nv130_shrine_search
        elif _return[1] == "archive_read":
            jump nv130_archive_read
        elif _return[1] == "aya_reports":
            jump nv130_aya_reports
        elif _return[1] == "sora":
            jump nv130_talk_sora

    jump nv130_explore


# ============================================================
# MAP ENTRY LABELS
# ============================================================

label nv130_map_home:
    $ nv130_set_scene("home_exterior")
    jump nv130_explore

label nv130_map_square:
    $ nv130_set_scene("village_square")
    jump nv130_explore

label nv130_map_training:
    $ nv130_set_scene("training_gate")
    jump nv130_explore

label nv130_map_market:
    $ nv130_set_scene("market_entrance")
    jump nv130_explore

label nv130_map_riverside:
    $ nv130_set_scene("riverside_path")
    jump nv130_explore

label nv130_map_aya_house:
    $ nv130_set_scene("aya_exterior")
    jump nv130_explore

label nv130_map_shrine:
    $ nv130_set_scene("shrine_path")
    jump nv130_explore

label nv130_map_archive:
    $ nv130_set_scene("archive")
    jump nv130_explore


# ============================================================
# OBJECT / ACTIVITY INTERACTIONS
# ============================================================

label nv130_sleep:
    scene bg_home
    with dissolve
    "Te preparas para terminar el día."
    $ start_new_day()
    $ nv130_set_scene("home_bedroom")
    "Una nueva mañana comienza."
    jump nv130_explore


label nv130_notes:
    $ _nv130_goals = guide_objectives()
    if _nv130_goals:
        $ _nv130_cat, _nv130_goal = _nv130_goals[0]
        "Objetivo actual — [_nv130_cat]: [_nv130_goal]"
    else:
        "No hay nada urgente anotado."
    jump nv130_explore


label nv130_eat:
    if nv130_ate_day == day:
        "Ya comiste algo hoy."
    else:
        $ nv130_ate_day = day
        $ energy = min(4, energy + 1)
        "Preparas algo rápido. Energía recuperada."
    jump nv130_explore


label nv130_wash:
    if nv130_washed_day == day:
        "Ya te arreglaste hoy."
    else:
        $ nv130_washed_day = day
        "Te aseas y te preparas para salir."
    jump nv130_explore


label nv130_train:
    if energy <= 0:
        "Estás demasiado cansado para entrenar."
        jump nv130_explore

    "Golpeas el muñeco una y otra vez hasta corregir tu postura."
    $ change_stat("strength", 1)
    $ spend_time(1)
    $ nv130_set_scene("training_yard")
    jump nv130_explore


label nv130_shop:
    merchant "¿Buscas algo?"

    menu:
        "Flores — 10 monedas" if coins >= 10:
            $ coins -= 10
            $ add_item("Flowers")
            merchant "Buena elección."

        "Snack de energía — 8 monedas" if coins >= 8:
            $ coins -= 8
            $ add_item("Energy Snack")
            merchant "Te vendrá bien."

        "Solo estaba mirando":
            pass

    $ nv130_set_scene("market_street")
    jump nv130_explore


label nv130_search_river:
    "Algo brilla entre las piedras mojadas."
    $ mark_event("find_charm")
    $ add_item("Silver Charm")
    "Encontraste el amuleto plateado de Aya."
    $ spend_time(1)
    $ nv130_set_scene("riverside_bank")
    jump nv130_explore


label nv130_rumors:
    "Dos residentes bajan la voz al verte pasar."
    "Residente" "Dicen que el viejo sendero del santuario volvió a abrirse."
    "Residente" "Yo no iría de noche."
    $ mark_event("shrine_rumor")
    $ unlock_location("old_shrine")
    $ spend_time(1)
    $ nv130_set_scene("village_square")
    jump nv130_explore


label nv130_open_archive:
    if not has_item("Moon Token"):
        "Hay una hendidura circular en la piedra, pero te falta algo."
        jump nv130_explore

    "El Moon Token encaja perfectamente en la pared."
    $ remove_item("Moon Token")
    $ flags["moon_token_used"] = True
    $ mark_event("archive_discovery")
    $ unlock_location("archive")
    "Una sección del muro se desplaza y deja ver una escalera."
    $ spend_time(1)
    $ nv130_set_scene("hidden_passage")
    jump nv130_explore


label nv130_shrine_search:
    if not flags.get("shrine_searched", False):
        $ flags["shrine_searched"] = True
        $ coins += 10
        "Encuentras una pequeña reserva escondida: 10 monedas."
    else:
        "No encuentras nada nuevo."
    jump nv130_explore


label nv130_archive_read:
    if dominant_route("aya") == "Love":
        "Un registro habla de dos agentes que sobrevivieron gracias a la confianza mutua."
    elif dominant_route("aya") == "Hatred":
        "Un registro describe una alianza destruida por una rivalidad que nunca se detuvo."
    else:
        "Los documentos mencionan relaciones y decisiones que todavía no comprendes del todo."
    $ spend_time(1)
    $ nv130_set_scene("archive")
    jump nv130_explore


label nv130_aya_reports:
    "La mesa está cubierta de informes y rutas de entrega."
    if npc_location("aya") == "aya_house":
        aya "Si vas a quedarte mirando, al menos ayúdame a ordenarlos."
        $ change_stat("reputation", 1)
        $ change_relation("aya", "love", 1)
        $ spend_time(1)
    else:
        "Aya no está en casa ahora mismo."
    $ nv130_set_scene("aya_living")
    jump nv130_explore


# ============================================================
# NPC INTERACTIONS
# ============================================================

label nv130_talk_aya:
    if not seen_events.get("aya_intro", False):
        $ mark_event("aya_intro")
        $ quests["aya_charm"] = "active"

        aya "Eres quien volvió al pueblo, ¿verdad?"
        mc "Ese soy yo."
        aya "Perdí un amuleto plateado cerca del río."

        menu:
            "Te ayudaré a encontrarlo":
                $ change_relation("aya", "love", 1)
                aya "Gracias. Te debo una."

            "Solo si admites que soy más rápido":
                $ change_relation("aya", "hatred", 1)
                aya "Ya estás empezando a molestarme."

        $ spend_time(1)

    elif quests.get("aya_charm") == "active" and has_item("Silver Charm"):
        $ mark_event("return_charm")
        $ remove_item("Silver Charm")
        $ quests["aya_charm"] = "complete"
        $ flags["aya_charm_returned"] = True
        $ change_stat("reputation", 1)

        aya "¿De verdad lo encontraste?"

        menu:
            "Devolvérselo sin pedir nada":
                $ change_relation("aya", "love", 2)
                aya "Te subestimé."

            "Hacer que admita que ganaste":
                $ change_relation("aya", "hatred", 2)
                aya "Bien. Ganaste esta vez."

        $ spend_time(1)

    elif (
        flags.get("aya_charm_returned", False) and
        not is_location_unlocked("aya_house") and
        day >= 2 and
        period_index >= 1 and
        relation("aya", "love") >= 3
    ):
        $ mark_event("aya_house_invite")
        $ unlock_location("aya_house")
        aya "Pasa por mi casa cuando quieras. Quiero enseñarte algo."
        $ spend_time(1)

    else:
        if dominant_route("aya") == "Love":
            aya "Últimamente apareces justo cuando necesito compañía."
        elif dominant_route("aya") == "Hatred":
            aya "¿Otra vez buscando competir conmigo?"
        else:
            aya "¿Necesitabas algo?"

        menu:
            "Ser amable":
                $ change_relation("aya", "love", 1)
                aya "No esperaba eso de ti."

            "Provocarla":
                $ change_relation("aya", "hatred", 1)
                aya "Sigue hablando."

            "Terminar la conversación":
                pass

        $ spend_time(1)

    jump nv130_explore


label nv130_talk_ren:
    if not seen_events.get("ren_intro", False):
        $ mark_event("ren_intro")
        $ flags["ren_met"] = True
        ren "Mirar no te hará más fuerte."

        menu:
            "Pedirle que te enseñe":
                $ change_relation("ren", "love", 1)
                ren "Entonces empieza por la disciplina."

            "Decirle que puedes seguirle el ritmo":
                $ change_relation("ren", "hatred", 1)
                ren "Ya veremos."

        $ spend_time(1)
    else:
        ren "La técnica antes que la velocidad."
        $ change_relation("ren", "love", 1)
        $ spend_time(1)

    $ nv130_set_scene("training_yard" if npc_location("ren") == "training" else "village_square")
    jump nv130_explore


label nv130_talk_sora:
    if not seen_events.get("night_trader_intro", False):
        $ mark_event("night_trader_intro")
        $ sora_trust = max(sora_trust, 1)
        sora "Quien camina por aquí de noche está perdido o busca algo."
        mc "¿Cuál de los dos soy?"
        sora "Vuelve unas cuantas veces y quizá lo decida."
        $ spend_time(1)
    else:
        sora "Has vuelto. Eso suele significar que necesitas algo."

        menu:
            "Hablar":
                if sora_trust < 3:
                    $ sora_trust += 1
                    sora "Quizá empiece a confiar en ti."
                else:
                    sora "Ya sé suficiente sobre ti."
                $ spend_time(1)

            "Comprar Moon Token — 25 monedas" if sora_trust >= 3 and coins >= 25 and not has_item("Moon Token") and not flags.get("moon_token_used", False):
                $ coins -= 25
                $ add_item("Moon Token")
                sora "No preguntes qué abre."
                $ spend_time(1)

            "Irte":
                pass

    $ nv130_set_scene("market_night_stall")
    jump nv130_explore
