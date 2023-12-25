from copy import deepcopy
from enum import Enum
import numpy as np


class Direction(Enum):
    Up = 1
    Left = 2
    Down = 3
    Right = 4


directions = {Direction.Up: (-1, 0), Direction.Left: (0, -1), Direction.Down: (1, 0), Direction.Right: (0, 1)}
directions_to_slope = {'^': Direction.Up, '>': Direction.Right, '<': Direction.Left, 'v': Direction.Down}
grid = []
test = False
with open('../test_input_files/day23test.txt' if test else '../input_files/day23input.txt', 'r') as f:
    for line in f:
        grid.append(list(line.rstrip()))

grid = np.array(grid)
START = (0, 1)
FINISH = (len(grid) - 1, len(grid[0]) - 2)
paths = [[(1, 1), [(0, 1), (1, 1)]]]
finished = []
finished_lengths = []
while len(paths) > 0:
    new_paths = []
    for path in paths:
        for direction, value in directions.items():
            new_path = deepcopy(path)
            new_pos = (path[0][0] + value[0], path[0][1] + value[1])
            # if grid[new_pos] in directions_to_slope.keys():
            #     new_direction = directions_to_slope[grid[new_pos]]
            #     new_value = directions[new_direction]
            #     new_path[1].append(new_pos)
            #     new_pos = (new_pos[0] + new_value[0], new_pos[1] + new_value[1])
            if (grid[new_pos] == '.' or grid[new_pos] in directions_to_slope.keys()) and new_pos not in path[1]:
                new_path[0] = new_pos
                new_path[1].append(new_pos)
                if new_path[0] == FINISH:
                    finished.append(new_path[1])
                    finished_lengths.append(len(new_path[1]))
                else:
                    new_paths.append(new_path)
    paths = new_paths
    print(len(paths))
print(max(finished_lengths) - 1)
# for step in finished[finished_lengths.index(max(finished_lengths))]:
#     grid[step] = 'O'
# for l in grid:
#     print(''.join(l))
        