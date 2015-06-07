one = sum([x for x in range(1, 101)]) ** 2
two = sum([x ** 2 for x in range(1, 101)])

print(abs(one - two))
