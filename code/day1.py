test = False
total = 0
digit = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open('../test_input_files/day1test.txt' if test else '../input_files/day1input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        found = False
        for i in range(len(line)):
            if line[i].isdigit():
                total += 10 * int(line[i])
                found = True
            else:
                for word, value in digit.items():
                    if line[i: i + len(word)] == word:
                        total += 10 * value
                        found = True
                        break
            if found:
                break
        found = False
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                total += int(line[i])
                found = True
            else:
                for word, value in digit.items():
                    if line[i+1 - len(word): i+1] == word:
                        total += value
                        found = True
                        break
            if found:
                break
print(total)


        