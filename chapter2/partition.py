# write a function to partition a linked list around a value x such that all nodes less than x
# come before all nodes greater than or equal to x
# if x is in the list, the values less than x need to be to the left of x and x can appear anywhere in the right partition

import unittest
from LinkedList import LinkedList, Node

def partition_list(linked_list: LinkedList, partition: int):
    # create a new list.
    current_node = linked_list.head
    output_list = LinkedList([current_node.data])
    current_node = current_node.next
    # go through each element in input list.
    while(current_node is not None):
        # if element is <= partition, append to tail
        if(current_node.data < partition):
            output_list.append_to_head(current_node.data)
        else:
            # if element is < partition, append to head
            output_list.append_to_tail(current_node.data)
        current_node = current_node.next
    return output_list

class TestPartition(unittest.TestCase):
    def test_partition(self):
        linked_list = LinkedList()
        [linked_list.append_to_tail(x) for x in [3, 9, 8, 5, 10, 2, 1]]
        returned_list = partition_list(linked_list, 5)
        print(returned_list)


if __name__ == "__main__":
    unittest.main()
