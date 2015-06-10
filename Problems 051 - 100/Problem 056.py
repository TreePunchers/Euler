from custom.math import digits

highest_sum = 0

for a in range(100):
    for b in range(100):
        length = sum(digits(a ** b))
        if length > highest_sum:
            highest_sum = length

print(highest_sum)
