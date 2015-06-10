from custom.math import triangle_number, hexagonal_number, pentagonal_number

max_iterations = 100000

pents = set([pentagonal_number(x) for x in range(max_iterations)])
hexes = set([hexagonal_number(x) for x in range(max_iterations)])

n = 1
answer = 0

while True:
    tri = triangle_number(n)
    if tri > 40755:
        if tri in pents and tri in hexes:
            answer = tri
            break
    n += 1

print(answer)
