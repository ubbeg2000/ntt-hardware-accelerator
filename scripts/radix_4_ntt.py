from my_ntt import ntt, intt

N = 1024
Q = 65537
PSI = 649

def r4ntt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//4):
            tf = pow(PSI, (2*k+1)*i, Q)
            if k % 4 == 0:
                accum = accum + tf * (
                    a[i] + pow(PSI, N//2, Q) * a[i + N//2] + 
                    pow(PSI, N//4, Q) * (a[i + N//4] + pow(PSI, N//2, Q) * a[i + 3*N//4])
                )
            elif k % 4 == 1:
                accum = accum + tf * (
                    a[i] - pow(PSI, N//2, Q) * a[i + N//2] + 
                    pow(PSI, 3*N//4, Q) * (a[i + N//4] - pow(PSI, N//2, Q) * a[i + 3*N//4])
                )
            elif k % 4 == 2:
                accum = accum + tf * (
                    a[i] + pow(PSI, N//2, Q) * a[i + N//2] - 
                    pow(PSI, N//4, Q) * (a[i + N//4] + pow(PSI, N//2, Q) * a[i + 3*N//4])
                )
            else:
                accum = accum + tf * (
                    a[i] - pow(PSI, N//2, Q) * a[i + N//2] - 
                    pow(PSI, 3*N//4, Q) * (a[i + N//4] - pow(PSI, N//2, Q) * a[i + 3*N//4])
                )

        # for i in range(N):
        #     tf = pow(PSI, (2*k+1)*i, Q)
        #     # print(f"k={k}, i={i}, tf={tf}, pow={(2*k+1)*i}, a[i]={a[i]}")
        #     accum = (accum + tf * a[i]) % Q
        
        an[k] = accum % Q

    return an

def r4nttopt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//4):
            tf = pow(PSI, (2*k+1)*i, Q)
            if k % 4 == 0:
                accum = accum + tf * (
                    a[i] + (a[i + N//2] << 8) + 
                    (a[i + N//4] + (a[i + 3*N//4] << 8) << 4)
                )
            elif k % 4 == 1:
                accum = accum + tf * (
                    a[i] - (a[i + N//2] << 8) + 
                    (a[i + N//4] - (a[i + 3*N//4] << 8) << 12)
                )
            elif k % 4 == 2:
                accum = accum + tf * (
                    a[i] + (a[i + N//2] << 8) - 
                    (a[i + N//4] + (a[i + 3*N//4] << 8) << 4)
                )
            else:
                accum = accum + tf * (
                    a[i] - (a[i + N//2] << 8) - 
                    (a[i + N//4] - (a[i + 3*N//4] << 8) << 12)
                )

        # for i in range(N):
        #     tf = pow(PSI, (2*k+1)*i, Q)
        #     # print(f"k={k}, i={i}, tf={tf}, pow={(2*k+1)*i}, a[i]={a[i]}")
        #     accum = (accum + tf * a[i]) % Q
        
        an[k] = accum % Q

    return an

def r4intt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//4):
            tf = pow(PSI, -(2*i+1)*k, Q)
            if k % 4 == 0:
                accum = accum + tf * (
                    (a[i] + a[i + N//2]) + 
                    (a[i + N//4] + a[i + 3*N//4])
                )
            elif k % 4 == 1:
                accum = accum + tf * (
                    (a[i] - a[i + N//2]) + 
                    (-((a[i + N//4] - a[i + 3*N//4]) << 8))
                )
            elif k % 4 == 2:
                accum = accum + tf * (
                    (a[i] + a[i + N//2]) - 
                    (a[i + N//4] + a[i + 3*N//4])
                )
            elif k % 4 == 3:
                accum = accum + tf * (
                    (a[i] - a[i + N//2]) - 
                    (-((a[i + N//4] - a[i + 3*N//4]) << 8))
                )

        # for i in range(N):
        #     tf = pow(PSI, -(2*i+1)*k, Q)
        #     # print(f"k={k}, i={i}, tf={tf}, pow={(2*k+1)*i}, a[i]={a[i]}")
        #     accum = accum + tf * a[i]
        
        an[k] = (accum * pow(N, -1, Q)) % Q

    return an

# print([1 for i in range(N)])
print(ntt([1 for i in range(N)], Q, psi=PSI))
# print(intt(ntt([1 for i in range(N)], Q, psi=PSI), Q, psi=PSI))
print(r4ntt([1 for i in range(N)]))
print(r4intt(r4nttopt([i for i in range(N)])))
# print(intt(ntt([1 for i in range(N)])))