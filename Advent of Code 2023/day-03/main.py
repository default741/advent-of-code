import string

with open('./advent_3.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1], input_data))
input_data = [i + '.' for i in input_data]

updated_input_data = [list(engine_no) for engine_no in input_data]

for i in range(len(updated_input_data)):
    val = []
    count = 0

    for j in range(len(updated_input_data[i])):
        if updated_input_data[i][j].isdigit():
            val.append(updated_input_data[i][j])
            count += 1

        if updated_input_data[i][j] in string.punctuation:
            if val != []:
                value = ''.join(val)

                for k in range(j - 1, j - 1 - count, -1):
                    updated_input_data[i][k] = value

                val = []
                count = 0


final_sum = []

for i in range(1, len(updated_input_data) - 1):
    for j in range(len(updated_input_data[i])):
        if updated_input_data[i][j] == '.' or updated_input_data[i][j].isdigit():
            continue

        if updated_input_data[i][j] in string.punctuation:

            record_top = updated_input_data[i - 1]
            record_bottom = updated_input_data[i + 1]
            record_current = updated_input_data[i]

            if record_top[j] not in string.punctuation:
                final_sum.append(record_top[j])

            else:
                if record_top[j - 1] not in string.punctuation:
                    final_sum.append(record_top[j - 1])

                if record_top[j + 1] not in string.punctuation:
                    final_sum.append(record_top[j + 1])

            if record_bottom[j] not in string.punctuation:
                final_sum.append(record_bottom[j])

            else:
                if record_bottom[j - 1] not in string.punctuation:
                    final_sum.append(record_bottom[j - 1])

                if record_bottom[j + 1] not in string.punctuation:
                    final_sum.append(record_bottom[j + 1])

            if record_current[j - 1] not in string.punctuation:
                final_sum.append(record_current[j - 1])

            if record_current[j + 1] not in string.punctuation:
                final_sum.append(record_current[j + 1])

# print(final_sum)
print(sum(list(map(lambda x: int(x), final_sum))))

final_sum = []

for i in range(1, len(updated_input_data) - 1):
    for j in range(len(updated_input_data[i])):
        gear_list = []

        if updated_input_data[i][j] == '.' or updated_input_data[i][j].isdigit():
            continue

        if updated_input_data[i][j] == '*':

            record_top = updated_input_data[i - 1]
            record_bottom = updated_input_data[i + 1]
            record_current = updated_input_data[i]

            if record_top[j] not in string.punctuation:
                gear_list.append(record_top[j])

            else:
                if record_top[j - 1] not in string.punctuation:
                    gear_list.append(record_top[j - 1])

                if record_top[j + 1] not in string.punctuation:
                    gear_list.append(record_top[j + 1])

            if record_bottom[j] not in string.punctuation:
                gear_list.append(record_bottom[j])

            else:
                if record_bottom[j - 1] not in string.punctuation:
                    gear_list.append(record_bottom[j - 1])

                if record_bottom[j + 1] not in string.punctuation:
                    gear_list.append(record_bottom[j + 1])

            if record_current[j - 1] not in string.punctuation:
                gear_list.append(record_current[j - 1])

            if record_current[j + 1] not in string.punctuation:
                gear_list.append(record_current[j + 1])

        if len(gear_list) == 2:
            final_sum.append(int(gear_list[0]) * int(gear_list[1]))

print(sum(final_sum))
