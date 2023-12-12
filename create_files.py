day_number = input('What day is it?')
openings = ['code/day', 'input_files/day', 'test_input_files/day']
endings = ['.py', 'input.txt', 'test.txt']
for i in range(3):
    f = open(openings[i] + day_number + endings[i], 'x')
    if i == 0:
        f.write(f'''\
test = False
with open('../{openings[2]}{day_number}{endings[2]}' if test else '../{openings[1]}{day_number}{endings[1]}', 'r') as f:
    for line in f:   
        ''')
    f.close()
