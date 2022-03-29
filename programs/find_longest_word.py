import unittest



def find_longest_word(words):
    """Return longest word in list of words."""

    longest = 0

    for word in words:
        longest = max(len(word), longest)

    return longest


class test_solution(unittest.TestCase):

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word(["hi", "hello"]), 5)
        self.assertEqual(find_longest_word(["Balloonicorn", "Hackbright"]), 12)



if __name__ == "__main__":
    unittest.main()
