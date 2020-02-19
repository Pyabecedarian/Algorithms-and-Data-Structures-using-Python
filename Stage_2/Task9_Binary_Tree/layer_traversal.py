"""
Implement a Layer Traversal algorithm for the binary tree. The traversal order like this has another name,
`BFS` (Breadth First Search), we will see this in Stage_3.

                7            traversal by layer
             1     2       --------------------->    [ 7, 1, 2, 3, 4, 6, 10 ]
           3  4  6  10

Idea
    Utilize a Queue to keep track of the left and right subtree if they are not None, then systematically check
    the subtree in front of the tree.
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