from fractions import Fraction

frac_set = set([])

for d in range(1000000, 999000, -1):
    print(d)
    for n in range(d):
        frac_set.add(Fraction(n, d))

new = sorted(list(frac_set))

print(new)
print(new[new.index(Fraction(3, 7)) - 1])
