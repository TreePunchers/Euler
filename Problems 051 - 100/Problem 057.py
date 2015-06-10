numerator = 3
denominator = 2
count = 0

# Noticing patterns is a good thing

for x in range(2, 1000):
    numerator, denominator = numerator + denominator * 2, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print(count)
