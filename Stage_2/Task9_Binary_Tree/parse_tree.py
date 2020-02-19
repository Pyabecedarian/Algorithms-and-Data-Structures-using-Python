"""
Build a parse tree to evaluate a fully parenthesised mathematical expression, ((7+3)∗(5−2)) = ?

                                             *
                                          /    \
                                         +      -
                                       /  \   /  \
                                      7   3  5    2
"""
from datastruct.collections import HashTable
from datastruct.abstract import Stack
from datastruct.tree import BinaryTree
import operator


def build_parse_tree(fpexp):
    """
    :param fpexp: fully parenthesised expression
    :return: BinaryTree
    """
    fpexp = fpexp.split()
    tree = BinaryTree()
    pStack = Stack()  # with the help of stack, we can get the parent node back with respect to current node

    pStack.push(tree)
    currTree = tree
    for c in fpexp:
        if c == '(':  # insert a new subtree
            currTree.insertLeft(None)
            pStack.push(currTree)
            currTree = currTree.left

        elif c in '+-*/':  # c is an operator, change root value and descent to right subtree
            currTree.key = c
            currTree.insertRight(None)
            pStack.push(currTree)
            currTree = currTree.right

        elif c == ')':  # ths subtree has been filled up with operand and operators
            currTree = pStack.pop()

        else:  # an operand, change root value and back to parent node
            currTree.key = int(c)
            currTree = pStack.pop()

    return tree


def evaluate(parseTree: BinaryTree):
    op = HashTable(11)
    op['+'] = operator.add
    op['-'] = operator.sub
    op['*'] = operator.mul
    op['/'] = operator.truediv

    if parseTree.left and parseTree.right:
        a = evaluate(parseTree.left)
        b = evaluate(parseTree.right)
        fn = op[parseTree.key]
        return fn(a, b)
    else:
        return parseTree.key


if __name__ == '__main__':
    pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(pt)
    print(evaluate(pt))
