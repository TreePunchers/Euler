from custom.math import trianglenumber, hexagonalnumber, pentagonalnumber

max_iterations = 100000

pents = set([pentagonalnumber(x) for x in range(max_iterations)])
hexes = set([hexagonalnumber(x) for x in range(max_iterations)])

n = 1
answer = 0

while True:
    tri = trianglenumber(n)
    if tri > 40755:
        if tri in pents and tri in hexes:
            answer = tri
            break
    n += 1

print(answer)
