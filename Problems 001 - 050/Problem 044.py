def penatagonalnumber(n):
    return n * (3 * n - 1) / 2


pents = set([penatagonalnumber(x) for x in range(1, 5000)])

for j in pents:
    for k in pents:
        if j < k:
            if j + k in pents and abs(j - k) in pents:
                print(abs(j - k))
                break  # Trust me, I'm not breaking early, it works, I think
