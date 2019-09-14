import unittest


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """
    brackets = {
                ']': '[',
                '}': '{',
                '[': '[',
                '>': '<',
                ')': '('
                }
    open_brackets = set(['[', '{', '[', '<', '('])
    close_brackets = set([']', '}', ']', '>', ')'])
    seen = []

    for let in phrase:
        if let in open_brackets:
            seen.append(let)
        if let in close_brackets:
            if seen != [] and brackets[let] == seen[-1]:
                seen.pop()
            else:
                return False


    if seen == []:
        return True



class test_solutions(unittest.TestCase):

    def test_has_balanced_brackets(self):
        self.assertTrue(has_balanced_brackets("<ok>"))
        self.assertTrue(has_balanced_brackets("<[ok]>"))
        self.assertTrue(has_balanced_brackets("<[{(yay)}]>"))
        self.assertTrue(has_balanced_brackets("No brackets here!"))

        self.assertFalse(has_balanced_brackets("(Oops!){"))
        self.assertFalse(has_balanced_brackets("{[[This has too many open square brackets.]}"))
        self.assertFalse(has_balanced_brackets(">"))
        self.assertFalse(has_balanced_brackets("(This has {too many} ) closers. )"))
        self.assertFalse(has_balanced_brackets("<{Not Ok>}"))



if __name__ == "__main__":
    unittest.main()
