from custom.math import combinations, permutations

def num_paths(x):
    return combinations(x * 2, x)

print(num_paths(20))
