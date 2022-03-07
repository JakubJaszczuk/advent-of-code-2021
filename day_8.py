"""
0 -> len == 6 | contains 1, 7, ~4
1 -> len == 2
2 -> len == 5 | else
3 -> len == 5 | contains 1, 7, ~4
4 -> len == 4
5 -> len == 5 | contains (4-1)
6 -> len == 6 | else
7 -> len == 3
8 -> len == 7
9 -> len == 6 | contains 1, 4, 7
"""


def task_1(path):
    with open(path) as file:
        count = 0
        for line in file:
            sig, out = line.split(' | ')
            count += sum(len(x) in (2, 3, 4, 7) for x in out.split())
        print(count)


def decode_digits(digits):
    res = {k: None for k in range(10)}
    for d in digits:
        match len(d):
            case 2: res[1] = d
            case 3: res[7] = d
            case 4: res[4] = d
            case 7: res[8] = d
    for d in digits:
        if len(d) == 6:
            if all(c in d for c in res[1]) and all(c in d for c in res[4]) and all(c in d for c in res[7]):
                res[9] = d
            elif all(c in d for c in res[1]) and not all(c in d for c in res[4]) and all(c in d for c in res[7]):
                res[0] = d
            else:
                res[6] = d
        elif len(d) == 5:
            if all(c in d for c in res[1]) and not all(c in d for c in res[4]) and all(c in d for c in res[7]):
                res[3] = d
            elif all(c in d for c in set(res[4]) - set(res[1])):
                res[5] = d
            else:
                res[2] = d
    return res


def sort_string(string):
    return ''.join(sorted(string))


def task_2(path):
    with open(path) as file:
        total = 0
        for line in file:
            digits, out = line.split(' | ')
            t = decode_digits(digits.split())
            rt = {sort_string(v): k for k, v in t.items()}
            number = ''.join([str(rt[sort_string(o)]) for o in out.split()])
            total += int(number)
    print(total)


def main():
    task_1('day_8_data')
    task_2('day_8_data')


if __name__ == '__main__':
    main()
