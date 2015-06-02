from custom.math import fib

answer = 0

for x in list(fib(33))[2::3]:
    answer += x

print(answer)
