"""
Backtracking: The Eight Queen Puzzle

Backtracking is an algorithmic paradigm that tries different solutions until finds a solution that `works`.
Problems which are typically solved using backtracking technique have following property in common:
    > these problem can be solved by trying every possible configurations, and
    > each configuration is tried only once.

The Eight-Queen puzzle or more general the N-Queen puzzle is the problem of placing N chess queens on an
N x N chessboard such that no two queens attack each other. `Attack` here means the next queen should
not be placed in the block that is of the same row, column and diagonal.

                         The queen attack area on 4x4 chessboard

                                    *    *    *    _

                                    *    X    *    *

                                    *    *    *    _

                                    _    *    _    *

                            (X: the Queen;  *: attack area)

Idea:
    The rule of the game tells that each row on the chessboard can place only ONE queen, the same as column.
    So we can try to place a queen on each row once at a time. Let's define the representation of the queen's
    position.
    We can represent the coordinate of the queen in a two dimensional matrix:
                                    [ 0, 1, 0, 0 ]
                                    [ 0, 0, 0, 1 ]
                                    [ 1, 0, 0, 0 ]
                                    [ 0, 0, 1, 0 ]
    Or we can also represent the places in a tuple, where the index of the each value is the row of the
    queen and the value itself is which column the queen is placed. For example,  s[0] = 1 means the queen
    on the 1st row places at column 2 (Note: the starting index is 0 in python).
                                          s[i] = col

    Representation:
    The first queen on the first row can be placed at any column in the beginning since there is no other
    queens on the board. But starts with the second queen, there will be some areas that cause `conflict`
    with the first queen. So we need a function that defines the conflict.


    Conflicts:
    The blocks are of the same rows and columns with the blocks that all the queens have been placed
    are not legal blocks. If `nextX` is the next column the queen is going to be placed, such that
                                   s[i] - nextX != 0,  for all i

    Again, the coordinate of the next queen is not allowed to be on the diagonal blocks of all previous queens,
    otherwise will cause a conflict. This can be expressed by the distance of the rows between every two queens
    must not be the same as the distance of their columns.
                              | s[i] - nextX |  !=  next_i - i

    Thus we have defined the conflict condition, see the code in `def conflict()` function.


    Procedure:
    We could first place a queen (row 1) at column 1, then to find the legal blocks for the next queen.
    Once we get the next legal blocks, we choose a block and find the next legal blocks for the third
    queen. Do the procedure until we find that:
        > 1. we have placed 8 queens, therefore the solution has found;
        > 2. we have no legal block for the next queen, thus we may think that the block of last queen
          is wrong, so we backtrack to the last queen and choose another legal block followed by repeat
          the procedure for the next queen.


    Implementation:
    See the procedure above, we need another function that can produce the legal blocks for the next queen.
    Given the previous queens' position, how could we produce all next legal blocks? Since we place the
    queens row by row, so the next queen's column must be in range of [0, n], while not meet the conflict
    condition.

    See the code in `def next_positions()` function.

    To let the algorithm follow the procedure where we have to backtrack the position when there is no
    legal blocks for the next queen, we may think that we need a Stack to preserve the current queen's
    position. If there is not next legal block, we pop the current queen's position and try another block.
    This lead to a recursive call of the main function naturally.


    Recursion:
    First let's deal with the base case. Assume all the queens before the last queen has placed properly,
    our main function will do as the same as what `next_positions()` did.

    Next we need to move the general case towards the base case in order to complete the recursion.
    We need the state `s` containing all the previous queens' position increases to length n - 1, we can
    add s with the position produces by last invocation. Therefore we need to change the return type to a
    tuple of length 1 other than a int.

    See the code in `def queen()` function.


    Optimization:
    We can see that in queen(), the for loop and conflict() invocation are the same, so we change the code
    to a simpler version, see the final code in `def queen_final()` function.
"""


def conflict(next_x: int, s: tuple) -> bool:
    """Return a boolean that defines the conflict condition of the next queen's position"""
    next_i = len(s)
    for i in range(next_i):
        if abs(s[i] - next_x) in (0, next_i - i):
            return True
    else:
        return False


def next_positions(n: int = 8, s: tuple = ()) -> tuple:
    """A generator that contains all legal positions for next queen"""
    for pos in range(n):
        if not conflict(pos, s):
            yield pos


def queen(n: int = 8, s: tuple = ()):
    """Main function of N-queen"""
    if len(s) == n - 1:  # base case
        for pos in range(n):
            if not conflict(pos, s):
                # yield pos
                yield (pos,)
    else:
        for pos in range(n):
            if not conflict(pos, s):
                for next_i in queen(n, s + (pos,)):
                    yield (pos,) + next_i


def queen_final(n: int = 8, s: tuple = ()):
    """Final version of N-queen solution"""
    for pos in range(n):
        if not conflict(pos, s):
            if len(s) == n - 1:
                yield (pos, )
            else:
                for next_pos in queen(n, s + (pos,)):
                    yield (pos,) + next_pos


if __name__ == '__main__':
    print(list(next_positions(4, (1, 3, 0))))
    print(list(queen(4, (1, 3, 0))))  # base case
    print(list(queen(4)))
    print(list(queen_final(4)))
