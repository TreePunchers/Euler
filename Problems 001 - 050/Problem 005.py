from custom.math import lcm
from functools import reduce

test = list(range(1, 20))

print(reduce(lcm, test))
