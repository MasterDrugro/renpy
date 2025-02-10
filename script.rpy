#script.rpy
define day = 0
define weekday = 0
define swichBotton = True 
define chiuderebotton = True
default inventory_open = True
default itemslot = False
default location = 0  # 0 per la mappa, 1 per la cucina, 2 per la musica, ecc.  
image slottino = "inventario.png"
default pizza_desc_visible = False
default prendipizza = True
define prendihotdog = True
define prendimela = True
define inventory = []  # Lista per memorizzare gli oggetti trovati
define servelapizza = False
default item_desc_visible = ""
define config.rollback_enabled = False
default carla_ha_ricevuto_pizza = False
default money = 1000000  # Quantità iniziale di soldi

label start:
    call screen mapScreen  # Avvia la mappa
    return


screen carla_screen:
    if location == 2:  # Mostra Carla solo se siamo nella stanza musica
        imagebutton:
            xpos 800
            ypos 500
            idle "Carla_idle.png"
            hover "Carla_hover.png"
            action Jump("parla_con_carla")



label parla_con_carla:
    if "pizza" in inventory and not carla_ha_ricevuto_pizza:
        "Carla sorride: \"Wow, una fetta di pizza! La stavo aspettando!\""
        $ inventory.remove("pizza")
        $ carla_ha_ricevuto_pizza = True
        "Le dai la pizza. Carla è molto felice!"
    
    elif carla_ha_ricevuto_pizza:
        $ money += 10  # Aggiunge 10 soldi
        "Carla: \"Buona la pizza!\""
        
    else:
        "Carla ti guarda: \"Non hai una pizza per me?\""
    
    jump musica

screen carla_screen:
    if location == 2:
        if servelapizza:
            text "Carla: \"Grazie per la pizza!\"" xpos 850 ypos 700 size 40
        else:
            imagebutton:
                xpos 1240
                ypos 400
                idle "Carla_idle.png"
                hover "Carla_hover.png"
                action Jump("parla_con_carla")

    
