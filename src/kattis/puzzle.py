"""Kattis puzzle problem solution."""

from collections import deque

def solve(grid: list[str]) -> int:
    """
    Kattis problem: https://open.kattis.com/problems/3puzzle

    grid: list of 3 strings, each length 3
          e.g. ["2-", "13", "3"]

    Returns: minimum number of moves to reach '12345678-' configuration.
    """

    start = "".join(grid)      # Convert rows to a single string
    target = "12345678-"

    if start == target:
        return 0

    # Possible moves based on blank position
    neighbors = {
        0: [1, 3],        1: [0, 2, 4],    2: [1, 5],
        3: [0, 4, 6],     4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7],        7: [4, 6, 8],    8: [5, 7]
    }

    q = deque([(start, start.index("-"), 0)])
    visited = {start}

    while q:
        state, z, dist = q.popleft()
        for nxt in neighbors[z]:
            lst = list(state)
            lst[z], lst[nxt] = lst[nxt], lst[z]
            new_state = "".join(lst)
            if new_state == target:
                return dist + 1
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, nxt, dist + 1))

    # Should never happen (guaranteed solvable)
    return -1
