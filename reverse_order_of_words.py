def reverse_order_of_words(lst):
    """
    >>> reverse_order_of_words(['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'y', 'o', 'u'])
    ['y', 'o', 'u', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

    """

    # Runtime: O(n)

    reversed_arr = []
    words = ''.join(lst)
    # 'practice makes perfect you'
    words_arr = words.split(' ')
    # ['practice', 'makes', 'perfect', 'you']
    while len(words_arr) > 0:
        word = words_arr.pop()
        reversed_arr.append(word)
        # ['you', 'perfect', 'makes', 'practice']
    reversed_words = ' '.join(reversed_arr)
    # 'you perfect makes practice'

    return list(reversed_words)

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print "ALL TESTS PASSED"
