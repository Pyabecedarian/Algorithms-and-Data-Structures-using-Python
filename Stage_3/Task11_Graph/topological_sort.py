"""
Topological Sort

    Problem Solving: decide the steps that stirring up a batch of pancake.
        Recipe:
            1 egg
            1 cup of pancake mix
            1 tablespoon oil
            3/4 cup of milk
            heap the griddle, mix all the ingredients together and spoon the mix onto a hot griddle.
            When the pancake start to bubble, then turn them over and let them cook until they are
            golden brown on bottom

        Graph:
                   1 egg  --------------
                                        \                     heap griddle
                                         ↓                         ↓
               1 Tbl oil  -------->   1 cup mix  -------->    pour 1/4 cup
                                         ↑  :                      ↓
                                        /   :                turn when bubble
            3/4 cup milk  -------------     :                      ↓
                                            :            cook until golden brown
                                            ↓                      ↓
                                        heap syrup ------------>  eat

    To make decision the precise order in which we would do each of the steps required to make the pancake,
    we turn to a graph algorithm called the `Topological Sort`.

    A topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices such
    that if the graph G contains an edge (v, w) then the vertex v comes before the vertex w in the ordering.
    Directed acyclic graph are used in many applications to indicate the precedence charts for optimizing
    database queries, and multiple matrices.

    The topological sort is a simple but useful adaptation of a depth first search. The algorithm for the
    topological sort is as follows:
        > 1. Call dfs(g) for some graph g. The main reason we want to call dfs is to compute the `finish_time`
             for each of the vertices;
        > 2. Store the vertices in a list in decreasing order of finish_time;
        > 3. Return the ordered list as the result of the topological sort.

"""
from datastruct.graph import Graph, Vertex
from functions.sorting import quick_sort


def stir_up_pancake_graph() -> Graph:
    """Build a graph that follows the recipe of stirring up a pancake"""
    g = Graph()
    g.add_edge('1 egg', '1 cup mix')
    g.add_edge('1 Tbl oil', '1 cup mix')
    g.add_edge('3/4 cup milk', '1 cup mix').add_next('pour 1/4 cup')
    g.add_edge('heap griddle', 'pour 1/4 cup').add_next('turn when bubble'). \
        add_next('cook until golden brown'). \
        add_next('eat')

    g.add_edge('1 cup mix', 'heap syrup').add_next('eat')
    return g


def dfs(g):
    """Do a dfs on graph g, such that all vertices's instance variable are
    set appropriately for topological sort"""
    global time
    time = 0

    for v in g:
        v.discovery = 0
        v.finish_time = 0
        v.color = 'white'

    for v in g:
        if v.color == 'white':
            dfs_visit(v)


def dfs_visit(v: Vertex):
    """Helper function of dfs"""
    global time
    v.color = 'gray'
    time += 1
    v.discovery = time
    for next_vert in v.get_connections():
        if next_vert.color == 'white':
           dfs_visit(next_vert)

    v.color = 'black'
    time += 1
    v.finish_time = time
    return time


def topological_sort(g) -> list:
    """Return the precise steps of stirring up a batch of pancake"""
    dfs(g)
    res = [v for v in g]
    quick_sort(res, key=lambda v: v.finish_time)
    res.reverse()
    return res


if __name__ == '__main__':
    time = 0
    g = stir_up_pancake_graph()
    steps = topological_sort(g)
    print(steps)
    for v in steps:
        print(v, '\t', v.finish_time)