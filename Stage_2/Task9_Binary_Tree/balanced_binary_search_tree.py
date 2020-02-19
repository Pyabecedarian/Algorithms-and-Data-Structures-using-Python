"""
Analysis of Binary Search Tree
    If the bst has the same number of both left and right child (balanced), then the height of the tree will be log2(n).
    But in case of extremely skewed that all the keys inserted in the same side, the tree will degrade
    to a linear structure, which causes the put() end get() function in O(n) complexity.

AVL Tree
    A special kind of bst that automatically makes sure that the tree remains balanced at all times. It keeps track
    of a `balanced factor` for each node in the tree.
                      balancedFactor = height(leftSubTree) - height(rightSubTree)

                                                          balancedFactor
                                             10        <--      1
                                          8     20     <--   1     0
                                       1               <-- 0

                                                          balancedFactor
                                             10        <--      1
                                          8     20     <--   0     0     (left subtree balanced, not affect root)
                                       1    9          <-- 0   0

                                                          balancedFactor
                                             10        <--      0
                                          8     20     <--   0    -1
                                       1    9      30  <-- 0   0     0

Balanced Factor
    update through put(), see `update_balance_factor_v1`:
        Since all new keys are inserted into the tree as leaf node, it's easy to see that balanced factor for a leaf
        is zero. Once a leaf node is added, all the parent node's bf has changed:
            > if the new key is left child, bf of the parent increases by 1;
            > if the new key is right child, bf of the parent decreased by 1;
            > all the bfs' update will recursively affect to every ancestor all the way up to the root of the tree;
            > *NOTE*: Once a bf of parent has been adjusted to zero, means the subtree is balanced, then the recursive
            update of bf should stop.
            > if the bf of one node is out of range [-1, 1], then the tree is unbalanced, we need to rebalance the tree

    update through delete(), see `update_balance_factor_v2`:
        We already know that there are three cases to delete a node in the tree:
            > if the node to be deleted is a leaf node;
            > if the node to be deleted has only on child node;
            > if the node to be deleted has both two children.

            Fot the first case, node is a leaf:
                > if the node is a left child of its parent, the bf of parent decreases by 1;
                > if the node is a right child, the bf of a parent increases by 1;
                > after the change of the bf, if it is not zero, which means the parent node has no
                  child any more, we should recursively update the bf of the parent of parent node.

            Fot the second case, node has only one child:
                > all the children's bf under the node is unchanged;
                > the height of the subtree in which the node located will decrease by 1;
                > therefore the bf of the parent node is changed by increasing/decreasing 1 if the node itself is
                  a right/left child of its parent;
                > if the bf of parent is changed to zero, which means that the height of the subtree in which the parent
                  node located decreases 1, therefore we need to recursively invoke the update procedure to the
                  parent of the parent node.

            For the third case, node has two children:
                > find the successor in the right subtree of the key node, which is either a leaf node or node with
                  only one child;
                > recursively update the bfs started with successor;
                > do the same delete operations in delete() function in BSTMap.


Re-balance the tree
    When updating a node'bf which is out of [-1, 1], the tree is unbalanced and need to re-balance. The strategy is:
        > if the root's bf > 0, the tree is left heavy, then rotate the tree to the right;
        > if the root's bf < 0, the tree is right heavy, then rotate the tree to the left;
        > the `root` can applies to every root node in subtrees

         balanced tree (root'bf = 1)      unbalance (root'bf = 2)                        balance
                10                                 10                                       5
            5       12       insert a 9        5       12       rotate to right         2      10
         2     7           ------------>    2     7            ---------------->     1       7   12
                                          1
    After rotating the tree, the nodes's bf has changed. The new bf is related to the its old as following:
        > only two nodes' bf has changed, the old and new root node;
        > the deviation of the new bf are as follows (where |A| means a subtree of B):
                              old tree                       new tree
                                 B                               D
        left rotation      |A|       D        --->          B        |E|       (only B's and D's bf has changed)
                                 |C|  |E|               |A|   |C|


        Deviation (left rotation):
            According bf's definition we have:
                old_bf(B) = h(A) - old_h(D)
                          = h(A) - ( 1 + max(h(C), h(E)) )
                new_bf(B) = h(A) - h(C)

            subtract old and new bf:
                new_bf(B) - old_bf(B) = h(A) - h(C) - { h(A) - [ 1 + max(h(C), h(E)) ] }
                                      = -h(C) + 1 + max(h(C), h(E))
                                      = 1 + max(0, h(E) - h(C))
                                      = 1 - min(0, h(C) - h(E))
                                      = 1 - min(0, old_bf(D))

            move old_bf(B) to the right, we have the result of new_bf(B):
                new_bf(B) = old_bf(B) + 1 - min(0, old_bf(D))

            The same deviation of new_bf(D) we get:
                new_bf(D) = old_bf(D) + 1 + max(new_bf(B), 0)


        Deviation (right rotation):
            The right rotation is the reverse of left rotation. It's easy to get the original bfs back by
            rename the new_bf to old_bf in the left rotation formulas and put all old_bfs to the right side:
                new_bf(D) = old_bf(D) - 1 - max(old_bf(B), 0)
                new_bf(B) = old_bf(B) - 1 + min(0, new_bf(D))


Special Case of Rotation
    Consider the unbalanced tree as follows, which will be a mirrored unbalanced tree after left rotation:

        unbalance                             unbalance
            A (-2)       left rotation           B (2)
               B (1)    --------------->     A (-1)
            C (0)                                C (0)

    So solve this problem, we must follow the rules:
        > if a subtree needs a left rotation to bring it into balance, first check the balance factor of the
          right child. If the right child is left heavy, then do a right rotation on right child, followed by
          the original left rotation;
        > if a subtree needs a right rotation, first check the bf of the left child. If the left child is
          right heavy, then do a left rotation on left child, followed by the original right rotation.

                            A (-2)            A (-2)                 C
                               B (1)  ---->      C (-1)   ---->   A     B
                            C (0)                   B (0)
"""
from datastruct.tree import BSTNode, BSTMap


class AVLNode(BSTNode):
    def __init__(self, key, value, parent=None):
        self.bf = 0
        super(AVLNode, self).__init__(key, value, parent)

    def is_left_heavy(self):
        return self.bf > 0

    def is_right_heavy(self):
        return self.bf < 0


class AVLMap(BSTMap):
    """AVL Tree inherit from normal bst"""

    def __repr__(self, node: AVLNode = None, i=0):
        node = node if node is not None else self.root
        s = ''
        if node is not None:
            gap = '\t' * i * bool(i)
            s += gap + ':-> ' * bool(i) + str(node.key) + ':' + str(node.value) + f'({node.bf})' + '\n'
            if node.has_left():
                s += self.__repr__(node.left, i + 1)
            else:
                if node.any_child():
                    s += '\t' + gap + ':-\n'
            if node.has_right():
                s += self.__repr__(node.right, i + 1)
            else:
                if node.any_child():
                    s += '\t' + gap + ':-\n'
        return s

    def update_balance_factor_v1(self, node: AVLNode, *args):
        """Update the node's balance factor recursively up to the root or stop until a subtree is balanced.
        If a node's balance factor is out of the range [-1, 1], invoke rebalance() for rearrangement to a
        balanced bst"""
        if node.bf > 1 or node.bf < -1:
            return self.re_balance(node)

        if node.parent:
            if node.is_left_child():
                node.parent.bf += 1
            elif node.is_right_child():
                node.parent.bf -= 1

            if node.parent.bf != 0:
                self.update_balance_factor_v1(node.parent)

    def update_balance_factor_v2(self, node: AVLNode, *args):
        """
        A revised version of update_balance_factor() for the delete() function of the AVL Tree.
        Once a key is deleted, the bf of its parent and all the ancestor nodes' bf will be changed:
            > if the node to be deleted is a left child of its parent, the bf of its parent must decrease by 1;
            > if the node is a right child, the bf of its parent must increase by 1;
            > recursively update the bf to the root node of the tree.
        """
        if node.bf > 1 or node.bf < -1:
            return self.re_balance(node)

        if node.parent:
            if node.is_left_child():
                node.parent.bf -= 1
            elif node.is_right_child():
                node.parent.bf += 1

            if node.parent.bf == 0:
                self.update_balance_factor_v2(node.parent)

    def re_balance(self, pivot_node: AVLNode):
        """
        Re-balance the subtree at its root, pivot_node using the strategy described above at
        section `Special Case of Rotation`.
        """
        # left heavy, the subtree at pivot_node needs a right rotation
        if pivot_node.is_left_heavy():
            # first check its left child, if left child is right heavy, then left rotate at left child first
            if pivot_node.left.is_right_heavy():
                self.left_rotate(pivot_node.left)
            self.right_rotate(pivot_node)

        # right heavy, the subtree at pivot_node needs a left rotation
        elif pivot_node.is_right_heavy():
            # first check its right child, if right child is left heavy, then right rotation at right child first
            if pivot_node.right.is_left_heavy():
                self.right_rotate(pivot_node.right)
            self.left_rotate(pivot_node)

    def right_rotate(self, old_pivot: AVLNode):
        """Do a right rotation around the input pivot node."""
        new_pivot = old_pivot.left
        old_pivot.left = new_pivot.right

        if new_pivot.has_right():
            new_pivot.right.parent = old_pivot

        if old_pivot is self.root:
            self.root = new_pivot
        else:
            if old_pivot.is_left_child():
                old_pivot.parent.left = new_pivot
            else:
                old_pivot.parent.right = new_pivot
        new_pivot.parent = old_pivot.parent

        new_pivot.right = old_pivot
        old_pivot.parent = new_pivot

        # update balance factor
        # new_bf(D) = old_bf(D) - 1 - max(old_bf(B), 0)
        # new_bf(B) = old_bf(B) - 1 + min(0, new_bf(D))
        old_pivot.bf += -1 - max(new_pivot.bf, 0)
        new_pivot.bf += -1 + min(0, old_pivot.bf)

    def left_rotate(self, old_pivot: AVLNode):
        """Do a left rotation around input pivot node."""
        new_pivot = old_pivot.right
        old_pivot.right = new_pivot.left
        if new_pivot.has_left():
            new_pivot.left.parent = old_pivot

        if old_pivot is self.root:
            self.root = new_pivot
        else:
            if old_pivot.is_left_child():
                old_pivot.parent.left = new_pivot
            else:
                old_pivot.parent.right = new_pivot
        new_pivot.parent = old_pivot.parent

        new_pivot.left = old_pivot
        old_pivot.parent = new_pivot

        # update balance factor
        # new_bf(B) = old_bf(B) + 1 - min(0, old_bf(D))
        # new_bf(D) = old_bf(D) + 1 + max(new_bf(B), 0)
        old_pivot.bf += 1 - min(0, new_pivot.bf)
        new_pivot.bf += 1 + max(old_pivot.bf, 0)

    def _put(self, key, value, node: AVLNode):
        """Helper function the insert a key-value pair to a proper position that preserve bst structure,
        and automatic rearrange the tree to a balanced bst tree."""
        f = self.func
        if f(key) < f(node.key):
            if node.has_left():
                self._put(key, value, node.left)
            else:
                node.left = AVLNode(key, value, parent=node)
                self.size += 1
                # the only difference with bst version is update_balance_factor()
                self.update_balance_factor_v1(node.left)

        elif f(key) > f(node.key):
            if node.has_right():
                self._put(key, value, node.right)
            else:
                node.right = AVLNode(key, value, parent=node)
                self.size += 1
                # the only difference with bst version is update_balance_factor()
                self.update_balance_factor_v1(node.right)
        else:
            node.value = value

    def put(self, key, value):
        """Add a key-value pair to the AVL Map"""
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = AVLNode(key, value)
            self.size += 1

    def delete(self, key):
        f = self.func
        node = self._get(key, self.root)
        if node:
            # 1. The node is a leaf
            if node.is_leaf():
                if node is not self.root:  # make sure the node isn't the root of the tree

                    # update the balance factor first
                    self.update_balance_factor_v2(node)

                    if node.is_left_child():
                        node.parent.left = None
                    else:
                        node.parent.right = None
                else:
                    self.root = None

            # 2. The node has only one child
            elif node.any_child():
                child = node.any_child()
                child.parent = node.parent
                if node is not self.root:

                    # update the balance factor first
                    self.update_balance_factor_v2(node)

                    if child.is_left_child():
                        node.parent.left = child
                    else:
                        node.parent.right = child
                else:
                    self.root = child

            # 3. The node has two children
            elif node.has_both_children():
                successor = self.findMin(node.right)
                node.replace(successor.key, successor.value)

                # update the balance factor first
                self.update_balance_factor_v2(successor)

                if successor.is_leaf():
                    if successor.is_left_child():
                        successor.parent.left = None
                    else:
                        successor.parent.right = None

                elif successor.has_right():
                    if successor.is_left_child():
                        successor.parent.left = successor.right
                        successor.right.parent = successor.parent
                    else:
                        successor.parent.right = successor.right
                        successor.right.parent = successor.parent

        else:
            # the key not found, raise KeyError
            raise KeyError(f'{key}')


if __name__ == '__main__':
    d = AVLMap()

    # after insert these three keys, the tree is balanced
    for key in [10, 8, 20]:
        d[key] = str(key)

    # add a new key, this will be the left most child
    d[1] = 1
    print(d)

    # # add another new key as left most child, this step will trigger the right rotation step
    d[0] = 0
    print(d)

    # test again, will trigger the left rotation
    print()
    d = AVLMap()
    for key in [10, 5, 12, 3, 6, 14, 32, 19, 21, 15, 31]:
        d[key] = str(key)
    print(d)

    del d[10]
    print(d)
