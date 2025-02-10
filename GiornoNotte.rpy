screen dayNightButton:  
    imagebutton:
        xpos 1730
        ypos 36
        idle "dw/DN_idle.png"
        hover "dw/DN_hover.png"
        action Jump("ciclo")

screen dayNightButton1:
    imagebutton:
        xpos 1730
        ypos 36
        idle "dw/DN_idle.png"
        hover "dw/DN_hover.png"
        action Jump("ciclo1")

screen dayNightButton2:
    imagebutton:
        xpos 1730
        ypos 36
        idle "dw/DN_idle.png"
        hover "dw/DN_hover.png"
        action Jump("ciclo2")

label ciclo:
    if day == 0:
        $ day = 1
    elif day == 1:
        $ day = 2
    elif day == 2:
        $ day = 0
        $ weekday += 1
        if weekday > 6:  # Reset weekday quando supera 6
            $ weekday = 0
    call screen mapScreen
    return

label ciclo1:
    if day == 0:
        $ day = 1
    elif day == 1:
        $ day = 2
    elif day == 2:
        $ day = 0
        $ weekday += 1
        if weekday > 6:  # Reset weekday
            $ weekday = 0
    call cucina
    return

label ciclo2:
    if day == 0:
        $ day = 1
    elif day == 1:
        $ day = 2
    elif day == 2:
        $ day = 0
        $ weekday += 1
        if weekday > 6:  # Reset weekday
            $ weekday = 0
    call musica
    return

screen week:
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


