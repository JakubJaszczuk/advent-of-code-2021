def load_data(path):
    with open(path, 'r') as file:
        return [int(line) for line in file]


def count_increases(data):
    counter = 0
    for l, p in zip(data, data[1:]):
        if p > l:
            counter += 1
    return counter


def count_increases_window(data):
    counter = 0
    for i in range(len(data)-3):
        l = sum(data[i:i+3])
        p = sum(data[i+1:i+4])
        if p > l:
            counter += 1
    return counter


def main():
    data = load_data('day_1_data')
    result = count_increases(data)
    print(result)
    result = count_increases_window(data)
    print(result)


if __name__ == '__main__':
    main()
