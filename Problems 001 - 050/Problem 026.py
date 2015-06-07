import fractions

def cycle_length(d):
    r_list = []
    qlist_len = 0
    remainder = 1

    while remainder:
        remainder = remainder % d
        if remainder in r_list:
            return qlist_len - r_list.index(remainder)
        r_list.append(remainder)
        remainder *= 10
        qlist_len += 1

    return 0

answer = 0

for x in range(1, 1000):
    if cycle_length(x) > answer:
        answer = x

print(answer)
