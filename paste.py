#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:56:50 2022

@author: k22005807
"""

import sys, os 
from concat import verifie_fichier
def fusion(fd1, fd2, fd_sortie):
    lecture = fd1.readline()
    lecture = lecture.rstrip("\n")
    fd_sortie.write(lecture)
    fd_sortie.write("\t")
    lecture = fd2.readline()
    fd_sortie.write(lecture)
    while lecture != "" :
        lecture = fd1.readline()
        lecture = lecture.rstrip("\n")
        fd_sortie.write(lecture)
        fd_sortie.write("\t")
        lecture = fd2.readline()
        fd_sortie.write(lecture)
    
                       
def main():
    if len(sys.argv) == 4 :
        if verifie_fichier(sys.argv[1]) and verifie_fichier(sys.argv[2]):
           with open(sys.argv[3], "w") as f3:
               with open(sys.argv[1], "r") as f1 :
                   with open(sys.argv[2], "r") as f2 :
                       fusion(f1, f2, f3)
                       f3.write("\n")

    else : 
        print("Format correct : fichier1 fichier2 fichier3")

if __name__ == "__main__":
    main()