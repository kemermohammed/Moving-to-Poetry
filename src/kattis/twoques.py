"""Kattis twoques problem solution."""


def faster_queue(left_times: list[int], right_times: list[int]) -> str:
    """
    https://open.kattis.com/problems/ataleoftwoqueues
    """
    l = sum(left_times)
    r = sum(right_times)

    if l < r:
        return "left"
    if r < l:
        return "right"
    return "either"
