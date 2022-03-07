import numpy as np


def load_data(path):
    with open(path, 'r') as file:
        numbers = [int(x) for x in file.readline().strip().split(',')]
        boards = []
        buffer = []
        for line in file:
            line = line.strip()
            if line != '':
                buffer.append([int(x) for x in line.split()])
                if len(buffer) == 5:
                    boards.append(np.array(buffer))
                    buffer = []
        return numbers, boards


def create_mark_buffers(boards):
    return [np.full_like(b, False, dtype=bool) for b in boards]


def check_win(board_mark):
    for row in board_mark:
        if np.all(row == True):
            return True
    for col in board_mark.T:
        if np.all(col == True):
            return True
    return False


def mark(board, board_mark, value):
    idx = np.where(board == value)
    board_mark[idx] = True


def get_winner():
    numbers, boards = load_data('day_4_data')
    marks = create_mark_buffers(boards)
    for n in numbers:
        for b, m in zip(boards, marks):
            mark(b, m, n)
            if check_win(m):
                return b, m, n


def get_winner_last():
    numbers, boards = load_data('day_4_data')
    marks = create_mark_buffers(boards)
    order = []
    last_num = 0
    for n in numbers:
        for i, (b, m) in enumerate(zip(boards, marks)):
            if i not in order:
                mark(b, m, n)
                if check_win(m):
                    order.append(i)
                    last_num = n
    last = order[-1]
    return boards[last], marks[last], last_num


def main():
    b, m, n = get_winner()
    s = np.sum(b[~m])
    print(s, n, s * n)
    b, m, n = get_winner_last()
    s = np.sum(b[~m])
    print(s, n, s * n)


if __name__ == '__main__':
    main()
