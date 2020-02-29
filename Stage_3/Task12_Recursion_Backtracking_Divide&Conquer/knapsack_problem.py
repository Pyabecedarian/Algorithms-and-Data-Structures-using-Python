"""
The 0/1 Knapsack problem

    Given n items with associated weights W and values V, how to choose the items to put them into a knapsack
    of capacity C such that the total value in the knapsack is maximum?

    NOTE: Each item can only be put (1) or not put (0) into the knapsack. To put a fraction of one item is
          not allowed.

Idea:
    Assume we have 4 items with weights and value as in the table bellow, and a knapsack of capacity 6:

                            item    weight    value
                             a        1         6
                             b        2        10
                             c        3        12
                             d        5        18

    We can try every possible combinations of items within which their total weight is less than or equal
    to capacity 6. We can count the maximum total value, therefore we can find the combination which is
    the optimal solution for the problem.

    Let's see how many combinations can we get from 5 items, start at putting d or not in knapsack:

                                      start (C=6,V=0)
                                   /                  \
                    d_1 (C=1,V=18)                    d_0 (C=6,V=0)
                    /    \                                   /   \
               None   C_0 (C=1,V=18)             c_1 (C=3,V=12)    c_1 (C=6,V=0)
                   /     \                                  /   \               / \
              None  b_0 (C=1,V=18)            b_1 (C=1,V=22)    b_0        ...     ...
                  /      \                               /  \     / \
    a_1 (C=0,V=24)  a_0 (C=1,V=18)         a_1 (C=0, V=28)  a_0 ... ...

    As you can see that the solution is in the binary tree of combinations, thus the time complexity
    is O(2^n).


    Recursion
    Assume we have got the maximum value in a combination of n-1 items, let f be the function that
    can get the maximum value, then the final solution must be in one of the following cases:

        > case 1:
            if the knapsack has no capacity for item_n, then
                                max_value = f(n-1, C)

        > case 2:
            if the knapsack has enough capacity for item_n, we need to make a decision whether or not
            to put item_n into the knapsack, because if we choose item_n, we may evict other items from
            the previous `n-1 combination`. Therefore we have two options as follows:

                >> Option 1: We choose item_n for solution, the maximum value will be
                            max_value_op1 = f(n-1, C-item_n.weight) + item_n.value

                >> Option 2: We don't choose item_n, then
                            max_value_op2 = f(n-1, C)

            In case 2, we now can conclude that:
                     max_value = max{ max_value_op1, max_value_op2 }

    Base case
    If there is no item to be checked, or no capacity, then f(0, *) or f(*, 0) must be 0.

    see the recursive version in code `knapsack_recursion()` function


    Dynamic Programming
    In the recursive version, we have visited all possible combinations of items to get the maximum value, the
    complexity is O(2^n). There will be many duplicated computations in the recursive version, since we always
    need to compute the `maximum_value` on deeper lever of the binary tree. For example, whether or not the
    algorithm decide to include item_d, it always need to compute whether or not to include item_b or item_a in
    deeper recursive call. But if we decide whether or not to include item_c, we will recompute item_b or item_a
    again.

    Just like what we did in `climbing_stairs` that we can store the intermediate results we first compute it,
    so if the algorithm need it again, the function can get the intermediate result directly rather than
    compute it again.

    see the dynamic programming version in code `def knapsack_dp()` function.


"""


class Item(object):
    def __init__(self, name: str, weight: int = 0, value: int = 0):
        self.n = name
        self.w = weight
        self.v = value

    def __repr__(self):
        return f'{self.n}'


def knapsack_recursion(n: int, c: int):
    global items

    if n == 0 or c == 0:
        return 0, ()
    else:
        item = items[n]

        # Case_1
        if item.w > c:
            res, comb = knapsack_recursion(n - 1, c)

        # Case_2
        else:
            # Option_1
            res1, comb1 = knapsack_recursion(n - 1, c - item.w)
            res1 += item.v
            comb1 += (item,)

            # Option_2
            res2, comb2 = knapsack_recursion(n - 1, c)

            # Choose the larger option
            if res1 >= res2:
                res = res1
                comb = comb1
            else:
                res = res2
                comb = comb2

    return res, comb


def knapsack_dp(n: int, c: int):
    result = [[None for _ in range(c + 1)] for _ in range(n + 1)]
    return knapsack_dp_helper(n, c, result)


def knapsack_dp_helper(n: int, c: int, result: list):
    global items

    if result[n][c] is not None:
        return result[n][c]
    elif n == 0 or c == 0:
        return 0, ()
    else:
        item = items[n]
        if item.w > c:
            return knapsack_dp_helper(n - 1, c, result)
        else:
            res1, comb1 = knapsack_dp_helper(n - 1, c - item.w, result)
            res1 += item.v
            comb1 += (item,)

            res2, comb2 = knapsack_dp_helper(n - 1, c, result)

            if res1 >= res2:
                result[n][c] = res1, comb1
                return res1, comb1
            else:
                result[n][c] = res2, comb2
                return res2, comb2


if __name__ == '__main__':
    a = Item('a', 3, 100)
    b = Item('b', 2, 20)
    c = Item('c', 4, 60)
    d = Item('d', 1, 40)
    capacity = 5

    items = [None, b, d, a, c]

    max_value, max_comb = knapsack_recursion(len(items) - 1, capacity)
    print(max_value, max_comb)

    print(knapsack_dp(len(items) - 1, capacity))
