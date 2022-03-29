import unittest


class MinHeap(object):

    def __init__(self):
        self.storage = []


    def swap(self, a, b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]


    def size(self):
        return len(self.storage)


    def peak(self):
        return self.storage[0]


    def insert(self, value):
        self.storage.append(value)
        index = self.size() - 1
        self.bubbleUp(index)


    def get_parent(self, child):
        if child % 2 == 0:
            return (child - 2)/2
        else:
            return (child - 1)/2


    def bubbleUp(self, child):
        parent = self.get_parent(child)

        while (child > 0) and parent >= 0 and (self.storage[child] < self.storage[parent]):
            self.swap(child, parent)
            child = parent
            parent = self.get_parent(child)


    def remove_peak(self):
        self.swap(0, self.size()-1)
        min_elem = self.storage.pop()
        self.bubbleDown(0)

        return min_elem


    def get_child(self, parent):
        child1 = 2 * parent + 1
        child2 = 2 * parent + 2

        if child1 >= self.size():
            return
        elif child2 >= self.size():
            return child1
        elif self.storage[child1] < self.storage[child2]:
            return child1
        else:
            return child2


    def bubbleDown(self, parent):
        child = self.get_child(parent)

        while child is not None and self.storage[parent] > self.storage[child]:
            self.swap(child, parent)
            parent = child
            child = self.get_child(parent)


    def remove(self, item):
        last_index = self.size() - 1
        swap_index = 0

        # can implement with hash table instead of for loop to keep this in
        # O(logn) time complexity, however need to keep track of every element
        # in hash table and update hash table in each method +O(n) space
        for i in range(len(self.storage)):
            if item == self.storage[i]:
                swap_index = i
                self.storage[i], self.storage[last_index] = self.storage[last_index], self.storage[i]

        self.bubbleUp(swap_index)
        self.bubbleDown(swap_index)

        removed_item = self.storage.pop()

        return removed_item



    def __repr__(self):
        return '<storage = {}>'.format(self.storage)



class Testing(unittest.TestCase):

    def setUp(self):
        self.test = MinHeap()
        self.test.storage = [4, 5, 6, 7, 8]

    def test_swap(self):
        self.test.swap(0, 3)
        self.assertEqual(repr(self.test), '<storage = [7, 5, 6, 4, 8]>', 'swap is incorrect')

    def test_size(self):
        self.assertEqual(self.test.size(), 5, 'size is incorrect')

    def test_peak(self):
        self.assertEqual(self.test.peak(), 4, 'peak is the wrong value')

    def test_insert(self):
        self.test.storage = []
        self.test.insert(7)
        self.test.insert(4)
        self.test.insert(10)
        self.test.insert(1)
        self.test.insert(8)
        self.test.insert(11)
        self.test.insert(9)
        self.test.insert(2)
        print self.test
        self.assertEqual(repr(self.test), '<storage = [1, 2, 9, 4, 8, 11, 10, 7]>', 'did not insert new value properly')

    def test_get_parent(self):
        self.assertEqual(self.test.get_parent(7), 3, 'getting child\'s parent index is incorrect')


    def test_bubbleUp(self):
        self.test.insert(1)
        self.assertEqual(repr(self.test), '<storage = [1, 5, 4, 7, 8, 6]>', 'did not bubble up correctly')
        self.test.insert(10)
        self.assertEqual(repr(self.test), '<storage = [1, 5, 4, 7, 8, 6, 10]>', 'did not bubble up correctly')
        self.test.insert(2)
        self.assertEqual(repr(self.test), '<storage = [1, 2, 4, 5, 8, 6, 10, 7]>', 'did not bubble up correctly')
        self.test.insert(9)
        self.assertEqual(repr(self.test), '<storage = [1, 2, 4, 5, 8, 6, 10, 7, 9]>', 'did not bubble up correctly')


    def test_remove_peak(self):
        self.test.storage = [1, 2, 4, 11]
        self.assertEqual(self.test.remove_peak(), 1, 'did not remove correct value')
        self.assertEqual(self.test.remove_peak(), 2, 'did not remove correct value')
        self.assertEqual(self.test.remove_peak(), 4, 'did not remove correct value')
        self.assertEqual(self.test.remove_peak(), 11, 'did not remove correct value')


    def test_get_child(self):
        self.assertEqual(self.test.get_child(0), 1, 'did not select the right child index')


    def test_bubbleDown(self):
        self.test.storage = [1, 2, 4, 11]
        self.test.remove_peak()
        self.assertEqual(repr(self.test), '<storage = [2, 11, 4]>', 'did not bubble down correctly')
        self.test.remove_peak()
        self.assertEqual(repr(self.test), '<storage = [4, 11]>', 'did not bubble down correctly')
        self.test.remove_peak()
        self.assertEqual(repr(self.test), '<storage = [11]>', 'did not bubble down correctly')
        self.test.remove_peak()
        self.assertEqual(repr(self.test), '<storage = []>', 'did not bubble down correctly')


    def test_remove(self):
        self.assertEqual(self.test.remove(8), 8, 'did not remove correct value')
        self.assertEqual(repr(self.test), '<storage = [4, 5, 6, 7]>', 'did not bubble down correctly')


if __name__ == '__main__':
    unittest.main()
