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

listProduit={
1:{"nom":"banane", "prix": 4},
2:{"nom":"Pomme","prix":2},
3:{"nom":"Orange", "prix":1.5},
4:{"nom":"Poire","prix":3}
}
print()
autreProduit="O"
totalAchat=0
while(autreProduit=="O"):
    prix=0
    while(prix==0):
        print("Veuillez entrer la référence du produit : ", end=" ")
        produitSelect = input()
        if(int(produitSelect) in listProduit.keys()):
            ref=listProduit[int(produitSelect)]
            prix = ref["prix"]
        else:
            print("Veuillez entrer une référence correct")
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
    totalAchat=totalAchat+total
    print("Voulez vous d'autres produits (O/N) ?", end=" ")
    autreProduit = input()
print(totalAchat)

