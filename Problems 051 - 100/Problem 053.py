from custom.math import combinations

answer = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        if combinations(n, r) > 1000000:
            answer += 1

print(answer)
