from src.calc_borwein import calc_borwein


def get_midpoint(n: int) -> float:
    xs = [x / 2 for x in range(0, 10000)]
    area = 0.0

    for i in range(0, len(xs), 2):
        mid = (xs[i] + xs[i + 1]) / 2
        area += calc_borwein(mid, n) * (xs[i] - xs[i + 1])
    return area
