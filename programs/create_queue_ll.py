class Node(object):
    """ Creates a node class. """

    def __init__(self, data):
        self.data = data
        self.next = None



class Queue(object):
    """ Creates a queue using a linked list. """

    def __init__(self):
        self.head = None
        self.tail = None


    def __repr__(self):
        if not self.length():
            return '<Queue (empty)>'
        else:
            return '<Queue %s>' % self.head


    def length(self):
        """ Gets length of queue.

            >>> q = Queue()

            >>> q.length()
            0
        """

        curr = self.head

        length = 0

        while curr is not None:
            length += 1
            curr = curr.next

        return length


    def enqueue(self, item):
        """ Add item to end of queue::

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.print_queue()
            ['buy flight', 'pack', 'enjoy vacation']

            >>> q.length()
            3
        """

        new_node = Node(item)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def dequeue(self):
        """ Add item to end of queue::

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("vacation")

            >>> q.print_queue()
            ['buy flight', 'pack', 'vacation']

            >>> q.dequeue()
            'buy flight'

            >>> q.print_queue()
            ['pack', 'vacation']

            >>> q2 = Queue()
            >>> q2.dequeue()

        """

        if self.head is None:
            return None
        else:
            dequeued = self.head.data
            self.head = self.head.next
            return dequeued


    def is_empty(self):
        """ True/false if queue is empty.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("vacation")
            >>> q.is_empty()
            False

            >>> q2 = Queue()
            >>> q2.is_empty()
            True
        """

        return self.head is None


    def peek(self):
        """ Return but don't remove the first item in the queue.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.peek()
            'buy flight'

            >>> q.print_queue()
            ['buy flight', 'pack', 'enjoy vacation']

        """

        return self.head.data


    def print_queue(self):
        """ Prints items in queue in a list.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.print_queue()
            ['buy flight', 'pack', 'enjoy vacation']

            >>> q2 = Queue()
            >>> q2.print_queue()
            []

        """

        curr = self.head

        if curr is None:
            return list()

        queue = []

        while curr is not None:
            queue.append(curr.data)
            curr = curr.next

        return queue



if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print("ALL TESTS PASSED!")

