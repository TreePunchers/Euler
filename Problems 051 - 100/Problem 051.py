from custom.math import primes

prime_list = list(primes(1000000))
prime_set = set(prime_list)

def eightreplacementprimes(digit_string, to_replace):
    count = 0
    for replacement_digit in '0123456789':
        number = digit_string.replace(to_replace, replacement_digit)
        if int(number) > 100000 and int(number) in prime_set:  # Stops stuff like 000857
            count += 1
    return count == 8


for p in prime_list:
    string_rep = str(p)
    if any(string_rep.count(char) >= 3 and
           string_rep[-1] != char and
           eightreplacementprimes(string_rep, char) for char in '012'):
        print(p)
        break
