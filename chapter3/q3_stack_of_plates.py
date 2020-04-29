# imagine a stack of plates. if the stack gets too high, it might topple. 
# Therefore, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several 
# stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push()
# and SetOfStacks.pop() should behave identically to a single stack. That is, pop() should
# return the same value as it would if there were just a single tack. 

# follow-up: implement a function pop_at(index) which performs a pop operation on a specific sub-stack
import unittest
from stack import MyStack, StackNode
from typing import List

class MyStackWithCapacity(MyStack):
    def __init__(self, capacity):
        self.capacity = capacity
        MyStack.__init__(self)
        self.size = 0

    def push(self, data):
        if self.size >= self.capacity:
            return False
        self.size += 1
        MyStack.push(self, data)

    def pop(self) -> StackNode:
        ''' pops an item off of the top of the stack'''
        if not self.top:
            return -1
        self.size -= 1
        return MyStack.pop(self)

    def is_full(self):
        return self.size == self.capacity


class SetOfStacks:
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks: List[MyStackWithCapacity] = []

    def get_last_stack(self):
        return None if not self.stacks else self.stacks[-1]

    def push(self, data: int):
        last_stack: MyStackWithCapacity = self.get_last_stack()
        if not (last_stack is None) and not (last_stack.is_full()):
            last_stack.push(data)
        else:
            new_stack = MyStackWithCapacity(self.stack_capacity)
            new_stack.push(data)
            self.stacks.append(new_stack)

    def pop(self):
        last_stack: MyStackWithCapacity = self.get_last_stack()
        if last_stack is None:
            return -1
        node = last_stack.pop()
        if last_stack.size is 0:
            del self.stacks[-1]
        return node.data

    


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    # def test_pop_at(self):
    #     stacks = SetOfStacks(5)
    #     for i in range(35):
    #         stacks.push(i)
    #     lst = []
    #     for _ in range(31):
    #         lst.append(stacks.pop_at(0))
    #     self.assertEqual(lst, list(range(4, 35)))

if __name__ == '__main__':
    unittest.main()