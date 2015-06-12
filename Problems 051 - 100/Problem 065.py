# TODO: Understand properly

n0 = 1
n1 = 2

for i in range(2, 100):
    print(n1)
    n1, n0 = n0, n1 + n0 * (1 if i % 3 else 2 * i // 3)

print(sum(map(int, str(n0))))
