with open('resources/p067_triangle.txt') as triangle:
    pyramid = [[int(x) for x in line.rstrip('\n').split(' ')] for line in triangle]

def recursive_sum_at_row(row_data, row_number):
    for i in range(len(row_data[row_number])):
        row_data[row_number][i] += max(row_data[row_number + 1][i], row_data[row_number + 1][i + 1])
    if len(row_data[row_number]) == 1:
        return row_data[row_number][0]
    else:
        return recursive_sum_at_row(row_data, row_number - 1)

result = recursive_sum_at_row(pyramid, len(pyramid) - 2)

print(result)
