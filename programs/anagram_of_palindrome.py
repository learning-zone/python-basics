# Is the word an anagram of a palindrome?

# A palindrome is a word that reads the same forward and backwards (eg, "racecar", "tacocat"). An anagram is a rescrambling of a word (eg for "racecar", you could rescramble this as "arceace").

# Determine if the given word is a re-scrambling of a palindrome.

# The word will only contain lowercase letters, a-z.

def is_anagram_of_palindrome(word):
    """ Is the word an anagram of a palindrome?
    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """

    # Runtime: O(n)

    word_dict = {}

    for l in word:
        word_dict['l'] = word_dict.get(l, 0) + 1

    for letter in word_dict:
        if word_dict[letter] % 2 != 0 and len(word) % 2 == 0:
            return False
    return True




if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
