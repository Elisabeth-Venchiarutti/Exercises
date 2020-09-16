




#! C:\Python34\python
# -*- coding: UTF-8 -*# pour spécifier le codage des caractères

from math import *

"""
script convertir.py, qui effectue une conversion euros en dollars.
"""

devise = input("Choissez la devise - € ou $ :   ")
montant = int (input("Tapez le montant :  "))


""" 1 euro = 1.19 dollar"""

taux_conversion_euro = 1.19


if devise == "€":
    montant_dollar = montant * taux_conversion_euro
    print ("%f €" % (montant), "  =  ",  "%f $" % (montant_dollar))
    
elif devise == "$":
    montant_euro = montant / taux_conversion_euro
    print ("%f $" % (montant), "  =  ", "%f €" % (montant_euro))
    
else :
    print(" Mauvaise devise")
    
    
