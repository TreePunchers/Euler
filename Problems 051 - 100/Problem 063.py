count = 0

for power in range(1, 30):
    n = 1
    while True:
        length = len(str(n ** power))
        if length == power:
            count += 1
        elif length > power:
            break
        n += 1

print(count)
