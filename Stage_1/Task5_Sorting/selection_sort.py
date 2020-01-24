"""
Selection Sort

    Improves on the bubble sort by making only one exchange for every pass through the list.
    To do this, selection sort looks for the largest value as it makes a pass.

    [5, 1, 3, 2]  ---- 1st pass ---->  [2, 1, 3, 5]
     ↓                                           ↑
     ---------------------------------------------

Complexity: O(n^2)
"""


def selection_sort(alist: list) -> list:

    for passnum in range(len(alist)-1, 0, -1):
        maxPos = 0
        # during each pass, find the index of the largest value
        for i in range(passnum+1):
            if alist[maxPos] < alist[i]:
                maxPos = i

        # exchange the largest value to proper place
        alist[maxPos], alist[passnum] = alist[passnum], alist[maxPos]

    return alist


if __name__ == '__main__':
    a = [5, 1, 3, 2]
    print(selection_sort(a))