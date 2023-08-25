
def arr_to_bin_str(arr, length=8):
    a_bin_str = ""
    for d in arr:
        a_bin_str = "{0:b}".format(d).rjust(length, "0") + a_bin_str
    return a_bin_str

def point_mult(a, b, Q):
    return [(a[i] * b[i])%Q for i in range(min(len(a), len(b)))]