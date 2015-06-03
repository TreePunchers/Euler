from custom.math import quadratic, primes
primes_set = set(primes(2 ** 16))

longest_n = 0
best_pair = (0, 0)
maximum = 1000

for a in range(-maximum, maximum + 1):
    for b in range(-maximum, maximum + 1):
        n = 0
        while True:
            if quadratic(n, 1, a, b) in primes_set:
                n += 1
            else:
                break
        if n > longest_n:
            longest_n = n
            best_pair = (a, b)

print(best_pair[0] * best_pair[1])
