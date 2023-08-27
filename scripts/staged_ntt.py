from mtt import ntt, intt
from math import ceil, log2, log

from math import log2, ceil

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


def gen_w_inv_table(q, n):
    w_inv_table = [[] for i in range(int(log2(n)))]
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


def ntt_with_tf(a, q, tf):
    n = len(a)
    res = [a[i] for i in range(n)]

    w_table = [[tf[pow(2, i)-1+j] for j in range(pow(2, i))] for i in range(ceil(log2(n)))]
    
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

                # print(i, j, k, a_idx, W)
        # print(res)

    return res

def intt(a, q):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_inv_table = gen_w_inv_table(q, n)
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

# if __name__ == "__main__":
    # print(gen_w_table(257, 8))
    # print(gen_w_inv_table(257, 8))
    # print(gen_w_table(65537, 32))
    # print(gen_w_inv_table(65537, 32))
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


def get_element_by_indexes(arr, indexes):
    retval = []
    for index in indexes:
        retval.append(arr[index])
    return retval

def set_element_by_indexes(arr, indexes, values):
    for (i, index) in enumerate(indexes):
        arr[index] = values[i]
    return arr

def gen_w_table(q, n):
    w_table = []
    psi = find_2nth_rou(q, n)
    for i in range(n):
        p = bit_reverse_int(i, length=ceil(log2(n)))
        w_table = w_table + [pow(psi, p, q)]

    # print("w_table")
    # for i in range(len(w_table)):
    #     for j in range(len(w_table[i])):
    #         print(f"psi_table[{i}][{j}] = {w_table[i][j]};")
    # print("")
    # generate_psi_table(n, q, w_table)

    return w_table

def split_twiddle_factor(w_table, n, k):
    ret = []
    logkn = ceil(log(n, k))
    print(w_table)
    for i in range(logkn):
        increment = pow(k, logkn-i-1)
        rep = pow(k, i)
        # offset = pow(k, i)
        # print("REP", rep)
        # print("INC", increment)
        for r in range(rep):
            # q = [bit_reverse_int((r * k + l) * increment, length=ceil(log2(n))) for l in range(1, k)]
            # q.sort()
            # print("XIXIX", q)
            for j in range(increment):
                base = r+pow(k, i)
                indexes = [pow(k, i)+j*i+r, 2*(pow(k, i)+j*i+r), 2*(pow(k, i)+j*i+r)+1]
                ret = ret + [[w_table[p] for p in indexes]]#  for l in range(k-1)]]

        # for j in range(n//pow(k, i+1)):
        #     indexes = [pow(k, i)+j*i - 1] #, 2*(pow(k, i)+j*i)+1]
        #     # print(indexes)
        #     # print("STAGE {:2d} : ".format(i+1), end="")
        #     # print(w_table[(k-1)*i*(j+1)+1:(k-1)*i*(j+1)+k])
        #     print(indexes)
        #     ret = ret + [[w_table[p] for p in indexes]] #[w_table[(k-1)*i*(j+1)+1:(k-1)*i*(j+1)+k]]
    
    return ret


# fungsi untuk generate index input dan output
# perhitungan ntt/intt di satu stage
def index_generator(n, k):
    ret = []
    logkn = ceil(log(n, k))
    for i in range(logkn):
        increment = pow(k, logkn-i-1)
        rep = pow(k, i)
        # offset = pow(k, i)
        # print("REP", rep)
        # print("INC", increment)
        for r in range(rep):
            for j in range(increment):
                ret = ret + [[r * k * increment + j + l*increment for l in range(k)]]

            # if i == logkn - 1:
            #     ret = ret + [[j*k+l*increment for l in range(k)]]
            # else:
            #     ret = ret + [[j+l*increment for l in range(k)]]
            # if i != 1:
            #     ret = ret + [[bit_reverse_int(j*k+r, length=ceil(log2(n))) for r in range(k)]]
            # else:
            #     ret = ret + [[j*k+r for r in range(k)]]

        # for j in range(n//k):
    return ret
    # if stage == 1:
    #     return [
    #         [i for i in range(4)],
    #         [i+4 for i in range(4)],
    #         [i+8 for i in range(4)],
    #         [i+12 for i in range(4)],
    #     ]
    # retval = []
    # for i in range(n//k):
    #     retval.append([i + j*k for j in range(k)])

    # return retval

if __name__ == "__main__":
    N = 16
    K = 4
    Q = 65537

    twiddle_fator = gen_w_table(Q, N)
    tf_table = split_twiddle_factor(twiddle_fator, N, K)
    idx_table = index_generator(N, K)

    # for i in idx_table:
    #     print(i)

    # print("STAGED NTT")
    # for i in range(ceil(log(N, K))):
    #     # print(i)
    #     indexes = index_generator(N, K, i)
    #     for j in range(D//K):
    for i in range(N//K * ceil(log(N, K))):
        print(tf_table[i], idx_table[i])

    tmp = [1 for i in range(N)]
    for i in range(N//K * ceil(log(N, K))):
        ntt_inp = get_element_by_indexes(tmp, idx_table[i])
        ntt_out = ntt_with_tf(ntt_inp, 65537, tf_table[i])
        tmp = set_element_by_indexes(tmp, idx_table[i], ntt_out)
    print(tmp)

    print(ntt([1 for i in range(N)], 65537))
    print(tmp == ntt([1 for i in range(N)], 65537))

    # for i in range(N):
    #     print(bit_reverse_int(i, length=ceil(log2(N))))
    # inp = [1 for i in range(D)]
    # tmp = [inp[i] for i in range(D)]


    # print("NORMAL NTT")
    # print(ntt(inp, 65537))

    # print("STAGED NTT")
    # for i in range(ceil(log(D, K))):
    #     print(i)
    #     indexes = index_generator(D, K, i)
    #     for j in range(D//K):
    #         ntt_inp = get_element_by_indexes(tmp, indexes[j])
    #         ntt_out = ntt(ntt_inp, 65537)
    #         tmp = set_element_by_indexes(tmp, indexes[j], ntt_out)

    #         print("TMP", tmp, indexes[j])
    
