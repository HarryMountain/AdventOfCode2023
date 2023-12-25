# 1-4000 xmas use ranges

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
print(parts)


def run_workflow(workflow_name, part):
    for wf in workflows[workflow_name]:
        if len(wf) > 1:
            r = False
            if wf[1] == '>':
                r = part[wf[0]] > wf[2]
            else:
                r = part[wf[0]] < wf[2]
            if r:
                next_thing = wf[3]
                break
        else:
            next_thing = wf[0]
            break
    if next_thing == 'A' or next_thing == 'R':
        return next_thing
    else:
        val = run_workflow(next_thing, part)
        if val == 'A':
            return val


total = 0
for part in parts:
    if run_workflow('in', part) == 'A':
        total += sum(part.values())
print(total)
        