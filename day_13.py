import numpy as np
from operator import itemgetter


def load_data(path):
    folds = []
    coords = []
    with open(path) as file:
        lines = file.read().splitlines()
        file_second_part = False
        for line in lines:
            if line == '':
                file_second_part = True
            elif file_second_part:
                data = line.split()[-1]
                axis, coord = data.split('=')
                folds.append((axis, int(coord)))
            else:
                x, y = (int(e) for e in line.split(','))
                coords.append((x, y))
    arr = to_numpy(coords)
    return arr, folds


def to_numpy(coords):
    max_x = max(coords, key=itemgetter(0))[0]
    max_y = max(coords, key=itemgetter(1))[1]
    arr = np.zeros((max_y+1, max_x+1), dtype=bool)
    for x, y in coords:
        arr[y, x] = True
    return arr


def fold_matrix(matrix, fold):
    if fold[0] == 'x':
        rows = matrix.shape[0]
        cols = fold[1]
        src = matrix.shape[1]
        arr = np.zeros((rows, cols), dtype=bool)
        for i in range(cols):
            for j in range(rows):
                arr[j, i] += matrix[j, i]
                arr[j, i] += matrix[j, src-i-1]
        return arr
    if fold[0] == 'y':
        rows = fold[1]
        cols = matrix.shape[1]
        src = matrix.shape[0]
        arr = np.zeros((rows, cols), dtype=bool)
        for i in range(cols):
            for j in range(rows):
                arr[j, i] += matrix[j, i]
                arr[j, i] += matrix[src-j-1, i]
        return arr


def apply_folds(matrix, folds, max_len=None):
    arr = matrix
    folds = folds[0:max_len]
    for fold in folds:
        arr = fold_matrix(arr, fold)
    return arr


def print_matrix(matrix):
    print(np.array2string(matrix, separator='', formatter={'bool': lambda x: '#' if x else '.'}))


def main():
    data, folds = load_data('day_13_data')
    arr = apply_folds(data, folds, 1)
    print(np.sum(arr))
    arr = apply_folds(data, folds)
    print_matrix(arr)


if __name__ == '__main__':
    main()
