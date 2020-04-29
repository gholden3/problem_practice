from typing import List
from tree import Tree, Node

class BinaryTreeNode(Node):
    def __init__(self, name, left = None, right = None):
        self.name: str = name
        self.left = left
        self.right = right

class BinaryTree(Tree): 
    # traverses left, node, right starting at a given node
    def in_order_traversal(self, node: BinaryTreeNode) -> None:
        if node:
            self.in_order_traversal(node.left)
            node.visit()
            self.in_order_traversal(node.right)

    # traverses node, left, right starting at given node
    def pre_order_traversal(self, node: BinaryTreeNode) -> None:
        if node:
            node.visit()
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # traverses in order left, right, node
    def post_order_traversal(self, node: BinaryTreeNode) -> None:
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            node.visit()
    
# def MinHeap(BinaryTree):
    #  def insert_into_min_heap(node: BinaryTreeNode):
        #insert the element at the bottom and swap with parents until 
        # the element is in its correct place

    # def extract_min_from_min_heap(node: BinaryTreeNode):
        # remove the min element from the top
        # place the bottommost right most element at the top and bubble it down, swapping
        # with the smaller of the left or right child


