class Stack(object):
    """LIFO stack.

    Implemented using a Python list; since stacks just need
    to pop and push, a list is a good implementation, as
    these are O(1) for native Python lists. However, in cases
    where performance really matters, it might be best to
    use a Python list directly, as it avoids the overhead
    of a custom class.

    Or, for even better performance (& typically smaller
    memory footprint), you can use the `collections.deque`
    object, which can act like a stack.

    (We could also write our own LinkedList class for a
    stack, where we push things onto the head and pop things
    off the head (effectively reversing it), but that would be less
    efficient than using a built-in Python list or a
    `collections.deque` object)
    """

    def __init__(self):
        self.items = []
        self.min_stack = []


    def __repr__(self):
        if not self.items:
            return "<Stack (empty)>"
        else:
            return "<Stack tail=%s length=%d>" % (
                self.items[-1], len(self.items))


    def push(self, item):
        """Add item to end of stack."""

        self.items.append(item)

        if self.min_stack == [] or self.min_stack[-1] > item:
            self.min_stack.append(item)

        else:
            self.min_stack.append(self.min_stack[-1])


    def pop(self):
        """Remove item from end of stack and return it."""

        if self.is_empty():
            return IndexError('pop from empty list')

        self.min_stack.pop()

        return self.items.pop()


    def __iter__(self):
        """Allow iteration over list.

        __iter__ is a special method that, when defined,
        allows you to loop over a list, so you can say things
        like "for item in my_stack", and it will pop
        successive items off.
        """

        while True:
            try:
                yield self.pop()
            except StackEmptyError:
                raise StopIteration


    def length(self):
        """Return length of stack::

            >>> s = Stack()
            >>> s.length()
            0

            >>> s.push(3)
            >>> s.push(4)
            >>> s.push(5)

            >>> s.length()
            3
        """

        count = 0
        for item in self.items:
            count += 1
        return count


    def empty(self):
        """Empty stack::

            >>> s = Stack()
            >>> s.push(4)
            >>> s.push(3)
            >>> s.push(2)

            >>> s.length()
            3

            >>> s.empty()

            >>> s.length()
            0
        """

        self.items = []
        self.min_stack = []


    def is_empty(self):
        """Is stack empty?

            >>> s = Stack()

            >>> s.is_empty()
            True

            >>> s.push(3)
            >>> s.push(2)
            >>> s.push(4)

            >>> s.is_empty()
            False
        """

        return self.items == []


    def find_min(self):
        """ Returns the minimum value of a numerical stack.

        >>> s = Stack()
        >>> s.push(2)
        >>> s.push(1)
        >>> s.push(3)
        >>> s.push(-1)
        >>> s.find_min()
        -1

        >>> s2 = Stack()
        >>> s2.push(2)
        >>> s2.push(1)
        >>> s2.push(3)
        >>> s2.find_min()
        1

        >>> s3 = Stack()
        >>> s3.push(2)
        >>> s3.push(1)
        >>> s3.push(3)
        >>> s3.push(3)
        >>> s3.push(1)
        >>> s3.find_min()
        1

        >>> s3.pop()
        1
        >>> s3.find_min()
        1

        >>> s3.pop()
        3
        >>> s3.pop()
        3
        >>> s3.pop()
        1
        >>> s3.find_min()
        2
        """

        if not self.is_empty():
            return self.min_stack[-1]



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print

