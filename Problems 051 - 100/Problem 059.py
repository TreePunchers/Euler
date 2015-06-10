with open('resources/p059_cipher.txt') as cipher:
    encrypted_message = eval('[' + cipher.read() + ']')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

codes = [(ord(a), ord(b), ord(c)) for a in alphabet for b in alphabet for c in alphabet]

for code in codes:
    code_index = 0
    temp_string = ''
    for n in encrypted_message:
        temp_string += chr(n ^ code[code_index % 3])
        code_index += 1
    if all([phrase in temp_string for phrase in (' the ', ' a ')]):
        print(temp_string)
        print(sum(ord(c) for c in temp_string))
        break
