"""
Insertion Sort
    Always keep sorted in the sublist of lower positions. Each new item is then `inserted` back into
    the previous sublist.

    The insertion step looks like bubble sort, if the item located at `i` is smaller than the one before,
    then exchange, until to a proper position.

    [5, 1, 3, 2]  --- 1st pass --->  [1, 5, 3, 2]  --- 2nd pass --->  [1, 3, 5, 2]
    ↑---↓                               ↑---↓
"""


def insertion_sort(alist: list) -> list:
    for idx in range(1, len(alist)):
        # during each pass, insert the item at `idx` back into the previous sublist
        sub_idx = idx - 1
        while sub_idx >= 0:
            if alist[sub_idx] > alist[idx]:
                alist[sub_idx], alist[idx] = alist[idx], alist[sub_idx]
                idx = sub_idx
            sub_idx -= 1

    return alist


if __name__ == '__main__':
    a = [5, 1, 3, 2]
    print(insertion_sort(a))
