def chain_operator(current):
    if current % 2 == 0:
        return current / 2
    else:
        return current * 3 + 1


def chain_gen(start):
    current = start
    while current != 1:
        yield current
        current = chain_operator(current)
    yield 1

answer = 0
longest_length = 0

for x in range(1, 1000000):
    length = len(list(chain_gen(x)))
    print(x, length)
    if length > longest_length:
        longest_length = length
        answer = x

print(answer)
