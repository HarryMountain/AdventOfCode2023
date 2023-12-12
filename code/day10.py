from enum import Enum

import numpy as np

grid = []


def flood_fill(position, directions, grid, path):
    new = True
    good = True
    positions = [position]
    while new:
        new = False
        for position in positions:
            for direction in directions:
                new_position = (position[0] + direction[1], position[1] + direction[0])
                if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]):
                    if new_position not in positions and new_position not in path and grid[
                        new_position[0], new_position[1]] != '#':
                        positions.append(new_position)
                        new = True
                    elif grid[new_position[0], new_position[1]] == '#':
                        good = False
    if not good:
        for p in positions:
            grid[p[0], p[1]] = '#'


class Direction(Enum):
    Up = 0
    Left = 1
    Down = 2
    Right = 3


CELL_DATA = {
    'J': {Direction.Right: Direction.Up, Direction.Down: Direction.Left},
    'L': {Direction.Down: Direction.Right, Direction.Left: Direction.Up},
    '7': {Direction.Up: Direction.Left, Direction.Right: Direction.Down},
    'F': {Direction.Up: Direction.Right, Direction.Left: Direction.Down},
    '|': {Direction.Up: Direction.Up, Direction.Down: Direction.Down},
    '-': {Direction.Left: Direction.Left, Direction.Right: Direction.Right}
}
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

direction = []
test = False
with open('../test_input_files/day10test.txt' if test else '../input_files/day10input.txt', 'r') as f:
    for line in f:
        grid.append(list(line.rstrip()))

grid = np.array(grid)
s_location = np.where(grid == 'S')
location = [s_location[0][0], s_location[1][0]]
direction = Direction.Down
print(grid[location[0] - 1: location[0] + 2, location[1] - 1: location[1] + 2])
path = [location]
done = False
t = 0
while not done:
    d = direction.value
    di = directions[d]

    new_pos = (location[0] + di[1], location[1] + di[0])
    if grid[new_pos[0], new_pos[1]] == 'S':
        done = True

    dir_to_check = (d + 1) % 4
    check_y = new_pos[0] + directions[dir_to_check][1]
    check_x = new_pos[1] + directions[dir_to_check][0]
    if 0 <= check_y < len(grid) and 0 <= check_x < len(grid[0]):
        if grid[check_y, check_x] == '.':
            grid[check_y, check_x] = '#'

    if grid[new_pos[0], new_pos[1]] != 'S':
        direction = CELL_DATA[grid[new_pos[0], new_pos[1]]][direction]

    d_temp = direction.value
    location = new_pos
    dir_to_check = (d_temp + 1) % 4
    check_y = location[0] + directions[dir_to_check][1]
    check_x = location[1] + directions[dir_to_check][0]
    if 0 <= check_y < len(grid) and 0 <= check_x < len(grid[0]):
        if grid[check_y, check_x] == '.':
            grid[check_y, check_x] = '#'

    path.append(location)
    t += 1

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if (y, x) not in path and grid[y, x] != '#':
            grid[y, x] = '.'

for l in grid:
    print(*l, sep='')
print("\n")

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y, x] == '#':
            flood_fill((y, x), directions, grid, path)
for l in grid:
    print(*l, sep='')
print(np.sum(grid == '.'))
