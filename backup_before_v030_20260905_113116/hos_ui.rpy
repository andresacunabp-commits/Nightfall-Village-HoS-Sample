# ============================================================
# HOUSE OF SHINOBI ORIENTED UI
# Original UI implementation for portfolio demonstration.
# ============================================================

# ------------------------------------------------------------
# DIALOGUE BOX
# Dialogue is deliberately anchored to the bottom of the screen.
# ------------------------------------------------------------

screen say(who, what):

    window:
        id "window"
        style "hos_say_window"

        vbox:
            spacing 7

            if who:
                text who:
                    id "who"
                    style "hos_say_who"

            text what:
                id "what"
                style "hos_say_what"


style hos_say_window:
    xalign 0.5
    yalign 0.985

    xsize 1200
    yminimum 150

    background Solid("#0b1018ee")

    xpadding 32
    ypadding 18


style hos_say_who:
    size 29
    bold True
    color "#d7b66f"


style hos_say_what:
    size 24
    color "#eeeeee"

    xmaximum 1120

    line_spacing 3


# ------------------------------------------------------------
# PLAYER CHOICES
# Choices appear above the dialogue area.
# ------------------------------------------------------------

screen choice(items):

    vbox:
        xalign 0.5
        yalign 0.66

        spacing 10

        for i in items:

            textbutton i.caption:
                action i.action
                style "hos_choice_button"


style hos_choice_button:
    xsize 700
    yminimum 55

    background Solid("#111a24e8")
    hover_background Solid("#26394ce8")

    xpadding 24
    ypadding 12


style hos_choice_button_text:
    xalign 0.5

    size 22
    color "#e6e6e6"
    hover_color "#ffffff"


# ------------------------------------------------------------
# ROUTE INDICATOR
# Useful during development/testing.
# ------------------------------------------------------------

screen hos_route_indicator():

    frame:
        xalign 0.015
        yalign 0.02

        background Solid("#0b1018cc")

        xpadding 14
        ypadding 8

        vbox:
            spacing 2

            text "AYA" size 16 color "#d7b66f"

            text "Love: [relation('aya', 'love')]" size 15
            text "Hatred: [relation('aya', 'hatred')]" size 15


init python:

    if "hos_route_indicator" not in config.overlay_screens:
        config.overlay_screens.append("hos_route_indicator")
