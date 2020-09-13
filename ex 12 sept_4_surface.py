
#! C:\Python34\python
# -*- coding: UTF-8 -*# pour spécifier le codage des caractères



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





          


