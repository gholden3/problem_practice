from typing import List
import unittest
import queue

class GraphNode:
    def __init__(self, name: str, adjacent_length: int):
        self.name = name
        self.visited = False
        self.adjacent = [0] * adjacent_length
        self.adjacent_count = 0
        # use marked to signify that this node has been put into the bfs queue
        self.marked = False

    def __str__(self):
        return f" {self.name} "

    def visit(self):
        print(self)
        self.visited = True
    
    def add_adjacent(self, node):
        self.adjacent[self.adjacent_count] = node
        self.adjacent_count += 1

class Graph:
    def __init__(self):
        self.nodes = []


    def add_node(self, node: GraphNode):
        self.nodes.append(node)

    # dfs is a little simpler and therefore preferred if we know we need to 
    # visit every node in the graph
    def depth_first_search(self, root: GraphNode):
        if root is None:
            return 
        root.visit()
        for adjacent_node in root.adjacent:
            if adjacent_node.visited == False:
                self.depth_first_search(adjacent_node)


    # often preferred if we want to find the shortest path or any path between two nodes
    # not recursive. uses a queue
    def breadth_first_search(self, root: GraphNode, node_to_find: GraphNode):
        ''' returns true or false based on if the node to find exists in the graph starting at root'''
        if root is None: 
            return
        if root == node_to_find:
            return True
        q = queue.Queue(len(self.nodes))
        root.marked = True
        # add root to the end of the queue
        q.put(root)
        while not q.empty():
            # remove from the front of the queue
            r: GraphNode = q.get()
            r.visit()
            for i in range(0,r.adjacent_count):
                n: GraphNode = r.adjacent[i]
                if n == node_to_find:
                    return True
                if not n.marked:
                    n.marked = True
                    q.put(n)
        return False
        

class Test(unittest.TestCase):
# 0--->1<----2
# |  \ |  \  ^
# v   vv    v|
# 5    4<----3


    graph = Graph()
    sizegraph = 6
    temp: List[GraphNode] = []

    temp.append(GraphNode("0", 3))
    temp.append(GraphNode("1", 2))
    temp.append(GraphNode("2", 1))
    temp.append(GraphNode("3", 2))
    temp.append(GraphNode("4", 0))
    temp.append(GraphNode("5", 5))

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[4])
    temp[0].add_adjacent(temp[5])
    temp[1].add_adjacent(temp[4])
    temp[1].add_adjacent(temp[3])
    temp[2].add_adjacent(temp[1])
    temp[3].add_adjacent(temp[2])
    temp[3].add_adjacent(temp[4])

    for i in range(sizegraph):
        graph.add_node(temp[i])

    def test_bfs(self):
        self.graph.breadth_first_search(self.temp[0], self.temp[5])


if __name__ == "__main__":
    unittest.main()