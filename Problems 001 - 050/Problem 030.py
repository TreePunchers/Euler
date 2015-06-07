from custom.math import digits

fifth_powers = [x ** 5 for x in range(0, 10)]
highest = 1000000  # Just a random guess, 6 digits should be enough

valid = [x for x in range(2, highest) if sum([fifth_powers[d] for d in digits(x)]) == x]

print(sum(valid))
