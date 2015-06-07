from itertools import permutations
from custom.math import tuple_to_int

base = [x for x in range(10)]

total = 0

for p in permutations(base):
    if (int(''.join(str(x) for x in p[1:4])) % 2 == 0 and
        int(''.join(str(x) for x in p[2:5])) % 3 == 0 and
        int(''.join(str(x) for x in p[3:6])) % 5 == 0 and
        int(''.join(str(x) for x in p[4:7])) % 7 == 0 and
        int(''.join(str(x) for x in p[5:8])) % 11 == 0 and
        int(''.join(str(x) for x in p[6:9])) % 13 == 0 and
        int(''.join(str(x) for x in p[7:10])) % 17 == 0):
        total += tuple_to_int(p)

print(total)
