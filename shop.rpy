# Variabile per tenere traccia della disponibilità della banana nel negozio
init python:
    banana_available = True  # La banana è disponibile inizialmente

# Parte dello shop
screen shopElisa:
    if location == 2:
        imagebutton:
            idle "elisa_idle.png"
            hover "elisa_hover.png"
            xpos 100
            ypos 200
            action Show("shopScreen")

# Inizializzazione della variabile solo se non è già stata definita
init python:
    if not hasattr(store, 'item_desc_visible'):
        item_desc_visible = ""

screen shopScreen:
    modal True
    add "shop.png"  

    # Bottone per chiudere il negozio
    imagebutton:
        xpos 1560
        ypos 894
        idle "chiudi_idle.png"
        hover "chiudi_hover.png"
        action Hide("shopScreen"), Jump("musica")

    # Mostra il pulsante della banana solo se è disponibile
    if banana_available:
        # Bottone per acquistare la banana
        imagebutton:
            xpos 192
            ypos 202
            idle "banana_idle.png"
            hover "banana_hover.png"
            action Function(buy_banana)
            hovered SetVariable("item_desc_visible", "banana")
            unhovered SetVariable("item_desc_visible", "")

    # Mostra descrizione se si passa sopra la banana
    if item_desc_visible == "banana":
        text "Banana bio - 1000 ₤" xpos 200 ypos 920 size 50 color "#000000"

init python:
    def buy_banana():
        global money, banana_available
        if money >= 1000:
            money -= 1000
            inventory.append("banana")
            banana_available = False  # La banana non è più disponibile nel negozio
            renpy.notify("Hai comprato una banana!")
        else:
            renpy.notify("Non hai abbastanza soldi!")