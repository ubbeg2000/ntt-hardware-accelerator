from my_ntt import ntt, intt

N = 16
Q = 65537
PSI = 33

def r2ntt(a):
    an = [0 for i in range(N)]
    for p in range(N//2):
        accum_2p = 0
        accum_2p_1 = 0

        for i in range(N//2):
            tf_2p = pow(PSI, (4*p+1)*i, Q)
            tf_2p_1 = pow(PSI, (4*p+3)*i, Q)
            
            accum_2p = accum_2p + tf_2p * (a[i] + pow(PSI, N//2, Q) * a[i + N//2])
            accum_2p_1 = accum_2p_1 + tf_2p_1 * (a[i] - pow(PSI, N//2, Q) * a[i + N//2])
        
        an[2*p] = accum_2p % Q
        an[2*p+1] = accum_2p_1 % Q

    return an

def r2ntt_v2(a):
    an = [0 for i in range(N)]
    for i in range(N//2):
        accum_2p = 0
        accum_2p_1 = 0

        for p in range(N//2):
            tf_2p = pow(PSI, (4*p+1)*i, Q)
            tf_2p_1 = pow(PSI, (4*p+3)*i, Q)
            
            accum_2p = accum_2p + tf_2p * (a[i] + pow(PSI, N//2, Q) * a[i + N//2])
            accum_2p_1 = accum_2p_1 + tf_2p_1 * (a[i] - pow(PSI, N//2, Q) * a[i + N//2])
        
        an[2*p] = accum_2p % Q
        an[2*p+1] = accum_2p_1 % Q

    return an

def r2intt(a):
    an = [0 for i in range(N)]
    for p in range(N//2):
        accum_2p = 0
        accum_2p_1 = 0

        for i in range(N//2):
            tf_2p = pow(PSI, -(2*i+1)*(2*p), Q)
            tf_2p_1 = pow(PSI, -(2*i+1)*(2*p+1), Q)
            
            accum_2p = accum_2p + tf_2p * (a[i] +  a[i + N//2])
            accum_2p_1 = accum_2p_1 + tf_2p_1 * (a[i] + pow(PSI, N, Q) * a[i + N//2])
        
        an[2*p] = (accum_2p * pow(N, -1, Q)) % Q
        an[2*p+1] = (accum_2p_1 * pow(N, -1, Q)) % Q

    return an

# print([1 for i in range(N)])
print(ntt([i for i in range(N)], Q, psi=PSI))
# print(intt(ntt([i for i in range(N)], Q, psi=PSI), Q, psi=PSI))
print(r2ntt_v2([i for i in range(N)]))
print(r2ntt([i for i in range(N)]))
print(r2intt(r2ntt([i for i in range(N)])))
# print(intt(ntt([1 for i in range(N)])))