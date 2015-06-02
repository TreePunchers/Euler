def sum_proper_divisors(n):
    return sum([x for x in range(1, n) if n % x == 0])

result = set([])

for a in range(1, 10000):
    a_sum_prop = sum_proper_divisors(a)
    if a_sum_prop != a:
        if sum_proper_divisors(a_sum_prop) == a:
            result.add(a)

print(result)
print(sum(result))
