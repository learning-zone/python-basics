""" Implement a singly linked list. """

class Node(object):
    """ Creates a node. """

    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt



class LinkedList(object):
    """ Creates a linked list. """

    def __init__(self, head=None):
        self.head = head
        self.tail = tail

    def insert(self, data, position):
        """ Takes data as an input and a position and adds it to the linked list as a node before that position. """

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node

        if position == self.size():
            self.tail.next = new_node
            self.tail = new_node


        prev = None
        curr = self.head
        index = 0

        while curr.next:
            if position == index:
                prev.next = new_node
                new_node.next = curr
                return
            index +=1
            prev = prev.next
            curr = curr.next


    def size(self):
        """ Returns the length of the linked list. """

        size = 0

        if head is None and tail is None:
            return size

        curr = self.head

        while curr:
            size += 1
            curr = curr.next

        return size


    def search(self, data):
        """ Takes data as an input and returns the node holding the data. """

        curr = self.head

        while curr:
            if curr.data == data:
                return curr
            curr = curr.next

        raise ValueError('Data not in linked list.')


    def delete(self, data):
        """ Takes data as an input and deletes the node with that data. """

        prev = None
        curr = self.head

        while curr:
            if curr.data == data:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next

            prev = curr
            curr = curr.next

        if curr is None:
            raise ValueError('Data not in linked list.')






