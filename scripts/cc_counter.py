from math import floor, log

def flog(base, a):
    return floor(log(a, base))

def cc_r2(N):
    return flog(2, N) * N / 2

def cc_r4(N):
    return flog(4, N) * N / 4

def cc_r8(N):
    return flog(8, N) * N / 8

def cc_r16(N):
    return flog(16, N) * N / 16

def cc_r42(N):
    N0 = N
    N1 = N0 // pow(4, flog(4, N0))
    
    return flog(4, N0) * N // 4 + flog(2, N1) * N // 2

def cc_r82(N):
    N0 = N
    N1 = N0 // pow(8, flog(8, N0))
    
    return flog(8, N0) * N // 8 + flog(2, N1) * N // 2

def cc_r162(N):
    N0 = N
    N1 = N0 // pow(16, flog(16, N0))
    
    return flog(16, N0) * N // 16 + flog(2, N1) * N // 2

def cc_r1642(N):
    N0 = N
    N1 = N0 // pow(16, flog(16, N0))
    N2 = N1 // pow(4, flog(4, N1))
    
    return flog(16, N0) * N // 16 + flog(4, N1) * N // 4 + flog(2, N2) * N // 2

def cc_r1682(N):
    N0 = N
    N1 = N0 // pow(16, flog(16, N0))
    N2 = N1 // pow(8, flog(8, N1))

    # print(flog(16, N0), flog(8, N1), flog(2, N2))
    
    return flog(16, N0) * N // 16 + flog(8, N1) * N // 8 + flog(2, N2) * N // 2

def cc_r1642(N):
    N0 = N
    N1 = N0 // pow(16, flog(16, N0))
    N2 = N1 // pow(4, flog(4, N1))
    
    return flog(16, N0) * N // 16 + flog(4, N1) * N // 4 + flog(2, N2) * N // 2

def cc_r16842(N):
    N0 = N
    N1 = N0 // pow(16, flog(16, N0))
    N2 = N1 // pow(8, flog(8, N1))
    N3 = N2 // pow(4, flog(4, N2))

    # print(N0, N1, N1, N3)
    # print(flog(16, N0), flog(8, N1), flog(4, N2), flog(2, N3))
    
    return flog(16, N0) * N // 16 + flog(8, N1) * N // 8 + flog(4, N2) * N // 4 + flog(2, N3) * N // 2

for i in range(10, 16):
    N = pow(2, i)

    print(f"{cc_r16842(N)};{cc_r42(N)};{cc_r82(N)};{cc_r162(N)};{cc_r1642(N)};{cc_r1682(N)}")