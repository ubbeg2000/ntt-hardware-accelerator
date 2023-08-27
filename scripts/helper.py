
from generate_prime import *
from random import randint

# Modular inverse of an integer


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# GCD of two integers


def gcd(n1, n2):
    a = n1
    b = n2
    while b != 0:
        a, b = b, a % b
    return a

# Bit-Reverse integer


def intReverse(a, n):
    b = ('{:0'+str(n)+'b}').format(a)
    return int(b[::-1], 2)

# Bit-Reversed index


def indexReverse(a, r):
    n = len(a)
    b = [0]*n
    for i in range(n):
        rev_idx = intReverse(i, r)
        b[rev_idx] = a[i]
    return b

# Reference Polynomial Multiplication
# with f(x) = x^n + 1


def RefPolMul(A, B, M):
    C = [0] * (2 * len(A))
    D = [0] * (len(A))
    for indexA, elemA in enumerate(A):
        for indexB, elemB in enumerate(B):
            C[indexA + indexB] = (C[indexA + indexB] + elemA * elemB) % M

    for i in range(len(A)):
        D[i] = (C[i] - C[i + len(A)]) % M
    return D

# Reference Polynomial Multiplication (w/ modulus)
# with f(x) = x^n + 1


def RefPolMulv2(A, B):
    C = [0] * (2 * len(A))
    D = [0] * (len(A))
    for indexA, elemA in enumerate(A):
        for indexB, elemB in enumerate(B):
            C[indexA + indexB] = (C[indexA + indexB] + elemA * elemB)

    for i in range(len(A)):
        D[i] = (C[i] - C[i + len(A)])
    return D

# Check if input is m-th (could be n or 2n) primitive root of unity of q


def isrootofunity(w, m, q):
    if w == 0:
        return False
    elif pow(w, m//2, q) == (q-1):
        return True
    else:
        return False

# Returns a proper NTT-friendly prime


def GetProperPrime(n, logq):
    factor = 2*n
    value = (1 << logq) - factor + 1
    lbound = (1 << (logq-1))
    while(value > lbound):
        if is_prime(value) == True:
            return value
        else:
            value = value - factor
    raise Exception("Failed to find a proper prime.")

# Returns a primitive root


def FindPrimitiveRoot(m, q):
    g = (q-1)//m

    if (q-1) != g*m:
        return False, 0

    attempt_ctr = 0
    attempt_max = 100

    while(attempt_ctr < attempt_max):
        a = randint(2, q-1)
        b = pow(a, g, q)
        # check
        if isrootofunity(b, m, q):
            return True, b
        else:
            attempt_ctr = attempt_ctr+1

    return True, 0

# Generate necessary BFV parameters given n and log(q)


def ParamGen(n, logq):
    pfound = False
    while (not(pfound)):
        #     # first, find a proper prime
        q = GetProperPrime(n, logq)
        # then find primitive root
        pfound, psi = FindPrimitiveRoot(2*n, q)
    psiv = modinv(psi, q)
    w = pow(psi, 2, q)
    wv = modinv(w, q)
    return q, psi, psiv, w, wv
