# myscreen.rpy
# SCREEN DELLA MAPPA

label map:
    $ location = 0
    call screen mapScreen
    
screen mapScreen:
    modal True  # Blocca interazioni sotto lo schermo
    if day == 0:
        add "map/mappagiorno.png"
    elif day == 1:
        add "map/mappapomeriggio.png"
    elif day == 2:
        add "map/Mappanotte.png"

    if swichBotton == True:
        if weekday == 0:
            add "dw/lun.png"
        elif weekday == 1:
            add "dw/mar.png"
        elif weekday == 2:
            add "dw/mer.png"
        elif weekday == 3:
            add "dw/gio.png"
        elif weekday == 4:
            add "dw/ven.png"
        elif weekday == 5:
            add "dw/sab.png"
        elif weekday == 6:
            add "dw/dom.png"
        
        # Cucina
        imagebutton:
            xpos 108 
            ypos 640 
            idle "R1_idle.png"
            hover "R1_hover.png"
            action Jump("cucina")

        # Stanza musica
        imagebutton:
            xpos 1310 
            ypos 630
            idle "R2_idle.png"
            hover "R2_hover.png"
            action Jump("musica")

        # Giorno/notte
        imagebutton:
            xpos 1730
            ypos 36
            idle "dw/DN_idle.png"
            hover "dw/DN_hover.png"
            action Jump("ciclo")

    # Inventario
        

    # BACK BUTTON
screen backButton:
        imagebutton:
            xpos 100
            ypos 100
            idle "button_idle.png"
            hover "button_hover.png"
            action Jump("map")
