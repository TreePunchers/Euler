from custom.math import (triangle_number as tri, square_number as squ,
                        pentagonal_number as pen, hexagonal_number as hex,
                         heptagonal_number as hep, octagonal_number as oct)

def poly_n(n):
    return (3, tri(n)), (4, squ(n)), (5, pen(n)), (6, hex(n)), (7, hep(n)), (8, oct(n))


def next(types, value):
    if len(types) == 6 and value[0] // 100 == value[-1] % 100:  # First two 0 == last two 6
        print(value, sum(value))
    else:
        for t, n in dic.get((types[-1], value[-1]), []):
            if t not in types:
                next(types+[t], value+[n])

polys = []
start = 19  # 19 oct is first > 999 so start here
end = 141  # 141 tri is first > 9999 so cut off here

for n in range(start, end):
    for type, value in poly_n(n):
        if 1000 <= value <= 9999 and value % 100 > 9:
            polys.append((type, value))

dic = {}

for type_1, value_1 in polys:
    for type_2, value_2 in polys:
        if type_1 != type_2 and value_1 % 100 == value_2 // 100:
            dic[type_1, value_1] = dic.get((type_1, value_1), []) + [(type_2, value_2)]

for type, value in dic:
    next([type], [value])
