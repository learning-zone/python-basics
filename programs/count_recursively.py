def count_recursively(lst):
    """ Return number of items in a list, using recursion.
    >>> count_recursively([])
    0

    >>> count_recursively([1, 2, 3])
    3
    """


    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
