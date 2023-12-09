with open('./input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1], input_data))

# final_list = []

# for data in input_data:
#     num_data = [i for i in list(data) if i.isdigit()]

#     if len(num_data) < 2:
#         num_data = num_data * 2

#     if len(num_data) > 2:
#         num_data = [num_data[0], num_data[-1]]

#     num_data = int(''.join(num_data))

#     final_list.append(num_data)

# print(sum(final_list))

final_list = []

nums = {'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'}

for data in input_data:
    # print(data)
    num_data = {}

    for key, value in nums.items():
        num_data[data.find(key)] = key
        num_data[data.rfind(key)] = key

    sorted_key_list = sorted(list(num_data.keys()))[1:]

    # print(num_data)
    # print(sorted_key_list)

    new_num_data = [nums[num_data[sorted_key_list[0]]],
                    nums[num_data[sorted_key_list[-1]]]]

    if len(new_num_data) < 2:
        new_num_data = new_num_data * 2

    new_num_data = int(''.join(new_num_data))

    final_list.append(new_num_data)
    # print()

# assert len(input_data) == len(final_list)

print(final_list)
print(sum(final_list))
