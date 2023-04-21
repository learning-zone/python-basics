def add_to_zero(nums):
    """ Given list of ints, return True if any two nums sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True
    """

    # Runtime: O(n)
    # Spacetime: O(n)

    if len(nums) < 2:
        return False

    num_set = set(nums)

    for num in nums:
        if -num in num_set:
            return True

    return False



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
