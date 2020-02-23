"""
Write a Heap Sort Algorithm
"""
from datastruct.abstract import BinaryHeap
from datastruct.collections import List


def heap_sort(alist: list, key=None) -> list:
    """A heap sort algorithm can be implemented by push and pop items in a heap data structure."""
    newList = List()
    hp = BinaryHeap(func=key)

    for item in alist:
        hp.heappush(item)

    for _ in range(len(alist)):
        newList.append(hp.heappop())

    return newList


if __name__ == '__main__':
    a = [5, 1, 7, 10, 2, 4, 1, 0]
    print(heap_sort(a))

    a = [(0, 'a'), (11, 'b'), (2, 'c'), (1, 'd', False), (10, 'e')]
    print(heap_sort(a, key=lambda x: x[0]))

