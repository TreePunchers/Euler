from custom.math import primes

top = 120000

prime_set = set(primes(top))
square_numbers = set([x ** 2 for x in range(1, int(top ** 0.5 + 1))])
odd_composite = [x for x in range(3, top, 2) if x not in prime_set]

for comp in odd_composite:
    if not any((2 * square + prime == comp) for square in square_numbers for prime in prime_set):
        print(comp)
        exit()
