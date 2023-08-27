from math import ceil, log2, log
from staged_ntt import bit_reverse_int, index_generator, ntt_with_tf, get_element_by_indexes, set_element_by_indexes, find_2nth_rou
from mtt import ntt, intt
from negacyclic_conv import negacyclic_conv
from helper import FindPrimitiveRoot, ParamGen


def clog2(a):
    return ceil(log2(a))

def clog(a, base):
    return ceil(log(a, base))

D = 64
K = 2
N = 17

q, psi, psiv, w, wv = ParamGen(D, N)
# Q = q
Q = q
PSI = psi

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

def get_tf(w_table, stages, indexes):
    temp = []
    for idx in indexes:
        for s in stages:
            if w_table[idx][s] not in temp:
                temp.append(w_table[idx][s])
    temp.sort()
    psi = PSI
    return [pow(psi, bit_reverse_int(v, length=clog2(D)), Q) for v in temp]

tr = generate_full_w_table(D)

# print(get_tf(tr, [2, 3], [0, 1, 2, 3]))
indexes = index_generator(D, K)
inp = [1 for i in range(D)]
tmp = [1 for i in range(D)]
print(len(tr), len(tr[0]))

# for t in tr:
#     print(t)

for (i, index) in enumerate(indexes):
    stages = [clog2(K)*(K*i//D)+j for j in range(clog2(K))]
    # print(stages)
    tf = get_tf(tr, stages, index)
    ntt_inp = get_element_by_indexes(tmp, index)
    ntt_out = ntt_with_tf(ntt_inp, Q, tf)
    tmp = set_element_by_indexes(tmp, index, ntt_out)
    # print(indexes[i], [2*(i//4), 2*(i//4)+1])
    # tf = get_tf(tr, [clog(D, K)*(i//K)+j for j in range(clog(D, K))], indexes[i])
    # ntt_with_tf()
    
tmp = [pow(t, 2)%Q for t in tmp]
# print(ntt(inp, Q))
# print(tmp == ntt(inp, Q))
tmp2 = ntt(inp, Q, psi=PSI)
tmp2 = [pow(t, 2)%Q for t in tmp2]
print(intt(tmp, Q, psi=PSI))
print(intt(tmp2, Q, psi=PSI))
print(negacyclic_conv(inp, inp, Q))

# for i in range(0, K, clog2(K)):
#     length = D // pow(2, i+1)
#     reps = pow(2, i)
#     for j in range(reps):
#         base = ret[i][2*j*length:(2*j+1)*length]
#         print(base, j*length*2)
#         for k in range(clog(D, K)):
#             print(ret[i+1][k*length:k*length+length], k*length)
#         base = ret[i][j*n_splits:j*n_splits+D//n_splits]
#         print(base)
#         for k in range(clog(D, K)):
#             print(ret[i+1][(j+k)*n_splits:(j+k)*n_splits+D//n_splits])
    # for j in range(D//2):
    #     print([tr[j][i] for k in range(K-1)])
    #     print(tr[j][i], tr[j][i+1], i, j)

# for i in range(clog(D, K)):
#     for j in range(D):
#         b = j // pow(2, clog(D, K)-i-1)
#         p = (b + 1) // 2
#         print("{:2d} {:2d}".format(j, pow(K, i)+p-1 if b % 2 != 0 else 0))
#     print("")