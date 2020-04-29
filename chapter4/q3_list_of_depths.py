# given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (eg if you have a tree with depth D, you'll have D linked lists)

import unittest
from binary_tree import BinaryTree, BinaryTreeNode
from typing import List
from queue import Queue
from LinkedList import LinkedList

def list_of_depths(root_node: BinaryTreeNode, lists: List[LinkedList], level: int) -> List[LinkedList]:
    # base case. bottom of the tree
    if root_node is None:
        return
    list = LinkedList()
    if (len(lists) == level):
        # this level is not contained in the list. 
        # since levels are traversed in order, if this is the first item
        # at this level, we can insert the list at the end of the array
        lists.append(list)
    else:
        # this level is in the list
        list: LinkedList = lists[level]
    list.append_to_tail(root_node.name)
    list_of_depths(root_node.left, lists, level + 1)
    list_of_depths(root_node.right, lists, level + 1)
    return lists

def run_list_of_depths(binary_tree: BinaryTree) -> List[LinkedList]:
    return list_of_depths(binary_tree.root, [], 0)

    


class Test(unittest.TestCase):
    def test_list_of_depths(self):

#          1
#       /     \
#      2        3
#    /   \     / \ 
#   4     5   6    7
        six_node = BinaryTreeNode("6")
        seven_node = BinaryTreeNode("7")
        three_node = BinaryTreeNode("3", six_node, seven_node)
        four_node = BinaryTreeNode("4")
        five_node = BinaryTreeNode("5")
        two_node = BinaryTreeNode("2", four_node, five_node)
        one_node = BinaryTreeNode("1", two_node, three_node)
        binary_tree = BinaryTree(one_node)
        response = run_list_of_depths(binary_tree)
        list_one: LinkedList = response[0]
        self.assertEqual('1', list_one.head.data)
        list_two = response[1]
        self.assertEqual('2', list_two.head.data)
        list_three = response[2]
        self.assertEqual('4', list_three.head.data)


if __name__ == "__main__":
    unittest.main()