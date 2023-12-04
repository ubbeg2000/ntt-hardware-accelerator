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
        ok = True
        for j in range(1, 2*n+1):
            if pow(i, j, q) == 1 and j != 2*n:
                ok = False

        if ok and pow(i, 2*n, q) == 1:
            return i

    return None

def is_power_of_two(num):
    return bin(num).count('1') == 1

def find_2nth_rous(q, n):
    for i in range(2, n):
        ok = True
        for j in range(1, 2*n+1):
            if pow(i, j, q) == 1 and j != 2*n:
                ok = False

        if ok and pow(i, 2*n, q) == 1:
            num = pow(i, n//2, q)
            num1 = pow(i, n//4, q)
            num2 = pow(i, n//8, q)
            if is_power_of_two(num) and is_power_of_two(num1) and is_power_of_two(num2):
                print(num, num1, num2)
                print(i)

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
    # 120833 55739
    N = pow(2, 10)
    Q = 65537
    for i in range(10, 17):
        print(f"N = {2**i}")
        psi = find_2nth_rous(Q, 2**i)
    # print("PSI", psi)
    # print(gen_w_table(257, 8))
    # print(gen_w_inv_table(257, 8))
    # print(gen_w_table(65537, N))
    # print(gen_w_inv_table(65537, N))
    # print(ntt([1  for i in range(32)]))
    # find_2nth_rous(Q, N)
    # x = ntt([1 for i in range(N)], Q, psi=psi)
    # print(x)
    # print(intt(x, Q, psi=psi))
    # inp_1 = [1 for i in range(N)]
    # inp_2 = [1 for i in range(N)]

    # a = [pow(e * e, 1, Q) for e in ntt(inp_1, Q, psi=psi)]
    # b = [pow(e * e, 1, 65537) for e in ntt(inp_1, 65537, psi=find_2nth_rou(65537, N))]
    # # print(a)
    # print(intt(a, Q, psi=psi))
    # # print(b)
    # print(intt(b, 65537, psi=find_2nth_rou(65537, N)))
    # # print(intt(b, 65537, psi=psi) == intt(a, Q, psi=psi))
    # print(find_2nth_rou(Q, N))
    # print(find_2nth_rou(65537, N))
    # c = [((a[i] * b[i]) % 65537) for i in range(N)]
    # ar = intt(a, 65537)
    # print(a, inp == ar)
    # print(ar)
    # print(b)
    # print(intt(c, 65537))
    # print("ASDF")
    # print(intt(a, 257))
    # print(intt(a, 65537))
