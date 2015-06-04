from custom.strings import is_palindrome

def bin_is_palindrome(n):
    return is_palindrome(str(bin(n))[2:])

palindromes = [x for x in range(1, 1000000) if is_palindrome(str(x))]
bin_also_palindromes = [x for x in palindromes if bin_is_palindrome(x)]

print(sum(bin_also_palindromes))