def is_int(n: str):
    try:
        int(n)
        return True
    except ValueError:
        return False


def error_handling(abrs: list[str]) -> int:
    if len(abrs) != 2 or not is_int(abrs[1]) or int(abrs[1]) < 0:
        return 84
    return 0
