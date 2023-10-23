import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/scripts")

from random import randint
from scripts.my_ntt import ntt, intt
from scripts.test_utils import arr_to_bin_str

from math import ceil, log2
from random import randint

N = 17
D = 32
Q = 65537

rand_arr = [randint(0, Q-1) for i in range(D)]

input_file = open("./tests/radix_4_ntt_intt_pe_cell/testcase.txt", "w")
input_file.write(f"{arr_to_bin_str([1 for i in range(D)], length=N)}0\n")
input_file.write(f"{arr_to_bin_str(ntt([1 for i in range(D)], Q, print_step=True), length=N)}0\n")
# input_file.write(f"{arr_to_bin_str([i+1 for i in range(D)], length=N)}0\n")
# input_file.write(f"{arr_to_bin_str([D-i for i in range(D)], length=N)}0\n")
input_file.close()

output_file = open("./tests/radix_4_ntt_intt_pe_cell/expected.txt", "w")
output_file.write(f"{arr_to_bin_str(intt(ntt([1 for i in range(D)], Q), Q), length=N)}\n")
output_file.write(f"{arr_to_bin_str([1 for i in range(D)], length=N)}\n")
# output_file.write(f"{arr_to_bin_str(ntt([i+1 for i in range(D)], Q), length=N)}\n")
# output_file.write(f"{arr_to_bin_str(ntt([D-i for i in range(D)], Q), length=N)}\n")
output_file.close()

print(ntt([i for i in range(D)], 65537, print_step=True))