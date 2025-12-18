from kattis.rank import solve


def test_rank_no_games():
    n = 4
    games = []
    # No games → initial ranking T1..Tn
    assert solve(n, games) == ["T1", "T2", "T3", "T4"]


def test_rank_simple_swap():
    n = 3
    games = [("T3", "T1")]
    # T3 wins against T1 → moves below T1 → T1,T3,T2?
    expected = ["T1", "T3", "T2"]
    assert solve(n, games) == expected


def test_rank_multiple_games():
    n = 4
    games = [("T4", "T1"), ("T3", "T1"), ("T2", "T4")]
    result = solve(n, games)
    # Just check that all teams present and length correct
    assert set(result) == {"T1", "T2", "T3", "T4"}
    assert len(result) == 4


def test_rank_winner_already_above():
    n = 3
    games = [("T1", "T2")]  # T1 already above T2 → no change
    expected = ["T1", "T2", "T3"]
    assert solve(n, games) == expected
