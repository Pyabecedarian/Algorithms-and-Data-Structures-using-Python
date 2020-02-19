"""
Linked List is a collection of items where each item holds a relative position with respect to the others.

The structure seems like:
    head -> node1 -> node2 -> ... -> tail

We can define three different types of linkedlist according to the positions it holds:
    > LinkedList:
    > Bidirectional LinkedList:
    > Cycle LinkedList

Unlike array, linkedlist is capable of containing any type of data with any mount. Some possible operations
are as follows:
    > LinkedList():
    > append(item):
    > appendleft(item):
    > pop()/pop(pos):
    > remove(item):
"""


class Node(object):
    """Meta class to hold the linked structure"""
    def __init__(self, initdata=None, _next_=None):
        self.data = initdata
        self.next = _next_

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, iterable=[]):
        self.head = self.tail = Node()
        self._size = 0

        for item in iterable:
            self.append(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        self.idx = self.head.next
        return self

    def __next__(self):
        if self.idx:
            res = self.idx.data
            self.idx = self.idx.next
            return res
        else:
            raise StopIteration

    def __repr__(self):
        s = ', '.join([str(i) for i in self])
        return 'LinkedList([' + s + '])'

    def __getitem__(self, idx):
        if isinstance(idx, int):
            if idx < 0: idx += len(self)
            if not 0 <= idx < len(self): raise KeyError('Index out of bound!')

            p = self.head
            while idx >= 0:
                p = p.next
                idx -= 1
            return p.data

        elif isinstance(idx, slice):
            start, stop, stride = idx.indices(len(self))
            newList = LinkedList()
            p, i = self.head, 0
            while i < stop:
                if i < start:
                    i += 1
                    p = p.next
                    continue
                newList.append(p.next.data)
                i += stride
                for k in range(stride):
                    p = p.next

            return newList

    def __setitem__(self, idx, value):
        if isinstance(idx, int):
            if idx < 0: idx += len(self)
            if not 0 <= idx < len(self): raise KeyError('Index out of bound!')

            p = self.head
            while idx >= 0:
                p = p.next
                idx -= 1
            p.data = value

        elif isinstance(idx, slice):
            start, stop, stride = idx.indices(len(self))
            try:
                it = iter(value)
            except TypeError:
                raise TypeError(f'values `{value}` must be iterable!')
            else:
                p, i = self.head, 0
                while i < stop:
                    if i < start:
                        i += 1
                        p = p.next
                        continue
                    p.next.data = next(it)
                    i += stride
                    for k in range(stride):
                        p = p.next

    def append(self, item):
        """Append item in the tail of the list"""
        tmpNode = Node(item)
        self.tail.next = tmpNode
        self.tail = tmpNode
        self._size += 1

    def appendleft(self, item):
        """Append item in the front of the list"""
        tmpNode = Node(item, self.head.next)
        self.head.next = tmpNode
        self._size += 1

    def extend(self, iterable):
        """Extend linkedlist from a iterable or another linkedlist"""
        if not isinstance(iterable, LinkedList):
            it = iter(iterable)
            while True:
                try:
                    self.append(next(it))
                except StopIteration:
                    return
        else:
            self.tail.next = iterable.head.next
            self.tail = iterable.tail
            self._size += len(iterable)

    def pop(self, pos: int = -1):
        """Pop item at position `pos`"""
        idx = pos if pos >= 0 else len(self) + pos
        if not 0 <= idx < len(self): raise KeyError('Index out of bound!')

        p = self.head
        while idx > 0:  # stop before pos
            p = p.next
            idx -= 1

        # be careful that pop from an empty Linkedlist
        if p.next is not None:
            res = p.next.data

            # be careful when pop the last element we must change the self.tail
            if p.next is self.tail:
                self.tail = p

            p.next = p.next.next
            self._size -= 1
        else:
            res = None

        return res

    def popleft(self):
        return self.pop(0)

    def search(self, item, *args):
        p = self.head  # p is the node before item
        for idx, value in enumerate(self):
            if value == item:
                return p if 'return_p' in args else idx
            p = p.next
        else:
            raise ValueError(f'No such value `{item}` exists')

    def remove(self, item):
        try:
            p = self.search(item, 'return_p')
        except ValueError:
            return False
        else:
            p.next = p.next.next
            self._size -= 1
            return True


if __name__ == '__main__':
    l = LinkedList([3,1,2])
    print(l)

    l.pop()
    l.pop()
    l.pop()
    print(l)
    l.append(3)
    print(l)