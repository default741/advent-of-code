with open('./input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1], input_data))

config = {
    'red': 12,
    'green': 13,
    'blue': 14
}

max_game_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0
}

mul_games = []
possible_games_id = []

input_data = list(map(lambda x: x.split(': '), input_data))

for data in input_data:
    data[1] = data[1].split('; ')

for data in input_data:
    print(data)
    possible = True

    temp_config = config.copy()
    temp_max = max_game_cubes.copy()

    for turn in data[1]:
        sets = turn.split(', ')

        for balls in sets:
            num_balls, color_balls = balls.split(' ')
            num_balls = int(num_balls)

            if temp_config[color_balls] - num_balls < 0:
                possible = False

            if temp_max[color_balls] < num_balls:
                temp_max[color_balls] = num_balls

    mul_val = 1
    for i in temp_max.values():
        mul_val *= i

    mul_games.append(mul_val)

    print(temp_config)
    print()

    if not possible:
        continue

    possible_games_id.append(int(data[0].split(' ')[1]))

print(possible_games_id)
print(sum(possible_games_id))

print(sum(mul_games))
