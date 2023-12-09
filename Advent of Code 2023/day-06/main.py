from tqdm import tqdm

with open('./input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1].split(':'), input_data))

# for idx_i in range(len(input_data)):
#     input_data[idx_i][0] = input_data[idx_i][0].strip()
#     input_data[idx_i][1] = input_data[idx_i][1].strip().split(' ')

#     updated_values = []

#     for idx_j in range(len(input_data[idx_i][1])):
#         if input_data[idx_i][1][idx_j] == '':
#             continue
#         updated_values.append(int(input_data[idx_i][1][idx_j].strip()))

#     input_data[idx_i][1] = updated_values

for idx_i in range(len(input_data)):
    input_data[idx_i][0] = input_data[idx_i][0].strip()
    input_data[idx_i][1] = input_data[idx_i][1].strip().split(' ')

    updated_values = []

    for idx_j in range(len(input_data[idx_i][1])):
        if input_data[idx_i][1][idx_j] == '':
            continue
        updated_values.append(input_data[idx_i][1][idx_j].strip())

    input_data[idx_i][1] = int(''.join(updated_values))

print(input_data)


possible_wins = []

race_time = input_data[0][1]
race_distance = input_data[1][1]

# for idx_i, idx_d in zip(race_time, race_distance):
#     button_hold = 0
#     remaining_time = 0
#     distance_covered = 0

#     count = 0

#     for idx_j in range(idx_i + 1):
#         button_hold = idx_j
#         remaining_time = abs(idx_i - button_hold)

#         distance_covered = remaining_time * button_hold

#         if distance_covered > idx_d:
#             count += 1

#     possible_wins.append(count)


# final_combinations = 1

# for idx_i in possible_wins:
#     final_combinations *= idx_i

# print(final_combinations)


button_hold = 0
remaining_time = 0
distance_covered = 0

count = 0

for idx_j in range(race_time + 1):
    button_hold = idx_j
    remaining_time = abs(race_time - button_hold)

    distance_covered = remaining_time * button_hold

    if distance_covered > race_distance:
        count += 1


print(count)
