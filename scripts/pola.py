from math import log2, ceil

N = 32

for j in range(N):
    for i in range(ceil(log2(N))):
        if j//(2**(i)) % 2 == 0:
            print(0, end=" ")
        else:
            k = (N*int(int(j//(2**i)-1))//4+(2**(i))) % (N - 2*(i+1))
            print((k + (N - 2*(i+1)) if k + (N - 2*(i+1))
                  == (N - 2**i) and int(j//(2**i)-1) != 0 else k), end=" ")

    print("")
