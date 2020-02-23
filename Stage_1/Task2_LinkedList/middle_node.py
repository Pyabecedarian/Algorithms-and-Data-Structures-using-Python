"""
★ Task: Find the middle node of a LinkedList ★

Idea: Set two pointers, the second pointer takes twice the steps as the first one does. When the second reaches
the end, the first points the middle node.
"""
from datastruct.collections import LinkedList


def middle_node(alist: LinkedList):
    p1 = p2 = alist.head.next
    while p2 is not None and p2.next is not None:
        p1 = p1.next
        p2 = p2.next.next

    return p1.data


if __name__ == '__main__':
    l = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(middle_node(l))
