from tqdm import tqdm
from collections import Counter
import pandas as pd


def max_char_count(string):
    max_char = ''
    max_count = 0
    for char in set(string):
        count = string.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char


with open('./test_input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1].split(' '), input_data))

cards_hands = {}

for idx_i in range(len(input_data)):
    print(input_data[idx_i][0])

    input_data[idx_i][0] = input_data[idx_i][0].replace('T', 'B')
    input_data[idx_i][0] = input_data[idx_i][0].replace('Q', 'D')
    input_data[idx_i][0] = input_data[idx_i][0].replace('K', 'E')
    input_data[idx_i][0] = input_data[idx_i][0].replace('A', 'F')

    max_value_card = sorted(input_data[idx_i][0])[-1]
    print(max_value_card)

    # temp_value = input_data[idx_i][0].replace('J', max_value_card)
    # input_data[idx_i][0] = input_data[idx_i][0].replace('J', '1')

    cards = Counter(input_data[idx_i][0])
    cards_count = Counter(list(cards.values()))

    print(cards)
    print(cards_count)

    if cards_count.get(1, 0) >= 4:
        temp_value = input_data[idx_i][0].replace('J', max_value_card)

        cards = Counter(temp_value)
        cards_count = Counter(list(cards.values()))

        if cards_count.get(2, 0) == 1 and cards_count.get(1, 0) == 3:
            input_data[idx_i][0] = input_data[idx_i][0].replace('J', '1')
            cards_hands[input_data[idx_i][0]] = 6
        else:
            cards_hands[input_data[idx_i][0]] = 7

    if cards_count.get(2, 0) == 1 and cards_count.get(1, 0) == 3:
        temp_value = input_data[idx_i][0].replace(
            'J', max_char_count(input_data[idx_i][0]))

        cards = Counter(temp_value)
        cards_count = Counter(list(cards.values()))

        if cards_count.get(3, 0) == 1:
            input_data[idx_i][0] = input_data[idx_i][0].replace('J', '1')
            cards_hands[input_data[idx_i][0]] = 4
        else:
            cards_hands[input_data[idx_i][0]] = 6

    if cards_count.get(2, 0) == 2:
        temp_value = input_data[idx_i][0].replace(
            'J', max_char_count(input_data[idx_i][0]))

        cards = Counter(temp_value)
        cards_count = Counter(list(cards.values()))

        if cards_count.get(3, 0) == 1:
            input_data[idx_i][0] = input_data[idx_i][0].replace('J', '1')
            cards_hands[input_data[idx_i][0]] = 4
        else:
            cards_hands[input_data[idx_i][0]] = 6

        cards_hands[input_data[idx_i][0]] = 5

    if cards_count.get(3, 0) == 1:
        cards_hands[input_data[idx_i][0]] = 4

    if cards_count.get(3, 0) == 1 and cards_count.get(2, 0) == 1:
        cards_hands[input_data[idx_i][0]] = 3

    if cards_count.get(4, 0) == 1:
        cards_hands[input_data[idx_i][0]] = 2

    if cards_count.get(5, 0) == 1:
        cards_hands[input_data[idx_i][0]] = 1


# for itm in range(len(cards_hands)):


cards_hands = [[k, v] for k, v in cards_hands.items()]
cards_hands = sorted(cards_hands, key=lambda tup: (
    tup[1], tup[0]), reverse=True)

for idx_i in range(len(cards_hands) - 1):
    for idx_j in range(idx_i + 1, len(cards_hands)):

        if cards_hands[idx_i][1] == cards_hands[idx_j][1]:
            if cards_hands[idx_i][0] > cards_hands[idx_j][0]:
                cards_hands[idx_i][0], cards_hands[idx_j][0] = cards_hands[idx_j][0], cards_hands[idx_i][0]


ranks = sorted(list(range(1, len(cards_hands) + 1)))

# for itm in range(1, len(cards_hands)):
#     if cards_hands[itm][0] == cards_hands[itm - 1][0]:
#         ranks[itm] = ranks[itm - 1]

# print(cards_hands)
# print(ranks)

input_dict = {itm[0]: itm[1] for itm in input_data}

winning_list = []

for itm in range(len(cards_hands)):
    # print(ranks[itm], int(input_dict[cards_hands[itm][0]]))
    winning_list.append(ranks[itm] * int(input_dict[cards_hands[itm][0]]))

print(sum(winning_list))
