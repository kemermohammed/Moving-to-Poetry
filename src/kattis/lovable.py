"""Kattis lvable problem solution."""


def make_lvable(s: str) -> int:
    """
    https://open.kattis.com/problems/lv-able
    """
    n = len(s)

    # Already contains "lv"
    if "lv" in s:
        return 0

    # Can fix with 1 operation?
    # Case 1: replace or insert to create "lv"
    for i in range(n - 1):
        a, b = s[i], s[i + 1]

        # replace one to form "lv"
        if a == "l" or b == "v":
            return 1
        # reverse can turn "vl" into "lv"
        if a == "v" and b == "l":
            return 1

    # Also possible to handle by inserting one letter anywhere
    return 1
