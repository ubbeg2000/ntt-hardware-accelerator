from mtt import ntt, intt
from math import ceil, log2, log

D = 16
K = 4

# fungsi untuk generate index input dan output
# perhitungan ntt/intt di satu stage
def index_generator(n, k, stage):
    if stage == 1:
        return [
            [i for i in range(4)],
            [i+4 for i in range(4)],
            [i+8 for i in range(4)],
            [i+12 for i in range(4)],
        ]
    retval = []
    for i in range(n//k):
        retval.append([i + j*k for j in range(k)])

    return retval

def get_element_by_indexes(arr, indexes):
    retval = []
    for index in indexes:
        retval.append(arr[index])
    return retval

def set_element_by_indexes(arr, indexes, values):
    for (i, index) in enumerate(indexes):
        arr[index] = values[i]
    return arr

if __name__ == "__main__":
    inp = [1 for i in range(D)]
    tmp = [inp[i] for i in range(D)]


    print("NORMAL NTT")
    print(ntt(inp, 65537))

    print("STAGED NTT")
    for i in range(ceil(log(D, K))):
        print(i)
        indexes = index_generator(D, K, i)
        for j in range(D//K):
            ntt_inp = get_element_by_indexes(tmp, indexes[j])
            ntt_out = ntt(ntt_inp, 65537)
            tmp = set_element_by_indexes(tmp, indexes[j], ntt_out)

            print("TMP", tmp, indexes[j])
    
