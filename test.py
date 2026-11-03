from pymongo import MongoClient
from db_init import liste_characters
from db_init import liste_monstres

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_rpg"]
collection = db ["personnages"]

# main 
    # db connect
    # afficher menu 
    # récupérer choix  
    # demander choix valide (1,3)
    # exec choix 

# afficher menu
    # reset console 
    # afficher options 
        # choix 1 jouer
        # choix 2 classement 
        # choix 3 quitter

# demander choix valide 
    # while true
        # choix = input("choisissez une option")
        # verif choix
            # return choix 
        # sinon 
            # message erreur 

# verif choix 
    # si choix pas digit 
        # return false 
    # choix = int(choix)
    # si min <= choix <= max 
        # else return false 

# exec choix
    # si choix 1
        # Demander nom joueur
        # lancer partie 

    # si choix 2 
        # afficher classement

    # si choix 3 
        # quitter 

# lancer partie 
    # créer équipe 
    # choisir ennemis 
    # lancer combat 

# créer équipe 
    # tant que [equipe] < 3 
        # afficher les personnages disponibles 
        # récupérer choix 
        # vérif choix
        # faire correspondre l'input avec le choix index = choix - 1
        # retirer le choix des perso disponibles
        # ajouter a l'équipe 
        # afficher équipe 

# lancer combat 
    # reset console 
    # lancer wave 

# lancer wave 
    # wave = 0 
    # tant que equipe est en vie 
        # selectionne monstre
        # combat 

# combat
    # tant que equipe alive() et monstre alive()
        # afficher ennemis 
        # calculer dégats
        # if monstre alive = false 
                # wave +1 
        # ajouter score
        # choisir ennemis 
    # fin jeu

# fin jeu
    # afficher game over 
    # reset equipe
    # afficher score
    # afficher menu

# choisir ennemis
    # tant que liste ennemis < 3 
    # choisir aléatoirement ennemi
    # return liste ennemis

# calculer dégats
    # tant que [ennemis] en vie = true 
    # choisir 1 ennemi et 1 personnage aléatoire 
    # "attack" ennemi - "defense" personnage - "health" personnage 
    # "attack" personnage - "defense" ennemis - "health" ennemis 

# tant que liste ennemis en vie = true 
    # si "health" [ennemis] > 1 
        # continue
    # sinon 
        # break

# equipe alive 
    # si "health" [personnages] < 1
        # return false
    # sinon 
        # return true 