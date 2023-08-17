from math import log2, ceil

D = 8
N = 9


def reverse_bit_order(num, D=D):
    # Mengubah angka menjadi representasi biner dalam bentuk string
    binary_representation = format(num, 'b').rjust(ceil(log2(D)), "0")
    # Membalik urutan string biner
    reversed_binary = binary_representation[::-1]
    # print(binary_representation, reversed_binary)
    # Mengubah kembali string biner menjadi angka bulat
    reversed_num = int(reversed_binary, 2)

    return reversed_num


for i in range(D):
    j = reverse_bit_order(i)
    print(f"assign b[{N*(j+1)-1}:{N*j}] = a[{N*(i+1)-1}:{N*i}];")
