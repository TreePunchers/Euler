# Surely could be optimised, but runs fast enough

from custom.math import eulers_totient

answer = 0

for i in range(2, 1000001):
    print(i)
    answer += eulers_totient(i)

print(int(answer))
