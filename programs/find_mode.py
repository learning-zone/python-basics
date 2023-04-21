def find_mode(arr):
    """ Finds the mode(s) of the array.

    >>> find_mode([3,5,6,2,6,7,8,3,6,6])
    set([6])

    >>> find_mode([1,2,3,4,5])
    set([1, 2, 3, 4, 5])

    >>> find_mode([2,1,2,1])
    set([1, 2])

    >>> find_mode([1,2,3,2,4])
    set([2])

    >>> find_mode([])
    set([])

    """

    if not arr:
        return set([])
    if len(arr) < 2:
        return set([arr[0]])

    nums = {}
    mode = None
    n = set()

    for i in arr:
        nums[i] = nums.get(i, 0) + 1

    for num, val in nums.iteritems():
        if val > mode:
            mode = val
            n = set([num])
        if val == mode and num not in n:
            n.add(num)
    return n





if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print("ALL TESTS PASSED!")
