# Given a string, return the same string, reversed.
# can't use .reverse()

def rev_str(string):
    """
    >>> rev_str('hello')
    'olleh'

    >>> rev_str('1234h')
    'h4321'

    >>> rev_str('')
    ''
    """

    # Runtime: O(n)

    reversed_str = ""
    list_str = list(string)
    # ['h', 'e', l, l, o]
    for l in range(len(list_str)):
        letter = list_str.pop()
        # l
        reversed_str += letter
        # oll
    return reversed_str


def rev_str_2(string):
    """
    >>> rev_str_2('hello')
    'olleh'

    >>> rev_str_2('1234h')
    'h4321'

    >>> rev_str_2('')
    ''
    """

    # Runtime: O(n)

    return string[::-1]


def rev_str_3(string):
    """
    >>> rev_str_3('hello')
    'olleh'

    >>> rev_str_3('1234h')
    'h4321'

    >>> rev_str_3('')
    ''
    """

    # Runtime: O(n)

    if len(string) == 0:
        return string

    return string[-1] + rev_str_3(string[:-1])



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED!"
