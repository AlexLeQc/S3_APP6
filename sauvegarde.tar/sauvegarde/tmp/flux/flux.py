'''
Created on 2009-07-14

@author: Administrateur
'''

import os.path
import array

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def get_masque_8bits(cle):
    masque = 0
    print "Ecrire le code pour extraire un masque de 8 bits de la cle"
    return masque

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def get_cle_modifiee(cle):
    nouvelle_cle = 0
    print "Ecrire le code pour preparer la cle pour la prochaine iteration"
    return nouvelle_cle

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def chiffre_caractere(caractere,masque):
    nouveau_caractere = caractere
    print "Ecrire le code pour chiffrer le caractere"
    return nouveau_caractere

# Procedure qui doit etre modifiee pour que le systeme fonctionne
def mise_a_jour_cle(tmpcle,cle):
    nouvelle_cle = 0
    print "Ecrire le code pour mettre a jour la cle au besoin"
    return nouvelle_cle


# Methode de chiffrement / dechiffrement par flux
# La cle est utilisee pour chiffrer le fichier d'entree (fichierin) et produire le fichier de sortie (fichierout)
# Si la cle est plus petite que la taille du fichier, elle doit etre repetee (est-ce une bonne idee?)
def chiffre_flux(cle,fichierin,fichierout):
    tmpcle = cle
    
    # Initialisation des fichiers en lecture et ecriture
    infileobj = open(fichierin,'rb')     # Lecture binaire du fichier
    outfileobj = open(fichierout,'wb')   # Ecriture binaire du fichier
    filesize = os.path.getsize(fichierin)
    
    # Initialisation des tableaux binaires, lecture du fichier d'entree (binaire)
    inbinvalues = array.array('B')
    inbinvalues.fromfile(infileobj, filesize)
    outbinvalues = array.array('B')
    
    # Traitement de tous les caracteres du fichier d'entree, un a la fois
    i = 0
    while (i < filesize):
        # Obtention du masque pour le prochain caractere, chiffrement de ce caractere
        mask = get_masque_8bits(tmpcle)
        tmpcle = get_cle_modifiee(tmpcle)
        newchar = chiffre_caractere(inbinvalues[i], mask)
        # Ecriture du cactere chiffre dans le tampon de sortie
        outbinvalues.append(newchar)
        
        i += 1
        tmpcle = mise_a_jour_cle(tmpcle,cle)

    # Ecriture dans le fichier de sortie, fermeture des fichiers
    infileobj.close()
    outbinvalues.tofile(outfileobj)
    outfileobj.close()

# Appel de la methode de chiffrement / dechiffrement de fichiers
cle = 2**25 - 1 - (2**17 - 1) + 2**9 - 1
chiffre_flux(cle,"test.txt","sortie.txt")