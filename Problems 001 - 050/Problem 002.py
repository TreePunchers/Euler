from custom.math import fib

answer = sum([x for x in list(fib(33))[2::3]])

print(answer)
