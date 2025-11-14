from kattis.abc import abc_order
from kattis.atmmachine import atm_results
from kattis.cocktail import solve
from kattis.floor import solve as floor_solve
from kattis.lovable import make_lvable
from kattis.prize import max_items_no_prize
from kattis.puzzle import solve
from kattis.rank import solve
from kattis.real import fence_length
from kattis.twoques import faster_queue


def test_floor():
    assert floor_solve(13) == 14


def test_abc():
    assert abc_order([1, 5, 3], "ABC") == [1, 3, 5]


def test_atm():
    assert atm_results(10, [3, 5, 3, 2, 1]) == "11010"
