"""
We have now Array and LinkedList. It's enough to create a new type of container that can store
any type of data and support indexing/assignment operations in O(1) time, like python built-in list.

Idea:
    Use an Array to store all addresses of Node (for O(1) indexing/assignment)
    Use an LinkedList to store all data (for supporting any type)
"""
import ctypes as c
from datastruct.collections import Array


def deref(id):
    """Dereference the object from id
    :argument id: int(c_longlong), The id of an object, returned by id(obj)
    """
    return c.cast(id, c.py_object).value


def get_index(idx, size):
    """Return the positive index against size"""
    if idx < 0:
        idx += size
    if not 0 <= idx < size:
        raise KeyError('Index out of bound!')
    return idx


class DNode(object):
    """List is a doubly linked structure. This is the primitive unit to construct a List"""

    def __init__(self, initdata=None, _prev_=None, _next_=None):
        self.data = initdata
        self.prev = _prev_
        self.next = _next_


class List(object):
    def __init__(self, iterable=[]):
        self._addrs = Array(None)  # store all node's ids for O(1) indexing
        self.head = DNode()
        self.tail = self.head
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
        return 'List([' + s + '])'

    def __getitem__(self, idx):
        if isinstance(idx, int):
            idx = get_index(idx, len(self))
            # directly get the node from array
            return deref(self._addrs[idx]).data

        elif isinstance(idx, slice):
            start, stop, stride = idx.indices(len(self))
            newList = List()
            for i in range(start, stop, stride):
                newList.append(deref(self._addrs[i]).data)
            return newList

    def __setitem__(self, idx, obj):
        if isinstance(idx, int):
            idx = get_index(idx, len(self))
            deref(self._addrs[idx]).data = obj

        elif isinstance(idx, slice):
            start, stop, stride = idx.indices(len(self))
            it = iter(obj)
            for i in range(start, stop, stride):
                deref(self._addrs[i]).data = next(it)

    def __contains__(self, obj):
        found = False
        for item in self:
            if item == obj:
                found = True
                break
        return found

    def append(self, obj):
        """Create a new Node, attach to the end of the list"""
        tmpNode = DNode(obj, self.tail)
        self.tail.next = tmpNode
        self.tail = tmpNode
        self._size += 1
        self._addrs.append(id(tmpNode))

    def pop(self, idx=-1):
        """Pop item at index `idx`"""
        idx = get_index(idx, len(self))

        # remove from linkedlist
        node = deref(self._addrs[idx])
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            # popping the last object, the self.tail must be changed
            self.tail = node.prev

        # remove from addrs array
        self._addrs.pop(idx)

        # don't forget resize
        self._size -= 1

        return node.data

    def extend(self, iterable):
        """Extend the list from a iterable"""
        for obj in iterable:
            self.append(obj)

    def insert(self, idx, obj):
        """Insert a object into the list at idx"""
        idx = get_index(idx, len(self))

        node_idx = deref(self._addrs[idx])
        tmpNode = DNode(obj, node_idx.prev, node_idx)
        node_idx.prev.next = tmpNode
        node_idx.prev = tmpNode
        self._addrs.insert(idx, id(tmpNode))
        self._size += 1

    def index(self, obj, start=0, stop=-1, *args):
        """Return first index of obj, if no obj in list, raise ValueError"""
        start = get_index(start, len(self))
        stop = get_index(stop, len(self))

        while start <= stop:
            tmpNode = deref(self._addrs[start])
            if tmpNode.data == obj and type(tmpNode.data) == type(obj):
                return (start, tmpNode) if 'return_p' in args else start
            else:
                start += 1
        raise ValueError(f'No such value `{obj}` in list!')

    def clear(self):
        """Remove all items in list"""
        self.__init__()
        import gc
        gc.collect()

    def remove(self, obj):
        """Remove first obj from list, raise ValueError if obj not present"""
        idx = self.index(obj)
        self.pop(idx)


if __name__ == '__main__':
    l = List([1, 'abc', True, 9.1])
    print(l)
    print(l[-1])

    l[:-1] = ['s', 1, 0.1]
    print(l)
