
def arr_to_bin_str(arr, length=8):
    a_bin_str = ""
    for d in arr:
        a_bin_str = "{0:b}".format(d).rjust(length, "0") + a_bin_str
    return a_bin_str

def point_mult(a, b, Q):
    return [(a[i] * b[i])%Q for i in range(min(len(a), len(b)))]

def int_to_bin_str(num, length=8, twos_complement=False):
    if twos_complement:
        mask = (1<<length)-1
        num = abs(num)
        return "{:b}".format((num^mask)+1).rjust(length, "0")

    return "{:b}".format(num).rjust(length, "0")