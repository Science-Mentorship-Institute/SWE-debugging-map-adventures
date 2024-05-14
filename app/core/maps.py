def read_map(file):
    with open(file) as f:
        return [list(line.strip()) for line in f.readlines()]