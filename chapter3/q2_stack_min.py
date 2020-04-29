# how would you design a stack which, in addition to push and pop, has a function "min" which returns the minimum element? 
# push, pop, and min should all operate in O(1) time

# general solution: keep a second stack that keeps track of the "local mins"
import unittest
from stack import MyStack, StackNode

class MinStack(MyStack):
  def __init__(self):
    super(MinStack, self).__init__()
    self.local_mins = MyStack()

  def push(self, data: int):
    super(MinStack, self).push(data)
    if self.local_mins.top is None:
      self.local_mins.push(data)
    elif self.local_mins.top.data > data:
      self.local_mins.push(data)
  
  def pop(self):
    node: StackNode = super(MinStack, self).pop()
    data: int = node.data
    if data == self.local_mins.top.data:
      self.local_mins.pop()
    return node
    


  def min(self):
    return self.local_mins.top.data


class TestStackMin(unittest.TestCase):
  def test_stack_min(self):
    my_stack = MinStack()
    my_stack.push(4)
    my_stack.push(5)
    my_stack.push(2)
    my_stack.push(7)
    self.assertEqual(2, my_stack.min())
    my_stack.push(1)
    my_stack.push(4)
    self.assertEqual(1, my_stack.min())
    my_stack.pop()
    my_stack.pop()
    self.assertEqual(2, my_stack.min())
    my_stack.pop()
    my_stack.pop()
    self.assertEqual(4, my_stack.min())


if __name__ == "__main__":
    unittest.main()