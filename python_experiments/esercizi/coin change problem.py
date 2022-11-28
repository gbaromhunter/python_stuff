def make_change(coin_vals, change):
    """coin_vals is a list of positive ints and coin_vals[0] = 1, change is a positive int > 0.
    return the minimum number of coins needed to have a set of coins the values of which sum to change.
    Coins may be used more than once. For example, make_change([1, 5, 8], 11) should return 3."""

    def combination(coin_vals, change):
        if change > 0:
            for coin in sorted(coin_vals, reverse=True):
                if change - coin >= 0:
                    return [coin] + combination(coin_vals, change - coin)
                else:
                    return combination(sorted(coin_vals, reverse=True)[1:], change)
        if change == 0:
            return []

    def combinations(coin_vals, change):
        if coin_vals == [1]:
            return [[1] * change]
        else:
            return [combination(coin_vals, change)] + combinations(sorted(coin_vals, reverse=True)[1:], change)

    result = combinations(coin_vals, change)
    return min(result, key=len)


def make_change_suggested(coin_vals, change):
    totals = set(coin_vals)
    result = 1
    while change not in totals:
        print(f"result is {result}")
        print(f"totals is {totals}")
        result += 1
        totals = {x+y for x in totals for y in coin_vals}
    return result


def coin_change_tab(coin_vals, change):
    tab = [1] * change
    for i in range(1, change):
        tab[i] = []