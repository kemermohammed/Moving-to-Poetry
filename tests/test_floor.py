from kattis.floor import solve as floor_solve

def test_floor_below_13():
    # Floors below 13 are unchanged
    assert floor_solve(1) == 1
    assert floor_solve(5) == 5
    assert floor_solve(12) == 12

def test_floor_exact_13():
    # Floor 13 is skipped, so label = 14
    assert floor_solve(13) == 14

def test_floor_above_13():
    # Floors above 13 are incremented by 1
    assert floor_solve(14) == 15
    assert floor_solve(20) == 21
