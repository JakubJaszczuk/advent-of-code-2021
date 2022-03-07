def split_line(line):
    command, value = line.split(' ')
    return command, int(value)


def load_data(path):
    with open(path, 'r') as file:
        return [split_line(line) for line in file]


def get_final_position(data):
    x = 0
    depth = 0
    for cmd, val in data:
        if cmd == 'forward':
            x += val
        elif cmd == 'down':
            depth += val
        elif cmd == 'up':
            depth -= val
    return x, depth


def get_final_position_2(data):
    x = 0
    depth = 0
    aim = 0
    for cmd, val in data:
        if cmd == 'forward':
            x += val
            depth += aim * val
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
    return x, depth


def main():
    data = load_data('day_2_data')
    x, y = get_final_position(data)
    print(x * y)
    x, y = get_final_position_2(data)
    print(x * y)


if __name__ == '__main__':
    main()
