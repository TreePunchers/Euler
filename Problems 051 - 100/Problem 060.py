# TODO: Something other than brute force

from custom.math import is_prime, primes

prime_list = list(primes(10000))

def valid_pair(a, b):
    if is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))):
        return True
    return False

valid_fives = []

# Actually finds the answer faster than 97
for p1 in prime_list[:prime_list.index(97)]:
    print(p1)
    for p2 in prime_list[prime_list.index(p1):]:
        if valid_pair(p1, p2):
            for p3 in prime_list[prime_list.index(p2):]:
                if valid_pair(p1, p3) and valid_pair(p2, p3):
                    for p4 in prime_list[prime_list.index(p3):]:
                        if valid_pair(p1, p4) and valid_pair(p2, p4) and valid_pair(p3, p4):
                            for p5 in prime_list[prime_list.index(p4):]:
                                if valid_pair(p1, p5) and valid_pair(p2, p5) and valid_pair(p3, p5) and valid_pair(p4, p5):
                                    print(p1, p2, p3, p4, p5, "sum:", sum((p1, p2, p3, p4, p5)))
                                    valid_fives.append((p1, p2, p3, p4, p5))

print(min(sum(five) for five in valid_fives))
