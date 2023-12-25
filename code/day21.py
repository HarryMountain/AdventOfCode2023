import numpy as np

grid = []
test = False
with open('../test_input_files/day21test.txt' if test else '../input_files/day21input.txt', 'r') as f:
    data = f.readlines()
    for x in range(len(data)):
        line = data[x].rstrip()
        grid.append(list(line))
        if 'S' in line:
            start = (x, line.index('S'))

grid = np.array(grid)
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def flood_fill(position, directions, number_of_moves, grid):
    positions = {position}
    for move in range(number_of_moves):
        new_positions = set()
        for position in positions:
            for direction in directions:
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]) and grid[new_position] != '#':
                    new_positions.add(new_position)
        positions = new_positions
    return positions


grid[start] = '.'
places_reached = flood_fill(start, directions, 64, grid)
for place in places_reached:
    grid[place] = 'O'
print(grid)
print(len(places_reached))
