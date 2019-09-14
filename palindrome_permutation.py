import unittest


def is_pal_perm(string):
    """
    Takes a string and returns true if the string is a permutation of a
    palindrome.
    """

    let_counts = {}
    odd = 0

    for let in string:
        let_counts[let] = let_counts.get(let, 0) + 1

    for val in let_counts.values():
        if val % 2 != 0:
            odd += 1

    return odd <= 1


class Testing(unittest.TestCase):

    def test_is_pal_perm(self):
        self.assertTrue(is_pal_perm('carereca'))
        self.assertTrue(is_pal_perm('a'))
        self.assertFalse(is_pal_perm('carelnreca'))


if __name__ == '__main__':
    unittest.main()
