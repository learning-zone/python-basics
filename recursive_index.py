def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"]

    >>> recursive_index("hey", lst)
    0

    >>> recursive_index("you", lst)
    2

    >>> recursive_index("porcupine", lst) is None
    True
    """

    if not haystack or needle not in haystack:
        return None

    count = 0

    if needle == haystack[0]:
        return count


    count += 1 + recursive_index(needle, haystack[1:])

    return count


def recursive_index_2(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"]

    >>> recursive_index_2("hey", lst)
    0

    >>> recursive_index_2("you", lst)
    2

    >>> recursive_index_2("porcupine", lst) is None
    True
    """

    if not haystack or needle not in haystack:
        return None

    if needle == haystack[0]:
        return 0


    else:
        return 1 + recursive_index_2(needle, haystack[1:])


def recursive_index_3(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

    >>> lst = ["hey", "there", "you"]

    >>> recursive_index_3("hey", lst)
    0

    >>> recursive_index_3("you", lst)
    2

    >>> recursive_index_3("porcupine", lst) is None
    True
    """

    def _recursive_index_3(needle, haystack, count):

        if len(haystack) == count:
            return None

        if needle == haystack[count]:
            return count

        return _recursive_index_3(needle, haystack, count+1)

    return _recursive_index_3(needle, haystack, 0)



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED!"
