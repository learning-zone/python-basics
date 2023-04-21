# In this challenge, you'll make binary search for the classic children's guessing game of "pick a number from 1 to 100".

def binary_search(val):
    """ Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """

    # Runtime: O(nlogn)

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    guess = None
    low = 0
    high = 101

    while guess != val:
        num_guesses += 1
        guess = (high - low)/2 + low

        if guess > val:
            high = guess
        elif guess < val:
            low = guess


    return num_guesses


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED")
