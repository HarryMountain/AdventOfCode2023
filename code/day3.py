import math

grid = []
directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]

test = False
with open('../test_input_files/day3test.txt' if test else '../input_files/day3input.txt', 'r') as f:
    for line in f:
        grid.append(line)

gears = {}
total = 0
for l in range(len(grid)):
    number = False
    x = 0
    lin = grid[l]
    num = ""
    while x < len(lin):
        if lin[x].isdigit():
            number = True
            num += lin[x]
        elif number:
            is_part = False
            gears_added = []
            for xx in range(x - len(num), x):
                for direction in directions:
                    new_pos = min(len(grid) - 1, max(0, l + direction[1])), min(len(grid[l]), max(0, xx + direction[0]))
                    if not(new_pos[0] == l and x-len(num) <= new_pos[1] < x):
                        char = grid[new_pos[0]][new_pos[1]]
                        if not(48 <= ord(char) <= 57 or ord(char) == 46 or char == "\n"):
                            is_part = True
                            if char == "*" and (new_pos[0], new_pos[1]) not in gears_added:
                                gears[(new_pos[0], new_pos[1])] = gears.get((new_pos[0], new_pos[1]), []) + [(int(num))]
                                gears_added.append((new_pos[0], new_pos[1]))
            if is_part:
                total += int(num)
            if not is_part:
                print(num)
            number = False
            num = ""
        x += 1
print(total)

second_total = 0
for key,value in gears.items():
    if len(value) == 2:
        second_total += math.prod(value)
print(second_total)
