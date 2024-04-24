from src.get_midpoint import get_midpoint
from src.get_trap import get_trap
from src.get_simpson import get_simpson
from src.calc.calc_diff import calc_diff
from src.print.print_estimation import print_estimation


def estimate_area(n: int) -> int:
    print("Midpoint:")
    midpoint = get_midpoint(n)
    diff_midpoint = calc_diff(midpoint)
    print_estimation(midpoint, diff_midpoint, n)
    print("\nTrapezoidal:")
    trapezoidal = get_trap(n)
    diff_trapezoidal = calc_diff(trapezoidal)
    print_estimation(trapezoidal, diff_trapezoidal, n)
    print("\nSimpson:")
    simpson = get_simpson(n)
    diff_simpson = calc_diff(simpson)
    print_estimation(simpson, diff_simpson, n)
    return 0
