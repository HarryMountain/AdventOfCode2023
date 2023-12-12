from copy import deepcopy

data = []

test = False
new_data = []
added = []
conversion = []
with open('../test_input_files/day5test.txt' if test else '../input_files/day5input.txt', 'r') as f:
    finding = 'soil'
    for line in f:
        line = line.rstrip().split()
        if len(line) > 1:
            if line[0] == "seeds:":
                for i in range(1, len(line), 2):
                    data.append([int(line[i]), int(line[i + 1]) + int(line[i])])
            elif line[1] == 'map:':
                if len(conversion) > 0:
                    conversion.sort(key=lambda c: c[1])
                    ranges_to_add = []
                    for x in range(len(conversion)):
                        conv = conversion[x]
                        if x == len(conversion) - 1:
                            ranges_to_add.append([conv[1] + conv[2], conv[1] + conv[2], max(max([y[1] for y in data]) - (conv[1] + conv[2]), 0)])
                        elif x == 0:
                            ranges_to_add.append([0, 0, conv[1]])
                        elif (conv[1] + conv[2]) < conversion[x+1][1]:
                            ranges_to_add.append([conv[1] + conv[2], conv[1] + conv[2], conversion[x + 1][1] - (conv[1] + conv[2])])
                    conversion.extend(ranges_to_add)
                    conversion.sort(key=lambda c: c[1])
                    for d in data:
                        for c in conversion:
                            if c[1] > d[1]:
                                break
                            elif c[1] <= d[0] < c[1] + c[2]:
                                if c[1] + c[2] > d[1]:
                                    new_data.append([(d[0] - c[1]) + c[0], (d[1] - c[1]) + c[0]])
                                else:
                                    new_data.append([(d[0] - c[1]) + c[0], (c[2] + c[0])])
                                    d[0] = c[1] + c[2]
                    data = deepcopy(new_data)
                    new_data = []
                    added = []
                    conversion = []
            else:
                dest = int(line[0])
                sour = int(line[1])
                rang = int(line[2])
                conversion.append([dest, sour, rang])

print(min(data))
