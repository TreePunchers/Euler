# Multiply as many consecutive primes as possible without exceeding 1 million
from custom.math import primes

best = 1

for p in primes(100):
    if best * p > 1000000:
        print(best)
        break
    best *= p
