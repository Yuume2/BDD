from pymongo import MongoClient
from db_init import liste_characters
from db_init import liste_monstres
import os
from database import db
import random

# main 
def main():
    # afficher menu
    afficher_menu() 
    # demander choix valide (1,3)
    choix = demander_choix_valide()
    # effectuer choix
    effectuer_choix(choix)

# afficher menu 
def afficher_menu():
    # clear terminal 
    clear_terminal()
    # afficher options
    afficher_options() 

# clear terminal
def clear_terminal():
    os.system("clear")

# demander choix valide (1,3)
def demander_choix_valide():
    # while true
    while True:
            # choix = input("choisissez une option")
        choix = input("Ton choix (1-3) : ")
            # verif choix
        if verif_choix(choix,1,3):
                # return choix
            return choix


    
# verif choix 
def verif_choix(choix,min, max):
    while True:    
        # si choix pas digit 
        if choix.isdigit() and min <= int(choix) <= max:
            choix = int(choix)
            # return false 
            return True
        else :
            print("Choix invalide")

    
# afficher options TODO
def afficher_options():
    # Option 1: Jouer 
    print("Option 1: Jouer")
    # Option 2: Classement
    print("Option 2: Classement")
    # Option 3: Quitter 
    print("Option 3: Quitter")
        
# effectuer choix       
def effectuer_choix(choix):
    #si choix 1 
    if choix ==  1:
        # recup username 
        recup_username()
        # lancer partie
        lancer_partie()
    # si choix 2 
    if choix == 2:
        # afficher le classement 
        afficher_classement()
    # si choix 3
    if choix == 3: 
        # Quitter 
        quitter()

def afficher_classement():
    print("AAAAAAA") #----------------------------------------------------------------# 

def quitter():
    quit()

# recup username 
def recup_username():
    # afficher "quel est ton nom"
    print("Entre ton pseudonyme :")
    # nom = str(input)
    input("...")
    nom = input(nom)

# lancer partie 
def lancer_partie():
    # Créer une équipe 
    equipe = cree_equipe()
    # choisir un ennemi
    ennemie_choisi = choisir_ennemie()
    # Lancer combat
    lancer_combat 

# Créer une équipe 
def cree_equipe():
    equipe = []
    # recuperer perso dispo 
    persos = get_perso() 
    # tant que taille [equipe] < 3 
    while len(equipe) < 3:
        # afficher perso_dispo
        print(persos)
        # faire choisir le personnage
        choisir_perso(persos, equipe)
        # afficher [equipe]
        print(equipe)

# recuperer perso dispo 
def get_perso():
    # prendre les perso dans la db 
    persos = list(db["personnages"].find({}, {"_id": 0}))
    return persos

# faire choisir le personnage
def choisir_perso(persos, equipe): 
    # récupérer input joueur 
    choix = demander_choix_valide(1,len(persos))
    # faire correspondre l'input avec le personnage [0,len(liste perso)]
    equipe.append(persos[choix - 1])
    # supprimer le personnage choisi de la liste
    persos.pop(choix - 1)

# choisir ennemi 
def choisir_ennemie():
    # prendre chiffre aléatoire [0,10]
    ennemie = list(db["monstres"].find({}, {"_id": 0}))
    # choisir le monstre associé 
    return random.choice(ennemie)

# lancer combat
def lancer_combat():
    # wave = 1 
    wave = 1
    # tant que equipe en vie 
    while equipe_alive() == True:
        # choisir ennemi 
        choisir_ennemie()
        # win = équipe en vie 
        win = equipe_alive()
        # si win 
        if win == True: 
            # wave = wave +1 
            wave = wave + 1 
            # jouer combat 
            jouer_combat
        # sinon 
        else :
            # afficher game over 
            print("Game Over !!")

# jouer combat 
def jouer_combat():
    # ennemie attaque 
    ennemie_attack
    # perso attaque
    personnage_attack 
    # vérifier perso et ennemie en vie 
    

# Equipe mort 
def equipe_mort():
    # Afficher nom 
    # afficher score 
    # attendre input 
        # afficher menu 

# équipe en vie
def equipe_alive():
    # pour i [equipe]
    # si pv > 0
        # true
    # sinin 
        # return false 

# ennemie attack
def ennemie_attack():
    # HP = "health" (PA)
    # récupérer "attack" [ennemie] "health","Defense" (PA)
    # attack - defense - health 
    # "health" (PA) = HP

# personnages attack
def personnage_attack():
    # HPE = "health" [ennemie]
    # récupérer "attack" [equipe]
    # "attack" 1 + 2 + 3 - "defense" - "Health" [ennemie]
    # "health" [ennemie] = HPA 