# ============================================================
# AYA STORY DEMO — v0.6
# A small vertical slice proving branching state + presentation.
# ============================================================

define narrator_demo = Character(None)

label v06_aya_demo_start:
    scene black
    with fade

    $ period_index = 3
    $ day = max(day, 3)

    scene expression "images/ui/village_night_bg.png"
    with dissolve

    show expression "images/characters/aya/aya_neutral.png" as aya_demo:
        xalign 0.70
        yalign 1.02
        zoom 0.58
        alpha 0.96

    aya "Llegaste tarde."

    mc "No esperaba encontrarte aquí."

    show expression "images/characters/aya/aya_serious.png" as aya_demo:
        xalign 0.70
        yalign 1.02
        zoom 0.58
        alpha 0.96

    aya "Eso depende. ¿Viniste porque necesitabas algo... o porque estabas buscándome?"

    menu:
        "Decirle que querías verla":
            $ change_relation("aya", "love", 1)
            $ flags["v06_aya_demo_choice"] = "love"

            show expression "images/characters/aya/aya_smile.png" as aya_demo:
                xalign 0.70
                yalign 1.02
                zoom 0.58
                alpha 0.96

            aya "Qué forma tan peligrosa de responder."

            mc "¿Peligrosa?"

            aya "Porque podría empezar a creerte."

        "Convertirlo en un desafío":
            $ change_relation("aya", "hatred", 1)
            $ flags["v06_aya_demo_choice"] = "hatred"

            show expression "images/characters/aya/aya_serious.png" as aya_demo:
                xalign 0.70
                yalign 1.02
                zoom 0.58
                alpha 0.96

            mc "Solo quería comprobar si eras tan difícil de encontrar como dices."

            aya "Entonces acabas de convertir esto en una competencia."

        "Preguntar por la misión":
            $ reputation += 1
            $ flags["v06_aya_demo_choice"] = "neutral"

            show expression "images/characters/aya/aya_surprised.png" as aya_demo:
                xalign 0.70
                yalign 1.02
                zoom 0.58
                alpha 0.96

            aya "Directo al trabajo. No era la respuesta que esperaba."

    hide aya_demo
    with dissolve

    "DEMO SYSTEM NOTE"

    "La elección anterior ya modificó el estado persistente de Aya."

    if flags.get("v06_aya_demo_choice") == "love":
        "Resultado: Love aumentó. Una cadena de eventos de confianza podría quedar disponible."
    elif flags.get("v06_aya_demo_choice") == "hatred":
        "Resultado: Hatred aumentó. Una ruta de rivalidad puede reaccionar a esta decisión."
    else:
        "Resultado: Reputation aumentó. Este tipo de estadística puede desbloquear eventos del mundo."

    "Puedes abrir Developer Tools con F2 para inspeccionar el estado y los requisitos de eventos."

    jump map