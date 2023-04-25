import math
for i in range(3, 17):
    for j in range(1, i):
        a = i
        b = j
        print("{} m {} = {}".format(a, b, math.comb(a, b)), end="\t")
    print()

