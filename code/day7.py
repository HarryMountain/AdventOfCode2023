from collections import Counter
from copy import deepcopy

order = "AKQT987654321J"

hands = []
test = False
with open('../test_input_files/day7test.txt' if test else '../input_files/day7input.txt', 'r') as f:
    for line in f:   
        hand, bid = line.split()
        hands.append([hand, bid])

new_hands = [[], [], [], [], [], [], []]
types = 0
for x in range(len(hands)):
    hand = hands[x][0]
    bid = hands[x][1]
    card_freq_old = Counter(hand)
    card_freq = deepcopy(card_freq_old)
    if 'J' in card_freq.keys():
        card_freq.pop('J')
    if card_freq_old['J'] == 5:
        card_freq['A'] = 5
    else:
        card_freq[max(card_freq, key=lambda key: card_freq[key])] += card_freq_old['J']
    types = 0
    highest_number = max(card_freq.values())
    if highest_number == 5:
        types = 0
    elif highest_number == 4:
        types = 1
    elif highest_number == 3:
        if 2 in card_freq.values():
            types = 2
        else:
            types = 3
    else:
        freq_vals = Counter(card_freq.values())
        if freq_vals[2] == 2:
            types = 4
        elif freq_vals[2] == 1:
            types = 5
        else:
            types = 6

    position_to_insert = 0
    for h in range(len(new_hands[types])):
        for index in range(7):
            if order.index(new_hands[types][h][0][index]) < order.index(hand[index]):
                position_to_insert = h + 1
                break
            elif order.index(new_hands[types][h][0][index]) > order.index(hand[index]):
                break
    new_hands[types].insert(position_to_insert, [hand, bid])

value = len(hands)
total = 0

for l in range(7):
    for b in new_hands[l]:
        total += value * int(b[1])
        value -= 1

print(total)
