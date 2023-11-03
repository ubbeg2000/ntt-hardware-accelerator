from random import randint, gauss
from my_ntt import ntt, intt, find_2nth_rou

D = 16
T = 16
M = 65536
Q = 65537
PSI = 2
BETA = 19

def sample_from_r2():
    return [randint(0, 1) for i in range(D)]

def sample_from_rQ():
    return [randint(0, M-1) for i in range(D)]

def sample_from_chi():
    return [int(gauss(0, 3.2)) % BETA for i in range(D)]

def poly_point_add(a, b):
    return [(a[i] + b[i]) % Q for i in range(D)]

def poly_point_mult(a, b):
    return [(a[i] * b[i]) % Q for i in range(D)]

def poly_mult(a, b):
    an = ntt(a, Q, psi=PSI)
    bn = ntt(b, Q, psi=PSI)
    cn = poly_point_mult(an, bn)
    return intt(cn, Q, psi=PSI)

def generate_keys():
    # secret key generation
    sk = sample_from_r2()

    # public key generation
    pk1 = sample_from_rQ()

    pk1n = ntt(pk1, Q, psi=PSI)
    skn = ntt(sk, Q, psi=PSI)
    en = ntt(sample_from_chi(), Q, psi=PSI)

    pk0n = poly_point_mult(poly_point_add(poly_point_mult(pk1n, skn), en), [-1 for i in range(D)])
    # pk0 = [-e % Q for e in intt(pk0n, Q, psi=PSI)]

    return skn, pk0n, pk1n

def encrypt(m, pk0n, pk1n):
    delta = M // T
    # deltas = [delta for i in range(D)]

    mn = [delta * e for e in ntt(m, Q, psi=PSI)]

    un = ntt(sample_from_r2(), Q, psi=PSI)
    e1n = ntt(sample_from_chi(), Q, psi=PSI)
    e2n = ntt(sample_from_chi(), Q, psi=PSI)

    ct0n = poly_point_add(poly_point_add(poly_point_mult(pk0n, un), e1n), mn)
    ct1n = poly_point_add(poly_point_mult(pk1n, un), e2n)

    return ct0n, ct1n

def decrypt(skn, ct0n, ct1n):
    # c0 + c1 · s
    
    temp = intt(poly_point_add(ct0n, poly_point_mult(ct1n, skn)), Q, psi=PSI)
    print(temp)
    print([round((e << 4) >> 16) % T for e in temp])
    print([T * e / M % T for e in temp])
    return [round((e << 4) >> 16) % T for e in temp]

if __name__ == "__main__":
    # inp = [1 for i in range(D)]
    # inpn = ntt(inp, Q, psi=PSI)
    # inp2 = [2 for i in range(D)]
    # print([4*i%Q for i in ntt(inp, Q, psi=PSI)])
    # print(ntt([4*i for i in inp], Q, psi=PSI))
    # print(intt([4*i%Q for i in ntt(inp, Q, psi=PSI)], Q, psi=PSI))
    # print(intt(poly_point_mult(inpn, inpn), Q, psi=PSI))
    sk, pk0, pk1 = generate_keys()
    CNT = 0
    for i in range(10):
        m1 = [randint(0, T-1) for i in range(D)]
        m2 = [randint(0, T-1) for i in range(D)]
        m3 = [(m1[i] + m2[i]) % T for i in range(D)]
        ct10, ct11 = encrypt(m1, pk0, pk1)
        ct20, ct21 = encrypt(m2, pk0, pk1)
        ct0 = poly_point_add(ct10, ct20)
        ct1 = poly_point_add(ct11, ct21)
        me = decrypt(sk, ct0, ct1)
        if me != m3:
            # print(me)
            # print(m3)
            print("NOK")
            CNT += 1
        # else:
        #     print("OK!")
        # print(me)
        # print(me)

    print(CNT)