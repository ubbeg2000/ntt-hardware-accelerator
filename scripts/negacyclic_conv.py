from numpy import convolve, append, subtract

def negacyclic_conv(a, b, Q):
    D = max(len(a), len(b))
    c = convolve(a, b)
    return list(subtract(c[0:D], append(c[D:], 0)) % Q)

