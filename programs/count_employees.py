class Node(object):
    """ Node in a tree. """

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []


    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.

        >>> henri = Node("Henri")
        >>> nora = Node("Nora", [henri])
        >>> nick = Node("Nick")
        >>> janet = Node("Janet", [nick, nora])
        >>> al = Node("Al")
        >>> bob = Node("Bob")
        >>> jen = Node("Jen")
        >>> jessica = Node("Jessica", [al, bob, jen])
        >>> jane = Node("Jane", [jessica, janet])

        >>> henri.count_employees()
        0

        >>> janet.count_employees()
        3

        >>> jessica.count_employees()
        3

        >>> jane.count_employees()
        8

        """

        if not self.children:
            return 0

        count = 0

        for child in self.children:
            count += 1 + child.count_employees()

        return count




if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
