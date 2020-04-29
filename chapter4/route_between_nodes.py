import unittest
from graph import Graph, GraphNode
from typing import List

def route_between_nodes(graph: Graph, node_one: GraphNode, node_two: GraphNode) -> bool:
    '''Returns whether there is a route between two nodes in a directed graph'''
    return graph.breadth_first_search(node_one, node_two)



class Test(unittest.TestCase):
# 0--->1<----2
# |  \ |  \  ^
# v   vv    v|
# 5    4<----3

    graph = Graph()
    sizegraph = 8
    temp: List[GraphNode] = []

    temp.append(GraphNode("0", 3))
    temp.append(GraphNode("1", 2))
    temp.append(GraphNode("2", 1))
    temp.append(GraphNode("3", 2))
    temp.append(GraphNode("4", 0))
    temp.append(GraphNode("5", 5))
    temp.append(GraphNode("6", 6))
    temp.append(GraphNode("7", 7))

    temp[0].add_adjacent(temp[1])
    temp[0].add_adjacent(temp[4])
    temp[0].add_adjacent(temp[5])
    temp[1].add_adjacent(temp[4])
    temp[1].add_adjacent(temp[3])
    temp[2].add_adjacent(temp[1])
    temp[3].add_adjacent(temp[2])
    temp[3].add_adjacent(temp[4])
    temp[6].add_adjacent(temp[7])

    for i in range(sizegraph):
        graph.add_node(temp[i])

    def test_route_between_nodes(self):
        self.assertEqual(True, route_between_nodes(self.graph, self.temp[0], self.temp[3]))
        self.assertEqual(False, route_between_nodes(self.graph, self.temp[0], self.temp[6]))


if __name__ == "__main__":
    unittest.main()