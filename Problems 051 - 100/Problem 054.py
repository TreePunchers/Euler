# TODO: Rewrite a spicy solution

from collections import Counter

hands = (line.split() for line in open('resources/p054_poker.txt'))

values = {symbol: value for value, symbol in enumerate('23456789TJQKA', start=2)}
straights = [(value, value - 1, value - 2, value - 3, value - 4) for value in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]


def hand_rank(hand):
    score = list(zip(*sorted(((v, values[k]) for k, v in Counter(x[0] for x in hand).items()), reverse=True)))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5
    if score[1] in straights:
        score[0] = 8 if score[0] == 5 else 4
    return score


print(sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))
