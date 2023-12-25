score = 0
test = False
cards = []
with open('../test_input_files/day4test.txt' if test else '../input_files/day4input.txt', 'r') as f:
    for line in f:
        data = line.split(":")[1].split('|')
        winning = data[0].split()
        have = data[1].split()
        cards.append([winning, have, 1])

for x in range(len(cards)):
    card = cards[x]
    winning_have = set(card[0]).intersection(set(card[1]))
    score += card[2]
    for i in range(x + 1, min(x + 1 + len(winning_have), len(cards))):
        cards[i][2] += card[2]
print(score)
