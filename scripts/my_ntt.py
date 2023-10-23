from math import log2, ceil
from ntt_utils import gen_w_table, gen_w_inv_table
from random import randint

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_nth_root_of_unity_mod_q(n, q):
    roots = []
    for x in range(1, q):
        if gcd(x, q) == 1 and pow(x, n, q) == 1:
            roots.append(x)
    return roots


def find_2nth_rou(q, n):
    for i in range(2, q):
        if pow(i, 2*n, q) == 1 and gcd(i, q) == 1:
            return i

    return None

def ntt(a, q, print_step=False, psi=0):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n, psi)
    # print("WTAB", w_table)
    # print(res)
    for i in range(int(log2(n))):
        # print(f"STAGE {i + 1}")
        for j in range(2**(i)):
            for k in range(n // (2 ** (i + 1))):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                W = w_table[i][j]

                b0 = res[a_idx] + res[a_idx + jump] * W
                b1 = res[a_idx] - res[a_idx + jump] * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

                # print(i, j, k, a_idx, W)
        if print_step:
            print(res)

    return res

def intt(a, q, psi=0, print_step=False):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_inv_table = gen_w_inv_table(q, n, psi)
    # print(res)
    for i in range(int(log2(n)) - 1, -1, -1):
        # print(f"STAGE {i + 1}")
        for j in range(2**(i)):
            for k in range(n // (2 ** (i + 1))):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                W = w_inv_table[i][j]

                b0 = (res[a_idx] + res[a_idx + jump]) * pow(2, -1, q)
                b1 = (res[a_idx] - res[a_idx + jump]) * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

                # print(i, j, k, a_idx, a_idx + jump, W)
    
        if print_step:
            print(res)

    # res = [(r * pow(n, -1, q)) % q for r in res]

    return res

if __name__ == "__main__":
    N = 16
    # print(gen_w_table(257, 8))
    # print(gen_w_inv_table(257, 8))
    print(gen_w_table(65537, N))
    print(gen_w_inv_table(65537, N))
    # print(ntt([1  for i in range(32)]))
    inp = [randint(0, 65536) for i in range(N)]
    a = ntt(inp, 65537)
    b = ntt(inp, 65537)
    c = [((a[i] * b[i]) % 65537) for i in range(N)]
    ar = intt(a, 65537)
    print(a, inp == ar)
    print(ar)
    print(b)
    print(intt(c, 65537))
    # print("ASDF")
    # print(intt(a, 257))
    # print(intt(a, 65537))
