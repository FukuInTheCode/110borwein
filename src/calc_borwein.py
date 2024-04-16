from math import sin


def calc_borwein(x: float, n: int) -> float:
    y = 1.0
    for i in range(0, n + 1):
        y *= sin(x / (2 * i + 1)) / (x / 2 * i + 1)
    return y
