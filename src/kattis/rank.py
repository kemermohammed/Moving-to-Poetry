"""Kattis rank problem solution."""


def solve(n: int, games: list[tuple[str, str]]) -> list[str]:
    """
    Kattis problem: https://open.kattis.com/problems/rankproblem

    n: number of teams (teams are T1 ... Tn)
    games: list of tuples (winner, loser) e.g. [("T4","T1"), ("T3","T1")]

    Returns: final ranking as a list of team names in order.
    """

    # Initial ranking: T1, T2, ..., Tn
    ranking = [f"T{i}" for i in range(1, n + 1)]

    for w, l in games:
        pos_w = ranking.index(w)
        pos_l = ranking.index(l)

        # If winner is above loser → no change
        if pos_w < pos_l:
            continue

        # Otherwise, move winner just below loser
        ranking.pop(pos_w)
        ranking.insert(pos_l + 1, w)

    return ranking
