def make_change(amount, denominations, index=0):
    """ Write a function that, given:
        1. an amount of money
        2. a list of coin denominations
        computes the number of ways to make the amount of money with coins of the available denominations.

    >>> make_change(amount=4, denominations=[1,2,3])
    4
    [1,1,1,1]
    [1,1,2]
    [1,3]
    [2,2]

    >>> make_change(amount=20, denominations=[5, 10])
    3
    [5,5,5,5]
    [5,5,10]
    [10,10]

    """


    # time:
    # space:


    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if index == len(denominations):
        return 0

    current_coin = denominations[index]

    combos = 0

    while amount >=0:
        combos += make_change(amount, denominations, index+1)
        amount -=current_coin

    return combos



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print 'All tests passed!'
