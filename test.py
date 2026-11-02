from pymongo import MongoClient
from db_init import liste_characters
from db_init import liste_monstres

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_rpg"]
collection = db ["personnages"]

# afficher menu
def afficher_menu():
    print("Bienvenue dans le jeu")
    print("1: Jouer")
    print("2: Classement")
    print("3: Quitter")
    # récupérer choix utilisateur 
    # Vérifier choix 
        # si choix n'est pas valide redemander 
        
        # Choix 1, Jouer
            # Entrer le nom du joueur
            # créé équipes
                # tant que équipe pas >3 
                # afficher les personnages disponibles
                # demander un nb valide
                # faire correspondre l'input avec le choix index = choix - 1
                # ajouter le choix a l'équipe 
                # retirer le choix de la liste des personnages disponibles
                # afficher équipe
            # Joueuer lance
            # Lancer le jeu 
                # choisir aléatoirement une vague d'ennemis
                # si joueur mort 
                    # perdu
                # si ennemis mort
                    # Nouvelle vague 
            # Récupérer Scores
            # Ecran fin
    
        # Choix 2 Classement 
            # afficher les classements
        
        # Choix 3 Quitter 
            # Quitter 

# 