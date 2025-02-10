label musica:
    $ location = 2  
    show screen borsa
    show screen dayNightButton2
    show screen week
    show screen shopElisa
    if day == 0:
        scene musicagiorno
    elif day == 1:
        scene musicapomeriggio
    elif day == 2:
        scene musicanotte

    # Mostra Elisa sulla sinistra dello schermo
    

    call screen backButton
    return
