def flood_fill(position, directions, dug_out, ub):
    new = True
    positions = [position]
    seen = {position}
    while new:
        new = False
        new_positions = []
        for position in positions:
            for direction in directions.values():
                new_position = (position[0] + direction[0], position[1] + direction[1])
                if new_position not in dug_out and new_position not in seen:
                    new_positions.append(new_position)
                    seen.add(new_position)
                    new = True
        positions = new_positions
        if len(seen) > ub:
            return None
    return len(seen)


dug_out = []
coloured_tiles = []
instructions = []
test = False
with open('../test_input_files/day18test.txt' if test else '../input_files/day18input.txt', 'r') as f:
    for line in f:
        instructions.append(line.rstrip().split())

directions = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}

position = (0, 0)
for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1])
    colour = instruction[2][1:-1]
    dir = directions[direction]
    for i in range(number):
        position = (position[0] + dir[0], position[1] + dir[1])
        dug_out.append(position)
        coloured_tiles.append([position, colour])


xs = [x[0] for x in dug_out]
ys = [y[1] for y in dug_out]
ub = (max(xs) - min(xs)) * (max(ys) - min(ys))
for direction in directions.values():
    place_to_start_from = (dug_out[0][0] + direction[0], dug_out[0][1] + direction[1])
    if place_to_start_from not in dug_out:
        filled = flood_fill(place_to_start_from, directions, dug_out, ub)
        if filled is not None:
            print(filled + len(dug_out))
            print(coloured_tiles)
        