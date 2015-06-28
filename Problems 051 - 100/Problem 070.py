from custom.math import eulers_totient
from collections import defaultdict

best_n = 0
min_ratio = 100

def same_permutations(a, b):
    d = defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())

for n in range(6636841, int(1e7), 2):  # It must be an odd number (from previous tests)
    eul = int(eulers_totient(n))
    meep = str(n)
    merp = str(eul)
    if len(meep) == len(merp):
        if sorted(meep) == sorted(merp):
            ratio = n / eul
            if n / eul < min_ratio:
                min_ratio = ratio
                best_n = n
                print("NEW:", n)

print("Final: ", best_n)
# Should find no more after 8319823
