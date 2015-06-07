from custom.math import primes

def rotations(string):
    answer = []
    rotation = string
    while rotation not in answer:
        answer.append(rotation)
        rotation = rotation[1:] + rotation[0]
    return answer

def circular_primes(max):
    prime_list = list(primes(max))
    circular_prime_list = set([])

    for p in prime_list:
        # If all permutations of the prime are also prime, then add them all
        string_rep = str(p)
        if all(c in "1379" for c in string_rep) or p < 10:
            if p not in circular_prime_list:
                perms = [int(perm) for perm in rotations(string_rep)]
                circular = all(x in prime_list for x in perms)
                if circular:
                    for x in perms:
                        circular_prime_list.add(x)

    return circular_prime_list

print(len(circular_primes(1000000)))
