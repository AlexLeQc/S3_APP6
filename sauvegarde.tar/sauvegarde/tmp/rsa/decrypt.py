# Python 3 program to find a prime factor of composite using
# Pollard's Rho algorithm
import random
import math


# Function to calculate (base^exponent)%modulus
def modular_pow(base, exponent, modulus):
    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result


# method to return prime divisor for n
def PollardRho(n):
    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        # ((x^2 mod n) + c + n) %
        x = (modular_pow(x, 2, n) + c + n) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d


def Pollard_pm1(n):
    m = 2
    max = n

    for i in range(1, max):
        m = modular_pow(m, i, n)
        if math.gcd(n, m - 1) != 1:
            return math.gcd(n, m - 1)


def phiN(p, q):
    return (p - 1) * (q - 1)


def inverse_multiplicatif_mod(a, n):
    if a == 0:
        return -1
    hg = n
    hv = 0
    bg = a
    bv = 1
    while (bg != 0):
        t = hg // bg
        tg = bg
        bg = hg - (t * bg)
        hg = tg
        tv = bv
        bv = hv - (t * bv)
        hv = tv
    return hv


def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


def calculate_PhiN(p, q):
    return (p - 1) * (q - 1)


def calculate_lambdaN(p, q):
    lamdaN = calculate_PhiN(p, q) // gcd(p - 1, q - 1)
    return lamdaN

def dechiffr(messagechiffre, d, n):
    message_dechiffre = pow(messagechiffre, d, n)
    return message_dechiffre

def programme():

    #    print("test: ", inverse_multiplicatif_mod(45,56))
    #    print("test pollard: ", PollardRho(86429))
    e = 13
    n = 86062381025757488680496918738059554508315544797
    p = Pollard_pm1(n)
    print(p)
    q = n // p
    nPQ = p * q
    if (nPQ != n):
        print("ERROR")
    phi_n = phiN(p, q)
    d = inverse_multiplicatif_mod(e, phi_n) % phi_n
    #    if (d < 0):
    #        d = n + d

    print("n= ", n, "\np=", p, "\nq=", q, "\nd=", d, "\nphiN=", phi_n)
    print("private-key (n,d)= (", n, ",", d, ")")
    lamda = calculate_lambdaN(p, q)
    print("lamda = ", lamda)
    print('-----deuxieme bhay----')
    e1 = 1009
    n1 = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    p1 = Pollard_pm1(n1)
    # print(p1)
    q1 = n1 // p1
    nPQ1 = p1 * q1
    if (nPQ1 != n1):
        print("ERROR")
    phi_n1 = phiN(p1, q1)
    d1 = inverse_multiplicatif_mod(e1, phi_n1) % phi_n1
    #    if (d < 0):
    #        d = n + d

    print("n= ", n1, "\np=", p1, "\nq=", q1, "\nd=", d1, "\nphiN=", phi_n1)
    print("private-key (n,d)= (", n1, ",", d1, ")")
    lamda1 = calculate_lambdaN(p1, q1)
    print("lamda = ", lamda1)

    qdh_chiffre_avec_RSA = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    pdh_chiffre_avec_RSA = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
    gdh_chiffre_avec_RSA = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308


    gdh = dechiffr(gdh_chiffre_avec_RSA, d1, n1)
    qdh = dechiffr(qdh_chiffre_avec_RSA, d1, n1)
    pdh = dechiffr(pdh_chiffre_avec_RSA, d1, n1)
    print('g = ', gdh)




    decryote1 = modular_pow(81530476374664351124876242644701327168836407987, d, n)
    decry2 = modular_pow(83740877821201430552252653974153238737996745098,d , n)
    decry3 = modular_pow(51373667846507963545859239582447701017826406175, d, n)
    decry4 =modular_pow(61167846837720209456441528754183777549647735855, d, n)
    decry5 = modular_pow(42340513171888188994504759277496496710896088718, d, n)
    decry6 = modular_pow(65069303637151076134861115122997306654987857614, d, n)
    decry7 = modular_pow(32785990179062766920584737848735367794508677603, d, n)
    print('Alain St-Malo,		Marketing :	',decryote1)
    print('Michele Denis, 		Marketing :	', decry2)
    print('Stephanie Desjardins,  	R&D :		', decry3)
    print('Fernand Tessier, 		R&D :		',decry4)
    print('Angele Tremblay, 		Ventes :	', decry5)
    print('Bernard Dumais, 		Service :	', decry6)
    print('Claude Dupuis, 		Reception :	', decry7)

    # Driver function
if __name__ == "__main__":
        programme()
#    c = modular_pow(50, 3, 55)
#    m = modular_pow(c, 27, 55)
#    print(m)

#    c = modular_pow(50, 13, 86062381025757488680496918738059554508315544797)
#    m = modular_pow(c, 46341282156994238628536118344529511083859039514, 86062381025757488680496918738059554508315544797)
#    print(m)


# This code is contributed by alexis guerard
