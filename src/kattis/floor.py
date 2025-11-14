"""Kattis floor problem solution."""


def solve(true_floor: int) -> int:
    """
    Kattis problem: https://open.kattis.com/problems/13thfloor

    Given the *true* floor number in a building, return the label
    that should be printed, assuming that floor 13 is skipped.

    - If true_floor < 13 → label is the same.
    - If true_floor >= 13 → label = true_floor + 1.
    """
    if true_floor >= 13:
        return true_floor + 1
    return true_floor
