
from random import randint
from typing import List

class Node:
    def __init__(self, d: int, next=None):
      self.data: int = d
      self.next: Node = None


    def __str__(self):
        return str(self.data)

# singly linked list
class LinkedList:
    'Simple singly linked list'
    def __init__(self, values: List[int] = None) -> None:
        self.head = None
        self.tail = None
        if values is not None:
            [self.append_to_tail(value) for value in values]

    def __str__(self) -> None:
        current: Node = self.head
        values = []
        while(current.next != None):
            values.append(str(current.data))
            current = current.next
        values.append(str(current.data))
        return (' -> ').join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
        
    def append_to_tail(self, d: int) -> None: 
        if self.head is None:
            self.head = self.tail = Node(d)
            return
        self.tail.next = Node(d)
        self.tail = self.tail.next
        return 
    
    def append_node_to_tail(self, n: Node) -> None:
        if self.head is None:
            self.head = self.tail = n
            return
        self.tail.next = n
        end = n
        while end.next:
            end = end.next
        self.tail = end
        return
    
    def append_to_head(self, d: int) -> None:
        if self.head is None:
            self.tail = self.head = Node(d)
            return
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node


    def length(self) -> int: 
        current = self.head
        length = 0
        while(current.next!=None):
            length += 1
            current = current.next
        return length + 1

    def generate(self, n, min_value, max_value):
        'generates n random values between min_value and max_value and adds them to the list'
        self.head = self.tail = None
        for _i in range(n):
            self.append_to_tail(randint(min_value, max_value))
        return self

    def contains(self, data: int):
        'returns whether or not the list contains a given value'
        current = self.head
        while (current):
            if current.data == data:
                return True
            current = current.next
        return False


import unittest

class Test(unittest.TestCase):

    def test_linked_list(self):
        my_list = LinkedList([7])
        self.assertEqual(my_list.length(), 1)
        [my_list.append_to_tail(x) for x in [9,8]]
        print(str(my_list))
        self.assertEqual(my_list.length(), 3)

    def test_linked_list_with_multiple_values_in_constructor(self):
        my_new_list = LinkedList([4, 5, 6])
        print(str(my_new_list))
        self.assertEqual(my_new_list.length(), 3)

    def test_linked_list_generator(self):
        my_new_list = LinkedList()
        my_new_list.generate(4, 1, 9)
        print(str(my_new_list))
        self.assertEqual(my_new_list.length(), 4)

    def test_contains(self):
        my_list = LinkedList([3, 4, 5])
        self.assertEqual(my_list.contains(5), True)
        self.assertEqual(my_list.contains(6), False)

    def test_append_to_head(self):
        my_list = LinkedList([3, 4, 5])
        my_list.append_to_head(Node(2))
        self.assertEqual(True, my_list.contains(2))

if __name__ == "__main__":
    unittest.main()