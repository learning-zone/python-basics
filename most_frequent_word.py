def most_frequent_word(str):
    """ Find k most frequent words in a string of words, and print them in space-separated alphabetical order.

    >>> most_frequent_word('hello my name is hello joanne')
    hello

    >>> most_frequent_word('hello my name is hello joanne is')
    hello is

    >>> most_frequent_word('hello my name is joanne')
    hello is joanne my name
    """

    # time: O(n log n)
    # space: O(n)

    words = {}
    list_of_words = str.split()

    for word in list_of_words:
        words[word] = words.get(word, 0) + 1

    most_frequent_words = []

    max_value = max(words.values())

    for word, value in words.iteritems():
        if value == max_value:
            most_frequent_words.append(word)

    for word in sorted(most_frequent_words):
        print word,







if __name__ == '__main__':
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print 'All tests passed!'
