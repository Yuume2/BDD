from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["jeu_rpg"]
collection = db ["personnages"]

# Entrer le nom du joueur
print(f"Entre ton prénom:")
nom = input("")
# Lui faire choisir son personnage
from db_init import liste_characters
print (liste_characters)




# Faire jouer les combats

# Récupérer Scores

# Ecran fin 



print(db.list_collection_names())