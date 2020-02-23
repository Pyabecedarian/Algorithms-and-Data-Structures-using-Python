"""
Problem Solving: the Knight's Tour Problem
    The knight's tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle
    is to find a sequence of moves that allow the knight to visit every square on the board exactly once.

    Solution:
        > Represent the legal moves of a knight on a chessboard as a graph
        > Use a graph algorithm to find a path of length `rows*columns - 1` where every vertex on the graph is visited
          exactly once.

    Details:
        1. Build the knight's tour graph (see the code in `build_knight_tour_graph`).

                     _     *1*       _      *3*      _              Vertex 12 should connect:

                    *5*      _       _       _      *9*               [ 5, 15, 1, 21, 3, 23, 9, 19 ]

                     _       _    *12*       _       _

                   *15*      _       _       _     *19*

                     _     *21*      _     *23*      _

        Start at vertex 12, a knight can moves to 8 places, each of them can represented by a couple of offsets
        to the original vertex. The offset of row/column can be [-2, -1, 1, 2]. Then we can calculate the
        tour vertex by the formula:
                            tour_vertex = new_row * board_size + new_col

        2. The search algorithm for this problem to find a path that has exactly 63 edges is DFS, which creates
           a search tree by exploring one branch of the tree as deeply as possible. Whereas the BFS builds a
           search tree one level at a time.

           DFS uses a Stack to backtracking, since dfs is recursive.

        3. Speed up the algorithm with heuristics by choose the next connected vertex of currVert to a vertex has
           the smallest connected vertices list.
"""
from datastruct.graph import Vertex, Graph
from functions.sorting import quick_sort


def build_knight_tour_graph(board_size: int = 8) -> Graph:
    """Build a knight tour graph given the chessboard size."""
    g = Graph()

    # offsets of rows and column for the knight tour on chess board
    offsets = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
               (1, 2), (1, -1), (2, 1), (2, -1)]

    for row in range(board_size):
        for col in range(board_size):
            curr_key = row * board_size + col

            # generate legal moves for this vertex
            for offset in offsets:
                to_row = row + offset[0]
                to_col = col + offset[1]

                # the legal moves must not go out of the board
                if 0 <= to_row < board_size and 0 <= to_col < board_size:
                    to_key = to_row * board_size + to_col
                    g.add_edge(curr_key, to_key)
    return g


def dfs(n: int, limit: int, path: list, v: Vertex):
    """Depth first search the knight's tour graph to find a path as deep as possible for the solution.
    The function will be recursively invoked, where
        :argument n: the current path length
        :argument limit: the final length of the solution
        :argument path: a list containing vertices tp build the path for the solution
        :argument v: a vertex that is going to be searched in this invocation

    NOTE:
    This function calling will be very slow for a 8x8 chessboard, since its complexity is O(k^N) where k
    is the average number of vertices in adjacent list and N is the solution length, for a 8x8 board k is
    roughly 5.25 and N is 64.
    """
    v.color = 'gray'
    path.append(v)
    if n < limit:
        connected = list(v.get_connections())
        i = 0
        done = False
        while i < len(connected) and not done:
            if connected[i].color == 'white':
                done = dfs(n + 1, limit, path, connected[i])
            i += 1

        if not done:
            path.pop()
            v.color = 'white'
    else:
        done = True

    return done


def dfs_speed_up_version(n: int, limit: int, path: list, v: Vertex):
    """A speedup version of dfs in which a sorting algorithm was implemented in sorting the next vertex for dfs
    from vertex with smallest adjacent list to largest. This technique is called `heuristics`, this will finally
    speed up the running time for dfs from half an hour original to several seconds."""
    v.color = 'gray'
    path.append(v.key)
    if n < limit:
        ordered_connected = orderByAvail(v)
        i = 0
        done = False
        while i < len(ordered_connected) and not done:
            if ordered_connected[i].color == 'white':
                done = dfs_speed_up_version(n + 1, limit, path, ordered_connected[i])
            i += 1

        if not done:
            path.pop()
            v.color = 'white'
    else:
        done = True

    return done


def orderByAvail(v: Vertex) -> list:
    """Sort the connected vertices from vertex with smallest adjacent list to largest.
    This function will replace the `get_connection` function in original dfs to get the
    next connected vertex. With this, our dfs will finally running within several seconds.
    """
    res = []
    for tv in v.get_connections():
        if tv.color == 'white':
            c = 0
            for ntv in tv.get_connections():
                if ntv.color == 'white':
                    c += 1
            res.append((c, tv))

    quick_sort(res, key=lambda x: x[0])
    return [i[1] for i in res]


if __name__ == '__main__':
    g = build_knight_tour_graph()

    for v in g:
        print(v)

    path = []
    # dfs(0, 63, path, g.get_vertex(5))  # take very lone time
    dfs_speed_up_version(0, 63, path, g.get_vertex(5))
    print(path)
