from typing import List


class Node(): 
    def __init__(self, name, children: List[int]):
        self.name: str = name
        self.children: List[int] = children
        self.visited = False


    def __str__(self):
        return f" {self.name} "

    def visit(self):
        print(self)


class Tree:
    def __init__(self, root):
        self.root: Node = root       

    def depth_first_search(self, node: Node) -> None:
        if node:
            for child in node.children:
                self.depth_first_search(child)
                node.visit()

