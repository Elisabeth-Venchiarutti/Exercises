"""Ce fichier contient le jeu du pendu.

Il s'appuie sur les fichiers :
- donnees_elisa.py
- fonctions_elisa.py"""

from donnees_elisa import *
from fonctions_elisa import *

# On récupère les scores de la partie

scores = recup_scores()

# On récupère le nom d'utilisateur
utilisateur = recup_nom_utilisateur()

# Si l'utilisateur n'a pas de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0

# la varaible pour savoir quand arrêter partie
continuer_partie = 'o'

while continuer_partie != 'n':
    print ("Jouer {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances > 0:
        print ("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà choisi cette lettre")
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print("Bien joué")
        else:
            nb_chances -= 1
            print (" ...  non, cette lettre ne se trouve pas dans le mot ... ")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    # A t'on trouvé le mot

    if mot_a_trouver == mot_trouve:
        print ("Félicitations ! Vous avez trouvé le mot {0}".format(mot_a_trouver))
    else:
        print("Pendu !!!   Vous avez perdu")

    # On met à jour le score du joueur
    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()

# La partie est finie
enregistrer_scores(scores)

# On affiche le score
print ("Vous finissez la partie avec {0} points".format(scores[utilisateur]))
        
