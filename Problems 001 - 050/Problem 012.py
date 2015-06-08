from custom.math import numberofdivisors

i = 1
number = 0

while numberofdivisors(number) < 500:
    print(i, number, numberofdivisors(number))
    number += i
    i += 1

print(number)
