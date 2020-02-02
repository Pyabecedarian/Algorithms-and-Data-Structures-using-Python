"""
* Task: Merge k sorted list using priority queue *

Analysis:
    The easies way is creating a n*k sized list and sort. The best sorting algorithm will be in O(nk log nk) time.
    If make use of the priority queue, We can do better in O(nk log k).

    Steps:
        0. Create a empty list;
        1. Create a Min Heap, push the 1st elements in each list, the minimum value must be on top of the heap;
        2. Pop the top and push the next element from which list the pop operation has just performed;
        3. Repeat the steps until all element in k lists are consumed.
"""
from datastruct import BinaryHeap


def mergeLists(*iterables, func=None):
    """
    Merge k sorted lists into a whole sorted list.

    :param iterables: any number of iterables, must be already sorted in ascending order.
    :return: an generator of the result list.
    """
    k = len(iterables)
    its = list(map(iter, iterables))  # [ it0, it1, ... itk ]

    # build an heap of k size
    hp = BinaryHeap(func=func)
    for i, it in enumerate(its):
        hp.heappush((next(it), i))

    # repeatedly push and pop element from iterables
    while True:
        tmp_value, i = hp.heappop()
        yield tmp_value

        try:
            hp.heappush((next(its[i]), i))
        except StopIteration:
            # the i-th iterable is exhausted, if no items in heap, merge complete
            if len(hp) <= 0:
                break


if __name__ == '__main__':
    a = [0, 1, 2, 4, 8, 9]
    b = [-2, 5, 9, 11]
    c = [1, 7, 12]
    d = [6]

    res = list(mergeLists(a, b, c, d))
    print(res)
