from src.calc_borwein import calc_borwein


def get_trap(n: int) -> float:
    xs = [x / 2 for x in range(0, 10001)]

    area = 0.0
    for i in range(0, len(xs) - 1):
        tmp = (calc_borwein(xs[i], n) + calc_borwein(xs[i + 1], n)) * (xs[i + 1] - xs[i]) * 1.0 / 2.0
        area += tmp
    return area
