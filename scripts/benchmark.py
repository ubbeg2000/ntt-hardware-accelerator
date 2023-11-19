from mixed_radix_ntt import rec2ntt, rec4ntt, rec8ntt, multirntt
from radix_2_ntt import r2ntt
from radix_8_ntt import r8ntt
from my_ntt import find_2nth_rou
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Waktu eksekusi untuk {func.__name__}: {elapsed_time} detik")
        return result
    return wrapper

timing_decorator(max(2, 1))

testcases = [
    # Multi-Radix Recursive NTT
    {"func": multirntt, "N": 2, "Q": 65537},
    {"func": multirntt, "N": 4, "Q": 65537},
    {"func": multirntt, "N": 8, "Q": 65537},
    {"func": multirntt, "N": 16, "Q": 65537},
    {"func": multirntt, "N": 32, "Q": 65537},
    {"func": multirntt, "N": 64, "Q": 65537},
    {"func": multirntt, "N": 128, "Q": 65537},
    {"func": multirntt, "N": 256, "Q": 65537},
    {"func": multirntt, "N": 512, "Q": 65537},
    {"func": multirntt, "N": 1024, "Q": 65537},

    # Radix-2 Recursive NTT
    {"func": rec2ntt, "N": 2, "Q": 65537},
    {"func": rec2ntt, "N": 4, "Q": 65537},
    {"func": rec2ntt, "N": 8, "Q": 65537},
    {"func": rec2ntt, "N": 16, "Q": 65537},
    {"func": rec2ntt, "N": 32, "Q": 65537},
    {"func": rec2ntt, "N": 64, "Q": 65537},
    {"func": rec2ntt, "N": 128, "Q": 65537},
    {"func": rec2ntt, "N": 256, "Q": 65537},
    {"func": rec2ntt, "N": 512, "Q": 65537},
    {"func": rec2ntt, "N": 1024, "Q": 65537},

    # Radix-4 Recursive NTT
    {"func": rec4ntt, "N": 4, "Q": 65537},
    {"func": rec4ntt, "N": 16, "Q": 65537},
    {"func": rec4ntt, "N": 64, "Q": 65537},
    {"func": rec4ntt, "N": 256, "Q": 65537},
    {"func": rec4ntt, "N": 1024, "Q": 65537},

    # Radix-8 Recursive NTT
    {"func": rec8ntt, "N": 8, "Q": 65537},
    {"func": rec8ntt, "N": 64, "Q": 65537},
    {"func": rec8ntt, "N": 512, "Q": 65537},

    # Radix-2 NTT
    {"func": r2ntt, "N": 2, "Q": 65537},
    {"func": r2ntt, "N": 4, "Q": 65537},
    {"func": r2ntt, "N": 8, "Q": 65537},
    {"func": r2ntt, "N": 16, "Q": 65537},
    {"func": r2ntt, "N": 32, "Q": 65537},
    {"func": r2ntt, "N": 64, "Q": 65537},
    {"func": r2ntt, "N": 128, "Q": 65537},
    {"func": r2ntt, "N": 256, "Q": 65537},
    {"func": r2ntt, "N": 512, "Q": 65537},
    {"func": r2ntt, "N": 1024, "Q": 65537},

    # Radix-8 NTT
    {"func": r8ntt, "N": 8, "Q": 65537},
    {"func": r8ntt, "N": 16, "Q": 65537},
    {"func": r8ntt, "N": 32, "Q": 65537},
    {"func": r8ntt, "N": 64, "Q": 65537},
    {"func": r8ntt, "N": 128, "Q": 65537},
    {"func": r8ntt, "N": 256, "Q": 65537},
    {"func": r8ntt, "N": 512, "Q": 65537},
    {"func": r8ntt, "N": 1024, "Q": 65537},
]

for tc in testcases:
    Q = tc["Q"]
    N = tc["N"]
    PSI = find_2nth_rou(Q, N)
    start_time = time.time()
    tc["func"]([i for i in range(N)], N=N, Q=Q, PSI=PSI)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{tc['func'].__name__}, {N}, {elapsed_time}")
