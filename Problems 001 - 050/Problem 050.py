from custom.math import primes

prime_list = list(p for p in primes(1000000))
prime_set = set(prime_list)

def highestconsecutive(start_index):
    total = 0
    current_index = start_index
    longest_chain_number = 0
    while total + prime_list[current_index] < 1000000:
        total += prime_list[current_index]
        if total in prime_set:
            longest_chain_number = total
            longest_index = current_index
        current_index += 1
    return longest_chain_number, longest_index - start_index

best_length = 0
answer = 0

for i in range(0, 21):
    x = highestconsecutive(i)
    if x[1] > best_length:
        best_length = x[1]
        answer = x[0]

print(answer)
