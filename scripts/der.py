# -*- coding: utf-8 -*-
"""HE_BFV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aVCbff24chsLiP_5Ub8YCN09J7QvqZMl
"""

import cupy as cp
import time
import numpy as np
from numpy.polynomial import polynomial as poly


def add_plain(ct, pt, q, t, poly_mod):
    size = len(poly_mod) - 1
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m % q
    new_ct0 = polyadd(ct[0], scaled_m, q, poly_mod)
    return (new_ct0, ct[1])


def mul_plain(ct, pt, q, t, poly_mod):
    size = len(poly_mod) - 1
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    new_c0 = polymul(ct[0], m, q, poly_mod)
    new_c1 = polymul(ct[1], m, q, poly_mod)
    return (new_c0, new_c1)


def gen_binary_poly(size):
    return np.random.randint(0, 2, size, dtype=np.int64)


def gen_uniform_poly(size, modulus):
    return np.random.randint(0, modulus, size, dtype=np.int64)


def gen_normal_poly(size):
    return np.int64(np.random.normal(0, 2, size=size))


def keygen(size, modulus, poly_mod):
    sk = gen_binary_poly(size)
    a = gen_uniform_poly(size, modulus)
    e = gen_normal_poly(size)
    b = polyadd(polymul(-a, sk, modulus, poly_mod), -e, modulus, poly_mod)
    return (b, a), sk


def polymul(x, y, modulus, poly_mod):
    print("nilai x", x)
    print("nilai y", y)
    print("nilai polymul x y", poly.polymul(x, y))
    print("nilai polydiv x y", poly.polydiv(x, y))

    return np.int64(
        np.round(poly.polydiv(poly.polymul(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )


def polyadd(x, y, modulus, poly_mod):
    return np.int64(
        np.round(poly.polydiv(poly.polyadd(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )


def encrypt(pk, size, q, t, poly_mod, pt):
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m % q
    e1 = gen_normal_poly(size)
    e2 = gen_normal_poly(size)
    u = gen_binary_poly(size)
    ct0 = polyadd(
        polyadd(
            polymul(pk[0], u, q, poly_mod),
            e1, q, poly_mod),
        scaled_m, q, poly_mod
    )
    ct1 = polyadd(
        polymul(pk[1], u, q, poly_mod),
        e2, q, poly_mod
    )
    return (ct0, ct1)


def decrypt(sk, size, q, t, poly_mod, ct):
    scaled_pt = polyadd(
        polymul(ct[1], sk, q, poly_mod),
        ct[0], q, poly_mod
    )
    decrypted_poly = np.round(scaled_pt * t / q) % t
    return int(decrypted_poly[0])


_start_time = time.time()
arrkos = []


def tic():
    global _start_time
    _start_time = time.time()


def tac():
    t_sec = round(time.time() - _start_time)
    arris = t_sec
    (t_min, t_sec) = divmod(t_sec, 60)
    (t_hour, t_min) = divmod(t_min, 60)
    arrkos.append(arris)
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour, t_min, t_sec))


def man(val):
    tic()
    # Scheme's parameters
    # polynomial modulus degree
    n = 2**11
    # ciphertext modulus
    q = 2**32
    # plaintext modulus
    t = 2**2

    # polynomial modulus
    poly_mod = np.array([1] + [0] * (n - 1) + [1])
    # Keygen
    pk, sk = keygen(n, q, poly_mod)
    # Encryption
    pt1, pt2 = 123, 16
    cst1, cst2 = 7, 16

    ct1 = encrypt(pk, n, q, t, poly_mod, pt1)
    ct2 = encrypt(pk, n, q, t, poly_mod, pt2)

    print("[+] Ciphertext ct1({}):".format(pt1))
    print("")
    print("\t ct1_0:", ct1[0])
    print("\t ct1_1:", ct1[1])
    print("")
    print("[+] Ciphertext ct2({}):".format(pt2))
    print("")
    print("\t ct1_0:", ct2[0])
    print("\t ct1_1:", ct2[1])
    print("")

    # Evaluation
    ct3 = add_plain(ct1, cst1, q, t, poly_mod)
    ct4 = mul_plain(ct2, cst2, q, t, poly_mod)

    # Decryption
    decrypted_ct3 = decrypt(sk, n, q, t, poly_mod, ct3)
    decrypted_ct4 = decrypt(sk, n, q, t, poly_mod, ct4)

    print("[+] Decrypted ct3(ct1 + {}): {}".format(cst1, decrypted_ct3))
    print("[+] Decrypted ct4(ct2 * {}): {}".format(cst2, decrypted_ct4))
    tac()
    print(arrkos)


for i in range(1):
    man(i)
print(arrkos)


def add_plain(ct, pt, q, t, poly_mod):
    size = len(poly_mod) - 1
    apaini = [pt] + [1]
    print("apa ini ", apaini * (size - 1), apaini[0], type([1]))
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    m_cp = cp.array([pt] + [0] * (size - 1), dtype=cp.int64) % t

    print("fungsi add_addplain m, ", m, m_cp)

    delta = q // t
    scaled_m = delta * m % q
    new_ct0 = polyadd(ct[0], scaled_m, q, poly_mod)
    return (new_ct0, ct[1])


def mul_plain(ct, pt, q, t, poly_mod):
    size = len(poly_mod) - 1
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    m_cp = cp.array([pt] + [0] * (size - 1), dtype=np.int64) % t

    print("fungsi mul_plain ", m, m_cp)

    new_c0 = polymul(ct[0], m, q, poly_mod)
    new_c1 = polymul(ct[1], m, q, poly_mod)
    return (new_c0, new_c1)


def gen_binary_poly(size):
    return np.random.randint(0, 2, size, dtype=np.int64)


def gen_uniform_poly(size, modulus):
    return np.random.randint(0, modulus, size, dtype=np.int64)


def gen_normal_poly(size):
    return np.int64(np.random.normal(0, 2, size=size))


def keygen(size, modulus, poly_mod):
    sk = gen_binary_poly(size)
    a = gen_uniform_poly(size, modulus)
    e = gen_normal_poly(size)
    b = polyadd(polymul(-a, sk, modulus, poly_mod), -e, modulus, poly_mod)
    return (b, a), sk


def polymul(x, y, modulus, poly_mod):
    print("test np.int64 ", np.int64(np.random.normal(0, 10000000)))
    print("nilai x dan y ", x, y)

    return np.int64(
        np.round(poly.polydiv(poly.polymul(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )


def polyadd(x, y, modulus, poly_mod):
    return np.int64(
        np.round(poly.polydiv(poly.polyadd(x, y) %
                              modulus, poly_mod)[1] % modulus)
    )


def encrypt(pk, size, q, t, poly_mod, pt):
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m % q
    e1 = gen_normal_poly(size)
    e2 = gen_normal_poly(size)
    u = gen_binary_poly(size)
    ct0 = polyadd(
        polyadd(
            polymul(pk[0], u, q, poly_mod),
            e1, q, poly_mod),
        scaled_m, q, poly_mod
    )
    ct1 = polyadd(
        polymul(pk[1], u, q, poly_mod),
        e2, q, poly_mod
    )
    return (ct0, ct1)


def decrypt(sk, size, q, t, poly_mod, ct):
    scaled_pt = polyadd(
        polymul(ct[1], sk, q, poly_mod),
        ct[0], q, poly_mod
    )
    decrypted_poly = np.round(scaled_pt * t / q) % t
    return int(decrypted_poly[0])


_start_time = time.time()
arrkos = []


def tic():
    global _start_time
    _start_time = time.time()


def tac():
    t_sec = round(time.time() - _start_time)
    arris = t_sec
    (t_min, t_sec) = divmod(t_sec, 60)
    (t_hour, t_min) = divmod(t_min, 60)
    arrkos.append(arris)
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour, t_min, t_sec))


def man(val):
    tic()
    # Scheme's parameters
    # polynomial modulus degree
    n = 2**4
    # ciphertext modulus
    q = 2**16
    # plaintext modulus
    t = 2**8

    # polynomial modulus
    poly_mod = np.array([1] + [0] * (n - 1) + [1])
    poly_mod_cp = cp.array([1] + [0] * (n - 1) + [1])
    print("fungsi man poly_mod ", poly_mod, poly_mod_cp)
    # Keygen
    pk, sk = keygen(n, q, poly_mod)
    # Encryption
    pt1, pt2 = 123, 16
    cst1, cst2 = 7, 16

    ct1 = encrypt(pk, n, q, t, poly_mod, pt1)
    ct2 = encrypt(pk, n, q, t, poly_mod, pt2)

    print("[+] Ciphertext ct1({}):".format(pt1))
    print("")
    print("\t ct1_0:", ct1[0])
    print("\t ct1_1:", ct1[1])
    print("")
    print("[+] Ciphertext ct2({}):".format(pt2))
    print("")
    print("\t ct1_0:", ct2[0])
    print("\t ct1_1:", ct2[1])
    print("")

    # Evaluation
    ct3 = add_plain(ct1, cst1, q, t, poly_mod)
    ct4 = mul_plain(ct2, cst2, q, t, poly_mod)

    # Decryption
    decrypted_ct3 = decrypt(sk, n, q, t, poly_mod, ct3)
    decrypted_ct4 = decrypt(sk, n, q, t, poly_mod, ct4)

    print("[+] Decrypted ct3(ct1 + {}): {}".format(cst1, decrypted_ct3))
    print("[+] Decrypted ct4(ct2 * {}): {}".format(cst2, decrypted_ct4))
    tac()
    print(arrkos)


for i in range(1):
    man(i)
print(arrkos)
