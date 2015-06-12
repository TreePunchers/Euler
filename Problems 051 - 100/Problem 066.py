# TODO: A solution that takes less than about an hour to run

def is_perfect_square(D):
    sqrt = D ** 0.5
    return sqrt == int(sqrt)

def minimal_x(D):
    y = 1
    while True:
        x = ((D * y ** 2) + 1) ** 0.5
        if x == int(x):
            return x
        y += 1

current_max_x = 0
current_best_D = 0

for D in range(660, 1001):  # I start later on because I have already tested a lot
    print(D)
    if not is_perfect_square(D):
        min_x = minimal_x(D)
        if min_x > current_max_x:
            print(D, min_x)
            current_max_x = min_x
            current_best_D = D

print(current_best_D)
