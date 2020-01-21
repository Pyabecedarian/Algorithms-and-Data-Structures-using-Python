"""
Queue is structured as an ordered collection of items which are added at one end, called 'rear', and removed
from the other end, called 'front'. Queues maintain a FIFO ordering property.

Possible operations are:
    > Queue():
    > enqueue():
    > dequeue():
    > isEmpty():
"""
from datastruct import LinkedList


class Queue(object):
    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        s = ', '.join(map(str, self.items))
        return f'Queue([ {s} ])'

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        """Items enqueue in the rear(tail) of the list"""
        self.items.append(item)

    def dequeue(self):
        """Items dequeue from the front(head) of the list"""
        return self.items.popleft()

    def isEmpty(self):
        return len(self) == 0
