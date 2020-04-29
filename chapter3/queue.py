import unittest

class QueueNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.first: QueueNode =None
        self.last: QueueNode = None

    def add(self, data):
        node = QueueNode(data)
        if(self.last != None):
            # add node to end of queue
            self.last.next = node
        self.last = node
        if(self.first is None):
            # queue is empty
            self.first = self.last

    def is_empty(self) -> bool:
        return (self.first is None)

    def peek(self):
        return self.first.data

    def remove(self):
        ''' removes the first element from the queue'''
        if self.first is None:
            return -1
        removed = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return removed.data

class Test(unittest.TestCase):
    def test_is_empty(self):
       my_queue = MyQueue()
       self.assertTrue(my_queue.is_empty())
       my_queue.add(6)
       self.assertFalse(my_queue.is_empty())
    def test_peek(self):
        my_queue = MyQueue()
        my_queue.add(6)
        self.assertEqual(6, my_queue.peek())
    def test_remove(self):
        my_queue = MyQueue()
        my_queue.add(5)
        my_queue.add(6)
        removed = my_queue.remove()
        self.assertEqual(removed, 5)
        my_queue.remove()
        self.assertTrue(my_queue.is_empty())
      
if __name__ == "__main__":
    unittest.main()