OPEN = ('(', '[', '{', '<')
CLOSE = (')', ']', '}', '>')
MAPPING = {k: v for k, v in zip(OPEN, CLOSE)}
SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
SCORES_2 = {')': 1, ']': 2, '}': 3, '>': 4}


def load_data(path):
    with open(path) as file:
        return file.read().splitlines()


def parse_line(line: str):
    stack = []
    for char in line:
        if char in OPEN:
            stack.append(char)
        else:
            opening = stack.pop()
            if MAPPING[opening] != char:
                return char
    return None


def task_1(data):
    score = 0
    for line in data:
        char = parse_line(line)
        if char is not None:
            score += SCORES[char]
    return score


def get_closing_sequence(line: str):
    stack = []
    for char in line:
        if char in OPEN:
            stack.append(char)
        else:
            stack.pop()
    return [MAPPING[c] for c in reversed(stack)]


def task_2(data):
    scores = []
    for line in data:
        score = 0
        sequence = get_closing_sequence(line)
        for char in sequence:
            score *= 5
            score += SCORES_2[char]
        scores.append(score)
    return sorted(scores)[len(scores) // 2 + 1]


def main():
    data = load_data('day_10_data')
    score = task_1(data)
    print(score)
    middle = task_2(data)
    print(middle)


if __name__ == '__main__':
    main()
