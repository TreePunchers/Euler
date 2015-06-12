# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def len_period_sqrt(n):
    a0 = int(n ** 0.5)
    if a0 ** 2 == n:
        return 0

    # Set up 0th terms
    m = 0
    d = 1
    a = a0

    len_period = 1

    while True:
        m = d * a - m
        d = (n - m ** 2) / d
        a = int((a0 + m) / d)
        if 2 * a0 == a:
            break
        len_period += 1

    return len_period

odd_period_count = 0

for x in range(1, 10001):
    if len_period_sqrt(x) % 2 == 1:
        odd_period_count += 1

print(odd_period_count)
