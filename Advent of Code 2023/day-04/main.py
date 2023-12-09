with open('./input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1], input_data))
input_data = list(map(lambda x: x.split(': '), input_data))

cards_dict = {}

for cards in input_data:
    cards_dict[cards[0]] = cards[1].split(' | ')

points = []

for card_num, nums in cards_dict.items():
    count = 0

    winning_nums = nums[0]
    elf_nums = nums[1]

    winning_nums = [i for i in winning_nums.split(' ') if i != '']
    elf_nums = [i for i in elf_nums.split(' ') if i != '']

    winning_nums = list(map(lambda x: int(x.strip()), winning_nums))
    elf_nums = list(map(lambda x: int(x.strip()), elf_nums))

    for n in elf_nums:
        if n in winning_nums:
            count += 1

    if count == 0:
        continue

    points.append(2 ** (count - 1))

print(sum(points))

cards_dict = {}

for cards in input_data:
    cards_dict[cards[0]] = cards[1].split(' | ')

card_itr = {0: 1}

for key, _ in cards_dict.items():
    card_keys = [i for i in key.split(' ') if i != '']
    card_num = int(card_keys[1])

    card_itr[card_num] = 1

points = []

for card_num, nums in cards_dict.items():
    count = 0

    card_keys = [i for i in card_num.split(' ') if i != '']
    card_num = int(card_keys[1])

    winning_nums = nums[0]
    elf_nums = nums[1]

    winning_nums = [i for i in winning_nums.split(' ') if i != '']
    elf_nums = [i for i in elf_nums.split(' ') if i != '']

    winning_nums = list(map(lambda x: int(x.strip()), winning_nums))
    elf_nums = list(map(lambda x: int(x.strip()), elf_nums))

    for n in elf_nums:
        if n in winning_nums:
            count += 1

    if count == 0:
        continue

    for i in range(card_num + 1, card_num + 1 + count):
        card_itr[i] += 1 * card_itr[card_num]

print(card_itr)


# copy_list = cards_list[:]

# card_counts = {}

# while len(copy_list) > 0:

#     card = copy_list.pop(0)

#     card_keys = [i for i in list(card.keys())[0].split(' ') if i != '']

#     card_num = int(card_keys[1])
#     nums = list(card.values())[0]

#     if card_num not in card_counts:
#         card_counts[card_num] = 1
#     else:
#         card_counts[card_num] += 1

#     # print(card_num, nums)

#     count = 0

#     winning_nums = nums[0]
#     elf_nums = nums[1]

#     winning_nums = [i for i in winning_nums.split(' ') if i != '']
#     elf_nums = [i for i in elf_nums.split(' ') if i != '']

#     winning_nums = list(map(lambda x: int(x.strip()), winning_nums))
#     elf_nums = list(map(lambda x: int(x.strip()), elf_nums))

#     for n in elf_nums:
#         if n in winning_nums:
#             count += 1

#     if count == 0:
#         continue

#     copy_list.extend(cards_list[card_num:card_num + count])


print(sum(list(card_itr.values())) - 1)
