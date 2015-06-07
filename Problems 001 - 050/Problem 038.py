largest = 0

for i in range(9000, 10000):
    temp = str(i) + str(i * 2)  # must have max multiplier of 2
    if '0' not in temp:
        if len(set(temp)) == 9:
            if int(temp) > largest:
                largest = int(temp)

print(largest)
