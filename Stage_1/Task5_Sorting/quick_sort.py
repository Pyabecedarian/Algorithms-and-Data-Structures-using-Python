"""
Quick Sort
    starts with a `pivot value`(here simply the 1st item in a list). Then starts to partition.

    The partition process find the `split point` for the `pivot` and move the items, where all items
    in the left part are less than the pivot and all larger on pivot's right.

    Recursively invoke the partition on both parts until the part size is 1 (base case).

    To find the `split point`, it begins by locating two position markers: left_marker & right_marker, at the
    beginning and the end of the remaining items in the list. The goal of this process is to move those items
    that are on the wrong side with respect to the pivot while converging on the split point.

                                [5, 1, 3, 9, 2, 4, 7]
                                 *  ↑              ↑    pivot: 5
                                [5, 1, 3, 9, 2, 4, 7]
                                 *        ↑     ↑       left_marker stop where 9 > 5,
                                                       right_marker stop where 4 < 5
                                [5, 1, 3, 4, 2, 9, 7]
                                 *        ↑     ↑       exchange 4 and 9
                                [5, 1, 3, 4, 2, 9, 7]
                                 *           ↑  ↑       left_marker stop where 9 > 5,
                                            rm  lm     right_marker stop where 2 < 5,
                                                       split_point found: at right_marker
                                [2, 1, 3, 4, 5, 9, 7]
                                             *          exchange 5 and 2
                                [2, 1, 3, 4]  [9, 7]
                                 *  ↑     ↑    *  ↑     recursive call on parts
                                                  ↑
    The choose of `pivot value` is the key to quick sort. A good pivot can split the list in half. However,
    a bad pivot can't not split the list (extremely skewed partition), it'll cost extra expenses.
    But if the pivot is good, the quick sort can perform just as good as merge sort while not using any
    additional storage.

Analysis
    Best case:
        If each partition splits the list in half, the result is `log n` divisions. In order to find the split
        point, each of the `n` items need to be checked against the pivot value. The result is O(n·log n)
    Bad case:
        If each partition cannot find the middle to split, this can causes a extremely skewed division, one part
        contains 0 items, the other n - 1. Then sorting a list of n - 1 divides into a list of size 0 and a list of
        size n - 2. The result is O(n^2).
"""


def quick_sort(alist: list, key=None):
    """Entry function of quick sort"""
    f = key if key is not None else lambda x: x
    return quick_sort_helper(alist, 0, len(alist) - 1, f)


def quick_sort_helper(alist: list, start: int, end: int, f):
    """Helper function that implement partition process"""
    # if `start == end`, means that the invocation reaches the base case (size 1 list)
    if start < end:
        # choose a `pivot`
        pivot = alist[start]

        # find the `split point`
        left_marker = start + 1
        right_marker = end

        # continuously move the wrong items and converge to split_point
        while True:
            while left_marker <= right_marker and f(alist[left_marker]) <= f(pivot):
                left_marker += 1

            while right_marker >= left_marker and f(alist[right_marker]) >= f(pivot):
                right_marker -= 1

            if left_marker <= right_marker:
                tmp = alist[left_marker]
                alist[left_marker] = alist[right_marker]
                alist[right_marker] = tmp
            else:
                break

        # split point found
        split_point = right_marker

        # exchange pivot with the item at right_marker
        alist[start] = alist[right_marker]
        alist[right_marker] = pivot

        # recursively invoke partition
        quick_sort_helper(alist, start, split_point - 1, f)
        quick_sort_helper(alist, split_point + 1, end, f)

    return alist


if __name__ == '__main__':
    a = [5, 1, 3, 9, 2, 4, 7]
    print(quick_sort(a))

    a = [(5, 'a'), (1, 'b'), (3, 'c'), (9, 'd'), (2, 'e'), (4, 'f'), (7, 'g')]
    quick_sort(a)
    print(a)
