def coins(num_coins):
    """ Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """


    combos = set()
    coins = [1, 10]


    def _coins(coins_left, combos, total):

        if not coins_left:
            combos.add(total)
            return

        for coin in coins:
            _coins(coins_left - 1, combos, total + coin)

    _coins(num_coins, combos, 0)


    return combos


def coins_2(num_coins):
    """ Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.

    >>> coins_2(1) == {1, 10}
    True

    >>> coins_2(2) == {2, 11, 20}
    True

    >>> coins_2(3) == {3, 12, 21, 30}
    True

    >>> coins_2(4) == {4, 13, 22, 31, 40}
    True

    >>> coins_2(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """


    combos = set()
    dimes = 10
    pennies = 1


    def _coins_2(coins_left, combos, total):

        if not coins_left:
            combos.add(total)
            return

        _coins_2(coins_left - 1, combos, total + dimes)
        _coins_2(coins_left - 1, combos, total + pennies)

    _coins_2(num_coins, combos, 0)


    return combos





if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print("ALL TESTS PASSED!")
