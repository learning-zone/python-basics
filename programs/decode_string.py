def decode(s):
    """ Decodes a string. A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

    Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'
    """

    # Runtime: O(n)
    # Spacetime: O(n)

    decoded = ''

    for l in range(len(s)):
        try:
            int(s[l])
            decoded += s[int(s[l]) + l + 1]
        except:
            continue

    return decoded



def decode_2(s):
    """ Decodes a string. A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

    Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

    >>> decode_2("0h")
    'h'

    >>> decode_2("2abh")
    'h'

    >>> decode_2("0h1ae2bcy")
    'hey'
    """

    # Runtime: O(n)
    # Spacetime: O(n)

    def _decode_2(s, decoded, i):

        if i >= len(s):
            return decoded

        current = s[i]

        if current.isdigit():
            decoded += s[int(current) + i + 1]

        return _decode_2(s, decoded, i+1)

    return _decode_2(s, '', 0)




if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
