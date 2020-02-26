"""
The Depth First Search (DFS)

    The goal of a dfs is to search as deeply as possible, connecting as many nodes in the graph as possible and
    branching where necessary. Think of the BFS that builds a search tree one level at a time, whereas the DFS
    creates a search tree by exploring one branch of the tree as deeply as possible.

    As with bfs the dfs makes use of `predecessor` links to construct the tree. In
    addition, the dfs will make use of two additional instance variables in the Vertex class, `discovery` and
    `finish_time`.

        predecessor : same as bfs
        discovery   : tracks the number of steps in the algorithm before a vertex is first encountered;
        finish_time : is the number of steps before a vertex is colored black

"""
from datastruct.graph import Vertex, Graph


class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

    def reset(self):
        self.time = 0
        for v in self:
            v.color = 'white'
            v.predecessor = None

    def dfs(self):
        self.reset()

        for v in self:
            if v.color == 'white':
                self._dfs_visit(v)

    def _dfs_visit(self, vert: Vertex):
        vert.color = 'gray'
        self.time += 1
        vert.discovery = self.time
        for nextv in vert.get_connections():
            if nextv.color == 'white':
                nextv.predecessor = vert
                self._dfs_visit(nextv)
        vert.color = 'black'
        self.time += 1
        vert.finish_time = self.time



