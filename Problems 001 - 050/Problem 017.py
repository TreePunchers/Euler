# TODO: Unsolved

#  - One Two Three Four Five Six Seven Eight Nine
length_units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]

# - <some teen> Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety
length_tens = [0, 0, 5, 6, 5, 5, 5, 7, 6, 6]

# [units] + Hundred
length_hundreds = [0, 10, 10, 12, 11, 11, 10, 12, 12, 11]

# Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen
length_teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

# Used for things with tens or units
length_and = 3

def valid_or_zero(collection, index):
    try:
        return collection[index]
    except IndexError:
        return 0

def length_number_as_word(n):
    from custom.math import digits

    result = 0
    digit_list = digits(n)

    units = valid_or_zero(digit_list, -1)
    tens = valid_or_zero(digit_list, -2)
    hundreds = valid_or_zero(digit_list, -3)

    if tens == 1:
        result += length_teens[units]
    else:
        result += length_tens[tens]
        result += length_units[units]

    if result > 0 and hundreds > 0:
        result += length_and

    result += length_hundreds[hundreds]

    return result

print(sum([length_number_as_word(x) for x in range(1, 1000)]) + 12)

# This is OFF BY 99 for some reason
