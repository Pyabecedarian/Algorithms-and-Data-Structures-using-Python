"""
★ Task: To reverse a linkedlist ★
"""
from datastruct import LinkedList


def reverse_linkedlist(alist: LinkedList) -> LinkedList:
    alist.tail = alist.head.next
    p = None
    while alist.head.next is not None:
        tmp = alist.head.next
        alist.head.next = tmp.next
        tmp.next = p
        p = tmp
    alist.head.next = p

    return alist


if __name__ == '__main__':
    l = LinkedList([0, 3, 2, 4])
    print(reverse_linkedlist(l))
