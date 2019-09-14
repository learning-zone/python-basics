# Given a num, get all the valid parenthesis permutations.
# Observations:
# - All permutations start with opens
# - Base case: if num of open used == num of closed used
# - Num of opens used up, then next to the end must be closed

import unittest


def valid_parens_perms(num):

    result = []

    def recurse(substr, left, right):
        if left == 0 and right == 0:
            result.append(substr)
            return

        elif left == 0:
            recurse(substr + ')', left, right - 1)

        elif left < right:
            recurse(substr + '(', left - 1, right)
            recurse(substr + ')', left, right - 1)

        elif left == right:
            recurse(substr + '(', left - 1, right)

    recurse('', num, num)

    return result


class Testing(unittest.TestCase):
    def test_valid_parens_perms(self):
        self.assertEqual(valid_parens_perms(1), ['()'])
        self.assertEqual(valid_parens_perms(2), ['(())', '()()'])
        self.assertEqual(valid_parens_perms(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
        self.assertEqual(valid_parens_perms(4), ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'])


if __name__ == '__main__':
    unittest.main()
