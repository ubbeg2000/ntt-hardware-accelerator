from poly import *
from poly import Poly

a = Poly(2, 2)
b = Poly(2, 2)

a.F = [1, 2, 1]
b.F = [2, 1, 2]

print(a * b)
