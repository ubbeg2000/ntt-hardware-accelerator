import os
import sys

sys.path.append(os.getcwd())

from random import randint
from scripts.my_ntt import ntt
from scripts.test_utils import arr_to_bin_str

from random import randint

N = 17
D = 16
Q = 65537

rand_arr = [randint(0, Q-1) for i in range(D)]

input_file = open("./tests/ntt_flat/testcase.txt", "w")
input_file.write(f"{arr_to_bin_str([1 for i in range(D)], length=N)}\n")
input_file.write(f"{arr_to_bin_str(rand_arr, length=N)}\n")
input_file.write(f"{arr_to_bin_str([i+1 for i in range(D)], length=N)}\n")
input_file.write(f"{arr_to_bin_str([D-i for i in range(D)], length=N)}\n")
input_file.close()

output_file = open("./tests/ntt_flat/expected.txt", "w")
output_file.write(f"{arr_to_bin_str(ntt([1 for i in range(D)], Q), length=N)}\n")
output_file.write(f"{arr_to_bin_str(ntt(rand_arr, Q), length=N)}\n")
output_file.write(f"{arr_to_bin_str(ntt([i+1 for i in range(D)], Q), length=N)}\n")
output_file.write(f"{arr_to_bin_str(ntt([D-i for i in range(D)], Q), length=N)}\n")
output_file.close()