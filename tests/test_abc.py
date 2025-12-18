from kattis.abc import abc_order


def test_abc_basic():
    assert abc_order([1, 5, 3], "ABC") == [1, 3, 5]


def test_abc_reverse():
    assert abc_order([1, 5, 3], "CBA") == [5, 3, 1]
