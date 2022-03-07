import numpy as np


def load_data(path):
    with open(path) as file:
        return np.array([[int(c) for c in line] for line in file.read().splitlines()])


def get_adjacent(x, y, rows, cols):
    adjacent = set()
    if x-1 >= 0:
        adjacent.add((y, x-1))
    if x+1 < cols:
        adjacent.add((y, x+1))
    if y-1 >= 0:
        adjacent.add((y-1, x))
    if y+1 < rows:
        adjacent.add((y+1, x))
    return adjacent


def generate_simple_path(matrix):
    max_row = matrix.shape[0]
    max_col = matrix.shape[1]
    path = [(0, v) for v in range(max_row)]
    path.extend([(v, max_row-1) for v in range(1, max_col)])
    return path


def score(matrix, path):
    score = -matrix[0, 0]
    for p in path:
        score += matrix[p]
    return score


def generate_paths(matrix):
    max_row = matrix.shape[0]
    max_col = matrix.shape[1]
    best_path = generate_simple_path(matrix)  # Initial solution
    best_score = score(matrix, best_path)
    stack = [((0, 0), [])]  # Current location and path
    while stack:
        top, path = stack.pop()
        q, w = top
        top = w, q
        path = path.copy()
        path.append(top)
        sc = score(matrix, path)
        if sc > best_score:
            continue
        elif top == (max_row-1, max_col-1) and sc < best_score:
            best_path = path
            best_score = sc
        else:
            adj = get_adjacent(*top, max_row, max_col)
            if len(path) > 1:
                adj.remove(path[-2])
            for e in adj:
                stack.append((e, path))
        #print(best_score, best_path)
    return best_path


def print_matrix(matrix):
    print(np.array2string(matrix, separator='', formatter={'bool': lambda x: '#' if x else '.'}))


def main():
    data = load_data('day_15_data')
    #print(data)
    path = generate_paths(data)
    print(score(data, path))
    print(path)
    vis = np.zeros(data.shape, dtype=bool)
    for p in path:
        vis[p] = True
    print_matrix(vis)


if __name__ == '__main__':
    main()
