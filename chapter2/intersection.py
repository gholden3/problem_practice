# given two singly linked lists, determine if the two lists intersect. return the intersecting node. 
# note that intersection is defined based on reference, not value. that is, if the kth node in the first list 
# is the exact same node (by reference) as the jth node of the second linked list, they are intersecting. 


import unittest
from LinkedList import LinkedList, Node

def find_last_node_of_list(linked_list):
  current_node = linked_list.head
  if current_node is None:
    return -1
  if current_node.next is None: 
    return current_node
  while(current_node.next):
   current_node = current_node.next
  return current_node

def advance_pointer(linked_list, number_to_advance):
  node = linked_list.head
  while number_to_advance > 0:
    node = node.next
    number_to_advance -= 1
  return node

def intersection(list_one, list_two) -> bool:
  last_node_one = find_last_node_of_list(list_one)
  last_node_two = find_last_node_of_list(list_two)
  if last_node_one is not last_node_two:
    return False

  length_one = len(list_one)
  length_two = len(list_two)
  starting_node_one = list_one.head
  starting_node_two = list_two.head

  if length_two > length_one:
    starting_node_two = advance_pointer(list_two, (length_two - length_one))
  elif length_one > length_two:
    starting_node_one = advance_pointer(list_one, length_one - length_two)
  
  while starting_node_one is not starting_node_two:
    starting_node_one = starting_node_one.next
    starting_node_two = starting_node_two.next

  return starting_node_one



class Test(unittest.TestCase):
  def test_intersection_true(self):
    tail = LinkedList([7, 2, 1])
    list_one = LinkedList([3, 1, 5, 9])
    list_one.append_node_to_tail(tail.head)
    list_two = LinkedList([4, 6])
    list_two.append_node_to_tail(tail.head)
    self.assertEqual(tail.head, intersection(list_one, list_two))

  def test_false(self):
    list_one = LinkedList([3, 1, 5, 9, 7, 2, 1])
    list_two = LinkedList([4, 6, 7, 2, 1])
    self.assertFalse(intersection(list_one, list_two))

if __name__ == "__main__":
    unittest.main()