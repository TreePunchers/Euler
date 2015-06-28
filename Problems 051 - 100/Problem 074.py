from math import factorial

def next_fact(n):
    return sum([factorial(int(c)) for c in str(n)])

prev_results = {}

def len_fact_chain(n):
    result = set([])
    current = n
    final_length = 0

    while True:
        result.add(current)
        current = next_fact(current)
        if current in prev_results.keys():
            final_length = len(result) + prev_results[current]
            break
        if current in result:
            final_length = len(result)
            break

    prev_results[n] = final_length
    return final_length

answer = 0

for n in range(1000000):
    if len_fact_chain(n) == 60:
        print(n)
        answer += 1

print(answer)
