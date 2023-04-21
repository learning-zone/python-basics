# import unittest


# def is_unique(string):
#     """ Takes a string and returns True if it has all unique characters. """

#     str_set = set(string)

#     return str_set == string


# class Testing(unittest.TestCase):
#     def is_unique_test(self):
#         assertEqual(is_unique('asdfghjkl'), True)
#         assertEqual(is_unique('1234567asdf'), True)
#         assertEqual(is_unique('!@#$%^&asdfg123'), True)
#         assertEqual(is_unique('abcdABCD'), True)

#         assertEqual(is_unique('asdfghjkll'), False)
#         assertEqual(is_unique('1qwerty1'), False)
#         assertEqual(is_unique('poiu$asdf$'), False)

# if __name__ == '__main__':
#     unittest.main()

import unittest


def is_unique(string):
    """ Takes a string and returns True if it has all unique characters. """

    str_set = set(string)

    return str_set == string


class Testing(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique('asdfghjkl'), True)
        self.assertEqual(is_unique('1234567asdf'), True)
        self.assertEqual(is_unique('!@#$%^&asdfg123'), True)
        self.assertEqual(is_unique('abcdABCD'), True)

        self.assertEqual(is_unique('asdfghjkll'), False)
        self.assertEqual(is_unique('1qwerty1'), False)
        self.assertEqual(is_unique('poiu$asdf$'), False)

if __name__ == '__main__':
    unittest.main()
