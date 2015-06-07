from collections import Counter

def generatetriangleperimeters():
    for a in range(1, 500):
        for b in range(a, 500):
            c = (a ** 2 + b ** 2) ** 0.5
            if int(c) == c:
                yield sum((a, b, c))


count = Counter(generatetriangleperimeters())

print(int(count.most_common(1)[0][0]))
