# 1-4000 xmas use ranges
import math
from copy import deepcopy

test = False
workflow = True
workflows = {}
parts = []
# Input form a{a>10:b,c>3:d,A}
with open('../test_input_files/day19test.txt' if test else '../input_files/day19input.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        if len(line) < 2:
            workflow = False
        elif workflow:
            line = line[:-1]
            name, actions = line.split('{')
            workflows[name] = []
            acts = actions.split(',')
            for action in acts[:-1]:
                var = action[0]
                act = action[1]
                end = action.index(':')
                check = action[2:end]
                location = action[end + 1:]
                workflows[name].append([var, act, int(check), location])
            workflows[name].append([acts[-1]])
        else:
            part = {}
            pars = line[1:-1].split(',')
            for p in pars:
                part[p[0]] = int(p[2:])
            parts.append(part)

print(workflows)


def run_workflow(workflow_name, part):
    possibilities = []
    completed = []
    for wf in workflows[workflow_name]:
        new_part = deepcopy(part)
        if len(wf) > 1:
            if wf[1] == '>':
                if part[wf[0]][1] > wf[2]:
                    new_part[wf[0]][0] = wf[2] + 1
                    if wf[3] == 'A':
                        completed.append([new_part, wf[3]])
                    elif wf[3] != 'R':
                        possibilities.append([new_part, wf[3]])
                    part[wf[0]][1] = wf[2]
            else:
                if part[wf[0]][0] < wf[2]:
                    new_part[wf[0]][1] = wf[2] - 1
                    if wf[3] == 'A':
                        completed.append([new_part, wf[3]])
                    elif wf[3] != 'R':
                        possibilities.append([new_part, wf[3]])
                    part[wf[0]][0] = wf[2]
        else:
            if wf[0] != 'R':
                if wf[0] == 'A':
                    completed.append([new_part, wf[0]])
                else:
                    possibilities.append([new_part, wf[0]])

    return possibilities, completed


complete_groups = []
groups = [[{'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in']]
while len(groups) > 0:
    new_groups = []
    for group in groups:
        all_possibilities, complete = run_workflow(group[1], group[0])
        new_groups.extend(all_possibilities)
        for c in complete:
            complete_groups.append(c)
    groups = new_groups

total = 0
for g in complete_groups:
    total += math.prod([x[1] - x[0] + 1 for x in g[0].values()])
print(total)


def overlaps(x, y):
    return not (x[1] < y[0] or y[1] < x[0])


def overall_overlaps(group1, group2):
    overlap = True
    for val in 'xmas':
        overlap &= overlaps(group1[val], group2[val])
    return overlap


