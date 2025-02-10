#cucina.rpy
label cucina:
    $ location = 1  # Imposta la location su 1 per la cucina
    show screen borsa  # Mostra la borsa solo se l'inventario è chiuso
    show screen dayNightButton1
    show screen week
    if itemslot == False:
        show screen hotdog
        show screen mela
        show screen pizza
    if day == 0:
            scene cucinagiorno
    elif day == 1:

            scene cucinapomeriggio
    elif day == 2:

            scene cucinanotte
        
    call screen backButton
return
