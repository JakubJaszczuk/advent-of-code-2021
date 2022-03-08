import numpy as np


def load_data(path):
    with open(path) as file:
        return np.array([[int(c) for c in line] for line in file.read().splitlines()])


def get_adjacent(y, x, rows, cols):
    adjacent = []
    if x-1 >= 0:
        adjacent.append((y, x-1))
    if x+1 < cols:
        adjacent.append((y, x+1))
    if y-1 >= 0:
        adjacent.append((y-1, x))
    if y+1 < rows:
        adjacent.append((y+1, x))
    return adjacent


def dijkstra(matrix):
    max_row = matrix.shape[0]
    max_col = matrix.shape[1]
    distances = np.full_like(matrix, np.iinfo(int).max)
    prevs = np.full((max_row, max_col, 2), -1)
    distances[0, 0] = 0
    visited = set()
    frontline = {(0, 0)}
    while frontline:
        coords = min(frontline, key=lambda x: distances[x])
        frontline.remove(coords)
        visited.add(coords)
        if coords == (max_row-1, max_col-1):
            return distances, prevs
        adj = get_adjacent(*coords, max_row, max_col)
        for n in (a for a in adj if a not in visited):
            frontline.add(n)
            dist = distances[coords] + matrix[n]
            if dist < distances[n]:
                distances[n] = dist
                prevs[n] = coords
    return distances, prevs


def create_data_larger(matrix):
    arr = matrix
    for i in range(1, 5):
        arr = np.append(arr, matrix + i, axis=1)
        arr[arr > 9] += 1
        arr = arr % 10
    tmp = arr
    for i in range(1, 5):
        arr = np.append(arr, tmp + i, axis=0)
        arr[arr > 9] += 1
        arr = arr % 10
    return arr


def print_matrix(matrix):
    print(np.array2string(matrix, separator='', formatter={'bool': lambda x: '#' if x else '.'}))


def main():
    data = load_data('day_15_data')
    distances, prevs = dijkstra(data)
    print(distances[-1, -1])
    # Task 2
    larger_data = create_data_larger(data)
    distances, prevs = dijkstra(larger_data)
    print(distances[-1, -1])


if __name__ == '__main__':
    main()
