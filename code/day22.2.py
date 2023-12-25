from copy import deepcopy

blocks = {}
test = True
with open('../test_input_files/day22test.txt' if test else '../input_files/day22input.txt', 'r') as f:
    file = f.readlines()
    for l in range(len(file)):
        line = file[l]
        start, end = [[int(thing) for thing in coord.split(',')] for coord in line.rstrip().split('~')]
        block = []
        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                for z in range(start[2], end[2] + 1):
                    block.append([x, y, z])
        blocks[l] = block

supports = {}
for block_name, value in blocks.items():
    supports[block_name] = []
for b, value in blocks.items():
    supported_by = set()
    for piece in value:
        for b2, value2 in blocks.items():
            if b2 != b:
                for piece2 in value2:
                    if piece2[0] == piece[0] and piece2[1] == piece[1] and piece2[2] < piece[2]:
                        supported_by.add(b2)
    for s in supported_by:
        supports[s].append(b)
print(supports)

total = 0
for block_name, stuff_it_supports in supports.items():
    stuff_needed_to_be_supported = deepcopy(stuff_it_supports)
    for second_block_name, stuff_this_other_one_supports in supports.items():
        if block_name != second_block_name:
            for block_name2 in stuff_this_other_one_supports:
                if block_name2 in stuff_needed_to_be_supported:
                    stuff_needed_to_be_supported.remove(block_name2)
    if len(stuff_needed_to_be_supported) == 0:
        total += 1
print(total)
total = 0
states = [supports]
done = False
while not done:
    new_states = []
    for state in states:
        for block_name, stuff_it_supports in state.items():
            new_state = deepcopy(state)
            stuff_needed_to_be_supported = deepcopy(stuff_it_supports)
            for second_block_name, stuff_this_other_one_supports in state.items():
                if block_name != second_block_name:
                    for block_name2 in stuff_this_other_one_supports:
                        if block_name2 in stuff_needed_to_be_supported:
                            stuff_needed_to_be_supported.remove(block_name2)
            if len(stuff_needed_to_be_supported) == 0:
                new_state.pop(block_name)
                for name, thing in new_state.items():
                    if block_name in thing:
                        thing.remove(block_name)
                new_states.append(new_state)
        if len(state) == 0:
            done = True
            total += 1
    states = new_states

print(total)
