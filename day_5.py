import numpy as np
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Coordinates:
    x0: int
    y0: int
    x1: int
    y1: int

    def is_non_diagonal(self):
        return self.x0 == self.x1 or self.y0 == self.y1

    def get_overlapping(self):
        if self.x0 == self.x1:
            b, e = (self.y0, self.y1) if self.y0 < self.y1 else (self.y1, self.y0)
            return [(self.x0, i) for i in range(b, e + 1)]
        if self.y0 == self.y1:
            b, e = (self.x0, self.x1) if self.x0 < self.x1 else (self.x1, self.x0)
            return [(i, self.y0) for i in range(b, e + 1)]

    def get_overlapping_with_diagonal(self):
        if self.x0 == self.x1:
            b, e = (self.y0, self.y1) if self.y0 < self.y1 else (self.y1, self.y0)
            return [(self.x0, i) for i in range(b, e + 1)]
        if self.y0 == self.y1:
            b, e = (self.x0, self.x1) if self.x0 < self.x1 else (self.x1, self.x0)
            return [(i, self.y0) for i in range(b, e + 1)]
        else:
            step = 1 if self.x0 < self.x1 else -1
            xs = range(self.x0, self.x1+step, step)
            step = 1 if self.y0 < self.y1 else -1
            ys = range(self.y0, self.y1+step, step)
            x = zip(xs, ys)
            return list(x)


def parse_line(line):
    l, p = line.split(' -> ')
    x0, y0 = [int(n) for n in l.split(',')]
    x1, y1 = [int(n) for n in p.split(',')]
    return x0, y0, x1, y1


def load_data(path: str | Path):
    with open(path, 'r') as file:
        return [Coordinates(*parse_line(line)) for line in file]


def create_matrix(data):
    max_x = max(max(c.x0, c.x1) for c in data)
    max_y = max(max(c.y0, c.y1) for c in data)
    matrix = np.zeros((max_x + 1, max_y + 1), int)
    for coords in data:
        if coords.is_non_diagonal():
            o = coords.get_overlapping()
            for c in o:
                matrix[c] += 1
    return matrix


def create_matrix_with_diagonal(data):
    max_x = max(max(c.x0, c.x1) for c in data)
    max_y = max(max(c.y0, c.y1) for c in data)
    matrix = np.zeros((max_x + 1, max_y + 1), int)
    for coords in data:
        o = coords.get_overlapping_with_diagonal()
        for c in o:
            matrix[c] += 1
    return matrix


def main():
    data = load_data('day_5_data')
    matrix = create_matrix(data)
    print(matrix.T)
    count = np.sum(matrix > 1)
    print(count)
    matrix = create_matrix_with_diagonal(data)
    print(matrix.T)
    count = np.sum(matrix > 1)
    print(count)


if __name__ == '__main__':
    main()
