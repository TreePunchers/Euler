def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            if a + b + c == 1000:
                if is_pythagorean_triplet(a, b, c):
                    print(a, b, c)
