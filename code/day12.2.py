from copy import deepcopy


def is_valid(path, spring, damage_index, damage):
    if len(path) == len(spring) and damage_index != len(damage):
        return False
    if len(path) > len(spring):
        return False
    for s in range(len(path)):
        if spring[s] == '.' and path[s] != '.':
            return False
        elif spring[s] == '#' and path[s] != '#':
            return False
    return True


def add_path(new_paths, indexes, path, multiplicity, spring):
    if is_valid(path, spring, indexes[1], damage):
        if indexes[0] == len(spring) and indexes[1] == len(damage):
            return multiplicity

        existing_path = new_paths.get(indexes, None)
        if existing_path is None:
            new_paths[indexes] = [path, multiplicity]
        else:
            existing_path[1] += multiplicity
    return 0


def add_block(new_paths, indexes, p, spring, damage):
    size = damage[indexes[1]]
    new_p = p[0] + '#' * size
    new_index = indexes[0] + size
    new_block = indexes[1] + 1
    if new_block == len(damage):
        new_p = new_p + '.' * (len(spring) - new_index)
        new_index = len(spring)
    else:
        new_p += '.'
        new_index += 1
    return add_path(new_paths, (new_index, new_block), new_p, p[1], spring)


total = 0
test = False
with open('../test_input_files/day12test.txt' if test else '../input_files/day12input.txt', 'r') as f:
    for line in f:
        spring, damage = line.rstrip().split()
        spring = list('?'.join([spring] * 5))
        # spring = list(spring)
        damage = [int(x) for x in damage.split(',')] * 5
        # damage = [int(x) for x in damage.split(',')]
        total_damaged = sum(damage)
        total_already_damaged = spring.count('#')
        to_change = total_damaged - total_already_damaged
        # Store [PathSoFar, Index, Block]
        paths = {(0, 0): ["", 1]}
        completed_paths = 0
        while len(paths) > 0:
            new_paths = {}
            for indexes, p in paths.items():
                match spring[indexes[0]]:
                    case '.':
                        completed_paths += add_path(new_paths, (indexes[0] + 1, indexes[1]), p[0] + '.', p[1], spring)
                    case '?':
                        # Add #
                        completed_paths += add_block(new_paths, indexes, p, spring, damage)

                        # Add .
                        completed_paths += add_path(new_paths, (indexes[0] + 1, indexes[1]), p[0] + '.', p[1], spring)

                    case '#':
                        completed_paths += add_block(new_paths, indexes, p, spring, damage)
            paths = new_paths
            # print(paths)
        print(completed_paths)
        total += completed_paths
print(total)
