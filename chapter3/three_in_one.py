# describe how  you could use a single array to implement three stacks

import unittest
from typing import List

class StackInfo:
    def __init__(self, start_idx, capacity):
      self.start_idx = start_idx
      self.capacity = capacity
      self.size = 0
    def is_full(self):
      return True if self.size == self.capacity else False
    def is_empty(self):
      return True if self.size is 0 else False

    def last_capacity_index(self):
      # note this could return an index that is outside of the bounds of the multi-stack array
      return self.start_idx + self.capacity - 1

    def is_within_stack_capacity(self, index, multi_stack):
      if index < 0  or index >= multi_stack.total_array_capacity:
        return False
      # if index wraps around, adjust it
      contiguoous_index = index + multi_stack.total_array_capacity if index < self.start_idx else index
      end = self.start_idx + self.capacity
      return self.start_idx <= contiguoous_index and contiguoous_index < end

    def last_element_index(self):
      # note this coule return an index that is outside of the bounds of the mult-stack array
      return self.start_idx + self.size - 1

class MultiStack:
  def __init__(self, num_stacks, default_size):
    # create stack info for each stack
    self.total_array_capacity: int = num_stacks * default_size
    self.num_stacks: int = num_stacks
    self.stack_infos: List[StackInfo] = [0] * num_stacks
    for i in range(num_stacks):
      self.stack_infos[i] = StackInfo(default_size * i, default_size)
    self.values = [0] * (num_stacks * default_size)

  def is_empty(self, stack_num):
    return self.stack_infos[stack_num].is_empty()

  def push(self, item, stack_number):
    if self.all_stacks_are_full():
      return None
    # if this stack is full, expand it
    stack_info: StackInfo = self.stack_infos[stack_number]
    if stack_info.is_full():
      self.expand(stack_number)
    stack_info.size += 1
    last_element_index = self.adjust_index(stack_info.last_element_index())
    self.values[last_element_index] = item

  def previous_index(self, index):
    # adjusts for wraparound
    return self.adjust_index(index-1)

  def shift(self, stack_to_shift):
    stack_info = self.stack_infos[stack_to_shift]
    # if this stack is at its capacity, you need to move the next stack over.
    if stack_info.size >= stack_info.capacity:
      next_stack = (stack_to_shift + 1) %  self.num_stacks
      self.shift(next_stack)
      stack_info.capacity += 1

    # shift all elements in the stack over by one
    index: int = self.adjust_index(stack_info.last_capacity_index())
    while stack_info.is_within_stack_capacity(index, self):
      self.values[index] = self.values[self.previous_index(index)]
      index = self.previous_index(index)


  def expand(self, stack_num):
    stack_to_shift = (stack_num +1) %  (len(self.stack_infos))
    self.shift(stack_to_shift)
    self.stack_infos[stack_num].capacity += 1

  def number_of_elements(self):
    count = 0
    for info in self.stack_infos:
      count += info.size

  def all_stacks_are_full(self):
    if self.number_of_elements() is self.total_array_capacity:
      return True
    else:
      return False

  def adjust_index(self, index):
    # accounts for negative mods for wrap around
    max = self.total_array_capacity
    contigous_index = (index % max) + max
    return contigous_index % max 

  def peek(self, stack_num):
    # return top element of the stack
    stack_info = self.stack_infos[stack_num]
    last_element_index = stack_info.last_element_index()
    last_element_index  = self.adjust_index(last_element_index)
    return self.values[last_element_index]
  
  def pop(self, stack_num: int):
    stack_info = self.stack_infos[stack_num]
    if stack_info.is_empty():
      return None
    last_element_index = stack_info.last_element_index()
    last_element_index = self.adjust_index(last_element_index)
    value = self.values[last_element_index]
    self.values[last_element_index] = 0
    stack_info.size -= 1
    return value

class Test(unittest.TestCase):
  def test_is_empty(self):
    num_stacks = 3
    default_size = 2
    multi_stack = MultiStack(num_stacks, default_size)
    self.assertTrue(multi_stack.is_empty(2))
    # remember stacks are zero indexed
    multi_stack.push(1, 2)
    self.assertFalse(multi_stack.is_empty(2))

  def test_peek(self):
    num_stacks = 3
    default_size = 2
    multi_stack = MultiStack(num_stacks, default_size)
    multi_stack.push(1, 2)
    multi_stack.push(2, 2)
    self.assertEqual(2, multi_stack.peek(2))
    # push a value that will cause the stack to expand and wrap around
    multi_stack.push(3, 2)
    self.assertEqual(3, multi_stack.peek(2))

  def test_pop(self):
    num_stacks = 3
    default_size = 2
    multi_stack = MultiStack(num_stacks, default_size)
    multi_stack.push(1, 1)
    multi_stack.push(2, 1)
    multi_stack.push(3, 1)
    popped = multi_stack.pop(1)
    self.assertEqual(3, popped)
    self.assertEqual(2, multi_stack.peek(1))

if __name__ == "__main__":
    unittest.main()
