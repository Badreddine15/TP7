#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:48:20 2022

@author: k22005807
"""

import sys, os 
def copie(fd_lect1,fd_lect2, fd_ecr):
    """copie le content de fd_lect df_ecrt"""
    lecture = fd_lect1.readline().rstrip("\n")
    lecture2 = "\t" + fd_lect2.readline()
    fd_ecr.write(lecture + lecture2)
    while lecture != "" and lecture2 != "" :
        lecture = fd_lect1.readline().rstrip("\n") 
        lecture2 =fd_lect2.readline().rstrip("\n")
        fd_ecr.write(lecture + "\t" + lecture2 + "\n")
    





def verifie_fichier(chemin):
    """verfie si le chemin existe et que c'est un fichier"""
    if os.path.exists(chemin) and not os.path.isfile(chemin) :
        print(chemin," n'est pas un fichier")
    elif not os.path.exists(chemin) :
        print("Le chemin" , chemin ,"n'existe pas")
    else :
        return True
                
        

def main():
    if len(sys.argv) == 4 :
        if verifie_fichier(sys.argv[1]) and verifie_fichier(sys.argv[2]):
           with open(sys.argv[3], "w") as f3:
               with open(sys.argv[1], "r") as f1 :
                   with open(sys.argv[2], "r") as f2 :
                       copie(f1,f2,f3)
                  
                   
    else : 
        print("Format correct : fichier1 fichier2 fichier3")
                       
    
if __name__ == "__main__":
    main()