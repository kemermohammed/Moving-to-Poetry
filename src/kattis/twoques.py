"""Kattis twoques problem solution."""


def faster_queue(left_times: list[int], right_times: list[int]) -> str:
    """
    https://open.kattis.com/problems/ataleoftwoqueues
    """
    L = sum(left_times)
    R = sum(right_times)

    if L < R:
        return "left"
    if R < L:
        return "right"
    return "either"
