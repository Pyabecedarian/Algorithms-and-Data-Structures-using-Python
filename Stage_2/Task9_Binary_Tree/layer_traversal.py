"""
Implement a Layer Traversal algorithm for the binary tree.

                7            traversal by layer
             1     2       --------------------->    [ 7, 1, 2, 3, 4, 6, 10 ]
           3  4  6  10
"""
from datastruct.collections import List
from datastruct.abstract import Queue
from datastruct.tree import BinaryTree


def layer_traversal(btree: BinaryTree) -> List:
    """Return a list of items in btree from layer to layer."""
    res = List()
    q = Queue()
    q.enqueue(btree)
    while not q.isEmpty():
        currNode = q.dequeue()
        res.append(currNode.key)
        if currNode.left:
            q.enqueue(currNode.left)
        if currNode.right:
            q.enqueue(currNode.right)

    return res


if __name__ == '__main__':
    t = BinaryTree(7)
    t.insertLeft(1)
    t.left.insertLeft(3).insertRight(4)
    t.insertRight(2)
    t.right.insertLeft(6).insertRight(10)
    print(t)

    # layer traversal
    print(layer_traversal(t))