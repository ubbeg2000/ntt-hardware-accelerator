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

def r8nttopt(a):
    an = [0 for i in range(N)]
    for p in range(N//8):
        accum_8p = 0
        accum_8p_1 = 0
        accum_8p_2 = 0
        accum_8p_3 = 0
        accum_8p_4 = 0
        accum_8p_5 = 0
        accum_8p_6 = 0
        accum_8p_7 = 0

        for i in range(N//8):
            tf_8p = pow(PSI, (2*(8*p)+1)*i, Q)
            tf_8p_1 = pow(PSI, (2*(8*p+1)+1)*i, Q)
            tf_8p_2 = pow(PSI, (2*(8*p+2)+1)*i, Q)
            tf_8p_3 = pow(PSI, (2*(8*p+3)+1)*i, Q)
            tf_8p_4 = pow(PSI, (2*(8*p+4)+1)*i, Q)
            tf_8p_5 = pow(PSI, (2*(8*p+5)+1)*i, Q)
            tf_8p_6 = pow(PSI, (2*(8*p+6)+1)*i, Q)
            tf_8p_7 = pow(PSI, (2*(8*p+7)+1)*i, Q)

            a0 = a[i + 0*N//8]
            a1 = a[i + 1*N//8]
            a2 = a[i + 2*N//8]
            a3 = a[i + 3*N//8]
            a4 = (a[i + 4*N//8] << 8)
            a5 = (a[i + 5*N//8] << 8)
            a6 = (a[i + 6*N//8] << 8)
            a7 = (a[i + 7*N//8] << 8)

            a04p, a04n = a0 + a4, a0 - a4
            a15p, a15n = a1 + a5, a1 - a5
            a26p, a26n = a2 + a6, a2 - a6
            a37p, a37n = a3 + a7, a3 - a7

            accum_8p = accum_8p + tf_8p * (
                a04p + (a26p << 4)
                + ((a15p + (a37p << 4)) << 2)
            )
            
            accum_8p_1 = accum_8p_1 + tf_8p_1 * (
                a04n + (a26n << 12)
                + ((a15n + (a37n << 12)) << 6)
            )
            
            accum_8p_2 = accum_8p_2 + tf_8p_2 * (
                a04p - (a26p << 4)
                + ((a15p - (a37p << 4)) << 10)
            )

            accum_8p_3 = accum_8p_3 + tf_8p_3 * (
                a04n - (a26n << 12)
                + ((a15n - (a37n << 12)) << 14)
            )
            
            accum_8p_4 = accum_8p_4 + tf_8p_4 * (
                a04p + (a26p << 4)
                - ((a15p + (a37p << 4)) << 2)
            )
            
            accum_8p_5 = accum_8p_5 + tf_8p_5 * (
                a04n + (a26n << 12)
                - ((a15n + (a37n << 12)) << 6)
            )
            
            accum_8p_6 = accum_8p_6 + tf_8p_6 * (
                a04p - (a26p << 4)
                - ((a15p -(a37p << 4)) << 10)
            )
            
            accum_8p_7 = accum_8p_7 + tf_8p_7 * (
                a04n
                - (a26n << 12)
                - ((a15n - (a37n << 12)) << 14)
            )
        
        an[8*p] = accum_8p % Q
        an[8*p+1] = accum_8p_1 % Q
        an[8*p+2] = accum_8p_2 % Q
        an[8*p+3] = accum_8p_3 % Q
        an[8*p+4] = accum_8p_4 % Q
        an[8*p+5] = accum_8p_5 % Q
        an[8*p+6] = accum_8p_6 % Q
        an[8*p+7] = accum_8p_7 % Q

    return an

def r8intt(a):
    an = [0 for i in range(N)]
    for p in range(N//8):
        accum_8p = 0
        accum_8p_1 = 0
        accum_8p_2 = 0
        accum_8p_3 = 0
        accum_8p_4 = 0
        accum_8p_5 = 0
        accum_8p_6 = 0
        accum_8p_7 = 0

        for i in range(N//8):
            tf_8p = pow(PSI, -(2*i+1)*(8*p), Q)
            tf_8p_1 = pow(PSI, -(2*i+1)*(8*p+1), Q)
            tf_8p_2 = pow(PSI, -(2*i+1)*(8*p+2), Q)
            tf_8p_3 = pow(PSI, -(2*i+1)*(8*p+3), Q)
            tf_8p_4 = pow(PSI, -(2*i+1)*(8*p+4), Q)
            tf_8p_5 = pow(PSI, -(2*i+1)*(8*p+5), Q)
            tf_8p_6 = pow(PSI, -(2*i+1)*(8*p+6), Q)
            tf_8p_7 = pow(PSI, -(2*i+1)*(8*p+7), Q)

            accum_8p = accum_8p + tf_8p * (
                (a[i] + a[i + N//2]) + 
                (a[i + N//4] + a[i + 3*N//4]) +
                (a[i + N//8] + a[i + 5*N//8]) + 
                (a[i + 3*N//8] + a[i + 7*N//8])
            )

            accum_8p_1 = accum_8p_1 + tf_8p_1 * (
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

            accum_8p_2 = accum_8p_2 + tf_8p_2 * (
                a[i] + a[i + N//2] 
                - (a[i + N//4] + a[i + 3*N//4])
                - pow(PSI, N//2, Q) * (
                    (a[i + N//8] + a[i + 5*N//8]) -
                    (a[i + 3*N//8] + a[i + 7*N//8])
                )
            )

            accum_8p_3 = accum_8p_3 + tf_8p_3 * (
                a[i] - a[i + N//2] 
                + pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                - pow(PSI, N//4, Q) * (
                    (a[i + N//8] - a[i + 5*N//8]) + 
                    (a[i + 3*N//8] - a[i + 7*N//8]) * pow(PSI, N//2, Q)
                )
            )

            accum_8p_4 = accum_8p_4 + tf_8p_4 * (
                a[i] + a[i + N//2] + (a[i + N//4] + a[i + 3*N//4])
                - ((a[i + N//8] + a[i + 5*N//8]) + (a[i + 3*N//8] + a[i + 7*N//8]))
            )

            accum_8p_5 = accum_8p_5 + tf_8p_5 * (
                a[i] - a[i + N//2] 
                - pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                + pow(PSI, N//4, Q) * (
                    (a[i + N//8] - a[i + 5*N//8]) * pow(PSI, N//2, Q) +
                    (a[i + 3*N//8] - a[i + 7*N//8])
                )
            )

            accum_8p_6 = accum_8p_6 + tf_8p_6 * (
                a[i] + a[i + N//2] 
                - (a[i + N//4] + a[i + 3*N//4])
                + pow(PSI, N//2, Q) * (
                    (a[i + N//8] + a[i + 5*N//8]) -
                    (a[i + 3*N//8] + a[i + 7*N//8])
                )
            )

            accum_8p_7 = accum_8p_7 + tf_8p_7 * (
                a[i] - a[i + N//2] 
                + pow(PSI, N//2, Q) * (a[i + N//4] - a[i + 3*N//4])
                + pow(PSI, N//4, Q) * (
                    (a[i + N//8] - a[i + 5*N//8]) + 
                    (a[i + 3*N//8] - a[i + 7*N//8]) * pow(PSI, N//2, Q)
                )
            )
        
        an[8*p+0] = (accum_8p * pow(N, -1, Q)) % Q
        an[8*p+1] = (accum_8p_1 * pow(N, -1, Q)) % Q
        an[8*p+2] = (accum_8p_2 * pow(N, -1, Q)) % Q
        an[8*p+3] = (accum_8p_3 * pow(N, -1, Q)) % Q
        an[8*p+4] = (accum_8p_4 * pow(N, -1, Q)) % Q
        an[8*p+5] = (accum_8p_5 * pow(N, -1, Q)) % Q
        an[8*p+6] = (accum_8p_6 * pow(N, -1, Q)) % Q
        an[8*p+7] = (accum_8p_7 * pow(N, -1, Q)) % Q

    return an

# print([1 for i in range(N)])
# print(r4nttopt([1 for i in range(N)]))
# print(intt(ntt([1 for i in range(N)], Q, psi=PSI), Q, psi=PSI))
print(r8ntt([i for i in range(N)]))
print(r8intt(r8nttopt([i for i in range(N)])))
# print(intt(ntt([1 for i in range(N)])))

# def r8nttopt(a):
#     an = [0 for i in range(N)]
#     for p in range(N//8):
#         accum_8p = 0
#         accum_8p_1 = 0
#         accum_8p_2 = 0
#         accum_8p_3 = 0
#         accum_8p_4 = 0
#         accum_8p_5 = 0
#         accum_8p_6 = 0
#         accum_8p_7 = 0

#         for i in range(N//8):
#             tf_8p = pow(PSI, (2*(8*p)+1)*i, Q)
#             tf_8p_1 = pow(PSI, (2*(8*p+1)+1)*i, Q)
#             tf_8p_2 = pow(PSI, (2*(8*p+2)+1)*i, Q)
#             tf_8p_3 = pow(PSI, (2*(8*p+3)+1)*i, Q)
#             tf_8p_4 = pow(PSI, (2*(8*p+4)+1)*i, Q)
#             tf_8p_5 = pow(PSI, (2*(8*p+5)+1)*i, Q)
#             tf_8p_6 = pow(PSI, (2*(8*p+6)+1)*i, Q)
#             tf_8p_7 = pow(PSI, (2*(8*p+7)+1)*i, Q)

#             accum_8p_1 = accum_8p_1 + tf_8p * (
#                 (a[i + 0*N//8] + (a[i + 4*N//8] << 8)) 
#                 + ((a[i + 2*N//8] + (a[i + 6*N//8] << 8)) << 4)
#                 + ((
#                     (a[i + 1*N//8] + (a[i + 5*N//8] << 8)) + 
#                     ((a[i + 3*N//8] + (a[i + 7*N//8] << 8)) << 4)
#                 ) << 2)
#             )

#             accum_8p_1 = accum_8p_1 + tf_8p_1 * (
#                 (a[i + 0*N//8] - (a[i + 4*N//8] << 8))
#                 + ((a[i + 2*N//8] - (a[i + 6*N//8] << 8)) << 12)
#                 + ((
#                     (a[i + 1*N//8] - (a[i + 5*N//8] << 8)) + 
#                     ((a[i + 3*N//8] - (a[i + 7*N//8] << 8)) << 12)
#                 ) << 6)
#             )

#             accum_8p_2 = accum_8p_2 + tf_8p_2 * (
#                 (a[i + 0*N//8] + (a[i + 4*N//8] << 8))
#                 - ((a[i + 2*N//8] + (a[i + 6*N//8] << 8)) << 4)
#                 + ((
#                     (a[i + 1*N//8] + (a[i + 5*N//8] << 8)) - 
#                     ((a[i + 3*N//8] + (a[i + 7*N//8] << 8)) << 4)
#                 ) << 10)
#             )

#             accum_8p_3 = accum_8p_3 + tf_8p_3 * (
#                 (a[i + 0*N//8] - (a[i + 4*N//8] << 8))
#                 - ((a[i + 2*N//8] - (a[i + 6*N//8] << 8)) << 12)
#                 + ((
#                     (a[i + 1*N//8] - (a[i + 5*N//8] << 8)) -
#                     ((a[i + 3*N//8] - (a[i + 7*N//8] << 8)) << 12)
#                 ) << 14)
#             )

#             accum_8p_4 = accum_8p_4 + tf_8p_4 * (
#                 (a[i + 0*N//8] + (a[i + 4*N//8] << 8))
#                 + ((a[i + 2*N//8] + (a[i + 6*N//8] << 8)) << 4)
#                 - ((
#                     (a[i + 1*N//8] + (a[i + 5*N//8] << 8)) + 
#                     ((a[i + 3*N//8] + (a[i + 7*N//8] << 8)) << 4)
#                 ) << 2)
#             )

#             accum_8p_5 = accum_8p_5 + tf_8p_5 * (
#                 (a[i + 0*N//8] - (a[i + 4*N//8] << 8))
#                 + ((a[i + 2*N//8] - (a[i + 6*N//8] << 8)) << 12)
#                 - ((
#                     (a[i + 1*N//8] - (a[i + 5*N//8] << 8)) + 
#                     ((a[i + 3*N//8] - (a[i + 7*N//8] << 8)) << 12)
#                 ) << 6)
#             )

#             accum_8p_6 = accum_8p_6 + tf_8p_6 * (
#                 (a[i + 0*N//8] + (a[i + 4*N//8] << 8))
#                 - ((a[i + 2*N//8] + (a[i + 6*N//8] << 8)) << 4)
#                 - ((
#                     (a[i + 1*N//8] + (a[i + 5*N//8] << 8)) -
#                     ((a[i + 3*N//8] + (a[i + 7*N//8] << 8)) << 4)
#                 ) << 10)
#             )

#             accum_8p_7 = accum_8p_7 + tf_8p_7 * (
#                 (a[i + 0*N//8] - (a[i + 4*N//8] << 8))
#                 - ((a[i + 2*N//8] - (a[i + 6*N//8] << 8)) << 12)
#                 - ((
#                     (a[i + 1*N//8] - (a[i + 5*N//8] << 8)) - 
#                     ((a[i + 3*N//8] - (a[i + 7*N//8] << 8)) << 12)
#                 ) << 14)
#             )
        
#         an[8*p] = accum_8p % Q
#         an[8*p+1] = accum_8p_1 % Q
#         an[8*p+2] = accum_8p_2 % Q
#         an[8*p+3] = accum_8p_3 % Q
#         an[8*p+4] = accum_8p_4 % Q
#         an[8*p+5] = accum_8p_5 % Q
#         an[8*p+6] = accum_8p_6 % Q
#         an[8*p+7] = accum_8p_7 % Q

#     return an
