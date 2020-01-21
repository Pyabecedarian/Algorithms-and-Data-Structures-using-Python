"""
Stack is a collection of items where items are added to and removed from the end called "top".
Stack s are ordered LIFO.

To implement a stack in python, it make sense to utilize the power and simplicity of the primitive collections
provided by python, also Array & LinkedList in previous tasks, as well as data types provided in python's
`collections` module.

Some possible methods of stack are:
    > Stack()   : The constructor, return a empty new stack object
    > push(item): adds a new item to the top of the stack
    > pop()     : removes the top item from the stack.
    > peek()    : returns the top item from the stack, but does not remove it
    > isEmpty() : tests to see whether the stack is empty.
"""
from datastruct import LinkedList


class Stack(object):
    def __init__(self):
        self.items = LinkedList()

    def __str__(self):
        s = ', '.join(map(str, self.items))
        return 'Stack([' + s + '])'

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.items.appendleft(item)

    def pop(self):
        try:
            return self.items.popleft()
        except KeyError:
            return None

    def peek(self):
        return self.items[0]

    def clear(self):
        while not self.isEmpty():
            self.pop()
