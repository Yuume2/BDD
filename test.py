from pymongo import MongoClient
from db_init import liste_characters
from db_init import liste_monstres

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_rpg"]
collection = db ["personnages"]

# Lancer la partie
# afficher menu
# Entrer le nom du joueur
# Lui faire choisir son personnage
    # afficher les personnages disponibles
    # demander a l'user un imput
    # vérifier choix valide
    # faire correspondre l'input avec le choix
    # faire choisir le personnage
# Faire jouer les combats
# Récupérer Scores
# Ecran fin 



print(db.list_collection_names())