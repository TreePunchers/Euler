from custom.math import primes

top = 1000000
possible_primes_list = list([x for x in primes(top) if not any(c in "0468" for c in str(x))])

def prime_truncatable(n):
    string_rep = str(n)
    length = len(str(string_rep))

    if all(int(string_rep[x:]) in possible_primes_list for x in range(length)):
        if all(int(string_rep[:x]) in possible_primes_list for x in range(1, length)):
            return True

    return False

print(sum([x for x in possible_primes_list if prime_truncatable(x) and x > 10]))
