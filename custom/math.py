def seeded_series(seed_a, seed_b, iterations):
    a, b = seed_a, seed_b
    for x in range(iterations):
        a, b = b, a + b
        yield a


def fib(iterations):
    return seeded_series(0, 1, iterations)


def primes(max):
    D = {}
    q = 2

    while q < max or max == -1:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def lcm(x, y):
    from fractions import gcd
    return (x * y) / gcd(x, y)


def triangle_number(n):
    return int((n * (n + 1)) / 2)


def number_of_divisors(n):
    nod = 0
    sqrt = int(n ** 0.5)

    for x in range(1, sqrt + 1):
        if n % x == 0:
            nod += 2

    if sqrt * sqrt == n:
        nod -= 1

    return nod


def combinations(n, k):
    from math import factorial

    return factorial(n) / (factorial(k) * factorial(n - k))


def permutations(n, k):
    from math import factorial

    return factorial(n) / factorial(n - k)