alphabet_values = {char: index + 1 for index, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def trianglenumbers(iterations):
    number = 1
    step = 2
    for i in range(iterations):
        yield number
        number += step
        step += 1


def valueofword(string):
    return sum(alphabet_values[char] for char in string)

tris = list(trianglenumbers(100))

with open('resources/p042_words.txt') as words:
    word_list = eval('[' + words.read() + ']')

count = 0

for word in word_list:
    if valueofword(word) in tris:
        count += 1

print(count)
