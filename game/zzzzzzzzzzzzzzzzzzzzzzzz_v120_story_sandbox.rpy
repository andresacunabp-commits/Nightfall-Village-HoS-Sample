# ============================================================
# NIGHTFALL VILLAGE v0.12.0 — STORY-DRIVEN SANDBOX CORE
# ============================================================
# Main-menu simplification + in-save free-roam navigation.
# The player starts/loads a persistent playthrough, then chooses
# where to go and what to do from inside that playthrough.
# ============================================================


default persistent.nv12_seen_events = {}


init 9800 python:

    NV12_GALLERY_ITEMS = [
        ("Village Square", "images/backgrounds/v110/village_square.jpg", None),
        ("Riverside", "images/backgrounds/v110/riverside.jpg", "find_charm"),
        ("Training Ground", "images/backgrounds/v110/training_ground.jpg", "ren_intro"),
        ("Market Alley", "images/backgrounds/v110/market_alley.jpg", "night_trader_intro"),
        ("Aya's Household", "images/backgrounds/v110/aya_house_ext.jpg", "aya_house_invite"),
        ("Old Shrine", "images/backgrounds/v110/shrine_path.jpg", "shrine_rumor"),
    ]

    NV12_REPLAY_ITEMS = [
        ("A Courier's Request", "Aya", "aya_intro", "nv12_replay_aya_intro"),
        ("Something in the Water", "Aya", "find_charm", "nv12_replay_find_charm"),
        ("The Instructor", "Ren", "ren_intro", "nv12_replay_ren_intro"),
        ("The Night Trader", "Sora", "night_trader_intro", "nv12_replay_sora_intro"),
    ]

    def nv12_unlocked(event_id):
        if event_id is None:
            return True
        data = persistent.nv12_seen_events or {}
        return bool(data.get(event_id, False))

    # Keep replay/gallery unlocks across save slots.
    # Runtime event code resolves this final mark_event definition.
    def mark_event(event_id):
        store.seen_events[event_id] = True
        if persistent.nv12_seen_events is None:
            persistent.nv12_seen_events = {}
        persistent.nv12_seen_events[event_id] = True
        renpy.save_persistent()


# ------------------------------------------------------------
# STYLES
# ------------------------------------------------------------

style nv12_menu_button is button:
    background None
    hover_background Solid("#073b4cdd")
    selected_background Solid("#0b5368dd")
    xsize 300
    ysize 43
    xpadding 14
    ypadding 7

style nv12_menu_button_text is button_text:
    size 19
    color "#c6d8df"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.0

style nv12_menu_primary is nv12_menu_button:
    background Solid("#087b97dd")
    hover_background Solid("#0ca5c5ee")

style nv12_menu_primary_text is nv12_menu_button_text:
    bold True
    color "#ffffff"

style nv12_travel_button is button:
    background Solid("#04121aee")
    hover_background Solid("#0a3f52ee")
    insensitive_background Solid("#04080bcc")
    xsize 330
    ysize 47
    xpadding 14
    ypadding 7

style nv12_travel_button_text is button_text:
    size 17
    color "#dbe8ed"
    hover_color "#ffffff"
    insensitive_color "#56656c"
    xalign 0.0

style nv12_small_button is button:
    background Solid("#051a24e8")
    hover_background Solid("#0a4055e8")
    xpadding 14
    ypadding 8

style nv12_small_button_text is button_text:
    size 14
    color "#c8dbe2"
    hover_color "#ffffff"


# ------------------------------------------------------------
# MAIN MENU — ONLY PLAYER-FACING GAME OPTIONS
# ------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/backgrounds/v110/village_square.jpg"
    add Solid("#01060a55")
    add SnowBlossom("images/ui/polish/petal.png", count=11, border=60, xspeed=(-13, 14), yspeed=(16, 34), start=2)

    # Left menu panel.
    frame:
        xpos 0
        ypos 0
        xsize 390
        ysize 720
        background Solid("#02080df4")
        padding (42, 26)

        fixed:
            xfill True
            yfill True

            add "images/ui/nightfall_logo.png":
                xpos 0
                ypos 0
                zoom 0.50

            text "NIGHTFALL VILLAGE":
                xpos 5
                ypos 145
                size 13
                bold True
                color "#63dcf5"

            text "Una partida. Tus decisiones.":
                xpos 5
                ypos 168
                size 13
                color "#7f99a4"

            vbox:
                xpos 0
                ypos 208
                spacing 3

                textbutton "COMENZAR" action Start("nv12_start") style "nv12_menu_primary"
                textbutton "CARGAR" action ShowMenu("load") style "nv12_menu_button"
                textbutton "GALERÍA" action ShowMenu("nv12_gallery") style "nv12_menu_button"
                textbutton "REPETIR ESCENAS" action ShowMenu("nv12_replay") style "nv12_menu_button"
                textbutton "PREFERENCIAS" action ShowMenu("preferences") style "nv12_menu_button"
                textbutton "ACERCA DE" action ShowMenu("nv12_about") style "nv12_menu_button"
                textbutton "AYUDA" action ShowMenu("nv12_help") style "nv12_menu_button"
                textbutton "SALIR" action Quit(confirm=False) style "nv12_menu_button"

            add Solid("#00c8ff55"):
                xpos 5
                ypos 645
                xsize 300
                ysize 1

            text "v[config.version] • Story-Driven Sandbox":
                xpos 5
                ypos 660
                size 11
                color "#8ecbd8"

    # Simple atmosphere card — no demo selectors or dev shortcuts.
    frame:
        xpos 820
        ypos 470
        xsize 405
        ysize 165
        background Solid("#02080bd9")
        padding (22, 18)

        vbox:
            spacing 7
            text "NIGHTFALL" size 12 bold True color "#e4bd68"
            text "Vive tu propia partida" size 27 bold True color "#ffffff"
            text "Explora, elige qué hacer, avanza el tiempo y descubre eventos según tus decisiones." size 14 color "#b8c9cf" line_spacing 3


# ------------------------------------------------------------
# NEW GAME ENTRY — ONE CONTINUOUS PLAYTHROUGH
# ------------------------------------------------------------

label nv12_start:
    scene bg_home
    with fade

    centered "{size=52}{b}NIGHTFALL VILLAGE{/b}{/size}\n{size=21}Day 1 • Morning{/size}"
    pause 0.7

    mc "I've been assigned to Nightfall Village again."
    mc "No fixed route. I decide where to go, how to spend the day, and who to trust."
    mc "Whatever I choose, the village will remember."

    jump loc_home


# ------------------------------------------------------------
# IN-SAVE TRAVEL — REPLACES THE OLD 'WORLD HUB' PRESENTATION
# ------------------------------------------------------------

screen world_map():
    tag menu
    modal True

    add "images/backgrounds/v110/village_square.jpg"
    add Solid("#01070b77")

    frame:
        xpos 18
        ypos 16
        xsize 1244
        ysize 67
        background Solid("#02080ded")
        padding (20, 9)

        hbox:
            xfill True

            vbox:
                text "NIGHTFALL VILLAGE" size 24 bold True color "#ffffff"
                text "¿Adónde quieres ir?" size 12 bold True color "#00d4ff"

            hbox:
                spacing 26
                xalign 1.0
                yalign 0.5

                text "DAY [day]" size 15 bold True color "#e4bd68"
                text period_name().upper() size 15 bold True color "#ffffff"
                text "$[coins]" size 15 bold True color "#e4bd68"
                text "ENERGY [energy]/4" size 14 color "#63dcf5"

    frame:
        xpos 18
        ypos 98
        xsize 375
        ysize 545
        background Solid("#02080de9")
        padding (18, 16)

        vbox:
            spacing 7

            text "DESTINOS" size 11 bold True color "#7aa8b7"

            for location_id in LOCATION_ORDER:
                $ loc = LOCATION_DATA[location_id]
                $ unlocked = is_location_unlocked(location_id)
                $ event_ready = location_has_event(location_id) if unlocked else False
                $ residents = residents_at(location_id) if unlocked else ""

                textbutton (loc["name"] + ("   • EVENT" if event_ready else "") + ("   • " + residents if residents else "")):
                    action Jump(loc["label"])
                    sensitive unlocked
                    style "nv12_travel_button"

    frame:
        xpos 415
        ypos 98
        xsize 847
        ysize 370
        background Solid("#02080dc9")
        padding (24, 22)

        vbox:
            spacing 14

            text "TU PARTIDA" size 12 bold True color "#e4bd68"
            text "El mundo continúa mientras decides qué hacer." size 28 bold True color "#ffffff"
            text "Cada acción puede avanzar la hora. Los personajes cambian de ubicación y los eventos aparecen solo cuando se cumplen sus condiciones." size 15 color "#b9cbd2" line_spacing 4

            null height 4

            $ _nv12_objectives = guide_objectives()
            if _nv12_objectives:
                $ _nv12_cat, _nv12_obj = _nv12_objectives[0]
                text "OBJETIVO ACTUAL" size 11 bold True color "#63dcf5"
                text "[_nv12_cat]" size 18 bold True color "#ffffff"
                text _nv12_obj size 15 color "#aebfc6" line_spacing 3

            hbox:
                spacing 24
                text "STR [strength]" size 15 color "#dce9ed"
                text "REP [reputation]" size 15 color "#dce9ed"
                text "AYA ♥ [relationships['aya']['love']]" size 15 color "#ff9db6"
                text "AYA ⚔ [relationships['aya']['hatred']]" size 15 color "#9fcfff"

    frame:
        xpos 415
        ypos 488
        xsize 847
        ysize 155
        background Solid("#02080de9")
        padding (20, 18)

        vbox:
            spacing 12
            text "PARTIDA" size 11 bold True color "#7aa8b7"
            hbox:
                spacing 10
                textbutton "INVENTARIO" action Show("inventory_screen") style "nv12_small_button"
                textbutton "RELACIONES" action Show("characters_screen") style "nv12_small_button"
                textbutton "GUARDAR" action ShowMenu("save") style "nv12_small_button"
                textbutton "CARGAR" action ShowMenu("load") style "nv12_small_button"
                textbutton "PREFERENCIAS" action ShowMenu("preferences") style "nv12_small_button"

            text "F2: herramientas de desarrollo (ocultas del menú principal)." size 11 color "#526a74"


# ------------------------------------------------------------
# CLEAN IN-GAME HUD
# ------------------------------------------------------------

screen hud():
    zorder 100

    if renpy.get_screen("main_menu") is None and renpy.get_screen("developer_tools") is None:
        frame:
            xpos 18
            ypos 14
            xsize 1244
            ysize 54
            background Solid("#02080de8")
            padding (15, 8)

            hbox:
                xfill True
                spacing 20
                text "DAY [day]" size 14 bold True color "#e4bd68"
                text period_name().upper() size 14 bold True color "#ffffff"
                text "$[coins]" size 14 bold True color "#e4bd68"
                text "ENERGY [energy]/4" size 13 color "#63dcf5"
                text "STR [strength]" size 13 color "#d8e4e8"
                text "REP [reputation]" size 13 color "#d8e4e8"

                hbox:
                    xalign 1.0
                    spacing 7
                    textbutton "OBJETOS" action Show("inventory_screen") style "nv12_small_button"
                    textbutton "PERSONAS" action Show("characters_screen") style "nv12_small_button"
                    textbutton "GUARDAR" action ShowMenu("save") style "nv12_small_button"


# ------------------------------------------------------------
# MAIN-MENU GALLERY
# ------------------------------------------------------------

screen nv12_gallery():
    tag menu

    add "images/backgrounds/v110/village_square.jpg"
    add Solid("#01070bcc")

    frame:
        xpos 32
        ypos 28
        xsize 1216
        ysize 650
        background Solid("#02080df0")
        padding (28, 22)

        vbox:
            spacing 16

            hbox:
                xfill True
                vbox:
                    text "GALERÍA" size 37 bold True color "#ffffff"
                    text "Imágenes desbloqueadas durante tus partidas." size 14 color "#8fa7b3"
                textbutton "VOLVER" action ShowMenu("main_menu") style "nv12_small_button" xalign 1.0

            vpgrid:
                cols 3
                spacing 16
                xfill True
                ymaximum 520

                for _title, _path, _event_id in NV12_GALLERY_ITEMS:
                    $ _unlocked = nv12_unlocked(_event_id)

                    frame:
                        xsize 360
                        ysize 225
                        background Solid("#07141de8" if _unlocked else "#03070acc")
                        padding (10, 10)

                        vbox:
                            spacing 7

                            if _unlocked:
                                add _path:
                                    xysize (340, 170)
                                text _title size 15 bold True color "#e4edf1"
                            else:
                                frame:
                                    xsize 340
                                    ysize 170
                                    background Solid("#05090dcc")
                                    text "BLOQUEADO" size 14 bold True color "#53636a" xalign 0.5 yalign 0.5
                                text "???" size 15 color "#53636a"


# ------------------------------------------------------------
# SCENE REPLAY
# ------------------------------------------------------------

screen nv12_replay():
    tag menu

    add "images/backgrounds/v110/riverside.jpg"
    add Solid("#01070bd5")

    frame:
        xpos 150
        ypos 52
        xsize 980
        ysize 615
        background Solid("#02080df2")
        padding (34, 28)

        vbox:
            spacing 18

            hbox:
                xfill True
                vbox:
                    text "REPETIR ESCENAS" size 36 bold True color "#ffffff"
                    text "Las repeticiones no modifican tu partida guardada." size 14 color "#8fa7b3"
                textbutton "VOLVER" action ShowMenu("main_menu") style "nv12_small_button" xalign 1.0

            for _title, _character, _event_id, _replay_label in NV12_REPLAY_ITEMS:
                $ _unlocked = nv12_unlocked(_event_id)

                frame:
                    xfill True
                    ysize 86
                    background Solid("#07141de8" if _unlocked else "#04090dcc")
                    padding (18, 12)

                    hbox:
                        xfill True

                        vbox:
                            text _title size 20 bold True color ("#ffffff" if _unlocked else "#53636a")
                            text _character size 13 color ("#63dcf5" if _unlocked else "#45545a")

                        textbutton ("REPETIR" if _unlocked else "BLOQUEADO"):
                            action Replay(_replay_label)
                            sensitive _unlocked
                            style "nv12_small_button"
                            xalign 1.0
                            yalign 0.5


# ------------------------------------------------------------
# ABOUT / HELP
# ------------------------------------------------------------

screen nv12_about():
    tag menu

    add "images/backgrounds/v110/aya_house_ext.jpg"
    add Solid("#01070bd8")

    frame:
        xpos 230
        ypos 100
        xsize 820
        ysize 520
        background Solid("#02080df1")
        padding (38, 34)

        vbox:
            spacing 18
            text "ACERCA DE" size 38 bold True color "#ffffff"
            text "Nightfall Village" size 27 bold True color "#63dcf5"
            text "Una novela visual sandbox centrada en una partida persistente: eliges dónde ir, qué hacer y cómo relacionarte con los personajes mientras el tiempo y los eventos avanzan." size 16 color "#c0d0d6" line_spacing 4
            text "Proyecto original construido con Ren'Py + Python como muestra de sistemas narrativos, eventos condicionales, relaciones, horarios y guardado persistente." size 15 color "#91a7b1" line_spacing 4
            null height 10
            text "Versión [config.version]" size 13 color "#e4bd68"
            textbutton "VOLVER" action ShowMenu("main_menu") style "nv12_small_button"


screen nv12_help():
    tag menu

    add "images/backgrounds/v110/training_ground.jpg"
    add Solid("#01070bd8")

    frame:
        xpos 230
        ypos 80
        xsize 820
        ysize 560
        background Solid("#02080df1")
        padding (38, 32)

        vbox:
            spacing 14
            text "AYUDA" size 38 bold True color "#ffffff"
            text "Controles" size 20 bold True color "#63dcf5"
            text "Clic izquierdo  — avanzar / seleccionar" size 15 color "#c3d3d9"
            text "Clic derecho    — volver" size 15 color "#c3d3d9"
            text "Rueda del ratón — historial" size 15 color "#c3d3d9"
            text "Ctrl             — omitir texto" size 15 color "#c3d3d9"
            text "Esc              — menú de juego" size 15 color "#c3d3d9"

            null height 8
            text "Cómo se juega" size 20 bold True color "#e4bd68"
            text "Dentro de tu partida decides adónde ir. Las acciones pueden gastar energía o avanzar la hora. Los personajes cambian de lugar y algunas escenas solo aparecen en determinados días, horarios o estados de relación." size 15 color "#aebfc6" line_spacing 4

            null height 8
            textbutton "VOLVER" action ShowMenu("main_menu") style "nv12_small_button"


# ------------------------------------------------------------
# REPLAY LABELS — SELF-CONTAINED, NO SAVE-STATE CHANGES
# ------------------------------------------------------------

label nv12_replay_aya_intro:
    scene bg_square
    with dissolve
    "A courier nearly collides with you in the Square."
    aya "You're the one who came back to the village, right?"
    mc "That's me."
    aya "Then maybe you can help. I lost a silver charm near the river."
    $ renpy.end_replay()
    return


label nv12_replay_find_charm:
    scene bg_riverside
    with dissolve
    "Something catches the light between the river stones."
    "You found Aya's Silver Charm."
    $ renpy.end_replay()
    return


label nv12_replay_ren_intro:
    scene bg_training
    with dissolve
    "A lone instructor practices precise strikes."
    ren "Watching won't make you stronger."
    mc "Maybe I was waiting to see if you're worth learning from."
    ren "Then stop watching."
    $ renpy.end_replay()
    return


label nv12_replay_sora_intro:
    scene bg_market
    with dissolve
    "Most of the Market is closed, but one narrow stall is still lit."
    sora "People who wander after dark are either lost or looking for something."
    mc "Which one am I?"
    sora "Come back enough times and I might decide."
    $ renpy.end_replay()
    return
