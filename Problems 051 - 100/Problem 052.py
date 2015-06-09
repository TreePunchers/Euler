def sixmultssamedigits(n):
    string_rep = sorted(str(n))
    return all(sorted(str(n * mult)) == string_rep for mult in range(2, 7))

num = 1

while True:
    if sixmultssamedigits(num):
        print(num)
        break
    else:
        num += 1

# This answer should be obvious for anyone who has ever typed 1/7
