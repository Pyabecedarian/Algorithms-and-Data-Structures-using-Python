"""
Graph
    is a set of vertices that connects by edges which may have costs (weights) from one vertex to another.

                                    w0               w1
                            V0  ---------->  V1  ---------> V2 --- ... -
                             |         w2                    ↑
                             ---------------------------------


Important Definitions
    Vertex
        is a `node` in graph

    Edge
        connects two vertices to show that there is a relationship between them. The edges may be one-way or
        two way. If the edges in graph are all one-way, the graph is a `direct graph` or a `digraph`.
        A edge can be represented by a tuple, (fromVertex, toVertex, weight).

    Weight
        is the cost to go from one vertex to another.

    Path
        is a sequence of vertices that are connected by edges.

    Cycle
        is a path in a digraph that starts and ends at the same vertex. A graph with no cycle is called `acyclic
        graph`.
        A digraph with no cycle is call `direct acyclic graph`, or `DAG`


Implementation Details
    There are two several ways can implement the `Graph` abstract data structure, the adjacency matrix and the
    adjacency list. The second is a space-efficient way to implement a sparsely connected graph.

    The adjacency list implementation keeps a master list of all the vertices in the Graph object, and
    each Vertex object in the graph maintains a list of the other vertices that it is connected to.

    Thr Vertex class uses a dictionary to keep track of the vertices to which it is connected, and the weight
    of each edge.
    The Graph class uses a dictionary that maps vertex keys to vertex objects.

        class Vertex
            self.key
            self.connected = { V0: w0, V1: w1, ... }
                                ↓
                              Vertex()

        class Graph:
            self.vertices_list = { k0: V0, k1: V1, ... }

                k0    :     V0          k1     :     V1...
                 ↓           ↓
            vert key     Vertex()

Possible methods of Graph() are as follows:
    > Graph()                           : constructor
    > addVertex(vert)                   : adds an instance of `Vertex` to the graph
    > addEdge(fromVert, toVert)         : adds a edge that connects two vertices
    > addEdge(fromVert, toVert, weight) : adds a new weighted edge
    > getVertex(vertKey)                : finds the vertex in the graph named by `vertKey`
    > in   statement
"""


class Vertex(object):
    """Vertex class that holds the vertex's key and a hash table to keep track of all the other vertices
    that it connected to.
    The hashtable's key is other vertices, value is the weight from this vertex to another."""

    def __init__(self, key):
        self.key = key
        self.connected = {}  # { Vertex object: weight, ... }

    def __str__(self):
        return f'{self.key}' + ' connected to ' + str([v.key for v in self.connected])

    def add_connections(self, vert, weight=0):
        assert isinstance(vert, Vertex)
        self.connected[vert] = weight

    def get_connections(self):
        return self.connected.keys()

    def get_weight(self, vert):
        assert isinstance(vert, Vertex)
        return self.connected.get(vert)


class Graph(object):
    def __init__(self):
        self.vertices_list = {}
        self.num_verts = 0

    def __iter__(self):
        return iter(self.vertices_list.values())

    def __contains__(self, key):
        return key in self.vertices_list

    def get_vertex(self, key):
        """Return the vertex object by key, or None if the key is not in vertices list."""
        return self.vertices_list.get(key)

    def add_vertex_by_key(self, vert_key):
        """Add a new Vertex object into the Graph and return the newly added vertex object."""
        self.num_verts += 1
        newVert = Vertex(vert_key)
        self.vertices_list[vert_key] = newVert
        return newVert

    def add_edge(self, from_key, to_key, weight=0):
        """Add an edge that connects two vertices."""
        from_vert = self.vertices_list.get(from_key)
        to_vert = self.vertices_list.get(to_key)
        if from_vert is None:
            from_vert = self.add_vertex_by_key(from_key)
        if to_vert is None:
            to_vert = self.add_vertex_by_key(to_key)

        from_vert.add_connections(to_vert, weight)


if __name__ == '__main__':
    g = Graph()

    for i in range(6):
        g.add_vertex_by_key(i)

    print(g.vertices_list)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 2)

    for fv in g:
        for tv in fv.get_connections():
            print(f'from {fv.key} to {tv.key}, weight:{fv.get_weight(tv)}')