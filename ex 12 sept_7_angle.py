
#! C:\Python34\python
# -*- coding: UTF-8 -*# pour spécifier le codage des caractères

"""
programme, qui donne la mesure de l’angle  d’un triangle rectangle, dont on saisit le
côté opposé et l’hypothénuse.
Rappel : sinφ = CoteOppose/Hypotenuse
"""


from math import *
import os

hypo = (input ("Hypoténusa :  "))
hypof = float(hypo)

oppose = (input ("Côté opposé :  "))
opposef = float(oppose)


print("Angle : ", degrees (asin (opposef/hypof)))







          




          


