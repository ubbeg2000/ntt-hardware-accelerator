from ntt_utils import clog2, gen_w_inv_table, int_to_bin
from helper import modinv
# from my_ntt import gen_w_table

D = 16
a = []
t = gen_w_inv_table(65537, D, 2)
mi = pow(D, -1, 65537)
print(t, mi)
i = 0
for r in t:
    for c in r:
        # print(c)
        a = [(c*mi)%65537] + a
for c in a:
    print(c, end=" ")
print("")
for c in a:
    print(int_to_bin(c, length=17), end="")

print(int_to_bin(0, length=17))

# c = 0
# for i in range(clog2(D)):
#     c = 0
#     for j in range(pow(2, i)):
#         for k in range(D//(2**i)):
#             print(pow(2, i)+j, D//(2**i)*j + k)
#             c = c + 1