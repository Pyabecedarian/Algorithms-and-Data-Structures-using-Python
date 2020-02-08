"""
* Task: Find the top-K largest numbers in a collection of numbers *

Idea:
    Build a heap of size k, iterate all the rest numbers in the input list, push to and pop from the heap.
    When the iteration has done, the k numbers in heap must be the top-K largest.
"""
from datastruct import BinaryHeap


def nlargest(n, iterable, key=None):
    """Return a iterator of the top-n largest values iterable"""
    it = iter(iterable)
    hp = BinaryHeap(func=key)

    for _ in range(n):
        try:
            hp.heappush(next(it))
        except StopIteration:
            # n is large than len(iterable), return all elements in heap
            return hp.items

    while True:
        try:
            hp.heappushpop(next(it))
        except StopIteration:
            # the iterable has exhausted, return all elements in heap
            return hp.items


if __name__ == '__main__':
    a = [0, 12, 8, 11, 4, 2, 1, 0, -1, 3, 6, 9, 13, 22, 9]
    print(list(nlargest(4, a)))
    print(list(nlargest(100, a)))
