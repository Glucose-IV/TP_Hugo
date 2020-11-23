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


def affichageCout(totalAchat):
    if(totalAchat>200):
        print("Sous-Total = " + str(round(totalAchat,2)))
        print("Réduction 5% : " + str(round((totalAchat*0.05),2)))
        print("Total HT = " + str(round((totalAchat*0.95),2)))
        print("TTC = " + str(round((totalAchat*1.20),2)))
    else:
        print("Total HT = " + str(round(totalAchat,2)))
        print("TTC = " + str(round((totalAchat*1.20),2)))


def affichageResume(affichage):
    print("---------+---------+-------------+-------------+")
    for ligne in affichage:
        x=affichage[ligne]
        print("", end="|")
        for col in x:
            print(x[col], end="     |")
        print()
        print("---------+---------+-------------+-------------+")


def saisieNombreArticle():
    nb=0
    while (nb<=0):
        print("Veuillez entrer le nombre de produit : ", end=" ")

        try:
            nb = int(input())
        except ValueError:
            print("Veuillez entrer un nombre")
        if(nb<=0):
            print("Vous devez saisir un nombre et ce dernier ne peux pas être égal ou inférieur à 0")
    return nb

def saisieRefArticle(listProduit):
    produitSelect=5
    while produitSelect>=5 or produitSelect<0 :
        print("Veuillez entrer la référence du produit : ", end=" ")
        try:
            produitSelect = int(input())
        except ValueError:
            print("Veuillez entrer un nombre")

        if(int(produitSelect) in listProduit.keys()):
            ref=listProduit[int(produitSelect)]
        else:
            print("Veuillez entrer une référence correct")
    return(ref)




affichage = {
1:{"Nom": "Nom", "Prix":"Prix", "Quantité": "Quantité", "Total HT":"Total HT"}
}

listProduit={
1:{"nom":"banane", "prix": 4},
2:{"nom":"Pomme","prix":2},
3:{"nom":"Orange", "prix":1.5},
4:{"nom":"Poire","prix":3}
}
autreProduit="o"
totalAchat=0
compt=1
while(autreProduit=="o"):
    compt=compt+1
    prix=0
    ref=saisieRefArticle(listProduit)
    prix = ref["prix"]
    nb=saisieNombreArticle()
    total=prix*nb
    affichage[compt]={"Nom": ref["nom"], "Prix": prix, "Quantité": nb, "Total HT": nb*prix}
    totalAchat=totalAchat+total
    print("Voulez vous d'autres produits (O/N) ?", end=" ")
    autreProduit = input()

affichageResume(affichage)
affichageCout(totalAchat)



