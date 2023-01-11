#!/usr/bin/env python3
# Séance de TP n° 9
# TP 7
# Exercice 1
# Auteur KHRIS Badreddine
# Date   :  23/11/2022

import os.path

def cat(chemin):
    """Lis un fichier et numerote les lignes"""
    if os.path.exists(chemin) :
        if os.path.isfile(chemin):
            user = True
            while user == True :
                
                with open(chemin, 'r') as fd:  # Ouverture en lecture
                        content = fd.read()               # Lecture du fichier
                        lignes = content.rstrip('\n').split('\n') # Liste des lignes
                        for no in range(len(lignes)) :
                            if no%20 == 0 and no != 0:
                                teste = input("appuyez sur entrée pour continuer") 
                                if teste == "" :
                                    user = False
                            ligne = lignes[no]
                            print(no+1, ':', ligne) # Affichage
                    
        else :
            print("Fichier inexsistan : ")
    else :
        print("Fichier inexsistan : ")
    return ""
            

   
    
        
# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
  print(cat("/etc/passwd"))
   
   
   
if __name__ == "__main__":
    main()