def sum_diagonal_numbers(n):
    answer = 1
    current_number = 1
    current_increment = 2
    increment_change = 2

    rings = int(n / 2)

    for r in range(rings):
        for x in range(4):
            current_number += current_increment
            answer += current_number
        current_increment += increment_change

    return answer

print(sum_diagonal_numbers(1001))
