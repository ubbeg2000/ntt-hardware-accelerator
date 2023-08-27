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

def model(a, b, tf, sub, inv):
    if sub == 0 and inv == 0:
        return (a + b * tf) % Q
    
    if sub == 1 and inv == 0:
        return (a - b * tf) % Q
    
    if sub == 0 and inv == 1:
        return (a * tf + b * tf) % Q
    
    if sub == 1 and inv == 1:
        return (a * tf - b * tf) % Q

input_file = open("./tests/ntt_intt_pe_cell/testcase.txt", "w")
output_file = open("./tests/ntt_intt_pe_cell/expected.txt", "w")

for i in range(3):
    for sub in range(2):
        for inv in range(2):
            input_file.write("{:s}{:s}{:s}{:s}{:s}\n".format(
                int_to_bin_str(a, length=N),
                int_to_bin_str(b, length=N),
                int_to_bin_str(tf, length=N),
                int_to_bin_str(sub, length=1),
                int_to_bin_str(inv, length=1)
            ))

            output_file.write("{:s}\n".format(
                int_to_bin_str(model(a, b, tf, sub, inv), length=N)
            ))

            print(model(a, b, tf, sub, inv))


input_file.close()
output_file.close()