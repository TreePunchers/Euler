def champernowneconstant(min_dp):
    number = 1
    result = ''
    while len(result) < min_dp:
        result += str(number)
        number += 1
    return result

champ = champernowneconstant(1000000)
print(int(champ[0]) *
      int(champ[9]) *
      int(champ[99]) *
      int(champ[999]) *
      int(champ[9999]) *
      int(champ[99999]) *
      int(champ[999999]))
