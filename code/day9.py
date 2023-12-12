test = False
starts = []
with open('../test_input_files/day9test.txt' if test else '../input_files/day9input.txt', 'r') as f:
    for line in f:
        starts.append([int(x) for x in line.rstrip().split()])

total = 0

for start in starts:
    history = [start]
    new_history = []
    while not all([x == 0 for x in history[-1]]):
        for i in range(len(history[-1]) - 1):
            new_history.append(history[-1][i + 1] - history[-1][i])
        history.append(new_history)
        new_history = []
    print(history)

    thing_to_add = 0
    for x in range(len(history) - 1, -1, -1):
        thing_to_add = history[x][0] - thing_to_add
    total += thing_to_add

print(total)
