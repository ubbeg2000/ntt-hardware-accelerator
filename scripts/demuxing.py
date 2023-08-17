from math import log2, ceil

D = 16

# for i in range(D):
#     for j in range(ceil(log2(D))):
#         a = (i//(2**(ceil(log2(D))-j-1)) % 2)
#         if a == 0:
#             print(f"{i} - {i+(2**(ceil(log2(D))-j-1))} ", end="")
#         else:
#             print(f"{i} - {i-(2**(ceil(log2(D))-j-1))} ", end="")

#     print("")

for i in range(D):
    for j in range(ceil(log2(D))):
        a = (i//(2**(ceil(log2(D))-j-1)))
        if a % 2 == 0:
            print("%2d - %2d  " % (i, 0), end="")
        else:
            a = (a + 1)//2-1
            # print(f"{i} - {a*D//(2<<j)%D}  ", end="")
            # print("%2d - %2d  " % (i, a*D//2-j*D//2), end="")
            print("%2d - %2d  " % (i, a + 2**j), end="")
            # print("%2d - %2d  " % (i, a), end="")

    print("")

# for i in range(D):
#     for j in range(ceil(log2(D))):
#         a = (i//(2**(ceil(log2(D))-j)))
#         # a = (a + 1)//2-1
#         print("%2d - %2d  " % (i, a + 2**j), end="")

#     print("")
