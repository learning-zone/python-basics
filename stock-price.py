def get_max_profit(prices):
    """ Finds the maximum profit for buying and selling stock within a day.

    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    6

    >>> stock_prices_yesterday = [10, 3]
    >>> get_max_profit(stock_prices_yesterday)
    -7

    >>> stock_prices_yesterday = [1, 10, 7, 14, 2, 11]
    >>> get_max_profit(stock_prices_yesterday)
    13

    >>> stock_prices_yesterday = [11, 10, 9, 8, 2, 1]
    >>> get_max_profit(stock_prices_yesterday)
    -1

    >>> stock_prices_yesterday = [11, 9, 5, 2, 2, 0]
    >>> get_max_profit(stock_prices_yesterday)
    0

    >>> stock_prices_yesterday = [1, 1, 1, 1, 1, 1]
    >>> get_max_profit(stock_prices_yesterday)
    0
    """

    # Runtime: O(n^2)
    # Spacetime: O(n)


    max_profit = prices[1] - prices[0]

    for a in range(len(prices)):  # O(n)
        for b in range(a + 1, len(prices)):  # O(n)
            gain_loss = prices[b] - prices[a]
            if gain_loss > max_profit:
              max_profit = gain_loss
    print max_profit


def get_max_profit_optimized(prices):
    """ Finds the maximum profit for buying and selling stock within a day.

    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    6

    >>> stock_prices_yesterday = [10, 3]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    -7

    >>> stock_prices_yesterday = [1, 10, 7, 14, 2, 11]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    13

    >>> stock_prices_yesterday = [11, 10, 9, 8, 2, 1]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    -1

    >>> stock_prices_yesterday = [11, 9, 5, 2, 2, 0]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    0

    >>> stock_prices_yesterday = [1, 1, 1, 1, 1, 1]
    >>> get_max_profit_optimized(stock_prices_yesterday)
    0
    """


    # Runtime: O(n)
    # Spacetime: O(1)


    max_profit = prices[1] - prices[0]
    low = prices[0]

    for i in prices:

        # Skip the first price in list
        if prices[0] == i:
            continue

        potential_profit = i - low
        max_profit= max(max_profit, potential_profit)
        low = min(low, i)

    print max_profit


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED"
