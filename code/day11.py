from copy import deepcopy

import numpy as np
grid = []
test = False
with open('../test_input_files/day11test.txt' if test else '../input_files/day11input.txt', 'r') as f:
    for line in f:
        grid.append([int(x) for x in line.rstrip().replace('.', '0').replace('#', '1')])

SPACE_EXPANSION = 999999

grid = np.array(grid)
new_grid = deepcopy(grid)
rows_added = 0
buffer_rows = []
buffer_cols = []
for y in range(len(grid)):
    if sum(grid[y]) == 0:
        new_grid = np.insert(new_grid, y + rows_added, 0, axis=0)
        rows_added += 1
        buffer_rows.append(y)
cols_added = 0
for x in range(len(grid[0])):
    if sum(grid.T[x]) == 0:
        new_grid = np.insert(new_grid, x + cols_added, 0, axis=1)
        cols_added += 1
        buffer_cols.append(x)

galaxies = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y, x] == 1:
            galaxies.append((y + len([yy for yy in buffer_rows if yy < y]) * SPACE_EXPANSION, x + len([xx for xx in buffer_cols if xx < x]) * SPACE_EXPANSION))
total = 0
for galaxy in galaxies:
    for galaxy2 in galaxies:
        if galaxy != galaxy2:
            total += abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
print(total // 2)


        