"""
★ Task: To merge two ordered linkedlist into a ordered one. ★
"""
from datastruct.collections import LinkedList


def merge_linkedlists(alist: LinkedList, blist: LinkedList) -> LinkedList:
    newlist = LinkedList()
    p1, p2 = alist.head, blist.head
    k1, k2 = 0, 0

    while p1.next and p2.next:
        v1, v2 = p1.next.data, p2.next.data
        if v1 >= v2:
            newlist.append(v1)
            p1 = p1.next
            k1 += 1
        else:
            newlist.append(v2)
            p2 = p2.next
            k2 += 1

    if p1 is not None and p2 is None:
        newlist.tail.next = p2
        newlist.tail = blist.tail
        newlist._size += len(blist) - k2
    elif p1 is None and p2 is not None:
        newlist.tail.next = p1
        newlist.tail = alist.tail
        newlist._size += len(alist) - k1

    return newlist


if __name__ == '__main__':
    a = LinkedList([6, 3, 1])
    b = LinkedList([10, 9, 2, 0, -2])

    c = merge_linkedlists(a, b)
    print(c)
    print(c[2:-1])
