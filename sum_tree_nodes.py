def num_nodes(tree):
    """Counts the number of nodes in a tree.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    nodes = 1

    if tree is None:
      return 0

    for child in tree.children:
      nodes += num_nodes(child)


    return nodes



if __name__ == "__main__":
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "ALL TESTS PASSED"
