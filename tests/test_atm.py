from kattis.atmmachine import atm_results

def test_atm_basic():
    # k = 10, requests that can be fully withdrawn
    k = 10
    requests = [3, 5, 3, 2, 1]
    # 10 >= 3 → 1, money=7
    # 7 >= 5 → 1, money=2
    # 2 < 3 → 0
    # 2 >= 2 → 1, money=0
    # 0 < 1 → 0
    expected = "11010"
    assert atm_results(k, requests) == expected

def test_atm_all_fail():
    # k too small, all requests fail
    k = 0
    requests = [1, 2, 3]
    expected = "000"
    assert atm_results(k, requests) == expected

def test_atm_exact_withdraw():
    # withdrawals match exactly k
    k = 6
    requests = [2, 2, 2]
    expected = "111"
    assert atm_results(k, requests) == expected

def test_atm_partial_fail():
    # k runs out during requests
    k = 5
    requests = [3, 3, 1]
    expected = "101"
    assert atm_results(k, requests) == expected
