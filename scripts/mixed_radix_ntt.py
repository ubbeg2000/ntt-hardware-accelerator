from radix_4_ntt import r4ntt
from radix_2_ntt import r2ntt
from my_ntt import ntt, find_2nth_rou

N = 256
Q = 65537
PSI = find_2nth_rou(Q, N)

def rec2ntt(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)
    if n == 1:
        return a
    
    else:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = rec2ntt(a_2p)
        y_2p_1 = rec2ntt(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q

        return y
    
def rec4ntt(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)
    if n == 1:
        return a
    
    else:
        a_4p = [a[4*i] for i in range(n//4)]
        a_4p_1 = [a[4*i+1] for i in range(n//4)]
        a_4p_2 = [a[4*i+2] for i in range(n//4)]
        a_4p_3 = [a[4*i+3] for i in range(n//4)]


        y_4p = rec4ntt(a_4p)
        y_4p_1 = rec4ntt(a_4p_1)
        y_4p_2 = rec4ntt(a_4p_2)
        y_4p_3 = rec4ntt(a_4p_3)

        y = [0 for i in range(n)]
        for i in range(n//4):
            tf =  pow(PSI, N//n, Q)
            tf_2p = pow(tf, (2*i+1), Q)
            tf_3p = pow(tf, (2*i+1), Q) * pow(PSI, N//2, Q)
            tf_2p_2 = pow(tf, 2*(2*i+1), Q)
            
            y[i+0*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] + tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+1*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] + tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q
            y[i+2*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] - tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+3*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] - tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q

        return y

def rec8ntt(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)
    if n == 1:
        return a
    
    else:
        a_8p_0 = [a[8*i+0] for i in range(n//8)]
        a_8p_1 = [a[8*i+1] for i in range(n//8)]
        a_8p_2 = [a[8*i+2] for i in range(n//8)]
        a_8p_3 = [a[8*i+3] for i in range(n//8)]
        a_8p_4 = [a[8*i+4] for i in range(n//8)]
        a_8p_5 = [a[8*i+5] for i in range(n//8)]
        a_8p_6 = [a[8*i+6] for i in range(n//8)]
        a_8p_7 = [a[8*i+7] for i in range(n//8)]

        y_8p_0 = rec8ntt(a_8p_0)
        y_8p_1 = rec8ntt(a_8p_1)
        y_8p_2 = rec8ntt(a_8p_2)
        y_8p_3 = rec8ntt(a_8p_3)
        y_8p_4 = rec8ntt(a_8p_4)
        y_8p_5 = rec8ntt(a_8p_5)
        y_8p_6 = rec8ntt(a_8p_6)
        y_8p_7 = rec8ntt(a_8p_7)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//8):
            tf = pow(psi, (2*i+1), Q)
            tf_2 = pow(psi, 2*(2*i+1), Q)
            tf_4 = pow(psi, 4*(2*i+1), Q)

            tf_shift_1 = tf * pow(PSI, 1*N//4, Q)
            tf_shift_2 = tf * pow(PSI, 2*N//4, Q)
            tf_shift_3 = tf * pow(PSI, 3*N//4, Q)
            
            tf_2_shift = tf_2 * pow(PSI, N//2, Q)
            
            y[i+0*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+1*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+2*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+3*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+4*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+5*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+6*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+7*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

        return y
    
def rec16ntt(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)
    if n == 1:
        return a
    
    else:
        a_16p_0 = [a[16*i+0] for i in range(n//16)]
        a_16p_1 = [a[16*i+1] for i in range(n//16)]
        a_16p_2 = [a[16*i+2] for i in range(n//16)]
        a_16p_3 = [a[16*i+3] for i in range(n//16)]
        a_16p_4 = [a[16*i+4] for i in range(n//16)]
        a_16p_5 = [a[16*i+5] for i in range(n//16)]
        a_16p_6 = [a[16*i+6] for i in range(n//16)]
        a_16p_7 = [a[16*i+7] for i in range(n//16)]
        a_16p_8 = [a[16*i+8] for i in range(n//16)]
        a_16p_9 = [a[16*i+9] for i in range(n//16)]
        a_16p_10 = [a[16*i+10] for i in range(n//16)]
        a_16p_11 = [a[16*i+11] for i in range(n//16)]
        a_16p_12 = [a[16*i+12] for i in range(n//16)]
        a_16p_13 = [a[16*i+13] for i in range(n//16)]
        a_16p_14 = [a[16*i+14] for i in range(n//16)]
        a_16p_15 = [a[16*i+15] for i in range(n//16)]

        y_16p_0 = rec16ntt(a_16p_0)
        y_16p_1 = rec16ntt(a_16p_1)
        y_16p_2 = rec16ntt(a_16p_2)
        y_16p_3 = rec16ntt(a_16p_3)
        y_16p_4 = rec16ntt(a_16p_4)
        y_16p_5 = rec16ntt(a_16p_5)
        y_16p_6 = rec16ntt(a_16p_6)
        y_16p_7 = rec16ntt(a_16p_7)
        y_16p_8 = rec16ntt(a_16p_8)
        y_16p_9 = rec16ntt(a_16p_9)
        y_16p_10 = rec16ntt(a_16p_10)
        y_16p_11 = rec16ntt(a_16p_11)
        y_16p_12 = rec16ntt(a_16p_12)
        y_16p_13 = rec16ntt(a_16p_13)
        y_16p_14 = rec16ntt(a_16p_14)
        y_16p_15 = rec16ntt(a_16p_15)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//16):
            tf = pow(psi, (2*i+1), Q)
            tf_4 = pow(psi, 2*(2*i+1), Q)
            tf_2 = pow(psi, 4*(2*i+1), Q)
            tf_8 = pow(psi, 8*(2*i+1), Q)

            psi_n_2 = pow(PSI, N//2, Q)
            psi_n_4 = pow(PSI, N//4, Q)
            psi_n_8 = pow(PSI, N//8, Q)

            tf_4_shift_1 = pow(psi_n_4, 1, Q) * tf_4
            tf_4_shift_2 = pow(psi_n_4, 2, Q) * tf_4
            tf_4_shift_3 = pow(psi_n_4, 3, Q) * tf_4

            tf_2_shift_1 = pow(psi_n_2, 1, Q) * tf_2

            tf_shift_1 = pow(psi_n_8, 1, Q) * tf
            tf_shift_2 = pow(psi_n_8, 2, Q) * tf
            tf_shift_3 = pow(psi_n_8, 3, Q) * tf
            tf_shift_4 = pow(psi_n_8, 4, Q) * tf
            tf_shift_5 = pow(psi_n_8, 5, Q) * tf
            tf_shift_6 = pow(psi_n_8, 6, Q) * tf
            tf_shift_7 = pow(psi_n_8, 7, Q) * tf
            
            y[i+0*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+1*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+2*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+3*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+4*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+5*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+6*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+7*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) -
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+8*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+9*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+10*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+11*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+12*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+13*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+14*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+15*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

        return y

def multirntt(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 16 == 0:
        a_16p_0 = [a[16*i+0] for i in range(n//16)]
        a_16p_1 = [a[16*i+1] for i in range(n//16)]
        a_16p_2 = [a[16*i+2] for i in range(n//16)]
        a_16p_3 = [a[16*i+3] for i in range(n//16)]
        a_16p_4 = [a[16*i+4] for i in range(n//16)]
        a_16p_5 = [a[16*i+5] for i in range(n//16)]
        a_16p_6 = [a[16*i+6] for i in range(n//16)]
        a_16p_7 = [a[16*i+7] for i in range(n//16)]
        a_16p_8 = [a[16*i+8] for i in range(n//16)]
        a_16p_9 = [a[16*i+9] for i in range(n//16)]
        a_16p_10 = [a[16*i+10] for i in range(n//16)]
        a_16p_11 = [a[16*i+11] for i in range(n//16)]
        a_16p_12 = [a[16*i+12] for i in range(n//16)]
        a_16p_13 = [a[16*i+13] for i in range(n//16)]
        a_16p_14 = [a[16*i+14] for i in range(n//16)]
        a_16p_15 = [a[16*i+15] for i in range(n//16)]

        y_16p_0 = multirntt(a_16p_0)
        y_16p_1 = multirntt(a_16p_1)
        y_16p_2 = multirntt(a_16p_2)
        y_16p_3 = multirntt(a_16p_3)
        y_16p_4 = multirntt(a_16p_4)
        y_16p_5 = multirntt(a_16p_5)
        y_16p_6 = multirntt(a_16p_6)
        y_16p_7 = multirntt(a_16p_7)
        y_16p_8 = multirntt(a_16p_8)
        y_16p_9 = multirntt(a_16p_9)
        y_16p_10 = multirntt(a_16p_10)
        y_16p_11 = multirntt(a_16p_11)
        y_16p_12 = multirntt(a_16p_12)
        y_16p_13 = multirntt(a_16p_13)
        y_16p_14 = multirntt(a_16p_14)
        y_16p_15 = multirntt(a_16p_15)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//16):
            tf = pow(psi, (2*i+1), Q)
            tf_4 = pow(psi, 2*(2*i+1), Q)
            tf_2 = pow(psi, 4*(2*i+1), Q)
            tf_8 = pow(psi, 8*(2*i+1), Q)

            psi_n_2 = pow(PSI, N//2, Q)
            psi_n_4 = pow(PSI, N//4, Q)
            psi_n_8 = pow(PSI, N//8, Q)

            tf_4_shift_1 = pow(psi_n_4, 1, Q) * tf_4
            tf_4_shift_2 = pow(psi_n_4, 2, Q) * tf_4
            tf_4_shift_3 = pow(psi_n_4, 3, Q) * tf_4

            tf_2_shift_1 = pow(psi_n_2, 1, Q) * tf_2

            tf_shift_1 = pow(psi_n_8, 1, Q) * tf
            tf_shift_2 = pow(psi_n_8, 2, Q) * tf
            tf_shift_3 = pow(psi_n_8, 3, Q) * tf
            tf_shift_4 = pow(psi_n_8, 4, Q) * tf
            tf_shift_5 = pow(psi_n_8, 5, Q) * tf
            tf_shift_6 = pow(psi_n_8, 6, Q) * tf
            tf_shift_7 = pow(psi_n_8, 7, Q) * tf
            
            y[i+0*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+1*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+2*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+3*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+4*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+5*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+6*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+7*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) -
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+8*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+9*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+10*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+11*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+12*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+13*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+14*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+15*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

        return y

    elif n % 8 == 0:
        a_8p_0 = [a[8*i+0] for i in range(n//8)]
        a_8p_1 = [a[8*i+1] for i in range(n//8)]
        a_8p_2 = [a[8*i+2] for i in range(n//8)]
        a_8p_3 = [a[8*i+3] for i in range(n//8)]
        a_8p_4 = [a[8*i+4] for i in range(n//8)]
        a_8p_5 = [a[8*i+5] for i in range(n//8)]
        a_8p_6 = [a[8*i+6] for i in range(n//8)]
        a_8p_7 = [a[8*i+7] for i in range(n//8)]

        y_8p_0 = multirntt(a_8p_0)
        y_8p_1 = multirntt(a_8p_1)
        y_8p_2 = multirntt(a_8p_2)
        y_8p_3 = multirntt(a_8p_3)
        y_8p_4 = multirntt(a_8p_4)
        y_8p_5 = multirntt(a_8p_5)
        y_8p_6 = multirntt(a_8p_6)
        y_8p_7 = multirntt(a_8p_7)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//8):
            tf = pow(psi, (2*i+1), Q)
            tf_2 = pow(psi, 2*(2*i+1), Q)
            tf_4 = pow(psi, 4*(2*i+1), Q)

            tf_shift_1 = tf * pow(PSI, 1*N//4, Q)
            tf_shift_2 = tf * pow(PSI, 2*N//4, Q)
            tf_shift_3 = tf * pow(PSI, 3*N//4, Q)
            
            tf_2_shift = tf_2 * pow(PSI, N//2, Q)
            
            y[i+0*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+1*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+2*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+3*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+4*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+5*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+6*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+7*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

        return y
    
    elif n % 4 == 0:
        a_4p = [a[4*i] for i in range(n//4)]
        a_4p_1 = [a[4*i+1] for i in range(n//4)]
        a_4p_2 = [a[4*i+2] for i in range(n//4)]
        a_4p_3 = [a[4*i+3] for i in range(n//4)]


        y_4p = multirntt(a_4p)
        y_4p_1 = multirntt(a_4p_1)
        y_4p_2 = multirntt(a_4p_2)
        y_4p_3 = multirntt(a_4p_3)

        y = [0 for i in range(n)]
        for i in range(n//4):
            tf =  pow(PSI, N//n, Q)
            tf_2p = pow(tf, (2*i+1), Q)
            tf_3p = pow(tf, (2*i+1), Q) * pow(PSI, N//2, Q)
            tf_2p_2 = pow(tf, 2*(2*i+1), Q)
            
            y[i+0*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] + tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+1*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] + tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q
            y[i+2*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] - tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+3*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] - tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q

        return y
    
    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt(a_2p)
        y_2p_1 = multirntt(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a

def multirntt42(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 4 == 0:
        a_4p = [a[4*i] for i in range(n//4)]
        a_4p_1 = [a[4*i+1] for i in range(n//4)]
        a_4p_2 = [a[4*i+2] for i in range(n//4)]
        a_4p_3 = [a[4*i+3] for i in range(n//4)]


        y_4p = multirntt(a_4p)
        y_4p_1 = multirntt(a_4p_1)
        y_4p_2 = multirntt(a_4p_2)
        y_4p_3 = multirntt(a_4p_3)

        y = [0 for i in range(n)]
        for i in range(n//4):
            tf =  pow(PSI, N//n, Q)
            tf_2p = pow(tf, (2*i+1), Q)
            tf_3p = pow(tf, (2*i+1), Q) * pow(PSI, N//2, Q)
            tf_2p_2 = pow(tf, 2*(2*i+1), Q)
            
            y[i+0*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] + tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+1*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] + tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q
            y[i+2*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] - tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+3*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] - tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q

        return y
    
    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt(a_2p)
        y_2p_1 = multirntt(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a
    
def multirntt82(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 8 == 0:
        a_8p_0 = [a[8*i+0] for i in range(n//8)]
        a_8p_1 = [a[8*i+1] for i in range(n//8)]
        a_8p_2 = [a[8*i+2] for i in range(n//8)]
        a_8p_3 = [a[8*i+3] for i in range(n//8)]
        a_8p_4 = [a[8*i+4] for i in range(n//8)]
        a_8p_5 = [a[8*i+5] for i in range(n//8)]
        a_8p_6 = [a[8*i+6] for i in range(n//8)]
        a_8p_7 = [a[8*i+7] for i in range(n//8)]

        y_8p_0 = multirntt(a_8p_0)
        y_8p_1 = multirntt(a_8p_1)
        y_8p_2 = multirntt(a_8p_2)
        y_8p_3 = multirntt(a_8p_3)
        y_8p_4 = multirntt(a_8p_4)
        y_8p_5 = multirntt(a_8p_5)
        y_8p_6 = multirntt(a_8p_6)
        y_8p_7 = multirntt(a_8p_7)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//8):
            tf = pow(psi, (2*i+1), Q)
            tf_2 = pow(psi, 2*(2*i+1), Q)
            tf_4 = pow(psi, 4*(2*i+1), Q)

            tf_shift_1 = tf * pow(PSI, 1*N//4, Q)
            tf_shift_2 = tf * pow(PSI, 2*N//4, Q)
            tf_shift_3 = tf * pow(PSI, 3*N//4, Q)
            
            tf_2_shift = tf_2 * pow(PSI, N//2, Q)
            
            y[i+0*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+1*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+2*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+3*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+4*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+5*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+6*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+7*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

        return y
    
    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt(a_2p)
        y_2p_1 = multirntt(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a

def multirntt162(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 16 == 0:
        a_16p_0 = [a[16*i+0] for i in range(n//16)]
        a_16p_1 = [a[16*i+1] for i in range(n//16)]
        a_16p_2 = [a[16*i+2] for i in range(n//16)]
        a_16p_3 = [a[16*i+3] for i in range(n//16)]
        a_16p_4 = [a[16*i+4] for i in range(n//16)]
        a_16p_5 = [a[16*i+5] for i in range(n//16)]
        a_16p_6 = [a[16*i+6] for i in range(n//16)]
        a_16p_7 = [a[16*i+7] for i in range(n//16)]
        a_16p_8 = [a[16*i+8] for i in range(n//16)]
        a_16p_9 = [a[16*i+9] for i in range(n//16)]
        a_16p_10 = [a[16*i+10] for i in range(n//16)]
        a_16p_11 = [a[16*i+11] for i in range(n//16)]
        a_16p_12 = [a[16*i+12] for i in range(n//16)]
        a_16p_13 = [a[16*i+13] for i in range(n//16)]
        a_16p_14 = [a[16*i+14] for i in range(n//16)]
        a_16p_15 = [a[16*i+15] for i in range(n//16)]

        y_16p_0 = multirntt162(a_16p_0)
        y_16p_1 = multirntt162(a_16p_1)
        y_16p_2 = multirntt162(a_16p_2)
        y_16p_3 = multirntt162(a_16p_3)
        y_16p_4 = multirntt162(a_16p_4)
        y_16p_5 = multirntt162(a_16p_5)
        y_16p_6 = multirntt162(a_16p_6)
        y_16p_7 = multirntt162(a_16p_7)
        y_16p_8 = multirntt162(a_16p_8)
        y_16p_9 = multirntt162(a_16p_9)
        y_16p_10 = multirntt162(a_16p_10)
        y_16p_11 = multirntt162(a_16p_11)
        y_16p_12 = multirntt162(a_16p_12)
        y_16p_13 = multirntt162(a_16p_13)
        y_16p_14 = multirntt162(a_16p_14)
        y_16p_15 = multirntt162(a_16p_15)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//16):
            tf = pow(psi, (2*i+1), Q)
            tf_4 = pow(psi, 2*(2*i+1), Q)
            tf_2 = pow(psi, 4*(2*i+1), Q)
            tf_8 = pow(psi, 8*(2*i+1), Q)

            psi_n_2 = pow(PSI, N//2, Q)
            psi_n_4 = pow(PSI, N//4, Q)
            psi_n_8 = pow(PSI, N//8, Q)

            tf_4_shift_1 = pow(psi_n_4, 1, Q) * tf_4
            tf_4_shift_2 = pow(psi_n_4, 2, Q) * tf_4
            tf_4_shift_3 = pow(psi_n_4, 3, Q) * tf_4

            tf_2_shift_1 = pow(psi_n_2, 1, Q) * tf_2

            tf_shift_1 = pow(psi_n_8, 1, Q) * tf
            tf_shift_2 = pow(psi_n_8, 2, Q) * tf
            tf_shift_3 = pow(psi_n_8, 3, Q) * tf
            tf_shift_4 = pow(psi_n_8, 4, Q) * tf
            tf_shift_5 = pow(psi_n_8, 5, Q) * tf
            tf_shift_6 = pow(psi_n_8, 6, Q) * tf
            tf_shift_7 = pow(psi_n_8, 7, Q) * tf
            
            y[i+0*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+1*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+2*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+3*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+4*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+5*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+6*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+7*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) -
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+8*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+9*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+10*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+11*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+12*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+13*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+14*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+15*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

        return y

    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt162(a_2p)
        y_2p_1 = multirntt162(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a

def multirntt1642(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 16 == 0:
        a_16p_0 = [a[16*i+0] for i in range(n//16)]
        a_16p_1 = [a[16*i+1] for i in range(n//16)]
        a_16p_2 = [a[16*i+2] for i in range(n//16)]
        a_16p_3 = [a[16*i+3] for i in range(n//16)]
        a_16p_4 = [a[16*i+4] for i in range(n//16)]
        a_16p_5 = [a[16*i+5] for i in range(n//16)]
        a_16p_6 = [a[16*i+6] for i in range(n//16)]
        a_16p_7 = [a[16*i+7] for i in range(n//16)]
        a_16p_8 = [a[16*i+8] for i in range(n//16)]
        a_16p_9 = [a[16*i+9] for i in range(n//16)]
        a_16p_10 = [a[16*i+10] for i in range(n//16)]
        a_16p_11 = [a[16*i+11] for i in range(n//16)]
        a_16p_12 = [a[16*i+12] for i in range(n//16)]
        a_16p_13 = [a[16*i+13] for i in range(n//16)]
        a_16p_14 = [a[16*i+14] for i in range(n//16)]
        a_16p_15 = [a[16*i+15] for i in range(n//16)]

        y_16p_0 = multirntt1642(a_16p_0)
        y_16p_1 = multirntt1642(a_16p_1)
        y_16p_2 = multirntt1642(a_16p_2)
        y_16p_3 = multirntt1642(a_16p_3)
        y_16p_4 = multirntt1642(a_16p_4)
        y_16p_5 = multirntt1642(a_16p_5)
        y_16p_6 = multirntt1642(a_16p_6)
        y_16p_7 = multirntt1642(a_16p_7)
        y_16p_8 = multirntt1642(a_16p_8)
        y_16p_9 = multirntt1642(a_16p_9)
        y_16p_10 = multirntt1642(a_16p_10)
        y_16p_11 = multirntt1642(a_16p_11)
        y_16p_12 = multirntt1642(a_16p_12)
        y_16p_13 = multirntt1642(a_16p_13)
        y_16p_14 = multirntt1642(a_16p_14)
        y_16p_15 = multirntt1642(a_16p_15)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//16):
            tf = pow(psi, (2*i+1), Q)
            tf_4 = pow(psi, 2*(2*i+1), Q)
            tf_2 = pow(psi, 4*(2*i+1), Q)
            tf_8 = pow(psi, 8*(2*i+1), Q)

            psi_n_2 = pow(PSI, N//2, Q)
            psi_n_4 = pow(PSI, N//4, Q)
            psi_n_8 = pow(PSI, N//8, Q)

            tf_4_shift_1 = pow(psi_n_4, 1, Q) * tf_4
            tf_4_shift_2 = pow(psi_n_4, 2, Q) * tf_4
            tf_4_shift_3 = pow(psi_n_4, 3, Q) * tf_4

            tf_2_shift_1 = pow(psi_n_2, 1, Q) * tf_2

            tf_shift_1 = pow(psi_n_8, 1, Q) * tf
            tf_shift_2 = pow(psi_n_8, 2, Q) * tf
            tf_shift_3 = pow(psi_n_8, 3, Q) * tf
            tf_shift_4 = pow(psi_n_8, 4, Q) * tf
            tf_shift_5 = pow(psi_n_8, 5, Q) * tf
            tf_shift_6 = pow(psi_n_8, 6, Q) * tf
            tf_shift_7 = pow(psi_n_8, 7, Q) * tf
            
            y[i+0*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+1*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+2*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+3*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+4*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+5*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+6*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+7*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) -
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+8*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+9*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+10*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+11*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+12*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+13*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+14*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+15*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

        return y

    elif n % 4 == 0:
        a_4p = [a[4*i] for i in range(n//4)]
        a_4p_1 = [a[4*i+1] for i in range(n//4)]
        a_4p_2 = [a[4*i+2] for i in range(n//4)]
        a_4p_3 = [a[4*i+3] for i in range(n//4)]


        y_4p = multirntt1642(a_4p)
        y_4p_1 = multirntt1642(a_4p_1)
        y_4p_2 = multirntt1642(a_4p_2)
        y_4p_3 = multirntt1642(a_4p_3)

        y = [0 for i in range(n)]
        for i in range(n//4):
            tf =  pow(PSI, N//n, Q)
            tf_2p = pow(tf, (2*i+1), Q)
            tf_3p = pow(tf, (2*i+1), Q) * pow(PSI, N//2, Q)
            tf_2p_2 = pow(tf, 2*(2*i+1), Q)
            
            y[i+0*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] + tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+1*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] + tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q
            y[i+2*n//4] = (y_4p[i] + tf_2p_2 * y_4p_2[i] - tf_2p * (y_4p_1[i] + tf_2p_2 * y_4p_3[i])) % Q
            y[i+3*n//4] = (y_4p[i] - tf_2p_2 * y_4p_2[i] - tf_3p * (y_4p_1[i] - tf_2p_2 * y_4p_3[i])) % Q

        return y
    
    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt1642(a_2p)
        y_2p_1 = multirntt1642(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a

def multirntt1682(a, N = N, Q = Q, PSI = find_2nth_rou(Q, N)):
    n = len(a)

    if n % 16 == 0:
        a_16p_0 = [a[16*i+0] for i in range(n//16)]
        a_16p_1 = [a[16*i+1] for i in range(n//16)]
        a_16p_2 = [a[16*i+2] for i in range(n//16)]
        a_16p_3 = [a[16*i+3] for i in range(n//16)]
        a_16p_4 = [a[16*i+4] for i in range(n//16)]
        a_16p_5 = [a[16*i+5] for i in range(n//16)]
        a_16p_6 = [a[16*i+6] for i in range(n//16)]
        a_16p_7 = [a[16*i+7] for i in range(n//16)]
        a_16p_8 = [a[16*i+8] for i in range(n//16)]
        a_16p_9 = [a[16*i+9] for i in range(n//16)]
        a_16p_10 = [a[16*i+10] for i in range(n//16)]
        a_16p_11 = [a[16*i+11] for i in range(n//16)]
        a_16p_12 = [a[16*i+12] for i in range(n//16)]
        a_16p_13 = [a[16*i+13] for i in range(n//16)]
        a_16p_14 = [a[16*i+14] for i in range(n//16)]
        a_16p_15 = [a[16*i+15] for i in range(n//16)]

        y_16p_0 = multirntt1682(a_16p_0)
        y_16p_1 = multirntt1682(a_16p_1)
        y_16p_2 = multirntt1682(a_16p_2)
        y_16p_3 = multirntt1682(a_16p_3)
        y_16p_4 = multirntt1682(a_16p_4)
        y_16p_5 = multirntt1682(a_16p_5)
        y_16p_6 = multirntt1682(a_16p_6)
        y_16p_7 = multirntt1682(a_16p_7)
        y_16p_8 = multirntt1682(a_16p_8)
        y_16p_9 = multirntt1682(a_16p_9)
        y_16p_10 = multirntt1682(a_16p_10)
        y_16p_11 = multirntt1682(a_16p_11)
        y_16p_12 = multirntt1682(a_16p_12)
        y_16p_13 = multirntt1682(a_16p_13)
        y_16p_14 = multirntt1682(a_16p_14)
        y_16p_15 = multirntt1682(a_16p_15)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//16):
            tf = pow(psi, (2*i+1), Q)
            tf_4 = pow(psi, 2*(2*i+1), Q)
            tf_2 = pow(psi, 4*(2*i+1), Q)
            tf_8 = pow(psi, 8*(2*i+1), Q)

            psi_n_2 = pow(PSI, N//2, Q)
            psi_n_4 = pow(PSI, N//4, Q)
            psi_n_8 = pow(PSI, N//8, Q)

            tf_4_shift_1 = pow(psi_n_4, 1, Q) * tf_4
            tf_4_shift_2 = pow(psi_n_4, 2, Q) * tf_4
            tf_4_shift_3 = pow(psi_n_4, 3, Q) * tf_4

            tf_2_shift_1 = pow(psi_n_2, 1, Q) * tf_2

            tf_shift_1 = pow(psi_n_8, 1, Q) * tf
            tf_shift_2 = pow(psi_n_8, 2, Q) * tf
            tf_shift_3 = pow(psi_n_8, 3, Q) * tf
            tf_shift_4 = pow(psi_n_8, 4, Q) * tf
            tf_shift_5 = pow(psi_n_8, 5, Q) * tf
            tf_shift_6 = pow(psi_n_8, 6, Q) * tf
            tf_shift_7 = pow(psi_n_8, 7, Q) * tf
            
            y[i+0*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+1*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+2*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+3*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+4*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+5*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+6*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) + 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+7*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) + 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) -
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+8*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+9*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_1 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+10*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) + 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_2 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) + 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+11*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) + 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_3 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) + 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+12*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] + tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4 * (y_16p_2[i] + tf_8 * y_16p_10[i] + tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_4 * ((y_16p_1[i] + tf_8 * y_16p_9[i] + tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4 * (y_16p_3[i] + tf_8 * y_16p_11[i] + tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+13*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] + tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_1 * (y_16p_2[i] - tf_8 * y_16p_10[i] + tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_5 * ((y_16p_1[i] - tf_8 * y_16p_9[i] + tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_1 * (y_16p_3[i] - tf_8 * y_16p_11[i] + tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

            y[i+14*n//16] = (
                (y_16p_0[i] + tf_8 * y_16p_8[i] - tf_2 * (y_16p_4[i] + tf_8 * y_16p_12[i])) - 
                tf_4_shift_2 * (y_16p_2[i] + tf_8 * y_16p_10[i] - tf_2 * (y_16p_6[i] + tf_8 * y_16p_14[i])) - 
                tf_shift_6 * ((y_16p_1[i] + tf_8 * y_16p_9[i] - tf_2 * (y_16p_5[i] + tf_8 * y_16p_13[i])) - 
                tf_4_shift_2 * (y_16p_3[i] + tf_8 * y_16p_11[i] - tf_2 * (y_16p_7[i] + tf_8 * y_16p_15[i])))
            ) % Q

            y[i+15*n//16] = (
                (y_16p_0[i] - tf_8 * y_16p_8[i] - tf_2_shift_1 * (y_16p_4[i] - tf_8 * y_16p_12[i])) - 
                tf_4_shift_3 * (y_16p_2[i] - tf_8 * y_16p_10[i] - tf_2_shift_1 * (y_16p_6[i] - tf_8 * y_16p_14[i])) - 
                tf_shift_7 * ((y_16p_1[i] - tf_8 * y_16p_9[i] - tf_2_shift_1 * (y_16p_5[i] - tf_8 * y_16p_13[i])) - 
                tf_4_shift_3 * (y_16p_3[i] - tf_8 * y_16p_11[i] - tf_2_shift_1 * (y_16p_7[i] - tf_8 * y_16p_15[i])))
            ) % Q

        return y

    elif n % 8 == 0:
        a_8p_0 = [a[8*i+0] for i in range(n//8)]
        a_8p_1 = [a[8*i+1] for i in range(n//8)]
        a_8p_2 = [a[8*i+2] for i in range(n//8)]
        a_8p_3 = [a[8*i+3] for i in range(n//8)]
        a_8p_4 = [a[8*i+4] for i in range(n//8)]
        a_8p_5 = [a[8*i+5] for i in range(n//8)]
        a_8p_6 = [a[8*i+6] for i in range(n//8)]
        a_8p_7 = [a[8*i+7] for i in range(n//8)]

        y_8p_0 = multirntt1682(a_8p_0)
        y_8p_1 = multirntt1682(a_8p_1)
        y_8p_2 = multirntt1682(a_8p_2)
        y_8p_3 = multirntt1682(a_8p_3)
        y_8p_4 = multirntt1682(a_8p_4)
        y_8p_5 = multirntt1682(a_8p_5)
        y_8p_6 = multirntt1682(a_8p_6)
        y_8p_7 = multirntt1682(a_8p_7)

        psi = pow(PSI, N//n, Q)

        y = [0 for i in range(n)]
        for i in range(n//8):
            tf = pow(psi, (2*i+1), Q)
            tf_2 = pow(psi, 2*(2*i+1), Q)
            tf_4 = pow(psi, 4*(2*i+1), Q)

            tf_shift_1 = tf * pow(PSI, 1*N//4, Q)
            tf_shift_2 = tf * pow(PSI, 2*N//4, Q)
            tf_shift_3 = tf * pow(PSI, 3*N//4, Q)
            
            tf_2_shift = tf_2 * pow(PSI, N//2, Q)
            
            y[i+0*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+1*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+2*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) + 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+3*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) + 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+4*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] + tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf * (y_8p_1[i] + tf_4 * y_8p_5[i] + tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+5*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] + tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_1 * (y_8p_1[i] - tf_4 * y_8p_5[i] + tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

            y[i+6*n//8] = (
                (y_8p_0[i] + tf_4 * y_8p_4[i] - tf_2 * (y_8p_2[i] + tf_4 * y_8p_6[i])) - 
                tf_shift_2 * (y_8p_1[i] + tf_4 * y_8p_5[i] - tf_2 * (y_8p_3[i] + tf_4 * y_8p_7[i]))
            ) % Q

            y[i+7*n//8] = (
                (y_8p_0[i] - tf_4 * y_8p_4[i] - tf_2_shift * (y_8p_2[i] - tf_4 * y_8p_6[i])) - 
                tf_shift_3 * (y_8p_1[i] - tf_4 * y_8p_5[i] - tf_2_shift * (y_8p_3[i] - tf_4 * y_8p_7[i]))
            ) % Q

        return y
    
    elif n % 2 == 0:
        a_2p = [a[2*i] for i in range(n//2)]
        a_2p_1 = [a[2*i+1] for i in range(n//2)]

        y_2p = multirntt1682(a_2p)
        y_2p_1 = multirntt1682(a_2p_1)

        y = [0 for i in range(n)]
        for i in range(n//2):
            tf_2p = pow(PSI, (2*i+1)*N//n, Q)
            
            y[i] = (y_2p[i] + tf_2p * y_2p_1[i]) % Q
            y[i+n//2] = (y_2p[i] - tf_2p * y_2p_1[i]) % Q
        
        return y

    else:
        return a

if __name__ == "__main__":
    inp = [i for i in range(N)]
    # print(find_2nth_rou(Q, N))
    print(rec16ntt(inp, N = N, Q = Q, PSI = PSI))
    print(r2ntt(inp, N = N, Q = Q, PSI = PSI))
    print(multirntt(inp, N = N, Q = Q, PSI = PSI)==rec16ntt(inp, N = N, Q = Q, PSI = PSI))