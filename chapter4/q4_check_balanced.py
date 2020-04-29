# implement a function to check if a binary tree is balanced. 
# for the purposes of this question, a balanced tree is defined to be a tree such that the heights
# of the two subtrees of any node never differ by more than one


import unittest
from binary_tree import BinaryTree, BinaryTreeNode
ERROR = -3

def check_height(node: BinaryTreeNode) -> bool:
  if node is None:
    return -1
  left_height = check_height(node.left)
  if left_height is ERROR:
    return ERROR
  
  right_height = check_height(node.right)
  if right_height is ERROR:
    return ERROR
  
  height_diff = left_height - right_height
  if abs(height_diff) > 1:
    return ERROR
  else:
    return max(left_height, right_height) + 1

def check_balanced(binary_tree_node: BinaryTreeNode) -> bool:
  return check_height(binary_tree_node) is not ERROR

def run_check_balanced( binary_tree: BinaryTree) -> bool: 
  return check_balanced(binary_tree.root)

class Test(unittest.TestCase):
  def test_balanced_true_perfect(self):

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
    balanced = run_check_balanced(binary_tree)
    self.assertTrue(balanced)

  def test_balanced_true(self):
  
#          1
#       /     \
#      2        3
#    /   \     / 
#   4     5   6    
    six_node = BinaryTreeNode("6")
    three_node = BinaryTreeNode("3", six_node)
    four_node = BinaryTreeNode("4")
    five_node = BinaryTreeNode("5")
    two_node = BinaryTreeNode("2", four_node, five_node)
    one_node = BinaryTreeNode("1", two_node, three_node)
    binary_tree = BinaryTree(one_node)
    balanced = run_check_balanced(binary_tree)
    self.assertTrue(balanced)

  def test_balanced_false(self):
    
#          1
#       /     \
#      2        3
#    /   \     / 
#   4     5   6  
#         |
#         7  
#         |
#         8
    six_node = BinaryTreeNode("6")
    three_node = BinaryTreeNode("3", six_node)
    four_node = BinaryTreeNode("4")
    eight_node = BinaryTreeNode("8")
    seven_node = BinaryTreeNode("7", eight_node)
    five_node = BinaryTreeNode("5", seven_node)
    two_node = BinaryTreeNode("2", four_node, five_node)
    one_node = BinaryTreeNode("1", two_node, three_node)
    binary_tree = BinaryTree(one_node)
    balanced = run_check_balanced(binary_tree)
    self.assertFalse(balanced)


if __name__ == "__main__":
    unittest.main()