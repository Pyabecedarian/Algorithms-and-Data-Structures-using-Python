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


Find the successor/predecessor node of a node in a tree

Successor:
    The BinaryTree has left/right attributes which reference to the successor of left/right subtree.
Predecessor (see ./parse_tree.py):
    To find predecessor node, we need a stack to keep the current node before descent to the child node.
    The peak node in the stack is the predecessor of current node.
"""


class BinaryTree(object):
    def __init__(self, rootobj=None):
        self.key = rootobj
        self.left = None
        self.right = None

    def __repr__(self, i: int = 0):
        """Print BinaryTree in a structured way"""
        s = ''
        s += '   ' * (i-1) * bool(i) + ':..' * bool(i) + str(self.key) + '\n'
        if self.left is not None:
            s += self.left.__repr__(i + 1)
        if self.right is not None:
            s += self.right.__repr__(i + 1)

        return s

    def insertLeft(self, newobj):
        """Insert a subtree as the left child"""
        tmp = BinaryTree(newobj)
        if self.left is None:
            self.left = tmp
        else:
            tmp.left = self.left
            self.left = tmp

        return self

    def insertRight(self, newobj):
        """Insert a subtree as the right child"""
        tmp = BinaryTree(newobj)
        if self.right is None:
            self.right = tmp
        else:
            tmp.right = self.right
            self.right = tmp

        return self


if __name__ == '__main__':
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    t.left.insertLeft('e')
    t.left.insertRight('f')
    print(t)
