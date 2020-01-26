"""
Reversed from binary_search.
    Given a item, if the item in the list, return its index.
                  If not in the list, return the index of the first item that is larger than the the given item
                  If all items in the list are less then the given item, return -1
"""


def binary_search_fuzzy(alist: list, item) -> int:
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

    if low_bound >= len(alist):
        return -1
    else:
        return low_bound


if __name__ == '__main__':
    a = [1, 3, 7, 9, 11, 13, 15]
    print(binary_search_fuzzy(a, 16))
