import unittest
from LinkedList import LinkedList

def remove_middle_node(linked_list: LinkedList, node_to_remove) -> None:
    node_after_node_to_remove = node_to_remove.next
    node_two_after_node_to_remove = node_after_node_to_remove.next
    node_to_remove.data = node_after_node_to_remove
    node_to_remove.next = node_two_after_node_to_remove

class Test(unittest.TestCase):
    def test_remove_middle(self):
        linked_list = LinkedList([2, 3, 4, 5, 6, 7])
        node_four = linked_list.head.next.next
        remove_middle_node(linked_list, node_four)
        self.assertEqual(linked_list.contains(4), False)
        self.assertEqual(linked_list.length(), 5 )
        #note: what happens if you try to remove the last element from the list? 

if __name__ == "__main__":
    unittest.main()