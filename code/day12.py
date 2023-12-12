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


total = 0
test = False
with open('../test_input_files/day12test.txt' if test else '../input_files/day12input.txt', 'r') as f:
    for line in f:
        spring, damage = line.rstrip().split()
        print(spring, damage)
        spring = list(spring)
        damage = [int(x) for x in damage.split(',')]
        total_damaged = sum(damage)
        total_already_damaged = spring.count('#')
        to_change = total_damaged - total_already_damaged
        # Store [PathSoFar, Index, Block]
        paths = [["", 0, 0, False]]
        completed_paths = 0
        while len(paths) > 0:
            new_paths = []
            for p in paths:
                match spring[p[1]]:
                    case '.':
                        p[0] += '.'
                        p[1] += 1
                    case '?':
                        # Add #
                        new_p = deepcopy(p)
                        size = damage[new_p[2]]
                        new_p[2] += 1
                        new_p[0] = new_p[0] + '#' * size
                        new_p[1] += size + 1
                        if new_p[2] == len(damage):
                            new_p[0] = new_p[0] + '.' * (len(spring) + 1 - new_p[1])
                            new_p[1] = len(spring)
                        else:
                            new_p[0] += '.'
                        new_paths.append(new_p)

                        # Add .
                        p[0] += '.'
                        p[1] += 1

                    case '#':
                        size = damage[p[2]]
                        p[0] = p[0] + '#' * size
                        p[1] += size + 1
                        p[2] += 1
                        if p[2] == len(damage):
                            p[0] = p[0] + '.' * (len(spring) + 1 - p[1])
                            p[1] = len(spring)
                        else:
                            p[0] += '.'

            paths.extend(new_paths)
            for p in paths:
                if is_valid(p[0], spring, p[2], damage):
                    if p[1] == len(spring):
                        if p[2] == len(damage):
                            completed_paths += 1
                            print(''.join(p[0]))
                            p[3] = True
                else:
                    p[3] = True
            paths = [xx for xx in paths if not xx[3]]
        print(completed_paths)
        total += completed_paths
print(total)
