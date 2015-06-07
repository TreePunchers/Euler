# Uses the concept of partitions

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
aim = 200
ways = [1] + [0] * aim

for coin in coin_values:
    for x in range(coin, aim + 1):
        ways[x] += ways[x - coin]

print(ways[aim])
