# Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

# Your solution should return such an integer or null if arr contains all possible integers.
# Analyze the runtime and space complexity of your solution.


import sys


def find_int(arr):
    """ Takes an array and returns a non-negative integer that is not in the original array. Returns null if all integers are in the array.

    Runtime: O(n)
    Spacetime: O(n)

    >>> find_int([0, 2, 1, 3, 4, 5, 11, 32, 42, 50, 100, 6])
    7

    >>> find_int([2, 4, 5, 1, 3])
    0

    >>> find_int([0, 2, 4, 5, 1, 3])
    6

    >>> find_int([0, 2, 4, 5, 1, 3, 6, 8])
    7

    >>> find_int([])
    0

    """

    arr2 = {}

    # If the length of the array is equal to the maximum allowed integers, there are no missing integers in the array.
    if len(arr) == sys.maxint:
        return None

    # Create an O(1) lookup hashtable using the integers from the array as the key, and set the value to True
    for i in range(len(arr)):
        arr2[arr[i]] = True

    # Loop through the length of the array + 1 and check if the number is a key in the hashtable. If it isn't return that number.
    for i in range(len(arr) + 1):
        if not arr2.get(i):
            return i

    return None


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print 'ALL TESTS PASSED!'

