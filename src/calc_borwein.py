from math import sin


def calc_borwein(x: float, n: int) -> float:
    y = 0.0
    if x == 0:
        return 1.0
    for i in range(0, n + 1):
        tmp = 2 * i + 1
        if i == 0:
            y = sin(x / tmp) / (x / tmp)
        else:
            y *= sin(x / tmp) / (x / tmp)
    return y
