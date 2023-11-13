from my_ntt import ntt, intt

N = 1024
Q = 65537
PSI = 925

def r8ntt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//8):
            tf = pow(PSI, (2*k+1)*i, Q)
            if k % 8 == 0:
                accum = accum + tf * (
                    (a[i + 0*N//8] + a[i + 4*N//8] * pow(PSI, N//2, Q)) 
                    + (a[i + 2*N//8] + a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    + (
                        (a[i + 1*N//8] + a[i + 5*N//8] * pow(PSI, N//2, Q)) + 
                        (a[i + 3*N//8] + a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    )  * pow(PSI, 1*N//8, Q)
                )
            elif k % 8 == 1:
                accum = accum + tf * (
                    (a[i + 0*N//8] - a[i + 4*N//8] * pow(PSI, N//2, Q))
                    + (a[i + 2*N//8] - a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    + (
                        (a[i + 1*N//8] - a[i + 5*N//8] * pow(PSI, N//2, Q)) + 
                        (a[i + 3*N//8] - a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    ) * pow(PSI, 1*3*N//8, Q)
                )
            elif k % 8 == 2:
                accum = accum + tf * (
                    (a[i + 0*N//8] + a[i + 4*N//8] * pow(PSI, N//2, Q))
                    - (a[i + 2*N//8] + a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    + (
                        (a[i + 1*N//8] + a[i + 5*N//8] * pow(PSI, N//2, Q)) - 
                        (a[i + 3*N//8] + a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    ) * pow(PSI, 1*5*N//8, Q)
                )
            elif k % 8 == 3:
                accum = accum + tf * (
                    (a[i + 0*N//8] - a[i + 4*N//8] * pow(PSI, N//2, Q))
                    - (a[i + 2*N//8] - a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    + (
                        (a[i + 1*N//8] - a[i + 5*N//8] * pow(PSI, N//2, Q)) -
                        (a[i + 3*N//8] - a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    ) * pow(PSI, 1*7*N//8, Q)
                )
            elif k % 8 == 4:
                accum = accum + tf * (
                    (a[i + 0*N//8] + a[i + 4*N//8] * pow(PSI, N//2, Q))
                    + (a[i + 2*N//8] + a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    - (
                        (a[i + 1*N//8] + a[i + 5*N//8] * pow(PSI, N//2, Q)) + 
                        (a[i + 3*N//8] + a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    ) * pow(PSI, N//8, Q)
                )
            elif k % 8 == 5:
                accum = accum + tf * (
                    (a[i + 0*N//8] - a[i + 4*N//8] * pow(PSI, N//2, Q))
                    + (a[i + 2*N//8] - a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    - (
                        (a[i + 1*N//8] - a[i + 5*N//8] * pow(PSI, N//2, Q)) + 
                        (a[i + 3*N//8] - a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    ) * pow(PSI, 3*N//8, Q)
                )
            elif k % 8 == 6:
                accum = accum + tf * (
                    (a[i + 0*N//8] + a[i + 4*N//8] * pow(PSI, N//2, Q))
                    - (a[i + 2*N//8] + a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    - (
                        (a[i + 1*N//8] + a[i + 5*N//8] * pow(PSI, N//2, Q)) -
                        (a[i + 3*N//8] + a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, N//4, Q)
                    ) * pow(PSI, 5*N//8, Q)
                )
            elif k % 8 == 7:
                accum = accum + tf * (
                    (a[i + 0*N//8] - a[i + 4*N//8] * pow(PSI, N//2, Q))
                    - (a[i + 2*N//8] - a[i + 6*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    - (
                        (a[i + 1*N//8] - a[i + 5*N//8] * pow(PSI, N//2, Q)) - 
                        (a[i + 3*N//8] - a[i + 7*N//8] * pow(PSI, N//2, Q)) * pow(PSI, 3*N//4, Q)
                    ) * pow(PSI, 7*N//8, Q)
                )
        
        an[k] = accum % Q

    return an

def r8intt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//8):
            tf = pow(PSI, -(2*i+1)*k, Q)
            if k % 8 == 0:
                accum = accum + tf * (
                    (a[i] + a[i + N//2]) + 
                    (a[i + N//4] + a[i + 3*N//4]) +
                    (a[i + N//8] + a[i + 5*N//8]) + 
                    (a[i + 3*N//8] + a[i + 7*N//8])
                )
            elif k % 8 == 1:
                accum = accum + tf * (
                    a[i] - a[i + 4*N//8] 
                    - pow(PSI, N//2, Q) * (
                        a[i + 2*N//8] - a[i + 6*N//8]
                    )
                    - pow(PSI, N//4, Q) * (
                        (
                        a[i + N//8] - a[i + 5*N//8]
                        ) * pow(PSI, N//2, Q) + 
                        (
                            a[i + 3*N//8] - a[i + 7*N//8]
                        )
                    )
                )
            elif k % 8 == 2:
                accum = accum + tf * (
                    a[i] + a[i + N//2] 
                    - (a[i + N//4] + a[i + 3*N//4])
                    - pow(PSI, N//2, Q) * (
                        (a[i + N//8] + a[i + 5*N//8]) -
                        (a[i + 3*N//8] + a[i + 7*N//8])
                    )
                )
            elif k % 8 == 3:
                accum = accum + tf * (
                    a[i] - a[i + N//2] 
                    + pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                    - pow(PSI, N//4, Q) * (
                        (a[i + N//8] - a[i + 5*N//8]) + 
                        (a[i + 3*N//8] - a[i + 7*N//8]) * pow(PSI, N//2, Q)
                    )
                )
            elif k % 8 == 4:
                accum = accum + tf * (
                    a[i] + a[i + N//2] + (a[i + N//4] + a[i + 3*N//4])
                    - ((a[i + N//8] + a[i + 5*N//8]) + (a[i + 3*N//8] + a[i + 7*N//8]))
                )
            elif k % 8 == 5:
                accum = accum + tf * (
                    a[i] - a[i + N//2] 
                    - pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                    + pow(PSI, N//4, Q) * (
                        (a[i + N//8] - a[i + 5*N//8]) * pow(PSI, N//2, Q) +
                        (a[i + 3*N//8] - a[i + 7*N//8])
                    )
                )
            elif k % 8 == 6:
                accum = accum + tf * (
                    a[i] + a[i + N//2] 
                    - (a[i + N//4] + a[i + 3*N//4])
                    + pow(PSI, N//2, Q) * (
                        (a[i + N//8] + a[i + 5*N//8]) -
                        (a[i + 3*N//8] + a[i + 7*N//8])
                    )
                )
            elif k % 8 == 7:
                accum = accum + tf * (
                    a[i] - a[i + N//2] 
                    + pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                    + pow(PSI, N//4, Q) * (
                        (a[i + N//8] - a[i + 5*N//8]) + 
                        (a[i + 3*N//8] - a[i + 7*N//8]) * pow(PSI, N//2, Q)
                    )
                )
        
        an[k] = (accum * pow(N, -1, Q)) % Q

    return an

# print([1 for i in range(N)])
# print(r4nttopt([1 for i in range(N)]))
# print(intt(ntt([1 for i in range(N)], Q, psi=PSI), Q, psi=PSI))
print(r8ntt([i for i in range(N)]))
print(r8intt(r8ntt([i for i in range(N)])))
# print(intt(ntt([1 for i in range(N)])))