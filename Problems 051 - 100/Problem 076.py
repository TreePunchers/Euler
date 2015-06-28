# Modified Problem 031

nums = [x for x in range(1, 101)]
aim = 100
ways = [1] + [0] * aim

for num in nums:
    for x in range(num, aim + 1):
        ways[x] += ways[x - num]

print(ways[aim] - 1)
