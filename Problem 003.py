from custom.math import primes

number = 600851475143

primes_lower = list(primes(number ** 0.5))[::-1]

for n in primes_lower:
    if number % n == 0:
        print(n)
        break
