from src.calc_borwein import calc_borwein


def get_midpoint(n: int) -> float:
    xs = [x / 2 for x in range(0, 10001)]

    area = 0.0
    for i in range(0, len(xs) - 1):
        mid = (xs[i] + xs[i + 1]) / 2
        tmp = calc_borwein(mid, n) * (xs[i + 1] - xs[i])
        area += tmp
    return area
