from custom.math import primes, digits

def ispandigital(n):
    n_digits = digits(n)
    length = len(n_digits)
    return set(n_digits) == set([x for x in range(1, length + 1)])

# Every 9 digit and 8 digit pandigital number is divisible by 3, because their digits sum a multiple of 3
prime_list = list(primes(7654321))

print(prime_list[-1])
