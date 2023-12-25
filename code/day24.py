hailstones = []
test = False
with open('../test_input_files/day24test.txt' if test else '../input_files/day24input.txt', 'r') as f:
    for line in f:
        hailstone_position, hailstone_velocity = [[int(y) for y in x] for x in line.rstrip().split('@')]
        print(hai(()))
