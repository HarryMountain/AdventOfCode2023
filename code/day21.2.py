import numpy as np
NUMBER_OF_STEPS = 26501365

dots = []
hashes = []
grid = []
test = True
with open('../test_input_files/day21test.txt' if test else '../input_files/day21input.txt', 'r') as f:
    data = f.readlines()
    for x in range(len(data)):
        line = data[x].rstrip()
        grid.append(list(line))
        if 'S' in line:
            start = (x, line.index('S'))
        for thing in range(len(line)):
            if line[thing] == '.':
                dots.append((x, thing))
            elif line[thing] == '#':
                hashes.append((x, thing))

grid = np.array(grid)
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def flood_fill(position, directions, grid, ideal_location):
    positions = {position}
    steps = 0
    there = False
    while not there and steps < len(grid) * len(grid[0]):
        new_positions = set()
        for position in positions:
            for direction in directions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position] != '#':
                    new_positions.add(new_position)
                    if new_position == ideal_location:
                        there = True
        positions = new_positions
        steps += 1
    if steps < len(grid) * len(grid[0]):
        return steps
    else:
        return -1


places = 0
check_grid = np.zeros((len(grid), len(grid[0])), dtype=int)
grid[start] = '.'
for dot in dots:
    s = flood_fill(start, directions, grid, dot)
    check_grid[dot] = s
for h in hashes:
    check_grid[h] = -1
for y in range(len(check_grid)):
    for x in range(len(check_grid[0])):
        if -1 < check_grid[y, x] <= NUMBER_OF_STEPS and check_grid[y, x] % 2 == 0:
            places += 1
            grid[y, x] = 'O'
print(grid)
print(places)

