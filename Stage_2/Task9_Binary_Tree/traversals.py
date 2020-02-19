"""
Implement `preorder`, `inorder` and `postorder` traversal.
"""
from datastruct.collections import List
from datastruct.tree import BinaryTree


def preorder(btree: BinaryTree) -> List:
    """
    Return a List of values in predorder
    """
    newList = List()
    newList.append(btree.key)
    if btree.left:
        newList.extend(preorder(btree.left))
    if btree.right:
        newList.extend(preorder(btree.right))

    return newList


def postorder(btree: BinaryTree) -> List:
    """
    Return a List of values in postorder
    """
    newList = List()
    if btree is not None:
        newList.extend(postorder(btree.left))
        newList.extend(postorder(btree.right))
        newList.append(btree.key)

    return newList


def inorder(btree: BinaryTree) -> List:
    """
    Return a List of values in inorder
    """
    newList = List()
    if btree is not None:
        newList.extend(inorder(btree.left))
        newList.append(btree.key)
        newList.extend(inorder(btree.right))

    return newList


def printMathExp(btree: BinaryTree) -> str:
    """Print the whole math expression"""
    s = ''
    if btree is not None:
        if btree.left is not None:
            s += '('
        s += printMathExp(btree.left)
        s += str(btree.key)
        s += printMathExp(btree.right)
        if btree.right is not None:
            s += ')'

    return s


if __name__ == '__main__':
    t = BinaryTree('a')
    t.insertLeft('b').insertRight('c')
    t.left.insertLeft('d')
    t.left.insertLeft('e').insertRight('f')
    t.left.right.insertLeft('g').insertRight('h')
    print(t)  # print the tree structure

    # traversal and get the values in three orders
    print(preorder(t), '\tpreorder')
    print(postorder(t), '\tpostorder')
    print(inorder(t), '\tinorder')

    # try to print a parse_tree in `./parse_tree.py`
    from Stage_2.Task9_Binary_Tree.parse_tree import build_parse_tree

    t = build_parse_tree('( ( 10 + 5 ) * 3 )')
    print(t)  # print the tree structure

    print(preorder(t), '\tpreorder')
    print(postorder(t), '\tpostorder')
    print(inorder(t), '\tinorder')  # we can recover the original expression back (without any parentheses)
                                    # using inorder traversal.

    # change the `inorder()` function a bit to get the fully parentheses expression
    print(printMathExp(t))
