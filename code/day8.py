import math
from functools import reduce

path_dict = {}
instructions = ""
done = False
test = False
with open('../test_input_files/day8test.txt' if test else '../input_files/day8input.txt', 'r') as f:
    for line in f:
        data = line.rstrip().split(" = ")
        if not done:
            instructions = "".join(data)
            done = True
        elif len(data) > 1:
            left, right = data[1].split(", ")
            path_dict[data[0]] = (left[1:], right[:-1])

paths = []
for p in path_dict.keys():
    if p[2] == "A":
        paths.append([p, p])
done = False
time = 0
instruction_index = 0
cycles = {}
while not done:
    new_paths = []
    instruction = instructions[instruction_index]
    for p in paths:
        original = p[0]
        position = p[1]
        new_pos = path_dict[position][0 if instruction == "L" else 1]
        new_paths.append([original, new_pos])
        if new_pos[2] == "Z":
            if cycles.get(original, None) is None:
                cycles[original] = [new_pos, -time, [instruction_index], [time]]
            elif cycles[original][1] < 0:
                cycles[original][1] = (time + cycles[original][1])
                cycles[original][3].append(time)
            else:
                cycles[original][2].append(instruction_index)
                cycles[original][3].append(time)
    instruction_index = (instruction_index + 1) % len(instructions)
    time += 1
    paths = new_paths
    if all([len(x[2]) > 2 for x in cycles.values()]) and len(cycles.keys()) > 0:
        done = True
        t = []
        lcm = 1
        for cycle in cycles.values():
            t.append(cycle[1])
            lcm = math.lcm(lcm, cycle[1])

        print(lcm)

print(time)
