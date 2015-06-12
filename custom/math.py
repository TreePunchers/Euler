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
    return (n * (n + 1)) / 2


def square_number(n):
    return n * n


def pentagonal_number(n):
    return n * (3 * n - 1) / 2


def hexagonal_number(n):
    return n * (2 * n - 1)


def heptagonal_number(n):
    return n * (5 * n - 3) / 2


def octagonal_number(n):
    return n * (3 * n - 2)


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


def isa_bundant(n):
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


def prime_factors(n):
    primfac = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def mr_is_prime(n):
    """
    Efficiently checks for primality of high numbers using miller rabin algorithm
    :param n: Number to check for primality
    :return: Bool
    """
    import random

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def is_prime(n):
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
    return True
