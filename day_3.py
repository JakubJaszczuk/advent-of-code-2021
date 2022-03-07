import numpy as np


def parse_line(line):
    return [int(c) for c in line.strip()]


def load_data(path):
    with open(path, 'r') as file:
        return [parse_line(line) for line in file]


def task_1(data):
    arr = np.array(data)
    total_count = arr.shape[0]
    ones_count = np.sum(arr, axis=0)
    num = ones_count > total_count / 2
    eps = int(''.join('1' if x else '0' for x in num), 2)
    gamma = int(''.join('0' if x else '1' for x in num), 2)
    print(eps, gamma, eps * gamma)


def task_2_first(data):
    arr = np.array(data)
    num = np.sum(arr, axis=0) >= arr.shape[0] / 2
    for i in range(arr.shape[1]):
        arr = arr[arr[:, i] == (1 if num[i] else 0)]
        num = np.sum(arr, axis=0) >= arr.shape[0] / 2
        if arr.shape[0] == 1:
            break
    return int(''.join('1' if x else '0' for x in arr.flatten()), 2)


def task_2_second(data):
    arr = np.array(data)
    num = np.sum(arr, axis=0) < arr.shape[0] / 2
    for i in range(arr.shape[1]):
        arr = arr[arr[:, i] == (1 if num[i] else 0)]
        num = np.sum(arr, axis=0) < arr.shape[0] / 2
        if arr.shape[0] == 1:
            break
    return int(''.join('1' if x else '0' for x in arr.flatten()), 2)


def main():
    data = load_data('day_3_data')
    task_1(data)
    x = task_2_first(data)
    y = task_2_second(data)
    print(x, y, x * y)


if __name__ == '__main__':
    main()
