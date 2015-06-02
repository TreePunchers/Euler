from custom.strings import is_palindrome

answer = 0

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        prod = x * y
        if is_palindrome(str(prod)) and prod > answer:
            answer = prod

print(answer)