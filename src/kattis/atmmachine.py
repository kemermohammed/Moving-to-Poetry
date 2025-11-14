"""Kattis atmmachine problem solution."""


def atm_results(k: int, requests: list) -> str:
    result = []
    money = k

    for r in requests:
        if money >= r:
            result.append("1")
            money -= r
        else:
            result.append("0")

    return "".join(result)
