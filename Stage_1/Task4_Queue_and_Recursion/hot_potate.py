"""

"""
from datastruct.abstract import Queue


def hot_potato(namelist: list, num: int) -> str:
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while len(q) > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    names = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    print('The last child is:', hot_potato(names, 4))