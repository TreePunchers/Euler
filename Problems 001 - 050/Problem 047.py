from custom.math import prime_factors

top = 1200000

for n in range(646, top):
    if len(set(prime_factors(n))) == 4:
        if (len(set(prime_factors(n + 1))) == 4 and
            len(set(prime_factors(n + 2))) == 4 and
            len(set(prime_factors(n + 3))) == 4):
            print(n)
            break
