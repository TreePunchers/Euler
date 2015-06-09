from custom.math import primes, tupletoint
from itertools import permutations

prime_set = set(primes(10000))
diff = 3330
two_diff = 2 * diff

for p in prime_set:
    p_diff = p + diff
    p_two_diff = p + two_diff
    if p_diff in prime_set and p_two_diff in prime_set:
        perms = [tupletoint(x) for x in permutations(str(p))]
        if p_two_diff in perms and p_two_diff in perms:
            print(sorted([p, p_diff, p_two_diff]))
            break
