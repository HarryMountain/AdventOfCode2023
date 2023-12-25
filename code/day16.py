from enum import Enum
import numpy as np

grid = []
test = False
with open('../test_input_files/day16test.txt' if test else '../input_files/day16input.txt', 'r') as f:
    for line in f:
        grid.append(list(line.rstrip()))

grid = np.array(grid)


class Direction(Enum):
    Up = 1
    Left = 2
    Down = 3
    Right = 4


directions = {Direction.Up: (-1, 0), Direction.Left: (0, -1), Direction.Down: (1, 0), Direction.Right: (0, 1)}


CELL_DATA = {
    '|': {Direction.Right: [Direction.Up, Direction.Down], Direction.Left: [Direction.Up, Direction.Down], Direction.Down: [Direction.Down], Direction.Up: [Direction.Up]},
    '-': {Direction.Down: [Direction.Right, Direction.Left], Direction.Up: [Direction.Left, Direction.Right], Direction.Right: [Direction.Right], Direction.Left: [Direction.Left]},
    '/': {Direction.Up: [Direction.Right], Direction.Right: [Direction.Up], Direction.Down: [Direction.Left], Direction.Left: [Direction.Down]},
    '\\': {Direction.Up: [Direction.Left], Direction.Left: [Direction.Up], Direction.Right: [Direction.Down], Direction.Down: [Direction.Right]},
    '.': {Direction.Up: [Direction.Up], Direction.Down: [Direction.Down], Direction.Left: [Direction.Left], Direction.Right: [Direction.Right]},
}


scores = []
for row in range(-1, len(grid) + 1):
    for col in (range(0, len(grid[0])) if row == -1 or row == len(grid) else [-1, len(grid[0])]):
        count_grid = np.zeros((len(grid), len(grid[0])), dtype=int)
        d = None
        if row == -1:
            d = Direction.Down
        elif row == len(grid):
            d = Direction.Up
        elif col == -1:
            d = Direction.Right
        else:
            d = Direction.Left
        paths = [[[row, col], d, False]]
        seen = set()
        while len(paths) > 0:
            for path in paths:
                new_position = [path[0][x] + directions[path[1]][x] for x in range(2)]
                if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]):
                    count_grid[new_position[0], new_position[1]] += 1
                    new_directions = CELL_DATA[grid[new_position[0], new_position[1]]][path[1]]
                    for i in range(len(new_directions)):
                        if i == 0:
                            path[0] = new_position
                            path[1] = new_directions[i]
                        else:
                            paths.append([new_position, new_directions[i], False])
                else:
                    path[0] = new_position
                    path[2] = True
            paths = [x for x in paths if not x[2] and (x[0][0], x[0][1], x[1]) not in seen]
            for p in paths:
                seen.add((p[0][0], p[0][1], p[1]))
            # print(paths)
            # print(count_grid)
        result = np.count_nonzero(count_grid)
        scores.append(result)

print(max(scores))

