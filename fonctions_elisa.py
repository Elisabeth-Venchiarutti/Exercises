"""Ce fichier définit des fonctions utiles pour le programme pendu.
On utilise les données du programme contenues dans donnees.py"""

import os
import pickle
from random import choice

from donnees_elisa import *

# Gestion des scores

def recup_scores() :
    """ Cette fonction récupère les scores enregistés si le fichier existe"""
    if os.path.exists(nom_fichier_scores) :  # Le fichier existe, on le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else:  #Le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    """Cette fonction enregistre les scores dans le fichier nom_fichier_scores"""

    fichier_scores = open(nom_fichier_scores, "wb")  # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

# Fonctions gérant les éléments saisis par le joueur

def recup_nom_utilisateur():
    """Fonction récupère le nom d'utilisateur
    Le nom doit être composé de 4 caractères minimum, chiffres et lettres exclusivement
    Si le nom n'est pas valide on appelle récursivement la fonction"""

    nom_utilisateur = input("Tapez votre nom: ")
    # On met la premiere lettre en majuscule et les autres en miniscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide")
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

def recup_lettre():
    """Cette fonction récupère la lettre saisie par l'utilisateur"""

    lettre = input ("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print ("Vous n'avez pas saisi une lettre valide")
        return recup_lettre()
    else:
        return lettre


def choisir_mot():
    """Cette fonction renvoie le mot choisi dans la liste des mots
    On utilise la fonction choice du module random"""

    return choice(liste_mots)


def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué tout ou en partie"""

    mot_masque =""
    for lettre in mot_complet:
        if lettre in mot_complet:
            if lettre in lettres_trouvees:
                mot_masque += lettre
            else:
                mot_masque += "*"
    return mot_masque


    
