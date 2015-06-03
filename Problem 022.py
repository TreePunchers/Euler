with open("resources/p022_names.txt") as names:
    name_list = sorted(names.read().replace('"', "").split(","))

alphabet_values = {char: index + 1 for index, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

total_score = 0

for index, name in enumerate(name_list):
    total_score += sum(alphabet_values[char] for char in name) * (index + 1)

print(total_score)
