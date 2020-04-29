
# given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
# definition: curcular linked list: a (corrupt) linked list in which a node's next pointer points to an 
# earlier node, so as to make aloop inthe linked list. 
# example: A -> B-> C -> D -> E -----
#                   ^                |
#                   |________________|
# output: C

# General algorithm: if the un-looped part of the list (example A and B) is K nodes long, use a fast pointer and a slow pointer. 
# When the two pointers meet, they will be K nodes away from the start of the loop. Then you move one of the nodes to the start of the list
# and when they meet again they will be at the start of the loop.
import unittest
from LinkedList import LinkedList, Node

def loop_detection(linked_list: LinkedList):
  fast = slow = linked_list.head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow is fast:
      break
  if fast is None or fast.next is None:
    return None
  slow = linked_list.head
  while slow is not fast:
    slow = slow.next
    fast = fast.next
  return slow


class Test(unittest.TestCase):
# example: 1 -> 2 -> 3 -> 4 -> 5 -----
#                    ^                |
#                    |________________|

    def test_loop_detection(self):
      linked_list = LinkedList([1, 2, 3, 4, 5])
      three_node = linked_list.head.next.next
      linked_list.tail.next = three_node
      linked_list.tail = None
      loop_start_node = loop_detection(linked_list)
      self.assertEqual(three_node, loop_start_node)



if __name__ == "__main__":
    unittest.main()
