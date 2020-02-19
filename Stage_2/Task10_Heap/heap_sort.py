"""
Write a Heap Sort Algorithm
"""
from datastruct.collections import List
from datastruct.abstract import BinaryHeap


def heap_sort(alist: list) -> list:
    """A heap sort algorithm can be implemented by push and pop items in a heap data structure."""
    newList = List()
    hp = BinaryHeap()

    for item in alist:
        hp.heappush(item)

    for _ in range(len(alist)):
        newList.append(hp.heappop())

    return newList


if __name__ == '__main__':
    a = [5, 1, 7, 10, 2, 4, 1, 0]
    print(heap_sort(a))