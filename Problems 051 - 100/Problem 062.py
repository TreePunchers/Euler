from custom.math import digits
from collections import Counter

cubes = set([x ** 3 for x in range(10000)])

count = Counter()

for cube in cubes:
    count[str(sorted(digits(cube)))] += 1

current_min = 1e20

for test in count.most_common(2):
    for cube in cubes:
        if str(sorted(digits(cube))) == test[0]:
            if cube < current_min:
                current_min = cube

print(current_min)
