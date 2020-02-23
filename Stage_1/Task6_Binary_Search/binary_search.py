"""
It's possible to take great advantage of the sorted list to speed up the search algorithm.

Binary Search
    starts by examining the middle item, if it is the item that we looking for, we are done. If the item we
    are searching is larger than the middle, we are sure that the entire lower half as well as the middle item
    can be eliminated from further consideration.
    By repeating this way on the upper half, we eliminate another half, therefore vastly reduce the searching space.

    Goal:  find `13` in the list.
                            [1, 3, 7, 9, 11, 13, 15]
                                      ↑               first guess: 9, 9 < 13, eliminate lower half
                                        [11, 13, 15]
                                              ↑      second guess: 13, found

Analysis:
    Complexity: O(log n)
    In the recursive version, since the slice operation in Python is actually O(k), which means the algorithm
    will not perform in strict logarithmic time as it is in the normal version. But it can be solved by passing
    the reference of the list and indices.
"""


def binary_search(alist: list, item) -> int:
    """
    :param alist: A sorted list
    :param item: The item searching for
    :return index of the item if found, otherwise return -1
    """
    low_bound = 0
    high_bound = len(alist) - 1

    while low_bound <= high_bound:
        mid = (low_bound + high_bound) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] < item:
            low_bound = mid + 1
        elif alist[mid] > item:
            high_bound = mid - 1

    return -1


def binarySearch(alist: list, item) -> int:
    """A recursive version of binary_search"""
    if len(alist) == 0:
        return -1

    mid = len(alist) // 2
    if alist[mid] == item:
        return mid
    else:
        if alist[mid] > item:
            res = binarySearch(alist[:mid], item)
            return res if res != -1 else -1
        else:
            res = binarySearch(alist[mid + 1:], item)
            return mid + 1 + res if res != -1 else -1


if __name__ == '__main__':
    a = [1, 3, 7, 9, 11, 13, 15]
    print(binary_search(a, 11))

    print(binarySearch(a, 11))
