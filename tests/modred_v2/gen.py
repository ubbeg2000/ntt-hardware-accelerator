import os
import sys

sys.path.append(os.getcwd())

from random import randint
from scripts.test_utils import int_to_bin_str

from random import randint

N = 17
D = 16
Q = 65537

a = randint(0, Q)
b = randint(0, Q)
tf = randint(0, Q)

def model(a, Q):
    return a % Q

input_file = open("./tests/modred_v2/testcase.txt", "w")
output_file = open("./tests/modred_v2/expected.txt", "w")

a = randint(0, pow(Q, 1))
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

a = randint(Q, 2*Q)
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

a = randint(2*Q, pow(Q, 2))
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

a = randint(-pow(Q, 1), 0)
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N, twos_complement=True)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

a = randint(-2*Q, -Q)
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N, twos_complement=True)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

a = -pow(Q, 2) + 1
input_file.write("{:s}\n".format(int_to_bin_str(a, length=2*N, twos_complement=True)))
output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

# a = randint(-pow(Q, 2), 0)
# input_file.write("{:s}\n".format(int_to_bin_str(a, twos_complement=True, length=2*N)))
# output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

# a = randint(-pow(Q, 2), 0)
# input_file.write("{:s}\n".format(int_to_bin_str(a, twos_complement=True, length=2*N)))
# output_file.write("{:s}\n".format(int_to_bin_str(model(a, Q), length=N)))

input_file.close()
output_file.close()