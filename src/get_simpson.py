from src.calc_borwein import calc_borwein


def get_simpson(n: int) -> float:
    xs = [x / 2 for x in range(0, 10001)]

    area = 0.0
    for i in range(0, len(xs) - 1):
        mid = (xs[i] + xs[i + 1]) / 2
        tmp = (
            (xs[i + 1] - xs[i]) / 6.0 * (calc_borwein(xs[i], n) + 4 * calc_borwein(mid, n) + calc_borwein(xs[i + 1], n))
        )
        area += tmp
    return area
