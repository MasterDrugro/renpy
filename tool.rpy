#tool.rpy

# Parte relativa al denaro
screen money_display:
    image "money.png" xpos 1695 ypos 435
    text "[money]₤" xpos 1770 ypos 577 size 40 color "#000000" xanchor 0.4

# Mostra sempre la schermata dei soldi
init python:
    config.overlay_screens.append("money_display")

# Schermata per aprire l'inventario
screen borsa:  # Mostra solo se l'inventario è chiuso
    imagebutton:
        xpos 1680
        ypos 843
        idle "borsa_idle.png"
        hover "borsa_hover.png"
        action [
            SetVariable("inventory_open", True),  # Apri l'inventario
            Show("inventariomap")
        ]

# Localizzatore per l'inventario nella mappa
init python:
    def location_label():
        if location == 0:
            return "map"  # Mappa
        elif location == 1:
            return "cucina"  # Cucina
        elif location == 2:
            return "musica"  # Musica
        else:
            return "map"  # Default, torna alla mappa se non è definito altro

# Schermata dell'inventario
screen inventariomap:
    modal True
    add "slott.png"

    $ slot_positions = [(192, 202), (412, 202), (633, 202), (853, 202), (1074, 202), (1294, 202)]

    # Pulsante per chiudere l'inventario
    imagebutton:
        xpos 1560
        ypos 894
        idle "chiudi_idle.png"
        hover "chiudi_hover.png"
        action [
            SetVariable("inventory_open", False),  # Chiude l'inventario
            Hide("inventariomap"),
            Jump(location_label())  # Torna alla posizione corrente
        ]

    # Mostra dinamicamente gli oggetti nell'inventario
    for i, item in enumerate(inventory):  # item è l'oggetto nell'inventario
        if i < 6:
            imagebutton:
                xpos slot_positions[i][0]
                ypos slot_positions[i][1]
                idle "{}_idle.png".format(item)   # Usa il nome dell'oggetto
                hover "{}_hover.png".format(item)
                action Jump("cosadice")
                hovered SetVariable("item_desc_visible", item)  # Mostra la descrizione
                unhovered SetVariable("item_desc_visible", "")  # Nasconde la descrizione

    # Mostra la descrizione dell'oggetto selezionato
    if item_desc_visible == "pizza":
        text "Una fetta di pizza gustosa" xpos 200 ypos 920 size 50 color "#000000"
    elif item_desc_visible == "hotdog":
        text "Un hotdog saporito" xpos 200 ypos 920 size 50 color "#000000"
    elif item_desc_visible == "mela":
        text "Una mela verde" xpos 200 ypos 920 size 50 color "#000000"
    elif item_desc_visible == "banana":
        text "Una banana bio" xpos 200 ypos 920 size 50 color "#000000"

label cosadice:
    call screen inventariomap
    return  # Torna all'inventario senza perdere il blocco modal