from LinkedList import LinkedList
import unittest

# assuming we know length of list
def kth_to_last(linked_list: LinkedList, k: int):
    length = linked_list.length()
    number_of_nodes_to_traverse = length - k
    current = linked_list.head
    for _i in range(number_of_nodes_to_traverse - 1):
        current = current.next
    return current

# if we dont know the length of the list 
def kth_to_last_2(linked_list: LinkedList, k: int):
    # first use a runner pointer to traverse k elements from the start
    runner = linked_list.head
    for _i in range(k):
        runner = runner.next
    # now you create another pointer that starts at the beginning of the list 
    # and you move both pointers together until the runner pointer.next is None
    current = linked_list.head
    while(runner.next):
        runner = runner.next
        current = current.next
    return current

class Test(unittest.TestCase):
    data = [
        (([1, 2, 3, 4, 5, 6], 1), 5 ),
        (([1, 2, 3, 4, 5, 6], 0), 6)]

    def test_kth_to_last(self):
        for [test_data, expected] in self.data:
            linked_list = LinkedList(test_data[0])
            actual = kth_to_last(linked_list, test_data[1])
            self.assertEqual(actual.data, expected)

    def test_kth_to_last_2(self):
        for [test_data, expected] in self.data:
            linked_list = LinkedList(test_data[0])
            actual = kth_to_last_2(linked_list, test_data[1])
            self.assertEqual(actual.data, expected)

if __name__ == "__main__":
    unittest.main()
