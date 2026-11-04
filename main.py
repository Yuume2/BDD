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

# db connect 

# afficher menu 
    # clear terminal 
    # afficher options 

# demander choix valide (1,3)
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
    # faire correspondre le choix valide avec l'option choisie 

# clear terminal 

# afficher options 
    # si Option 1: Jouer 
        # recup username 
        # lancer partie 
    # si Option 2: Classement
        # afficher le classement 
    # si Option 3: Quitter 
        # Quitter 

# recup username 
    # afficher "quel est ton nom"
    # nom = str(input)

# lancer partie 
    # Créer une équipe 
    # choisir un ennemi
    # Lancer combat 

# Créer une équipe 
    # tant que [equipe] < 3 
        # afficher personnages disponibles 
        # faire choisir le personnage
        # afficher [equipe]

# faire choisir le personnage 
    # récupérer input joueur 
    # faire correspondre l'input avec le personnage [0,10]
    # supprimer le personnage choisi de la liste

# choisir ennemi 
    # prendre chiffre aléatoire [0,10]
    # choisir le monstre associé 

# lancer combat
    # clear terminal 
    # wave = 0
    # tant que equipe en vie = true
        # si ennemie pv > 0 
            # jouer un tour 
            # calculer les dégats
        # sinon 
            # choisir ennemi 
            # wave + 1 
    # Equipe mort 

# Equipe mort 
    # Afficher nom 
    # afficher score 
    # attendre input 
        # afficher menu 

# équipe en vie
    # pour i [equipe]
    # si pv > 0
        # true
    # sinin 
        # return false 

# jouer un tour 
    # choisir personnage attaqué (PA)
    # ennemie attack
    # personnages attack 

# ennemie attack
    # HP = "health" (PA)
    # récupérer "attack" [ennemie] "health","Defense" (PA)
    # attack - defense - health 
    # "health" (PA) = HP

# personnages attack
    # HPE = "health" [ennemie]
    # récupérer "attack" [equipe]
    # "attack" 1 + 2 + 3 - "defense" - "Health" [ennemie]
    # "health" [ennemie] = HPA 