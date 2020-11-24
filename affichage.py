#-------------------------------------------------------------------------------
# Name:        affichage
# Purpose:
#
# Author:      hugot
#
# Created:     24/11/2020
# Copyright:   (c) hugot 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#!/usr/bin/python

# Affichage des prix, du sous-total et de la réduction si il y en a une
def affichageCout(totalAchat):
    if(totalAchat>200):
        print("Sous-Total = " + str(round(totalAchat,2)))
        print("Réduction 5% : " + str(round((totalAchat*0.05),2)))
        print("Total HT = " + str(round((totalAchat*0.95),2)))
        print("TTC = " + str(round((totalAchat*1.20),2)))
    else:
        print("Total HT = " + str(round(totalAchat,2)))
        print("TTC = " + str(round((totalAchat*1.20),2)))

# Affichage du détails des produits acheté
def affichageResume(affichage):
    print("---------+---------+-------------+-------------+")
    for ligne in affichage:
        x=affichage[ligne]
        print("", end="|")
        for col in x:
            print(x[col], end="     |")
        print()
        print("---------+---------+-------------+-------------+")



