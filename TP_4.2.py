#-------------------------------------------------------------------------------
# Name:        caisse1
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
import affichage as aff
import calculPrix as cp

# Noms des colonnes pour l'affichages du résumé des achats
affichage = {
1:{"Nom": "Nom", "Prix":"Prix", "Quantité": "Quantité", "Total HT":"Total HT"}
}

# Dictionnaire de références des produits
listProduit={
1:{"nom":"banane", "prix": 4},
2:{"nom":"Pomme","prix":2},
3:{"nom":"Orange", "prix":1.5},
4:{"nom":"Poire","prix":3}
}

#Condition pour acheter un autre produit
autreProduit="o"

totalAchat=0
compt=1

while(autreProduit=="o"):
    compt=compt+1
    prix=0
    ref=cp.saisieRefArticle(listProduit)
    prix = ref["prix"]
    nb=cp.saisieNombreArticle()
    total=prix*nb
    affichage[compt]={"Nom": ref["nom"], "Prix": prix, "Quantité": nb, "Total HT": nb*prix}
    totalAchat=totalAchat+total
    print("Voulez vous d'autres produits (O/N) ?", end=" ")
    autreProduit = input()

aff.affichageResume(affichage)
aff.affichageCout(totalAchat)



