from math import ceil, log, log2

def clog2(a):
    return ceil(log2(a))

def clog(a, base):
    return ceil(log(a, base))
def bit_reverse_int(a, length=8):
    return int("{:b}".format(a).rjust(length, "0")[::-1], 2)

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


def int_to_bin(number, length):
    binary_string = bin(number)[2:].zfill(length)
    return binary_string


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

def get_element_by_indexes(arr, indexes):
    retval = []
    for index in indexes:
        retval.append(arr[index])
    return retval

def set_element_by_indexes(arr, indexes, values):
    for (i, index) in enumerate(indexes):
        arr[index] = values[i]
    return arr

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
            f"        {ceil(log2(n))}'B{int_to_bin(i, clog2(n))}: value = {psi[i]};\n")
    f.write("    endcase\n")
    f.write("    end\n")
    f.write("endmodule\n")
