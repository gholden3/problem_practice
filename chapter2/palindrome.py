# implement a function to check if a linked list is a palindrome

import unittest
from LinkedList import LinkedList
from collections import deque

def is_palindrome(linked_list: LinkedList) -> bool:
  # push the first half of the list onto a stack
  fast_ptr = linked_list.head
  slow_ptr = linked_list.head
  my_stack = deque()
  while(fast_ptr != None):
    my_stack.append(slow_ptr.data)
    if fast_ptr.next and fast_ptr.next.next:
      fast_ptr = fast_ptr.next.next
      slow_ptr = slow_ptr.next
    else:
      fast_ptr = None
  slow_ptr = slow_ptr.next
  # remove the last element if stack length is odd
  if((len(my_stack) % 2)>0):
    my_stack.pop()
  while(my_stack):
    data = my_stack.pop()
    if(data != slow_ptr.data):
      return False
    slow_ptr = slow_ptr.next
  return True


class Test(unittest.TestCase):

  def test_palindrome(self):
    # ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
    # self.assertTrue(is_palindrome(ll_true))
    ll_true = LinkedList([1, 2, 3, 4,  4, 3, 2, 1])
    self.assertTrue(is_palindrome(ll_true))
    ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    self.assertFalse(is_palindrome(ll_false))


if __name__ == "__main__":
    unittest.main()