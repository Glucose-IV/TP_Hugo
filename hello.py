#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hugot
#
# Created:     23/11/2020
# Copyright:   (c) hugot 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#!/usr/bin/python
prix=0
while (prix<=0):
    print("Veuillez entrer le prix du produit : ", end=" ")
    prixIn = input()
    prix = float(prixIn)
    if(prix<=0):
        print("le prix de produit ne peux pas être égal ou inférieur à 0")
nb=0
while (nb<=0):
    print("Veuillez entrer le nombre de produit : ", end=" ")
    nbIn = input()
    nb = int(nbIn)
    if(nb<=0):
        print("le nombre de produit ne peux pas être égal ou inférieur à 0")
total=prix*nb*1.20
if (total>200):
    total=total*0.95
print(total)

