import math


class Module:
    def __init__(self, outputs, name):
        self.outputs = outputs
        self.name = name
        self.pulses = {0: 0, 1: 0}

    def pulse(self, pulse_recieved, node_sent_from):
        self.pulses[pulse_recieved] += 1
        return self.outputs, pulse_recieved


class FlipFlop(Module):
    def __init__(self, outputs, name, on):
        super().__init__(outputs, name)
        self.on = on

    def pulse(self, pulse_recieved, node_sent_from):
        self.pulses[pulse_recieved] += 1
        if pulse_recieved == 0:
            self.on = not self.on
            if self.on:
                pulse_to_send = 1
            else:
                pulse_to_send = 0
            return self.outputs, pulse_to_send
        return [], 0


class Conjunction(Module):
    def __init__(self, outputs, name, memory):
        super().__init__(outputs, name)
        self.memory = memory

    def pulse(self, pulse_recieved, node_sent_from):
        self.pulses[pulse_recieved] += 1
        self.memory[node_sent_from] = pulse_recieved
        if all([x == 1 for x in self.memory.values()]):
            pulse_to_send = 0
        else:
            pulse_to_send = 1
        return self.outputs, pulse_to_send


class Broadcast(Module):
    def __init__(self, outputs, name):
        super().__init__(outputs, name)


class Output(Module):
    def __init__(self, outputs, name):
        super().__init__(outputs, name)

    def pulse(self, pulse_recieved, node_sent_from):
        self.pulses[pulse_recieved] += 1
        return [[], 0]


nodes = {}
conjunctions = []
test = False
with open('../test_input_files/day20test.txt' if test else '../input_files/day20input.txt', 'r') as f:
    for line in f:
        name, os = line.rstrip().split(' -> ')
        outs = os.split(', ')
        if name == 'broadcaster':
            nodes['broadcaster'] = Broadcast(outs, name)
        elif name[0] == '%':
            nodes[name[1:]] = FlipFlop(outs, name[1:], False)
        else:
            nodes[name[1:]] = Conjunction(outs, name[1:], dict())
            conjunctions.append(name[1:])

for c in conjunctions:
    for na, n in nodes.items():
        if na != c and c in n.outputs:
            nodes[c].memory[na] = 0
nodes['button'] = Module(['broadcaster'], 'button')
nodes['rx'] = Output([], 'rx')
pulses = [0, 0]
done = False
index = 0
# pg sp sv qs
modules = [0, 0, 0, 0]
while not done:
    groups = [['button', 0, 'broadcaster']]
    while len(groups) > 0:
        new_groups = []
        for group in groups:
            to_pulse, value_to_pulse = nodes[group[2]].pulse(group[1], group[0])
            for thing in to_pulse:
                if thing == 'rx' and value_to_pulse == 0:
                    done = True
                new_groups.append([group[2], value_to_pulse, thing])
                if value_to_pulse == 1:
                    if group[2] == 'pg':
                        modules[0] = index + 1
                    elif group[2] == 'sp':
                        modules[1] = index + 1
                    elif group[2] == 'sv':
                        modules[2] = index + 1
                    elif group[2] == 'qs':
                        modules[3] = index + 1
        groups = new_groups
    for node in nodes.values():
        pulses[0] += node.pulses[0]
        pulses[1] += node.pulses[1]
        node.pulses[0] = 0
        node.pulses[1] = 0
    index += 1
    if all([x > 0 for x in modules]):
        print(math.prod(modules))
        break
print(index)
print(pulses[0] * pulses[1])
        