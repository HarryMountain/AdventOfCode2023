test = False
with open('../test_input_files/day6test.txt' if test else '../input_files/day6input.txt', 'r') as f:
    index = 0
    for line in f:
        if index == 0:
            times = int("".join([x for x in line.rstrip().split()[1:]]))
        else:
            dists = int("".join([x for x in line.rstrip().split()[1:]]))
        index += 1


total = 0
time = times
dist = dists
for i in range(time):
    if i * (time - i) > dist:
        total += 1
print(total)

