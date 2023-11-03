from my_ntt import ntt, intt
from negacyclic_conv import negacyclic_conv
from helper import ParamGen
from ntt_utils import clog2, clog, get_element_by_indexes, set_element_by_indexes, bit_reverse_int


D = 1024
K = 2
N = 17

def ntt_with_tf(a, q, tf):
    n = len(a)
    res = [a[i] for i in range(n)]

    w_table = [[tf[pow(2, i)-1+j] for j in range(pow(2, i))] for i in range(clog2(n))]
    
    for i in range(clog2(n)):
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


def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])

    ret = [[0 for i in range(m)] for j in range(n)]

    for i in range(m):
        for j in range(n):
            ret[j][i] = matrix[i][j]

    return ret

def generate_full_w_table(D):
    ret = []
    for i in range(clog2(D)):
        temp = []
        for j in range(D):
            b = j // pow(2, clog(D, 2)-i) + 1
            v = pow(2, i)+b-1
            temp.append(v)

        ret.append(temp)

    tr = transpose(ret)

    return tr

def get_tf(w_table, stages, indexes, psi, q):
    temp = []
    for idx in indexes:
        for s in stages:
            if w_table[idx][s] not in temp:
                temp.append(w_table[idx][s])
    temp.sort()
    return [pow(psi, bit_reverse_int(v, length=clog2(D)), Q) for v in temp]


def index_generator(n, k):
    ret = []
    logkn = clog(n, k)
    for i in range(logkn):
        increment = pow(k, logkn-i-1)
        rep = pow(k, i)
        for r in range(rep):
            for j in range(increment):
                ret = ret + [[r * k * increment + j + l*increment for l in range(k)]]

    return ret

def staged_ntt(a, D, K, Q, PSI):
    tr = generate_full_w_table(D)

    indexes = index_generator(D, K)
    tmp = [a[i] for i in range(D)]
    print(len(tr), len(tr[0]))

    for (i, index) in enumerate(indexes):
        stages = [clog2(K)*(K*i//D)+j for j in range(clog2(K))]
        tf = get_tf(tr, stages, index, PSI, Q)
        ntt_inp = get_element_by_indexes(tmp, index)
        ntt_out = ntt_with_tf(ntt_inp, Q, tf)
        tmp = set_element_by_indexes(tmp, index, ntt_out)

    return tmp
        
if __name__ == "__main__":
    Q, PSI, psiv, w, wv = ParamGen(D, N)
    print(Q, PSI)
    Q = 65537
    PSI = 33

    inp = [1 for i in range(D)]
    ntt1 = ntt(inp, Q, psi=PSI)
    ntt2 = staged_ntt(inp, D, K, Q, PSI)

    ntt1 = [pow(n, 2, Q) for n in ntt1]
    ntt2 = [pow(n, 2, Q) for n in ntt2]

    print(f"INDEX GEN: {len(index_generator(64, 4))}", index_generator(64, 4))

    print(intt(ntt1, Q, psi=PSI))
    print(intt(ntt2, Q, psi=PSI))
    print(intt(ntt1, Q, psi=PSI) == intt(ntt2, Q, psi=PSI))
    print(intt(ntt1, Q, psi=PSI) == negacyclic_conv(inp, inp, Q))
    # print(negacyclic_conv(inp, inp, Q))
