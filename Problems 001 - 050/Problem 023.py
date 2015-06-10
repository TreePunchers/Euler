from custom.math import isa_bundant

abundant_numbers = set([x for x in range(1, 28123) if isa_bundant(x)])
def can_be_sum_of_two_abundant(n):
    for x in abundant_numbers:
        if x > n:
            return False
        if n - x in abundant_numbers:
            return True
    return False

end = 20161

valid = [x for x in range(1, end + 1) if not can_be_sum_of_two_abundant(x)]

print(sum(valid))
