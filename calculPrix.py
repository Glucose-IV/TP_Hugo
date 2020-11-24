#-------------------------------------------------------------------------------
# Name:        calculPrix
# Purpose:
#
# Author:      hugot
#
# Created:     24/11/2020
# Copyright:   (c) hugot 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Fonction de saisie du nombre de produit acheté
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

# Fonction de saisie du choix de produit
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