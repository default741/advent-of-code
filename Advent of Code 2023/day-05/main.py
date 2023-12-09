from tqdm import tqdm
import numpy as np

with open('./test_input.txt', 'r') as file:
    input_data = file.readlines()

input_data = list(map(lambda x: x[:-1], input_data))

seeds_planted = list(
    map(lambda x: int(x), input_data[0].split(': ')[1].split(' ')))

seed_ranges = []

for i in range(0, len(seeds_planted), 2):
    seed_ranges.append(
        range(seeds_planted[i], seeds_planted[i] + seeds_planted[i + 1] + 1))

mappings_dict = {}
mapping_list = []

input_data.append('')

for mapping in input_data[2:]:

    if mapping == '':
        mappings_dict[mapping_list[0][:-5]] = mapping_list[1:]
        mapping_list = []

        continue

    mapping_list.append(mapping)

for key, value in mappings_dict.items():
    mapping_list = []

    for mapping in value:
        mapping = list(map(lambda x: int(x), mapping.split(' ')))
        mapping_list.append(mapping)

    mappings_dict[key] = mapping_list


final_mapping = {}

for key, value in mappings_dict.items():
    source_name, destination_name = key.split('-to-')

    src_dest_mapping = []

    for mapping in value:
        dest_range_start, source_range_start, range_length = mapping

        src_range = range(source_range_start,
                          source_range_start + range_length)
        dest_range = range(dest_range_start, dest_range_start + range_length)

        src_dest_mapping.append([src_range, dest_range])

    final_mapping[key] = src_dest_mapping

location_map = []

for seed in seeds_planted:
    keys = list(final_mapping.keys())

    init_loc = seed

    for key in keys:
        map_ranges = final_mapping[key]

        for mappings in map_ranges:
            if init_loc in mappings[0]:
                loc = init_loc - mappings[0][0]
                init_loc = mappings[1][loc]

                break

    location_map.append(init_loc)

print(min(location_map))
print()

location_map = []


for seed_range in seed_ranges:
    min_loc_map = []

    seeds = np.arange(seed_range[0], seed_range[-1])

    print(seeds)

    for key in keys:
        map_ranges = final_mapping[key]

        for mappings in map_ranges:
            print(mappings)
            map_array = np.arange(mappings[0][0], mappings[0][-1])

            print(seeds == map_array)

    # for seed in tqdm(seed_range):
    #     keys = list(final_mapping.keys())

    #     init_loc = seed

    #     for key in keys:
    #         map_ranges = final_mapping[key]

    #         for mappings in map_ranges:
    #             if init_loc in mappings[0]:
    #                 loc = init_loc - mappings[0][0]
    #                 init_loc = mappings[1][loc]

    #                 break

    #     min_loc_map.append(init_loc)

    # location_map.append(min(min_loc_map))


# print(min(location_map))
