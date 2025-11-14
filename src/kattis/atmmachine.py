def atm_results(K: int, requests: list) -> str:
    result = []
    money = K

    for r in requests:
        if money >= r:
            result.append("1")
            money -= r
        else:
            result.append("0")

    return "".join(result)
