import os
import sys

sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/scripts")

from scripts.test_utils import arr_to_bin_str

D = 8
N = 17

tf_in = [0, 1, 2, 3, 4, 5, 6, 7]
tf_in_inv = [7, 6, 5, 4, 3, 2, 1, 0]

def model(stage, inv):
    if stage == 0 and inv == 0:
        return [1, 1, 1, 1, 1, 1, 1, 1]
    
    if stage == 1 and inv == 0:
        return [2, 2, 2, 2, 3, 3, 3, 3]
    
    if stage == 2 and inv == 0:
        return [4, 4, 5, 5, 6, 6, 7, 7]
    
    if stage == 0 and inv == 1:
        return [7, 7, 7, 7, 7, 7, 7, 7]
    
    if stage == 1 and inv == 1:
        return [6, 6, 6, 6, 5, 5, 5, 5]
    
    if stage == 2 and inv == 1:
        return [4, 4, 3, 3, 2, 2, 1, 1]
    
input_file = open("./tests/twiddle_factor_generator/testcase.txt", "w")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}000\n")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}001\n")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}010\n")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}100\n")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}101\n")
input_file.write(f"{arr_to_bin_str(tf_in, length=N)}{arr_to_bin_str(tf_in_inv, length=N)}110\n")
input_file.close()

output_file = open("./tests/twiddle_factor_generator/expected.txt", "w")
output_file.write(f"{arr_to_bin_str(model(0, 0), length=N)}\n")
output_file.write(f"{arr_to_bin_str(model(1, 0), length=N)}\n")
output_file.write(f"{arr_to_bin_str(model(2, 0), length=N)}\n")
output_file.write(f"{arr_to_bin_str(model(0, 1), length=N)}\n")
output_file.write(f"{arr_to_bin_str(model(1, 1), length=N)}\n")
output_file.write(f"{arr_to_bin_str(model(2, 1), length=N)}\n")
output_file.close()