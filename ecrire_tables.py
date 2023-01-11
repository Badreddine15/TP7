#!/usr/bin/env python3
# Séance de TP n° 9
# TP 7
# Exercice 2
# Auteur KHRIS Badreddine
# Date   :  24/11/2022
import os
def ecrire_table(fd , num_table):
            
    for i in range(1,10):
                fd.write(str(num_table))
                fd.write(" ")
                fd.write("*")
                fd.write(" ")
                fd.write(str(i))
                fd.write(" ")
                fd.write("=")
                fd.write(" ")
                fd.write(str(i*num_table))
                fd.write("\n")

            

# --------------------------------------------------
# Programme principal
# --------------------------------------------------
def main():
    with open("table.txt", "w") as fd:
        for i in range(2,11):
            ecrire_table(fd, i)
            fd.write("\n")
   
   
if __name__ == "__main__":
    main()