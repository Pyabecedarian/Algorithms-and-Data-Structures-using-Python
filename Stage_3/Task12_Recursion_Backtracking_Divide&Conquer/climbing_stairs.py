"""
Recursion:  Climbing Stairs(link: https://leetcode-cn.com/problems/climbing-stairs)


You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps


Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

Idea:
    Use recursion:
        Think of we have already achieved at stair n-1, there is only 1 stair left thus we only need
        to take 1 more step to get to the top. If we have already achieved at stair n-2, therefore we
        also can get to the top by taking 2 more steps. So the number of ways to climb to stair n
        is the ways that climb to n-1 plus the ways that climb to n-2:
                                        f(n) = f(n-1) + f(n-2)

        Then the ways to climb to n-1 can be expressed by n-2 and n-3, ... all the way to the base case.

        See the recursive version of the code in `climb_stairs_recursion`.


    Use Dynamic Programming:
        Look at the code in recursive version, we can see lots of repeating computations on the same
        number of stairs in the algorithm.
                                               f(5)
                                        f(4)          f(3)
                                    f(3)   f(2)   f(2)   f(1)
        To compute f(5) we have to compute f(4) and f(3), but to compute f(4) we need to compute f(3) again.
        This problem will be more severe when n is large. Why not store all the results in the lower level
        to compute the higher level problem?
                                            f(5)
                                                    f(4)
                                                            f(3)
                                                                    f(2)
                                                                            f(1)

        See the code of dp version in `climb_stairs_dp`.

"""


def climb_stairs_recursion(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs_recursion(n - 1) + climb_stairs_recursion(n - 2)


def climb_stairs_dp(n: int) -> int:
    res = [0, 1, 2]
    for i in range(3, n+1):
        res.append(res[i-1] + res[i-2])
    return res[n]


def climb_stairs_final(n: int) -> int:
    """Optimize Space complexity"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        pre_n1, pre_n2 = 1, 2
        for i in range(3, n+1):
            pre_n1, pre_n2 = pre_n2, pre_n1 + pre_n2
        return pre_n2


if __name__ == '__main__':
    print(climb_stairs_recursion(4))
    print(climb_stairs_dp(4))
    print(climb_stairs_final(4))