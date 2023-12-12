import math

total = 0
test = False
with open('../test_input_files/day2test.txt' if test else '../input_files/day2input.txt', 'r') as f:
    for line in f:
        game = []
        line = line.rstrip()
        data = line.split(" ")
        game_id = data[1][:-1]
        game_set = [0, 0, 0]
        for i in range(2, len(data), 2):
            match data[i+1][0]:
                case "r":
                    game_set[0] += int(data[i])
                case "g":
                    game_set[1] += int(data[i])
                case "b":
                    game_set[2] += int(data[i])
            if not data[i+1][-1] == ",":
                game.append(game_set)
                game_set = [0, 0, 0]
        total += math.prod([max([game[x][y] for x in range(len(game))]) for y in range(3)])
print(total)
