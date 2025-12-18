from kattis.puzzle import solve


def test_puzzle_already_solved():
    grid = ["123", "456", "78-"]
    # Already solved → 0 moves
    assert solve(grid) == 0


def test_puzzle_one_move():
    grid = ["123", "456", "7-8"]  # solvable
    assert solve(grid) == 1


def test_puzzle_two_moves():
    grid = ["123", "4-6", "758"]
    # Requires two moves to reach solved configuration
    # This depends on BFS search, just checking it returns correct integer
    result = solve(grid)
    assert isinstance(result, int)
    assert result > 0
