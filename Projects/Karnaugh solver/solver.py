import numpy as np
from assgn import Assgn

# Ask exponent of 2
a = Assgn(['Quantes variables?'],rules=[False,False,True],vals=(range(1,51))).llista[0]

current = 2**a
# Array in which are all binary combinations of that exponent (2^x combinations, int(x) > 0)
bins = []
for x in range(current):
    bi = bin(x)[2:]
    while len(bi) < a:
        bi = "0" + bi
    bins.append(bi)
print(bins)
""" number = [[[0,1,2],[0,1,2],[0,1,2]],[[0,1,2],[0,1,2],[0,1,2]]]
print(np.array(number)) """