import numpy as np


RAW_INPUT = '''8577245547
    1654333653
    5365633785
    1333243226
    4272385165
    5688328432
    3175634254
    6775142227
    6152721415
    2678227325'''

INPUT = np.array([list(line.strip()) for line in RAW_INPUT.splitlines()], dtype=int)


def get_adjacent_indices(x, y, shape):
    ym, xm = shape
    xs = range(max(0, x-1), min(x+2, xm))
    ys = range(max(0, y-1), min(y+2, ym))
    return ((y, x) for y in ys for x in xs)


def task_1(data, iters):
    count = 0
    for i in range(iters):
        data += 1
        while True:
            end = True
            for (y, x), v in np.ndenumerate(data):
                if v > 9:
                    count += 1
                    data[y, x] = 0
                    adj = get_adjacent_indices(x, y, data.shape)
                    adj = [e for e in adj if data[e] != 0]
                    for ya, xa in adj:
                        data[ya, xa] += 1
                        if data[ya, xa] > 9:
                            end = False
            if end:
                break
    return count


def task_2(data, iters):
    for i in range(iters):
        data += 1
        while True:
            end = True
            for (y, x), v in np.ndenumerate(data):
                if v > 9:
                    data[y, x] = 0
                    adj = get_adjacent_indices(x, y, data.shape)
                    adj = [e for e in adj if data[e] != 0]
                    for ya, xa in adj:
                        data[ya, xa] += 1
                        if data[ya, xa] > 9:
                            end = False
            if end:
                break
        if np.all(data == 0):
            return i + 1
    return None


def main():
    # flashes = task_1(INPUT, 100)
    # print(flashes)
    time = task_2(INPUT, 1000)
    print(time)


if __name__ == '__main__':
    main()
