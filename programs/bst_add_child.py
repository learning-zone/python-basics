class Node(object):

    def __init__(self, data, left=None, right=None):
        """ Creates a node with data and optional left/right nodes. """
        self.data = data
        self.left = left
        self.right = right


    def insert(self, new_data):
        """ Inserts a new node with 'new_data' to BST tree rooted here.
        A "balanced" binary search tree is one where the nodes are equitably spread out to guarantee O(log n) search. For this code challenge, you should not try to re-arrange the tree to rebalance it after adding an item; instead, you should simply find the correct place in the current tree to add it.

                    4
                2       7
            1   3       5   8

        >>> t = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(8)))

        >>> t.insert(0)
        >>> t.left.left.left.data == 0
        True
        >>> t.left.left.right is None
        True

        >>> t.insert(9)
        >>> t.right.right.right.data == 9
        True
        >>> t.right.right.left is None
        True

        >>> t.insert(6)
        >>> t.right.left.right.data == 6
        True
        >>> t.right.left.left is None
        True
        """

        if new_data < self.data:

            if self.left is None:
                self.left = Node(new_data)
            else:
                self.left.insert(new_data)

        else:
            if self.right is None:
                self.right = Node(new_data)
            else:
                self.right.insert(new_data)




if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if results.failed == 0:
        print("ALL TESTS PASSED!")
