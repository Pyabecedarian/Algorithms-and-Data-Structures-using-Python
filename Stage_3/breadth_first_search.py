"""
The Breath First Search (BFS)

    is one of the easiest algorithms for searching a graph. Given a graph G and a starting vertex s, a bfs
    proceeds by exploring edges in the graph to find all the vertices in G for which there is a path from s.

    The remarkable thing about a bfs is that it finds all the vertices that are a distance k from s before
    it finds any vertex that are a distance k+1.

    The crucial point of BFS is using a Queue to keep track of the further vertices been explored, but not until
    all the other vertices on the adjacent list of current vertex have been explored.


Problem Solving: the Word Ladder Problem
    Transform the word `fool` into the word `sage`. You must make the change gradually by changing one letter at
    a time. At each step you must transform one word into another word, non-word is not allowed.

                        fool -> pool -> poll -> pale -> sale -> sage

    Solution:
        > Represent the relationships between words as a graph;
        > Use the graph algorithm known as breath first search to find an efficient path from the starting word
          to the ending word.

    Details:
        1. Build the Word Ladder Graph (see the code in  `build_ladder_graph` ).

                          fail --- fall                 pope
                          /            \              /
                       foil            pall --------/------
                       /  |             |         /         \       sale
                    foul  |             |     pole           \    /      \
                      \   |             |   /     \--------- pale       *sage*
                     *fool* ---       poll                      \       /
                        \      \     /                             page
                       cool --- pool

        Suppose we have a vocabulary of a list of words, to build a ladder graph with edges that connects two
        words that is different with only one letter, we could compare each word with every other word in
        vocabulary. In this way, roughly speaking, we need n^2 times of comparison. This works work fine if
        the vocabulary is small.

        A better way to build the graph is that suppose we have a huge number of buckets, each of them with a
        four-letter word on the outside, except that one of the letters in the label has been replaced by an
        underscore. Every time we find a matching bucket, we put our word in that bucket. Once we have all words
        in the appropriate buckets we know that all the words in the bucket must be connected.

            bucket                          words
             _ope           pope, rope, nope, hope, lope, mope, cope
             p_pe           pope, pipe, pape
             po_e           pope, pole, pore, pose, poke
             pop_           pope, pops



        2. Use BFS to search the ladder graph to find a shortest path from `fool` to `sage`.

        The BFS uses an extended version of class Vertex in which there are three additional instance variables,
        `predecessor` and `distance` and `color`.

            class Vertex
                self.key
                self.connected

                self.predecessor
                self.distance
                self.color


        Steps:
            BFS begins at the starting vertex s and colors s to `gray` to show that it is currently being explored.
            Place s onto a Queue. Next is to systematically explore vertices at the front of the queue.
            Dequeue and explore the current vertex on the front of Queue. As each node on the adjacent list is
            examined its color is checked. If it is white, the vertex is unexplored, and four things happen:

                1. The new, unexplored vertex v, is colored `gray`;
                2. The predecessor of v is set to the current node `currVert`;
                3. The distance to v is set to the distance to `currVert + 1`;
                4. Add the vertex v to the end of the queue.
"""
from datastruct.graph import Graph
from datastruct.abstract import Queue


def build_ladder_graph(vocab_file) -> Graph:
    """Build a ladder graph from a file of words"""
    buckets = {}
    g = Graph()
    for line in open(vocab_file):
        word = line.strip()
        for i in range(len(word)):
            label = word[:i] + '_' + word[i + 1:]
            buckets.setdefault(label, []).append(word)

    for label in buckets:
        for word1 in buckets[label]:
            for word2 in buckets[label]:
                if word1 != word2:
                    g.add_edge(word1, word2)
    return g


def bfs(g: Graph, s):
    """
    The Breadth First Search algorithm of a graph given a start vertex s.
    :param G: a graph object
    :param s: key of the start vertex
    """
    start = g.get_vertex(s)
    start.distance = 0
    start.predecessor = None

    q = Queue()
    q.enqueue(start)

    while not q.isEmpty():
        currVert = q.dequeue()
        for v in currVert.get_connections():
            if v.color == 'white':
                v.color = 'gray'
                v.distance = currVert.distance + 1
                v.predecessor = currVert
                q.enqueue(v)

        currVert.color = 'black'


def traverse(g: Graph, s):
    """Start at any vertex in graph and follow the predecessor arrow back to the start vertex after a bfs."""
    currVert = g.get_vertex(s)
    while currVert.get_pred():
        print(currVert.key, end=' -> ')
        currVert = currVert.get_pred()

    print(currVert.key)


if __name__ == '__main__':
    file = './vocab.txt'
    g = build_ladder_graph(file)
    for v in g:
        print(v)

    # find the shortest path using bfs
    bfs(g, 'fool')

    # traverse back through the graph
    traverse(g, 'sage')
