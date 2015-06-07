from custom.math import fib

stuff = list(fib(10000))

for x in stuff:
    if len(str(x)) == 1000:
        print(stuff.index(x) + 1)
        break
