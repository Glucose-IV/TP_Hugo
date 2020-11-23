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
affichage = {
1:{"Nom": "Nom", "Prix":"Prix", "Quantité": "Quantité", "Total HT":"Total HT"}
}

listProduit={
1:{"nom":"banane", "prix": 4},
2:{"nom":"Pomme","prix":2},
3:{"nom":"Orange", "prix":1.5},
4:{"nom":"Poire","prix":3}
}

autreProduit="O"
totalAchat=0
compt=1

while(autreProduit=="O"):
    compt=compt+1
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

    total=prix*nb
    affichage[compt]={"Nom": ref["nom"], "Prix": prix, "Quantité": nb, "Total HT": nb*prix}
    totalAchat=totalAchat+total
    print("Voulez vous d'autres produits (O/N) ?", end=" ")
    autreProduit = input()
print("---------+---------+-------------+-------------+")
for ligne in affichage:
    x=affichage[ligne]
    print("", end="|")
    for col in x:
        print(x[col], end="     |")
    print()
    print("---------+---------+-------------+-------------+")
montantreduc=0

if(totalAchat>200):
    print("Sous-Total = " + str(totalAchat))
    print("Réduction 5% : " + str(totalAchat*0.05))
    print("Total HT = " + str(totalAchat*0.95))
    print("TTC = " + str(totalAchat*1.20))
else:
    print("Total HT = " + str(totalAchat))
    print("TTC = " + str(totalAchat*1.20))



