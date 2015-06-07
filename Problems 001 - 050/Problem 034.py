from custom.math import digits
from math import factorial

def is_curious(n):
    return sum([factorial(d) for d in digits(n)]) == n

print(sum([x for x in range(3, 100000) if is_curious(x)]))
