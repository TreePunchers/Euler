# Takes ages but gets there eventually

from fractions import Fraction

frac_set = set()

for d in range(2, 12001):
    print(d)
    for n in range(int(d / 3) + 1, int(d / 2 + 0.5)):
        frac_set.add(Fraction(n, d))

print(len(frac_set))
