from pymongo import MongoClient
from db_init import liste_characters
from db_init import liste_monstres

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_rpg"]
collection = db ["personnages"]

# afficher menu
    # reset console 
    # afficher options 
        # choix 1 jouer
        # choix 2 classement 
        # choix 3 quitter 
    # récupérer choix valide
        # vérif choix

# vérif choix
    # si choix [1,3] 
        # return choix 
    # sinon 
        # message erreur 

# si choix 1
    # Demander nom joueur
    # Créer équipe 
    # Lancer combat 

# si choix 2 
    # afficher classement

# si choix 3 
    # quitter 

# créer équipe 
    # tant que [equipe] < 3 
        # afficher les personnages disponibles 
        # récupérer choix valide 
        # retirer le choix des perso disponibles
        # faire correspondre l'input avec le choix index = choix - 1
        # ajouter a l'équipe 
        # afficher équipe 
        # lancer combat 

# lancer combat 
    # reset console 
    # lancer wave 
    # afficher options 

# lancer wave 
    # wave = 0 
    # choisir ennemis
    # afficher ennemis
    # calculer dégats
    # équipe en vie   
    # afficher game over 
    # reset équipe 

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

# equipe en vie 
    # tant que équipe est en vie
        # ajouter score  
        # wave +1 
        # choisir ennemis 
