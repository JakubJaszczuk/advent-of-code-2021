INPUT = 'target area: x=79..137, y=-176..-117'
X0, X1, Y0, Y1 = 79, 137, -176, -117


def task_1():
    # x position isn't important in this task.
    # Probe starts with velocity y0 and reaches y_max = sum(1..y0) (inclusive).
    # In Python it can be expressed as sum(range(y0 + 1)) (ranges are exlusive).
    # When probe falls at y=0 it has velocity of y1 = y0 + 1.
    # From this point maximum velocity allowing probe to stay inside area
    # is equal to dostance from y=0 to y=-176, that is 176.
    # y1 = y0 + 1 -> 176 = y0 + 1 -> y0 = 175
    # In similar way x velocity can be bounded.
    res = sum(range(175 + 1))  # Ranges ale exlusive so add 1
    print(res)


def simulate(x0, y0, x_bound, y_bound):
    x, y = 0, 0
    vx, vy = x0, y0
    while x+vx < x_bound and y+vy > y_bound:
        x += vx
        y += vy
        vx -= 1
        vy -= 1
        if vx < 0:
            vx = 0
    return x, y


def task_2():
    min_y = Y0  # Higher values immediately overshoot
    max_y = abs(Y0) - 1  # Higher values will overshoot
    max_x = X1  # Higher values immediately overshoot
    for i in range(max_x):
        v = sum(range(i))
        if X0 < v < X1:
            min_x = i - 1
            break
    count = 0
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            x, y = simulate(i, j, X1+1, Y0-1)
            if (X0 <= x <= X1) and (Y0 <= y <= Y1):
                count += 1
    print(count)


def main():
    task_1()
    task_2()


if __name__ == '__main__':
    main()
