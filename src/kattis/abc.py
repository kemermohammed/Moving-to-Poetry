def abc_order(nums: list[int], order: str) -> list[int]:
    """
    https://open.kattis.com/problems/abc
    """
    a, b, c = sorted(nums)
    mapping = {'A': a, 'B': b, 'C': c}
    return [mapping[ch] for ch in order]
