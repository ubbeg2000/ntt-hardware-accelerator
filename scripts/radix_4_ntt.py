from ntt_utils import gen_w_table, gen_w_inv_table, clog2
from staged_ntt import index_generator, get_tf

def radix_4_ntt_pe_cell(a, tf, q):
    [a0, a1, a2, a3] = a
    [tf0, tf1, tf2] = tf
    
    b0 = ((a0 + a2 * tf0) + (a1 + a3 * tf0) * tf1)%q
    b1 = ((a0 + a2 * tf0) - (a1 + a3 * tf0) * tf1)%q
    b2 = ((a0 - a2 * tf0) + (a1 - a3 * tf0) * tf2)%q
    b3 = ((a0 - a2 * tf0) - (a1 - a3 * tf0) * tf2)%q

    return [b0, b1, b2, b3]

def radix_4_intt_pe_cell(a, tf, q):
    [a0, a1, a2, a3] = a
    [tf0, tf1, tf2] = tf
    
    b0 = ((a0 + a1)       + (a2 + a3))%q
    b1 = ((a0 - a1) * tf0 + (a2 - a3) * tf1) % q
    b2 = ((a0 + a1)       - (a2 + a3)) * tf2 % q
    b3 = ((a0 - a1) * tf0 - (a2 - a3) * tf1) * tf2 % q

    b = [b0, b1, b2, b3]
    return [(r * pow(4, -1, q)) % q for r in b]

def intt(a, q, psi=0, print_step=False):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_inv_table = gen_w_inv_table(q, n, psi)
    # print(res)
    for i in range(clog2(n) - 1, -1, -1):
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
        if print_step:
            print(res)

    # res = [(r * pow(n, -1, q)) % q for r in res]

    return res


def ntt(a, q, print_step=False, psi=0):
    n = len(a)
    res = [a[i] for i in range(n)]
    w_table = gen_w_table(q, n, psi)
    # print(res)
    for i in range(clog2(n)):
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

def radix_4_ntt():
    pass

def radix_4_intt():
    pass


if __name__ == "__main__":
    inp = [1, 1, 1, 1]
    inpt = ntt(inp, 65537, psi=2)
    print(ntt(inp, 65537, psi=2))
    print(gen_w_table(65537, 4, 2))
    print(gen_w_inv_table(65537, 4, 2))
    print([pow(2, -1, 65537),
        pow(2, -3, 65537),
        pow(2, -2, 65537)])
    print(radix_4_ntt_pe_cell(inp, [4, 2, 8], 65537))
    print(intt(inpt, 65537, psi=2))
    print(radix_4_intt_pe_cell(radix_4_ntt_pe_cell(inp, [4, 2, 8], 65537), [
        pow(2, -1, 65537),
        pow(2, -3, 65537),
        pow(2, -2, 65537)
        ], 65537))