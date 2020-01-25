"""
Merge Sort
    recursively splits a list in half. If the list is empty or at least one item, it is sorted by definition
    (base case). If the list has more than one item, we split the list and recursively invoke a merge sort
    on both halves.

    Once the two halves are sorted, the fundamental operation, called a `merge`, is performed. Merging is the
    process of taking two smaller sorted lists and combining them together into a single, sorted, new list.

                             [5, 1, 3, 2]
                                  ↓
                          [5, 1]      [3, 2]
                             ↓           ↓
                         [5]  [1]    [3]  [2]
                             ↓           ↓
                          [1, 5]      [2, 3]
                                   ↓
                             [1, 2, 3, 5]

Analysis
    Split Phase:
        We can divide a list in half `log n` times where n is the length of the list.
    Merge Phase:
        This operation costs `n` times to merge a list of size n.
    Conclude:
        Complexity: O(n·log n)
"""


def merge_sort(alist: list) -> list:
    """split phase"""
    if len(alist) > 1:
        mid = len(alist) // 2
        l_half = alist[:mid]
        r_half = alist[mid:]

        # recursively split the list
        # Note that `merge_sort()` is capable of sorting list in place,
        # so no need to write explicitly: l_half = merge_sort(l_half)
        merge_sort(l_half)
        merge_sort(r_half)

        """merge phase"""
        i1 = i2 = 0
        k = 0

        while i1 < len(l_half) and i2 < len(r_half):
            if l_half[i1] > r_half[i2]:
                alist[k] = r_half[i2]
                i2 += 1
            else:
                alist[k] = l_half[i1]
                i1 += 1
            k += 1

        while i1 < len(l_half):
            alist[k] = l_half[i1]
            i1 += 1
            k += 1

        while i2 < len(r_half):
            alist[k] = r_half[i2]
            i2 += 1
            k += 1

    return alist


if __name__ == '__main__':
    alist = [5, 3, 1, 2]
    merge_sort(alist)
    print(alist)
