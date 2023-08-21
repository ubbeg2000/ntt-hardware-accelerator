from math import ceil, log2
from random import randint

N = 17
D = 128
Q = 65537

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


def gen_w_table(q, n):
    w_table = [[] for i in range(int(log2(n)))]
    psi = find_2nth_rou(q, n)
    for i in range(int(log2(n))):
        for j in range(2 ** i):
            p = n//(2 ** (i + 1)) + j * n//2
            while p > n:
                p -= (n - 2)
            w_table[i] = w_table[i] + [pow(psi, p, q)]

    return w_table


def gen_w_inv_table(q, n):
    w_inv_table = [[] for i in range(int(log2(n)))]
    psi = find_2nth_rou(q, n)
    # print(psi)
    for i in range(int(log2(n))):
        for j in range(2 ** i):
            p = n//(2 ** (i + 1)) + j * n//2
            while p > n:
                p -= (n - 2)
            w_inv_table[i] = w_inv_table[i] + [pow(psi, -p, q)]

    return w_inv_table


def ntt(a, q):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n)
    for i in range(int(log2(n))):
        for j in range(2**(i)):
            for k in range(n // (2 ** (i + 1))):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                W = w_table[i][j]

                b0 = res[a_idx] + res[a_idx + jump] * W
                b1 = res[a_idx] - res[a_idx + jump] * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

        print(res)
    return res


def ntt_radix_4(a, q):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n)
    for i in range(int(log2(n)/2)):
        for j in range(2**(i)):
            for k in range(n // (2 ** (i + 1))):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                W = w_table[i][j]

                b0 = res[a_idx] + res[a_idx + jump] * W
                b1 = res[a_idx] - res[a_idx + jump] * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

    return res


def intt(a, q):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_inv_table = gen_w_inv_table(q, n)
    # print(res)
    for i in range(int(log2(n)) - 1, -1, -1):
        for j in range(2**(i)):
            for k in range(n // (2 ** (i + 1))):
                a_idx = j * n // (2 ** (i)) + k
                jump = n // (2 ** (i + 1))

                W = w_inv_table[i][j]

                b0 = (res[a_idx] + res[a_idx + jump])
                b1 = (res[a_idx] - res[a_idx + jump]) * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

    res = [(r * pow(n, -1, q)) % q for r in res]

    return res

def arr_to_bin_str(arr):
    a_bin_str = ""
    for d in arr:
        a_bin_str = "{0:b}".format(d).rjust(N, "0") + a_bin_str
    return a_bin_str

rand_arr = [randint(0, Q-1) for i in range(D)]

input_file = open("./tests/ntt_intt/testcase.txt", "w")
input_file.write(f"{arr_to_bin_str([1 for i in range(D)])}\n")
input_file.write(f"{arr_to_bin_str(rand_arr)}\n")
input_file.write(f"{arr_to_bin_str([i+1 for i in range(D)])}\n")
input_file.write(f"{arr_to_bin_str([D-i for i in range(D)])}\n")
input_file.close()

output_file = open("./tests/ntt_intt/expected.txt", "w")
output_file.write(f"{arr_to_bin_str(ntt([1 for i in range(D)], Q))}\n")
output_file.write(f"{arr_to_bin_str(ntt(rand_arr, Q))}\n")
output_file.write(f"{arr_to_bin_str(ntt([i+1 for i in range(D)], Q))}\n")
output_file.write(f"{arr_to_bin_str(ntt([D-i for i in range(D)], Q))}\n")
output_file.close()

print(ntt([1 for i in range(D)], Q))