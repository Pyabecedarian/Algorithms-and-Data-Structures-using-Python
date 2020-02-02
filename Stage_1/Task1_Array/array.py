"""
★ Task: To implement an array, supporting dynamic storage expansion ★
Cause we have python's built-in list, the concept and implementation of array is invisible in daily use.
But to understand the idea of array, which is widely used in other languages, and its implementation can
help us dig deeper and know better about python list.
==========  Big-O Efficiency of Python list Operations  ==========
    Operation                             Big-O Efficiency
------------------------------------------------------------------
index []                                        O(1)
index assignment                                O(1)
append                                          O(1)
pop()                                           O(1)
pop(i)                                          O(n)
insert(i,item)                                  O(n)
del operator                                    O(n)
iteration                                       O(n)
contains (in)                                   O(n)
get slice [x:y]                                 O(k)
del slice                                       O(n)
set slice                                       O(n+k)
reverse                                         O(n)
concatenate                                     O(k)
sort                                            O(n log n)
multiply                                        O(nk)
==================================================================
As shown in the table above, python list is efficient in indexing/assignment and append/pop in the end
of the list. We also have to remember that python list support any type of data being stored.
An array in C/C++ is a linear structure allocated in a contiguous space in memory, which performs O(1)
efficiency in indexing/assignment, but can only store fixed number of data with same data type.
An linked-list, however, can store any type and any number of data with O(1) efficiency in append/pop
in the end.
In practice, python list is a comprehensive of linked-list and array combined. To make life easy, we can
use ctypes module to simulate arrays in python
"""
from ctypes import *

_types_ = {int: [c_longlong, "int"],
           bool: [c_bool, "bool"],
           float: [c_float, "float"],
           bytes: [c_char, "bytes"],
           str: [c_wchar_p, "str"],
           None: [c_void_p, "None"],
           }


def _new_array(ctype, size):
    """Create an array"""
    return (size * ctype)()


def _get_index(k, size):
    if k < 0: k += size
    if not 0 <= k < size:
        raise KeyError('Index out of bound!')
    return k


class Array(object):
    def __init__(self, pytype=None, size=1, *args):
        """
        To initiate an array, one must specify the data type and total length
        :param pytype: The fundamental data type of each element, must be one of {int, float, bool, None, str}
        :param size: Indicate how many elements being stored
        """
        self._pytype = pytype
        self._ctype, self._tname = _types_[pytype]
        self._size = size
        self._n = 0  # current length
        self._i = 0  # for iteration
        self._A = _new_array(self._ctype, self._size)

        if 'full' in args:
            self._n = size

    def __len__(self):
        return self._n

    def __repr__(self):
        s = '[' + ', '.join([str(self._A[i]) for i in range(self._n)]) + ']'
        return f'Array({self._tname}, {s})'

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._n:
            self._i = 0
            raise StopIteration
        i, self._i = self._i, self._i + 1
        return self._A[i]

    def __getitem__(self, k):
        k = _get_index(k, len(self))
        return self._A[k]

    def __setitem__(self, k, v):
        k = _get_index(k, len(self))
        if self._pytype is None:
            pass

        elif not isinstance(v, self._pytype):
            try:
                v = self._pytype(v)
            except ValueError:
                raise ValueError(f'could not convert {type(v)} to {self._tname}')
        self._A[k] = v

    def _resize(self):
        """If try to add more elements in array, it'll automatically resize (double the size)"""
        self._size, oldSize = 2 * self._size, self._size
        tmpA = _new_array(self._ctype, self._size)
        for i in range(self._n):
            tmpA[i] = self._A[i]
        self._A = tmpA

    def append(self, v):
        if self._n >= self._size:
            self._resize()

        self._A[self._n] = v
        self._n += 1

    def extend(self, iterable):
        it = iter(iterable)
        while True:
            try:
                self.append(next(it))
            except StopIteration:
                break

    def insert(self, i, v):
        # 1. append v
        self.append(v)
        # 2. move v to index i
        j = len(self) - 1
        while j > i:
            tmp = self._A[j - 1]
            self._A[j - 1] = self._A[j]
            self._A[j] = tmp
            j -= 1

    def pop(self, k=-1):
        """Pop the item at idx"""
        k = _get_index(k, len(self))
        res = self._A[k]
        while k < len(self) - 1:
            self._A[k] = self._A[k + 1]
            k += 1
        self._n -= 1
        return res


if __name__ == '__main__':
    a = Array(None, 5, 'full')
    print(a)

    a = Array(None, 5)
    print(a)
