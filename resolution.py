#!/usr/bin/env python3
# Séance de TP n° 9
# TP 7
# Exercice 2
# Auteur KHRIS Badreddine
# Date   :  24/11/2022
import sys

def resoud(hote): 
    '''resolution d'hote dns'''
    with open("/etc/hosts", 'r')as fd :
        hote = str(hote)
        retour = []
        content = fd.read()
        lignes = content.rstrip('\n').split('\n')
        for i in lignes : 
            if "#" in i :
                lignes.pop(lignes.index(i))
        for i in range(len(lignes)):
            retour.append(lignes[i].split())
        for i in range(len(retour)):
            if hote in retour[i]:
                print(retour[i][0])
            

# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
    if len(sys.argv) == 2:
        resoud(sys.argv[1])
    else :
        print("syntaxe : resolution.py nom_d_hote")
   
   
if __name__ == "__main__":
    main()