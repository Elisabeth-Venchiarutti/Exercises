
#! C:\Python34\python
# -*- coding: UTF-8 -*# pour spécifier le codage des caractères

"""
Une machine découpe dans une plaque, des disques circulaires de rayon rExt, percés d’un trou
circulaire de rayon rInt avec rInt < rExt et ne débordant pas du disque.
Quelle est la surface d’un disque découpé ?
"""

from math import *
import os

rExt = float (input ("Rayon ext :  "))
rInt = float (input ("Rayon int :  "))

if rInt >= rExt:
    print ("Rayon int > Rayon ext")
    print ("Fin d'exercice")
    os.system("pause")

else :
    sGrandDisque = pi * rExt**2
    sTrou = pi * rInt**2

    surface = sGrandDisque - sTrou

    print("Surface du disque découpé =   ", surface)





          


