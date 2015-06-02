from custom.math import number_of_divisors

i = 1
number = 0

while number_of_divisors(number) < 500:
    print(i, number, number_of_divisors(number))
    number += i
    i += 1

print(number)
