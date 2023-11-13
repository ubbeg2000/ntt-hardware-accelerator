from my_ntt import ntt, intt

N = 1024
Q = 65537
PSI = 33

def r2ntt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        # for i in range(N//2):
        #     tf = pow(PSI, (2*k+1)*i, Q)
        #     if k % 2 == 0:
        #         accum = accum + tf * (a[i] + pow(PSI, N//2, Q) * a[i + N//2])
        #     else:
        #         accum = accum + tf * (a[i] - pow(PSI, N//2, Q) * a[i + N//2])

        for i in range(N):
            tf = pow(PSI, (2*k+1)*i, Q)
            # print(f"k={k}, i={i}, tf={tf}, pow={(2*k+1)*i}, a[i]={a[i]}")
            accum = (accum + tf * a[i]) % Q
        
        an[k] = accum % Q

    return an

def r2intt(a):
    an = [0 for i in range(N)]
    for k in range(N):
        accum = 0

        for i in range(N//2):
            tf = pow(PSI, -(2*i+1)*k, Q)
            if k % 2 == 0:
                accum = accum + tf * (a[i] +  a[i + N//2])
            else:
                accum = accum + tf * (a[i] + pow(PSI, N, Q) * a[i + N//2])

        # for i in range(N):
        #     tf = pow(PSI, -(2*i+1)*k, Q)
        #     # print(f"k={k}, i={i}, tf={tf}, pow={(2*k+1)*i}, a[i]={a[i]}")
        #     accum = accum + tf * a[i]
        
        an[k] = (accum * pow(N, -1, Q)) % Q

    return an

# print([1 for i in range(N)])
print(ntt([i for i in range(N)], Q, psi=PSI))
# print(intt(ntt([i for i in range(N)], Q, psi=PSI), Q, psi=PSI))
print(r2ntt([i for i in range(N)]))
print(r2intt(r2ntt([i for i in range(N)])))
# print(intt(ntt([1 for i in range(N)])))