from custom.strings import is_palindrome

def reverse_int(n):
    return int(str(n)[::-1])


def is_lynchrel(n):
    attempts = 0
    current = n
    while attempts < 50:
        current += reverse_int(current)
        if is_palindrome(str(current)):
            return False
        attempts += 1
    return True

print(len([x for x in range(1, 10000) if is_lynchrel(x)]))
