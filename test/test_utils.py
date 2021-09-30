def read_seed_data(file_path):
    seed_data = []
    with open(file_path) as source:
        for line in source:
            values = line.rstrip().split(sep=' ')
            seed_data.append(values)
    # print(seed_data)
    return seed_data
