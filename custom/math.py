def seeded_series(seed_a, seed_b, iterations):
    a, b = seed_a, seed_b
    for x in range(iterations):
        yield a
        a, b = b, a + b


def fib(iterations):
    for n in seeded_series(1, 1, iterations):
        yield n


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


def digits(n):
    return [int(x) for x in str(n)]


def proper_divisors(n):
    yield 1

    largest = int(n ** 0.5)
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    for x in range(2, largest):
        if n % x == 0:
            yield x
            yield n / x


def is_abundant(n):
    if n < 12:
        return False
    return sum(proper_divisors(n)) > n


def quadratic(x, a, b, c):
    return (a * (x ** 2)) + (b * x) + c


def list_prod(values):
    from operator import mul
    from functools import reduce
    return reduce(mul, values, 1)


def tuple_to_int(t):
    try:
        return int(''.join(map(str, t)))
    except ValueError:
        return 0
