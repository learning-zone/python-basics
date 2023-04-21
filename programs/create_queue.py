class Queue(object):
    """ Creates a queue. """

    def __init__(self):
        self.items = []


    def __repr__(self):
        if not self.length():
            return '<Queue (empty)>'
        else:
            return '<Queue %s>' % self.items


    def length(self):
        return len(self.items)


    def dequeue(self):
        """ Removes item from the front of the queue. """

        if self.items > 0:
            return self.items.pop(0)
        else:
            raise IndexError('queue is empty.')


    def enqueue(self, item):
        """Add item to end of queue::

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>

            >>> q.length()
            3
        """
        self.items.append(item)


    def is_empty(self):
        return not self.items


    def peek(self):
        """Return but don't remove the first item in the queue.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.peek()
            'buy flight'

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>
        """
        return self.items[0]

if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print("ALL TESTS PASSED!")

