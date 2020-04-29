# you have two numbers re[resented by a linked list, where each node contains a single digit. 
# the digits are stored in reverse order such taht the 1's digit is at the head of the list. 
# write a function that adds the two numbers and returns the sum as a linked list. 

# follow up: suppose the digits are stored in forward order. repeat the above problem. 

import unittest
from math import floor
from LinkedList import LinkedList, Node

def sum_two_nodes(first_node: Node, second_node: Node, carryover: int) -> (int, int):
    first_value = 0 if first_node is None else first_node.data
    second_value = 0 if second_node is None else second_node.data
    sum = first_value + second_value + carryover
    if(sum < 10):
        carryover = 0
    if(sum >= 10):
        carryover = floor(sum/10)
        sum = (sum % 10)
    return (sum, carryover)

def sum_lists(first_list: LinkedList, second_list: LinkedList) -> LinkedList:
    first_node = first_list.head
    second_node = second_list.head
    return_list = LinkedList()
    carryover = 0
    while((first_node is not None) or (second_node is not None)):
        (sum, carryover) = sum_two_nodes(first_node, second_node, carryover)
        return_list.append_to_tail(sum)
        first_node = first_node.next if first_node else None
        second_node = second_node.next if second_node else None
    if(carryover is not 0):
        return_list.append_to_head(carryover)
    return return_list

def zero_pad_if_different_lengths(first_list: LinkedList, second_list: LinkedList) -> (LinkedList, LinkedList):
    ''' Given two linked lists, pad zeros to the front of the shorter one'''
    first_length = first_list.length()
    second_length = second_list.length()
    if(first_length < second_length):
        [first_list.append_to_head(0) for _i in range(0, second_length - first_length)] 
    elif (second_length < first_length):
        [second_list.append_to_head(0) for _i in range(0, first_length - second_length)]
    return (first_list, second_list) 

def calculate_sum_lists(first_node: Node, second_node: Node, carryover, result_list):
    if(first_node.next is None and second_node.next is None):
        # base case. summing the last two nodes in the list
        (sum, carryover) = sum_two_nodes(first_node, second_node, carryover)
        # append the sum to the result list and return result list and carryover
        result_list.append_to_head(sum)
        return(result_list, carryover)
    (result_list, carryover) = calculate_sum_lists(first_node.next, second_node.next, carryover, result_list)
    (sum, carryover) = sum_two_nodes(first_node, second_node, carryover)
    # append the sum to the result list and return result list and carryover
    result_list.append_to_head(sum)
    return(result_list, carryover)

def sum_lists_followup(first_list: LinkedList, second_list: LinkedList) -> LinkedList:
    (first_list, second_list) = zero_pad_if_different_lengths(first_list, second_list)
    result_list = LinkedList()
    (result_list, carryover) = calculate_sum_lists(first_list.head, second_list.head, 0, result_list)
    return result_list


class TestSum(unittest.TestCase):
    def test_sum_lists(self):
        first_list = LinkedList([7, 1, 6])
        second_list = LinkedList([5, 9, 2])
        
        result_list = sum_lists(first_list, second_list)
        # expected: 2 -> 1 -> 9
        print(result_list)

        first_list = LinkedList([6, 1, 7])
        second_list = LinkedList([2, 9, 5])
        
        result_list = sum_lists_followup(first_list, second_list)
        # expected: 9 -> 1 -> 2
        print(result_list)


        first_list = LinkedList([1, 2, 3, 4])
        second_list = LinkedList([5, 6, 7])
        
        result_list = sum_lists_followup(first_list, second_list)
        # expected: 1 -> 8 -> 0 -> 1
        print(result_list)


if __name__ == "__main__":
    unittest.main()