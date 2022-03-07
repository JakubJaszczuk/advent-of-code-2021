from collections import defaultdict


def load_graph(path):
    res = defaultdict(list)
    with open(path) as file:
        lines = file.read().splitlines()
        for line in lines:
            l, r = line.split('-')
            res[l].append(r)
            res[r].append(l)
    return res


def check_path_is_correct(path):
    only_lower = [n for n in path if n.islower()]
    if len(only_lower) != len(set(only_lower)):
        return False
    else:
        return True


def check_path_is_correct_2(path):
    only_lower = [n for n in path if n.islower()]
    if only_lower.count('start') != 1:
        return False
    elif len(only_lower) - len(set(only_lower)) > 1:
        return False
    else:
        return True


def generate_paths(graph, predicate):
    paths = []
    stack = [('start', [])]  # Current node and path
    while stack:
        top, path = stack.pop()
        path = path.copy()
        path.append(top)
        if top == 'end':
            paths.append(path)
        elif predicate(path):
            for e in graph[top]:
                stack.append((e, path))
    return paths


def main():
    graph = load_graph('day_12_data')
    paths = generate_paths(graph, check_path_is_correct)
    print(len(paths))
    paths = generate_paths(graph, check_path_is_correct_2)
    print(len(paths))


if __name__ == '__main__':
    main()
