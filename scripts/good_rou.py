from generate_prime import is_prime
N = 1024

for k in range(64, N):
    Q = k * N + 1
    if not is_prime(Q):
        continue

    print(f"PRIME : {Q}")
    for psi in range(2, Q):
        if pow(psi, 2*N) == 1 + pow(psi, 2*N) // Q:
            print(psi)