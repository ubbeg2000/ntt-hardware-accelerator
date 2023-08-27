import os
import sys

sys.path.append(os.getcwd())

from random import randint
from scripts.my_ntt import ntt, intt
from scripts.test_utils import point_mult, arr_to_bin_str

N = 17
D = 8
Q = 65537

ones_arr = [1 for i in range(D)]
num_arr = [i+1 for i in range(D)]
rand_arr_1 = [randint(0, 8) for i in range(D)]
rand_arr_2 = [randint(0, 8) for i in range(D)]

ones_arr_n = ntt(ones_arr, Q)
num_arr_n = ntt(num_arr, Q)
rand_arr_1_n = ntt(rand_arr_1, Q)
rand_arr_2_n = ntt(rand_arr_2, Q)

case_1 = intt(point_mult(ones_arr_n, ones_arr_n), Q)
case_2 = intt(point_mult(num_arr_n, num_arr_n), Q)
case_3 = intt(point_mult(rand_arr_1_n, rand_arr_2_n), Q)

input_file = open("./tests/karatsuba_negacyclic_conv/testcase.txt", "w")
input_file.write(f"{arr_to_bin_str(ones_arr, length=N)}{arr_to_bin_str(ones_arr, length=N)}\n")
input_file.write(f"{arr_to_bin_str(num_arr, length=N)}{arr_to_bin_str(num_arr, length=N)}\n")
input_file.write(f"{arr_to_bin_str(rand_arr_1, length=N)}{arr_to_bin_str(rand_arr_2, length=N)}\n")
input_file.close()

output_file = open("./tests/karatsuba_negacyclic_conv/expected.txt", "w")
output_file.write(f"{arr_to_bin_str(case_1, length=N)}\n")
output_file.write(f"{arr_to_bin_str(case_2, length=N)}\n")
output_file.write(f"{arr_to_bin_str(case_3, length=N)}\n")
output_file.close()