"""
Dijkstra's Algorithm
    can determine the shortest weighted path from a particular node to all other nodes in a graph. This is
    similar to BFS.
                    V ----- 3 ----- W ---
                  / :         --- / :    \
                2   :       /   /   :     5
              /     :     5   /     :      \
            U --------- /   3       1       Z
             \      :     /         :     /
              1     2   /           :   1
               \    : /             : /
                --- X ----- 1 ----- Y

    To keep track of the total cost from start node to each destination we will make use of the `distance`
    instance variable in Vertex class.

        > distance: contain the current total weight of the smallest weighted path from start node to the vertex
                    in question. When the vertex is first created, distance is set to a very large number.

    The algorithm iterates once over every vertex in the graph, while the order that the iteration keeps is
    controlled by a Priority Queue, where the value of distance is the priority.

    The implementation of PriorityQueue/BinaryHeap in `Stage2/Task10` need to change a little bit that an
    additional method can update the item's priority in-place if the item's priority key has changed.

        > percItem(obj): is the additional method that takes the object already in heap as an argument and
                         swap it up to a proper position if the object's priority key has changed.

"""
from datastruct.collections import HashTable
from datastruct.abstract import BinaryHeap
from datastruct.graph import Vertex, Graph


class PriorityQueue(BinaryHeap):
    """A heap class for Dijkstra's algorithm that changes from BinaryHeap where we can get the value in heapList
    by a key using a HashTable"""

    def __init__(self, func=None):
        super(PriorityQueue, self).__init__(func=func)
        self.verts = HashTable()

    def heapify(self, g: Graph):
        iterable = [[v.distance, v] for v in g]
        super(PriorityQueue, self).heapify(iterable)
        for obj in iterable:
            self.verts[obj[1].key] = obj

    def heappop(self):
        popobj = super(PriorityQueue, self).heappop()
        del self.verts[popobj[1].key]
        return popobj[1]

    def percItem(self, vert: Vertex):
        obj = self.verts[vert.key]
        obj[0] = vert.distance
        super(PriorityQueue, self).percItem(obj)


def Dijkstra(g: Graph, start_key):
    """Search shortest path from start to all nodes in graph."""
    pq = PriorityQueue(func=lambda x: x[0])
    start = g[start_key]
    start.distance = 0
    pq.heapify(g)

    while len(pq) > 0:
        currVert = pq.heappop()
        for nextVert in currVert.get_connections():
            new_dist = currVert.distance + currVert.get_weight(nextVert)
            if new_dist < nextVert.distance:
                nextVert.distance = new_dist
                nextVert.predecessor = currVert
                pq.percItem(nextVert)


def path(g, f, t):
    """Return the shortest path in graph from vertex f to vertex t"""
    fv = g[f]
    tv = g[t]

    path_list = []
    while tv.predecessor:
        path_list.append(repr(tv))
        tv = tv.predecessor
    path_list.append(repr(tv))

    path_list.reverse()
    path = ' -> '.join(path_list)
    print(path)


if __name__ == '__main__':
    g = Graph()
    g.add_edge('u', 'v', 2).add_edge('v', 'u', 2)
    g.add_edge('u', 'x', 1).add_edge('x', 'u', 1)
    g.add_edge('u', 'w', 5).add_edge('w', 'u', 5)
    g.add_edge('v', 'x', 2).add_edge('x', 'v', 2)
    g.add_edge('v', 'w', 3).add_edge('w', 'v', 3)
    g.add_edge('x', 'w', 3).add_edge('w', 'x', 3)
    g.add_edge('x', 'y', 1).add_edge('y', 'x', 1)
    g.add_edge('w', 'y', 1).add_edge('y', 'w', 1)
    g.add_edge('w', 'z', 5).add_edge('z', 'w', 5)
    g.add_edge('y', 'z', 1).add_edge('z', 'y', 1)

    Dijkstra(g, 'u')
    path(g, 'u', 'z')
