import numpy as np
from collections import deque


def load_data(path):
    with open(path) as file:
        return np.array([[int(c) for c in line.strip()] for line in file])


def get_adjacent(x, y, data):
    adjacent = []
    if x-1 >= 0:
        adjacent.append(((y, x-1), data[y, x-1]))
    if x+1 < data.shape[1]:
        adjacent.append(((y, x+1), data[y, x+1]))
    if y-1 >= 0:
        adjacent.append(((y-1, x), data[y-1, x]))
    if y+1 < data.shape[0]:
        adjacent.append(((y+1, x), data[y+1, x]))
    return adjacent


def get_basins_location(data):
    basin_location = []
    for (y, x), v in np.ndenumerate(data):
        adjacent = get_adjacent(x, y, data)
        adjacent = [v for _, v in adjacent]
        if all(v < adjacent):
            basin_location.append((y, x))
    return basin_location


def task_1(data, basins):
    return sum(data[b] + 1 for b in basins)


def task_2(data, basins):
    res = []
    for y, x in basins:
        size = 0
        q = deque()
        q.append((y, x, data[y, x]))
        visited = {(x, y)}
        while q:
            y, x, val = q.pop()
            size += 1
            adjacent = get_adjacent(x, y, data)
            for (ya, xa), v in adjacent:
                if v < 9 and (xa, ya) not in visited:
                    q.appendleft((ya, xa, v))
                    visited.add((xa, ya))
        res.append(size)
    return res


def main():
    data = load_data('day_9_data')
    basins = get_basins_location(data)
    count = task_1(data, basins)
    print(count)
    sizes = task_2(data, basins)
    best = sorted(sizes, reverse=True)[0:3]
    result = 1
    print(best)
    for v in best:
        result *= v
    print(result)


if __name__ == '__main__':
    main()
