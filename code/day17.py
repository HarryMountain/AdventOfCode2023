from enum import Enum
import numpy as np


class Direction(Enum):
    Up = 1
    Left = 2
    Down = 3
    Right = 4


directions = {Direction.Up: (-1, 0), Direction.Left: (0, -1), Direction.Down: (1, 0), Direction.Right: (0, 1)}

grid = []
test = False
with open('../test_input_files/day17test.txt' if test else '../input_files/day17input.txt', 'r') as f:
    for line in f:
        grid.append([int(x) for x in line.rstrip()])

scores = []
finished = []
grid = np.array(grid)
FINISH = (len(grid) - 1, len(grid[0]) - 1)
paths = [[(0, 0), Direction.Right, 0, 0, [(0, 0)]]]
seen = {(0, 0, Direction.Right, 0): 0}
while len(paths) > 0:
    new_paths = []
    for path in paths:
        for direction, value in directions.items():
            new_pos = (path[0][0] + value[0], path[0][1] + value[1])
            if (direction.value + 1) % 4 != path[1].value - 1 and 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(
                    grid[0]):
                if path[1] == direction:
                    if path[2] < 3:
                        if new_pos == FINISH:
                            scores.append(path[3] + grid[new_pos])
                            finished.append(path[4])
                        else:
                            new_paths.append(
                                [new_pos, direction, path[2] + 1, path[3] + grid[new_pos], path[4] + [new_pos]])

                else:
                    if new_pos == FINISH:
                        scores.append(path[3] + grid[new_pos])
                        finished.append(path[4])
                    else:
                        new_paths.append([new_pos, direction, 1, path[3] + grid[new_pos], path[4] + [new_pos]])
    paths = []
    for np in new_paths:
        best_current_score = seen.get((np[0][0], np[0][1], np[1], np[2]), -1)
        if np[3] < best_current_score or best_current_score == -1:
            seen[(np[0][0], np[0][1], np[1], np[2])] = np[3]
            paths.append(np)
    print(len(paths))
print(scores)
print(min(scores))
for move in finished[scores.index(min(scores))]:
    grid[move] = 0
print(grid)
