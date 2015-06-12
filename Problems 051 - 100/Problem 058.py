from custom.math import mr_is_prime

diagonals = [1]
primes_found = 0
current_number = 1
current_increment = 2
increment_change = 2
ring_count = 1

while True:
    ring_count += 1
    for x in range(4):
        current_number += current_increment
        diagonals.append(current_number)
        if mr_is_prime(current_number):
            primes_found += 1
    current_increment += increment_change
    if primes_found/len(diagonals) < 0.1:
        print(ring_count * 2 - 1)
        break
