"""
Tree
    is either empty or consists of a root and zero or more subtrees, each of which is also a tree. The root
    of each subtree is connected to the root of the parent tree by an edge.

                                         *
                                    left  right
                                    /         \
                                   *           *
                              left  right  left  right
                                     \
                                      *
                                  left  right

methods:
    > insert(position, newobj): add a left/right child to the tree.

"""


class BinaryTree(object):
    def __init__(self, rootobj=None):
        self.root = rootobj
        self.left = None
        self.right = None

    def insertLeft(self, newobj):
        tmp = BinaryTree(newobj)
        if self.left is None:
            self.left = tmp
        else:
            tmp.left = self.left
            self.left = tmp

    def insertRight(self, newobj):
        tmp = BinaryTree(newobj)
        if self.right is None:
            self.right = tmp
        else:
            tmp.right = self.right
            self.right = tmp


if __name__ == '__main__':
    t = BinaryTree('r')
    print(t)
