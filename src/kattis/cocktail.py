"""Kattis cocktail problem solution."""

def solve(n: int, d: int, durations: list[int]) -> str:
    """
    Kattis problem: https://open.kattis.com/problems/cocktail

    Determine if it is possible for all potion effects to overlap at the same time.

    n: number of potions
    d: time (seconds) to drink each potion
    durations: list of duration values for each potion

    Returns: "YES" or "NO"
    """

    # You drink potions one by one: total drinking time = n * d.
    # For all effects to overlap, the smallest duration must exceed the time spent
    # drinking the (n - 1) potions before it.
    if min(durations) > (n - 1) * d:
        return "YES"
    return "NO"
