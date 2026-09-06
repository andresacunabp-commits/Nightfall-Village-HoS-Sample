# ============================================================
# NIGHTFALL VILLAGE v0.14.0 — HOME MASTER HOTSPOTS
# ============================================================
# Final positioning pass for the six 1920x1080 protagonist-home masters.
# The v140 art pipeline scales them to 1280x720 at runtime, so these
# coordinates are authored directly in game-space.
# ============================================================

init 17000 python:

    def nv140_home_layout(scene_id, moves=None, actions=None):
        if scene_id not in NV130_SCENES:
            return
        if moves is not None:
            NV130_SCENES[scene_id]["moves"] = moves
        if actions is not None:
            NV130_SCENES[scene_id]["actions"] = actions

    # Bedroom: bed left, desk/notes right, hallway doorway upper-right.
    nv140_home_layout("home_bedroom",
        moves=[
            ("PASILLO  →", "home_hallway", 865, 385, "always"),
        ],
        actions=[
            ("CAMA", "sleep", 245, 465, "always"),
            ("REVISAR NOTAS", "notes", 1010, 455, "always"),
        ])

    # Hallway: five clear navigation anchors across the corridor.
    nv140_home_layout("home_hallway",
        moves=[
            ("DORMITORIO", "home_bedroom", 95, 365, "always"),
            ("BAÑO", "home_bathroom", 355, 355, "always"),
            ("SALIR", "home_exterior", 705, 350, "always"),
            ("SALA", "home_living", 875, 350, "always"),
            ("COCINA", "home_kitchen", 1050, 360, "always"),
        ],
        actions=[])

    # Kitchen: hallway opening is on the left; breakfast is on the table.
    nv140_home_layout("home_kitchen",
        moves=[
            ("←  PASILLO", "home_hallway", 95, 395, "always"),
        ],
        actions=[
            ("DESAYUNAR", "eat", 1000, 475, "always"),
        ])

    # Living room: hallway/doorway is left; mission notes/mail sit on table.
    nv140_home_layout("home_living",
        moves=[
            ("←  PASILLO", "home_hallway", 165, 405, "always"),
        ],
        actions=[
            ("MESA / CORREO", "notes", 720, 475, "always"),
        ])

    # Bathroom: hallway opening on left, bathing interaction on the tub.
    nv140_home_layout("home_bathroom",
        moves=[
            ("←  PASILLO", "home_hallway", 165, 410, "always"),
        ],
        actions=[
            ("ASEARSE", "wash", 855, 470, "always"),
        ])

    # Exterior: front door left, village road exits toward the right.
    nv140_home_layout("home_exterior",
        moves=[
            ("ENTRAR", "home_hallway", 405, 385, "always"),
            ("CALLE RESIDENCIAL  →", "residential_street", 925, 485, "always"),
        ],
        actions=[])


# Make hotspot chrome slightly lighter on top of master art so the
# illustration remains the visual focus while interaction stays obvious.
style nv130_hotspot is button:
    background Solid("#031016ae")
    hover_background Solid("#0786a9e8")
    xpadding 10
    ypadding 6

style nv130_action_hotspot is nv130_hotspot:
    background Solid("#4b350bad")
    hover_background Solid("#a77a18e8")
