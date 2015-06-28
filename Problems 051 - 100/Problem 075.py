# Slow, and using someone else's pyth triple gen

import numpy as np
from collections import Counter

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        print(prim)
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim

data = [sum(trip) for trip in gen_all_pyth_trips(1500000 // 2)]
print("Data done")
counts = Counter(data)
print("Counter made")

answer = 0

for key, count in counts.items():
    if count == 1 and key <= 1500000:
        answer += 1

print(answer)
