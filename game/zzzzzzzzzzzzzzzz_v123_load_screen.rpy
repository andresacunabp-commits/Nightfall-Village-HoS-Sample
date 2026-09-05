screen load():
    tag menu

    add "images/ui/load_bg.png"

    add Solid("#00000055")

    frame:
        xpos 0
        ypos 0
        xsize 360
        ysize 720
        background Solid("#02080de8")
        padding (28, 28)

        vbox:
            spacing 12

            text "Cargar":
                size 44
                bold True
                color "#39cfff"

            text "Continúa una partida guardada.":
                size 14
                color "#9cb7c2"

            null height 12

            textbutton "Regresar" action Return()

    use file_slots(_("Cargar"))
