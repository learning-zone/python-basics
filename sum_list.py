def sum_list(nums):
    """ Using recursion, return the sum of numbers in a list.

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

    >>> sum_list([])
    0
    """

    # Runtime: O(n)
    # Spacetime: O(1)

    if not nums:
        return 0

    return nums[0] + sum_list(nums[1:])



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED!"
