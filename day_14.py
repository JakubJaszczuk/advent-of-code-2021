from collections import Counter, defaultdict


def load_data(path):
    with open(path) as file:
        sequence = file.readline().strip()
        file.readline()  # Just skip empty line
        rules = {}
        for line in file.readlines():
            l, r = line.strip().split(' -> ')
            rules[l] = r
        return sequence, rules


def evolve(initial, rules, time):
    seq = initial
    for _ in range(time):
        buffer = []
        for l, r in zip(seq, seq[1:]):
            buffer.extend([l, rules[l+r]])
        buffer.append(seq[-1])
        seq = buffer
    return seq


def evolve_counts(initial, rules, time):
    seq = Counter(zip(initial, initial[1:]))
    for _ in range(time):
        buffer = defaultdict(int)
        for (l, r), v in seq.items():
            new = rules[l+r]
            buffer[(l, new)] += v
            buffer[(new, r)] += v
        seq = buffer
    return seq


def split_by_element(data):
    res = defaultdict(int)
    for (l, r), v in data.items():
        res[l] += v
        res[r] += v
    return res


def main():
    seq, rules = load_data('day_14_data')
    res = evolve(seq, rules, 10)
    c = Counter(res)
    common = c.most_common()
    print(common[0][1] - common[-1][1])
    res = evolve_counts(seq, rules, 40)
    print(res)
    res = split_by_element(res)
    c = Counter(res)
    common = c.most_common()
    print((common[0][1] - common[-1][1]) // 2 + 1)


if __name__ == '__main__':
    main()
