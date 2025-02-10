#item.rpy

screen pizza:
    if location == 1 and prendipizza:
        imagebutton:
            xpos 171
            ypos 880
            idle "pizza_idle.png"
            hover "pizza_hover.png"
            action Jump("pizzaitem")

label pizzaitem:
    if "pizza" not in inventory and len(inventory) < 6:
        $ inventory.append("pizza")  # Aggiunge la pizza al primo slot libero
        $ prendipizza = False  # Nasconde la pizza dalla cucina

    hide screen pizza  # Nasconde la pizza dallo schermo
    "Hai trovato una fetta di pizza!"
    jump cucina  # Torna alla cucina

screen hotdog:
    if location == 1 and prendihotdog:
        imagebutton:
            xpos 300
            ypos 880
            idle "hotdog_idle.png"
            hover "hotdog_hover.png"
            action Jump("hotdogitem")

label hotdogitem:
    if "hotdog" not in inventory and len(inventory) < 6:
        $ inventory.append("hotdog")  # Aggiunge l'hotdog al primo slot libero
        $ prendihotdog = False  # Nasconde l'hotdog dalla cucina

    hide screen hotdog  # Nasconde l'hotdog dallo schermo
    "Hai trovato un hotdog!"
    jump cucina  # Torna alla cucina

screen mela:
    if location == 1 and prendimela:
        imagebutton:
            xpos 500
            ypos 880
            idle "mela_idle.png"
            hover "mela_hover.png"
            action Jump("melaitem")

label melaitem:
    if "mela" not in inventory and len(inventory) < 6:
        $ inventory.append("mela")  
        $ prendimela = False 
         
    hide screen mela  
    "Hai trovato una mela!"
    jump cucina 