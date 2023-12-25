# Animate it
import random
from copy import deepcopy
import numpy as np

blocks = {}
test = False
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


def hit_ground(grounded, blocks, supports):
    keys_to_remove = []
    for name, block in blocks.items():
        supported_by_ground = False
        supported_by_blocks = False
        names_of_supports = set()
        for piece in block:
            if piece[2] == 1:
                supported_by_ground = True
            for name2, block2 in grounded.items():
                for piece2 in block2:
                    if block2 != block:
                        new_piece = deepcopy(piece)
                        new_piece[2] -= 1
                        if piece2 == new_piece:
                            supported_by_blocks = True
                            names_of_supports.add(name2)
        if supported_by_ground:
            grounded[name] = block
            keys_to_remove.append(name)
            supports[name] = []
        elif supported_by_blocks:
            grounded[name] = block
            keys_to_remove.append(name)
            supports[name] = []
            for n in names_of_supports:
                supports[n].append(name)
    for key_to_remove in keys_to_remove:
        blocks.pop(key_to_remove)
    return grounded, blocks, supports


grounded = {}
supports = {}
grounded, blocks, supports = hit_ground(grounded, blocks, supports)
print(blocks)
while len(blocks) > 0:
    for name, block in blocks.items():
        for thing in block:
            thing[2] -= 1
    grounded, blocks, supports = hit_ground(grounded, blocks, supports)
    print(len(blocks))
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
