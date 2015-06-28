# Partitions again, with a variable target

from custom.math import primes

prime_list = list(primes(80))

aim = 11

while True:
    ways = [1] + [0] * aim
    for p in prime_list:
        for i in range(p, aim + 1):
            ways[i] += ways[i - p]
    if ways[aim] > 5000:
        break
    aim += 1

print(aim)
