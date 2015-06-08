from custom.math import primefactors

top = 1200000

for n in range(646, top):
    if len(set(primefactors(n))) == 4:
        if (len(set(primefactors(n + 1))) == 4 and
            len(set(primefactors(n + 2))) == 4 and
            len(set(primefactors(n + 3))) == 4):
            print(n)
            break
