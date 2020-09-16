




#! C:\Python34\python
# -*- coding: UTF-8 -*# pour spécifier le codage des caractères

from math import *

"""
programme qui affiche un joli sapin de Noël, dont la taille est donnée par l’utilisateur
"""

space = " "

char_sapin = "^"

nombre_lignes = 20

padSize = nombre_lignes - 1

num_ligne = 0


print ()

for num_ligne in range (1, nombre_lignes + 1) :
    if (num_ligne == 1):
        nbre_char_sapin = 1
    else:
        nbre_char_sapin = 2 * num_ligne - 1


    # Affichage d'une ligne de sapin
    print ( space * padSize, char_sapin * nbre_char_sapin, space * padSize )
    # Décrémenter le nombre de caractères de remplissage
    padSize -= 1
