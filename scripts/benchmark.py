from mixed_radix_ntt import rec2ntt, rec4ntt, rec8ntt, rec16ntt, multirntt, multirntt42, multirntt82
from radix_2_ntt import r2ntt
from radix_4_ntt import r4ntt
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
    {"func": multirntt, "N": pow(2, 10), "Q": 65537},
    {"func": multirntt, "N": pow(2, 11), "Q": 65537},
    {"func": multirntt, "N": pow(2, 12), "Q": 65537},
    {"func": multirntt, "N": pow(2, 13), "Q": 65537},
    {"func": multirntt, "N": pow(2, 14), "Q": 65537},
    {"func": multirntt, "N": pow(2, 15), "Q": 65537},

    # Multi-Radix Recursive NTT 4 2
    {"func": multirntt42, "N": pow(2, 10), "Q": 65537},
    {"func": multirntt42, "N": pow(2, 11), "Q": 65537},
    {"func": multirntt42, "N": pow(2, 12), "Q": 65537},
    {"func": multirntt42, "N": pow(2, 13), "Q": 65537},
    {"func": multirntt42, "N": pow(2, 14), "Q": 65537},
    {"func": multirntt42, "N": pow(2, 15), "Q": 65537},

    # Multi-Radix Recursive NTT 8 2
    {"func": multirntt82, "N": pow(2, 10), "Q": 65537},
    {"func": multirntt82, "N": pow(2, 11), "Q": 65537},
    {"func": multirntt82, "N": pow(2, 12), "Q": 65537},
    {"func": multirntt82, "N": pow(2, 13), "Q": 65537},
    {"func": multirntt82, "N": pow(2, 14), "Q": 65537},
    {"func": multirntt82, "N": pow(2, 15), "Q": 65537},

    # Radix-2 Recursive NTT
    {"func":rec2ntt, "N": pow(2, 10), "Q": 65537},
    {"func":rec2ntt, "N": pow(2, 11), "Q": 65537},
    {"func":rec2ntt, "N": pow(2, 12), "Q": 65537},
    {"func":rec2ntt, "N": pow(2, 13), "Q": 65537},
    {"func":rec2ntt, "N": pow(2, 14), "Q": 65537},
    {"func":rec2ntt, "N": pow(2, 15), "Q": 65537},

    # Radix-4 Recursive NTT
    {"func": rec4ntt, "N": pow(2, 10), "Q": 65537},
    {"func": rec4ntt, "N": pow(2, 12), "Q": 65537},
    {"func": rec4ntt, "N": pow(2, 14), "Q": 65537},

    # Radix-8 Recursive NTT
    {"func": rec8ntt, "N": pow(2, 12), "Q": 65537},
    {"func": rec8ntt, "N": pow(2, 15), "Q": 65537},

    # Radix-16 Recursive NTT
    {"func":rec16ntt, "N": pow(2, 12), "Q": 65537},

    # Radix-2 NTT
    # {"func": r2ntt, "N": pow(2, 10), "Q": 65537},
    # {"func": r2ntt, "N": pow(2, 11), "Q": 65537},
    # {"func": r2ntt, "N": pow(2, 12), "Q": 65537},
    # {"func": r2ntt, "N": pow(2, 13), "Q": 65537},
    # {"func": r2ntt, "N": pow(2, 14), "Q": 65537},
    # {"func": r2ntt, "N": pow(2, 15), "Q": 65537},

    # Radix-4 NTT
    # {"func": r4ntt, "N": pow(2, 10), "Q": 65537},
    # {"func": r4ntt, "N": pow(2, 11), "Q": 65537},
    # {"func": r4ntt, "N": pow(2, 12), "Q": 65537},
    # {"func": r4ntt, "N": pow(2, 13), "Q": 65537},
    # {"func": r4ntt, "N": pow(2, 14), "Q": 65537},
    # {"func": r4ntt, "N": pow(2, 15), "Q": 65537},

    # Radix-8 NTT
    {"func": r8ntt, "N": pow(2, 10), "Q": 65537},
    {"func": r8ntt, "N": pow(2, 11), "Q": 65537},
    {"func": r8ntt, "N": pow(2, 12), "Q": 65537},
    {"func": r8ntt, "N": pow(2, 13), "Q": 65537},
    {"func": r8ntt, "N": pow(2, 14), "Q": 65537},
    {"func": r8ntt, "N": pow(2, 15), "Q": 65537},
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
