"""
Priority Queue

In Stage1, we have learned about the FIFO data structure `queue`. A `priority queue` acts like a queue,
however, in a priority queue the logical order of items inside a queue is determined by its priority.

It's easy to implement a priority queue using sorting algorithms, but remember that inserting into a list
is O(n) and sorting a list is O(n log n). There is a better way to do this.

`Binary Heap` is a key to this problem. A priority queue implemented by a binary heap can allow us
enqueue/dequeue in O(log n) time.

If we diagram the heap, it looks like a binary tree, but we implement it only use a single list.
There are two variations: `Min Heap` and `Max Heap`. The min heap always keep the smallest item
in front, while the max heap keeps the largest as priority.


Structure Property
    In order to guarantee the logarithmic performance, we must keep our tree balanced, that is, a binary tree
    almost has the same number of nodes in the left and right subtrees, except for the leave nodes. The tree
    like this also called a `complete binary tree`:
                                            5
                                        7       9
                                     16  17  10  21     --->   [0, 5, 7, 9, 16, 17, 10, 21, 19, 18]
                                   19  18                    a `0` here just for simple integer division
    ※IMPORTANT※
        > a complete tree can be represented by a single list, in which any left child of a parent (at position p)
        is the node that is found in position `2p` in the list. Similarly the right child is at `2p+1`.

        > reversely, to find the parent of any node in the tree, we can simply use integer division (`//`), for a
        node at position `x` in a tree, its parent is at `x//2`.

Order Property
    In a heap, for every node x with parent p, the (root) value in p is <= value in x


Possible methods of a Binary Heap:
    > BinaryHeap()   :  constructor
    > enqueue(item)  :  add a new item to the heap
    > min()          :  returns the item with the minimum value
    > dequeue()      :  returns the item with the minimum value, removing the item from the heap
    > buildHeap(list):  builds a new heap from a list of values
"""
from datastruct import List


# Min Heap
class BinaryHeap(object):
    """Heap is implemented by a single list, but it diagram like a binary tree."""

    def __init__(self, func=None):
        self.heapList = List([0])  # 0 here just for simple integer division in following methods

        # func takes 1 argument (each element in list) and return a value that will be used for comparison.
        # If None, element itself will be used to compare with its child value
        self.func = func if func else lambda x: x

    def __len__(self):
        return len(self.heapList) - 1

    def items(self):
        """An iterator containing all items in heap"""
        i = 1
        while i <= len(self):
            yield self.heapList[i]
            i += 1

    def heappush(self, value):
        """
        Add an item to the priority queue.
        append() is the easiest way to add an item to a list, but will be very likely violate the
        order property. If the value is too small, we need to swap it up another level according
        structure property.
        """
        self.heapList.append(value)
        x = len(self.heapList) - 1

        # keep swapping until value >= parent.root
        f = self.func
        while x // 2 > 0:
            if f(self.heapList[x]) < f(self.heapList[x // 2]):
                tmp = self.heapList[x // 2]
                self.heapList[x // 2] = self.heapList[x]
                self.heapList[x] = tmp
                x //= 2
            else:
                break

    def heappop(self):
        """
        Pop the top most item in the list, and restore the heap order.
        After popping, move the last item to the top, but this will probably be incompliance with heap order,
        we need to swap it down.
        """
        # the top item is going to be popped
        if len(self.heapList) > 1:
            self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
            res = self.heapList.pop()

            self._percDown(1)  # swap the top value to proper position
            return res

    def _percDown(self, p):
        """
        Keep swapping the value at position p down to the child, until a proper position has reached
        according heap order property.
        Steps:
            1. find the smaller child's position (2p or 2p+1);
            2. compare with the parent;
            3. if parent > min(children) then swap, otherwise a proper position has reached
        """
        f = self.func
        while 2 * p < len(self.heapList):
            # when 2*p is the last value in list, then there will be no right child of the last parent.
            # in such case, when indexing 2*p+1 to the list, will raise a KeyError. We only need to
            # compare with the left child value
            try:
                if f(self.heapList[p]) > f(self.heapList[2 * p]) or \
                        f(self.heapList[p]) > f(self.heapList[2 * p + 1]):

                    smaller_idx = 2 * p if f(self.heapList[2 * p]) <= f(self.heapList[2 * p + 1])\
                             else 2 * p + 1
                    self.heapList[p], self.heapList[smaller_idx] = self.heapList[smaller_idx], self.heapList[p]
                    p = smaller_idx
                else:
                    # p has already reached to proper position, break the loop
                    break
            except KeyError:
                if f(self.heapList[p]) > f(self.heapList[2 * p]):
                    self.heapList[p], self.heapList[2 * p] = self.heapList[2 * p], self.heapList[p]
                break

    def heapify(self, iterable):
        """Build the heap from a iterable"""
        self.heapList = List([0])
        self.heapList.extend(iterable)

        i = len(self.heapList) // 2
        while i > 0:
            self._percDown(i)
            i -= 1
        return self

    def heappushpop(self, value):
        """A method performs push&pop combined, which is a little bit faster than
        push() followed by pop() separately."""
        f = self.func
        if len(self) <= 0 or f(value) < f(self.heapList[1]):
            return value
        else:
            res = self.heapList[1]
            self.heapList[1] = value
            self._percDown(1)
            return res


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.heapify([1, 5, 12, -1, 6])
    for i in range(len(bh)):
        print(bh.heappop())

    # test what function do
    bh = BinaryHeap(lambda x: x[1])
    bh.heappush(('good', 0))
    bh.heappush((3.14,   4))
    bh.heappush((False, -2))
    bh.heappush(('bad',  1))

    print(bh.heappushpop(('12', 12)))
    print(list(bh.items()))
