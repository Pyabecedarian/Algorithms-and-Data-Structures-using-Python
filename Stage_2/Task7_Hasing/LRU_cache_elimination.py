"""
link： https://leetcode-cn.com/problems/lru-cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
following operations: `get` and `put`:

    > get(key)
        Get the value (will always be positive) of the key if the key exists
        in the cache, otherwise return -1.

    > put(key, value)
        Set or insert the value if the key is not already present. When the cache reached its
        capacity, it should invalidate the least recently used item before inserting a new item.


The cache is initialized with a positive capacity.


Follow up:
    Could you do both operations in O(1) time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4


Idea:
    Hash table can store/retrieve key-value pair in O(1) time. But hash table cannot record which key
    uses most recently.

    To keep recently used keys while evict the keys that are `out of date`, we could push the keys in a
    Stack (FILO order). But we need to move the items to the top of the stack in O(1) time
    for records.

    A stack is a linkedlist performed in such a way that recently added items are pushed on the top,
    can perform O(1) operations on either end, but how could we move a middle node to the end in O(1)
    time? The answer is whether we can get the node directly. This is much similar with the implementation
    of `List` in `datastruct/python_like_List.py`, where each node's id has kept in a array. We can get the
    node at any position directly through dereferencing of the node's id.

    So we can keep the node in a hash table, and record the recently used keys on the top of the stack,
    while evict the out dated item on the bottom.
"""
from datastruct import DNode, HashTable


class LRUCache(object):
    def __init__(self, capacity=2):
        self.capacity = capacity
        self._size = 0

        # cache stores key-node pair; node.data = [key, value]
        self.cache = HashTable()  # or {}

        self.head, self.tail = DNode(), DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        s = ''
        p = self.head.next
        while p != self.tail:
            s += str(p.data[0]) + ' '
            p = p.next
        return f'LRU >[ {s}]'

    def _remove_node(self, node: DNode):
        """remove a node in a linkedlist"""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

        self._size -= 1

    def _add_node(self, node: DNode):
        """add the node at the head of linkedlist"""
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        self._size += 1

    def _move_to_top(self, node: DNode):
        """move the node to the head of the linkedlist"""
        self._remove_node(node)
        self._add_node(node)

    def get(self, key):
        node = self.cache.get(key)
        if node:
            # key exists, move this node to the end
            self._move_to_top(node)
            return node.data[1]
        else:
            # key not in cache
            return -1

    def put(self, key, value):
        node = self.cache.get(key)
        if node:
            # key exists, move this node to the end, update the value
            self._move_to_top(node)
            node.data[1] = value
        else:
            # key not exists, check capacity
            if self._size >= self.capacity:
                # the stack is full, remove the node at end
                tmpNode = self.tail.prev
                self._remove_node(tmpNode)
                del self.cache[tmpNode.data[0]]

            # add the node to the top
            tmpNode = DNode([key, value])
            self._add_node(tmpNode)
            self.cache[key] = tmpNode


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    print()

    print(cache.get(1))
    print(cache)
    print()

    cache.put(3, 3)  # evict 2
    print(cache)
    print(cache.get(1))
    print(cache)

    cache.put(4, 4)  # evict 3
    print(cache)
    print(cache.get(3))
