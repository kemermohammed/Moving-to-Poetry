"""Kattis prize problem solution."""


def max_items_no_prize(prices: list[int], x: int) -> int:
    """
    https://open.kattis.com/problems/aprizenoonecanwin
    """
    prices.sort()
    n = len(prices)

    for i in range(n - 1):
        if prices[i] + prices[i + 1] > x:
            return i + 1  # items up to i are safe

    return n  # all items safe
