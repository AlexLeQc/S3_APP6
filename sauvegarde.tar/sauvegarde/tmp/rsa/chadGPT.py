# Python 3 program to find a prime factor of composite using
# Pollard's Rho algorithm
import random
import math



# method to return prime divisor for n
def pollard_factorize(n):
    def rho_pollard_function(x):
        return (x**2 + 1) % n

    x = 2
    y = 2
    d = 1

    while d == 1:
        x = rho_pollard_function(x)
        y = rho_pollard_function(rho_pollard_function(y))
        d = gcd(abs(x - y), n)

    if d == n:
        # La méthode a échoué, essayez une autre approche
        return None

    return d, n // d


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi_n):
    # Utilisation de la fonction pow pour calculer l'inverse modulaire de e par rapport à phi_n
    d = pow(e, -1, phi_n)
    return d

def decrypt_rsa(nombre_chiffre, d, n):
    nombre_clair = pow(nombre_chiffre, d, n)
    return nombre_clair


# Driver function
if __name__ == "__main__":
    n = 86062381025757488680496918738059554508315544797
    e = 13
    #p, q = pollard_factorize(n)
    p = 1296005097246682578520326409
    q = 66405897020462343733
    print("One of the divisors for", n, "is ", p)
    print("q = ", q)
    phiN = (p - 1) * (q - 1)
    d = pow(e, -1, phiN)
    print("d = ", d)

    n_pour_dh = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    e_pour_dh = 1009

    qdh_chiffre_avec_RSA = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    pdh_chiffre_avec_RSA = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
    gdh_chiffre_avec_RSA = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308

    # Obtenir la clé privée d_pour_dh en utilisant la méthode de calcul appropriée

    # Déchiffrer les valeurs chiffrées avec RSA pour obtenir les valeurs de l'échange de clés Diffie-Hellman
    d_pour_dh = 68154027933166660914890730344092864878649198983935455529422960423721490188331665603876350587274300325806236608234316636462122036878942632337283353153592541640319773342392893703531066563494763814398430222694200307505853252489959059416692855383645323370594713153758488784999568103148728933198795871416131541009  # Remplacez par la clé privée d_pour_dh obtenue
    qdh = decrypt_rsa(qdh_chiffre_avec_RSA, d_pour_dh, n_pour_dh)
    pdh = decrypt_rsa(pdh_chiffre_avec_RSA, d_pour_dh, n_pour_dh)
    gdh = decrypt_rsa(gdh_chiffre_avec_RSA, d_pour_dh, n_pour_dh)

    print("Valeurs déchiffrées de l'échange Diffie-Hellman:")
    print("qdh:", qdh)
    print("pdh:", pdh)
    print("gdh:", gdh)
    clé_secrète = (gdh ^ pdh) % qdh
    print('cle secrette = ' ,clé_secrète)

    chiffre = 81530476374664351124876242644701327168836407987
    inverse_pdh_mod_qdh = pow(pdh, -1, qdh)
    dechiffre = (chiffre * inverse_pdh_mod_qdh) % qdh

    # Afficher le résultat déchiffré
    print('salaire : ', dechiffre)

# This code is contributed by chitranayal
