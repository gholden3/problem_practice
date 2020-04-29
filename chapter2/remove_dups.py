import unittest
from LinkedList import LinkedList, Node


def remove_dups(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head
    seen = [current.data]
    while current.next:
        if(current.next.data in seen):
            # this works fine for the case of removing the last element bc
            # current.next.next will be None
            current.next = current.next.next
        else:
            seen.append(current.next.data)
            current = current.next
    return linked_list


def remove_any_further_occurences_of_data(node: Node) -> bool:
    'given a node, traverse a linked list and remove any nodes that contain the same data'
    current = node
    while current.next:
        if current.next.data == current.data:
            current.next = current.next.next
        else: 
            current = current.next



def remove_dups_no_addtl_storage(linked_list: LinkedList) -> LinkedList:
    current = linked_list.head
    while current.next:
        remove_any_further_occurences_of_data(current)
        current = current.next
    return linked_list


class Test(unittest.TestCase):

    def test_remove_dups(self):
        test_cases = [([4, 5, 6, 6, 7], 4),([3, 4, 5, 6, 7, 7], 5)]
        for test_case in test_cases:
            linked_list = LinkedList(test_case[0])
            linked_list = remove_dups(linked_list)
            print(str(linked_list))
            self.assertEqual(linked_list.length(), test_case[1])

    def test_remove_dups_no_addtl_storage(self):
        test_cases = [([4, 5, 6, 6, 7], 4),([3, 4, 5, 6, 7, 7], 5)]
        for test_case in test_cases:
            linked_list = LinkedList(test_case[0])
            linked_list = remove_dups_no_addtl_storage(linked_list)
            print(str(linked_list))
            self.assertEqual(linked_list.length(), test_case[1])


if __name__ == "__main__":
    unittest.main()