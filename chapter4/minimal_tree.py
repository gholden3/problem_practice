# given a sorted (ascending) array with unique integer elements, write an algorithm to create a 
# BST with minimal height

import unittest
from typing import List
from binary_tree import BinaryTree, BinaryTreeNode
from math import floor

def create_minimal_tree_runner(input_arr):
    root_node = create_minimal_tree(input_arr)
    return BinaryTree(root_node)

def create_minimal_tree(list_of_values: List[int]) -> BinaryTreeNode:
    length_of_list = len(list_of_values)
    if length_of_list == 1:
        node =  BinaryTreeNode(list_of_values[0])
        return node
    middle_index = floor(length_of_list/2)
    left_tree_root: BinaryTreeNode = create_minimal_tree(list_of_values[0:middle_index])
    right_tree_root: BinaryTreeNode = create_minimal_tree(list_of_values[middle_index+1:length_of_list])
    root_node: BinaryTreeNode = BinaryTreeNode(list_of_values[middle_index], left_tree_root, right_tree_root)
    return root_node

class Test(unittest.TestCase):
    def test_minimal_tree(self):
        input_arr = [1, 2, 3, 4, 5, 6, 7]
        tree: BinaryTree = create_minimal_tree_runner(input_arr)
        tree.in_order_traversal(tree.root)


if __name__ == "__main__":
    unittest.main()