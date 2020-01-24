"""
Bubble Sort
    Compare adjacent items and exchange those are out of order. Each pass through the list places the next
    largest value in its proper place.

    If not exchanges during a pass, then the list has been sorted.

        [5, 1, 3, 2]  ---- 1st pass ---->  [1, 3, 2, 5]

Complexity: O(n^2)
"""


def bubble_sort(alist: list) -> list:

    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchanges = True

    return alist


if __name__ == '__main__':
    a = [5, 1, 3, 2]
    print(bubble_sort(a))