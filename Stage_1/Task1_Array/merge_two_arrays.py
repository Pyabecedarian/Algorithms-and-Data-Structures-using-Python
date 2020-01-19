"""
★ Task: To merge two ordered arrays into a ordered one. ★

Idea:
    Kind of the merge procedure in `merge sort`.
"""
from collections import deque
from Stage_1.Task1_Array.array import Array


def merge(arr1, arr2):
    """
    :param arr1, arr2:  Two sorted arrays (desending order)
    """
    if len(arr1) == 0: return arr2
    if len(arr2) == 0: return arr1

    resArr = Array(arr1.type)
    it1, it2 = iter(arr1), iter(arr2)
    tmp1, tmp2 = map(next, [arr1, arr2])

    while True:
        if tmp1 >= tmp2:
            resArr.append(tmp1)
            try:
                tmp1 = next(it1)
            except StopIteration:
                resArr.extend(it2)
                break

        else:
            resArr.append(tmp2)
            try:
                tmp2 = next(it2)
            except StopIteration:
                resArr.extend(it1)
                break

    return resArr


if __name__ == '__main__':
    a = Array(int, 5)
    a.extend([12, 8, 5, 1])

    b = Array(int, 3)
    b.extend([10, 9, 4])

    print(merge(a, b))

