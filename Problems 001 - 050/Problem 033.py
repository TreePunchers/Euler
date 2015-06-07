from custom.math import digits, list_prod
from fractions import Fraction

# Last term for first-second swap if true or second-first swap if false
fractions_to_test = [(x, y, digits(x)[0] == digits(y)[1]) for x in range(10, 100) for y in range(x, 100)
                     if x <= y and (digits(x)[0] == digits(y)[1]) != (digits(x)[1] == digits(y)[0])]

solutions = []

for fract in fractions_to_test:
    full_fraction = Fraction(fract[0], fract[1])
    try:
        if fract[2]:
            if Fraction(digits(fract[0])[1], digits(fract[1])[0]) == full_fraction:
                solutions.append(Fraction(fract[0], fract[1]))
        else:
            if Fraction(digits(fract[0])[0], digits(fract[1])[1]) == full_fraction:
                solutions.append(full_fraction)
    except ZeroDivisionError:
        pass

print(list_prod(solutions))
