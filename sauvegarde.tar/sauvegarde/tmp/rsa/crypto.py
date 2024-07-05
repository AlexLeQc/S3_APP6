'''
Created on 2009-07-14

@author: Administrateur
'''

from math import *


verbose = 1
max = 1000
premier = list(range(0,max+1))


n_prob = 86062381025757488680496918738059554508315544797
e_prob = 13

# Plus grand commun diviseur (entre a et b)
def pgcd(a, b):
    if (a < b):
        t = a
        a = b
        b = t
    r = a % b
    while (r != 0):
        a = b
        b = r
        r = a % b
    return b

# Crible d'Eratosthene:  trouve les nombres premiers plus petits que max
# Le tableau premier[] contient un '1' si le nombre correspondant a cet indice est premier
def eratosthene():
    global verbose, max, premier
    for i in range(2, max):
         premier[i] = 1
    sqrt_max = int(floor(sqrt(max)))
    for i in range (2, sqrt_max + 1) :
        if (premier[i] == 1):
            j = 2 * i
            while( j < max):
                premier[j] = 0
                j += i
    if (verbose):
        for i in range(2, max):
            if (premier[i] == 1):
                print(i, "\n")

# Retourne le nombre de bits de la valeur passee en parametre
def get_taille(m):
    return int(round(log(m)/log(2)))
