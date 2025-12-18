from kattis.cocktail import solve

def test_cocktail_possible():
    # 3 potions, drink time 2, durations long enough to overlap
    n = 3
    d = 2
    durations = [5, 4, 6]  # min(durations)=4 > (3-1)*2=4? 4 not > 4 → NO
    assert solve(n, d, durations) == "NO"

def test_cocktail_exact_overlap():
    # 3 potions, drink time 1, durations allow overlap
    n = 3
    d = 1
    durations = [3, 4, 2]  # min=2 > (3-1)*1=2? → NO
    assert solve(n, d, durations) == "NO"

def test_cocktail_yes():
    # 2 potions, drink time 2, durations exceed overlap requirement
    n = 2
    d = 2
    durations = [5, 3]  # min=3 > (2-1)*2=2 → YES
    assert solve(n, d, durations) == "YES"

def test_cocktail_no():
    # 4 potions, drink time 1, one potion too short
    n = 4
    d = 1
    durations = [1, 2, 1, 3]  # min=1 > (4-1)*1=3? NO
    assert solve(n, d, durations) == "NO"
