#!/usr/bin/env python3
# Séance de TP n° 9
# TP 7
# Exercice 2
# Auteur KHRIS Badreddine
# Date   :  23/11/2022

import os
import sys
def cat(chemin):
    """Lis un fichier et numerote les lignes"""
    n = nbre_lignes_terminal()
    if os.path.exists(chemin) :
        if os.path.isfile(chemin):
            tracker = -1
            user = True
            while user == True :
                with open(chemin, 'r') as fd:  # Ouverture en lecture
                        content = fd.read()               # Lecture du fichier
                        lignes = content.rstrip('\n').split('\n') # Liste des lignes
                        for no in range(len(lignes)) :
                            tracker += 1 
                            if tracker == n-1 : 
                                tracker = 0
                                teste = input("appuyez sur entrée pour continuer") 
                                if teste == "" :
                                    user = False
                            ligne = lignes[no]
                            print(no+1, ':', ligne)
                teste = input("appuyez sur entrée pour continuer") 
                            
                            # Affichage
                    
        else :
            print("Fichier inexsistant : ")

    return ""
            

def nbre_lignes_terminal():
    return os.get_terminal_size()[1]

# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
    for i in range(len(sys.argv)-1):
        cat(sys.argv[i+1])
        
   
   
if __name__ == "__main__":
    main()