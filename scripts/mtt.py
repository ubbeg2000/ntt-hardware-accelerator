from math import log2, ceil


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


def gen_w_table(q, n, psi=0):
    w_table = [[] for i in range(int(log2(n)))]
    if psi == 0:
        psi = find_2nth_rou(q, n)
    for i in range(int(log2(n))):
        for j in range(2 ** i):
            p = int("{:b}".format((2**i)+j).rjust(int(log2(n)), "0")[::-1], 2)
            w_table[i] = w_table[i] + [pow(psi, p, q)]

    # print("w_table")
    # for i in range(len(w_table)):
    #     for j in range(len(w_table[i])):
    #         print(f"psi_table[{i}][{j}] = {w_table[i][j]};")
    # print("")
    generate_psi_table(n, q, w_table)

    return w_table


def gen_w_inv_table(q, n, psi=0):
    w_inv_table = [[] for i in range(int(log2(n)))]

    if psi == 0:
        psi = find_2nth_rou(q, n)
    
    for i in range(int(log2(n))):
        for j in range(2 ** i):
            p = int("{:b}".format((2**i)+j).rjust(int(log2(n)), "0")[::-1], 2)
            w_inv_table[i] = w_inv_table[i] + [pow(psi, -p, q)]

    # print("w_inv_table")
    # for i in range(len(w_inv_table)):
    #     for j in range(len(w_inv_table[i])):
    #         print(f"psi_table[{i}][{j}] = {w_inv_table[i][j]};")

    generate_psi_table(n, q, w_inv_table, "psi_inv_table")

    return w_inv_table


def ntt(a, q, print_step=False, psi=0):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n, psi)
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


def ntt_radix_4(a, q):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n)
    # print(res)
    for i in range(int(log2(n)/2)):
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
        # print(res)

    return res


def intt(a, q, psi=0):
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

                b0 = (res[a_idx] + res[a_idx + jump])
                b1 = (res[a_idx] - res[a_idx + jump]) * W

                res[a_idx] = b0 % q
                res[a_idx + jump] = b1 % q

                # print(i, j, k, a_idx, a_idx + jump, W)
        # print(res)

    res = [(r * pow(n, -1, q)) % q for r in res]

    return res


def int_to_bin(number, length):
    binary_string = bin(number)[2:].zfill(length)
    return binary_string


def generate_psi_table(n, q, table, name="psi_table"):
    psi = [t for sub in table for t in sub]
    psi = [1] + psi
    f = open(f"{name}.v", "w")
    f.write("`timescale 1ps/1ns\n\n")

    f.write(f"module {name} (\n")
    f.write(f"    input [{ceil(log2(n))-1}:0] addr,\n")
    f.write(f"    output reg [{ceil(log2(q))-1}:0] value\n")
    f.write("    );\n\n")

    f.write("    always @ (addr) begin\n")
    f.write("    case (addr)\n")
    for i in range(0, n):
        f.write(
            f"        {ceil(log2(n))}'B{int_to_bin(i, ceil(log2(n)))}: value = {psi[i]};\n")
    f.write("    endcase\n")
    f.write("    end\n")
    f.write("endmodule\n")

if __name__ == "__main__":
    # print(gen_w_table(257, 8))
    # print(gen_w_inv_table(257, 8))
    print(gen_w_table(65537, 32))
    print(gen_w_inv_table(65537, 32))
    # print(ntt([1  for i in range(32)]))
    # a = ntt([1 for i in range(16)], 65537)
    # b = ntt([1 for i in range(16)], 65537)
    # c = [((a[i] * b[i]) % 65537) for i in range(16)]
    # print(a)
    # print(b)
    # print(intt(c, 65537))
    # print("ASDF")
    # print(intt(a, 257))
    # print(intt(a, 65537))
