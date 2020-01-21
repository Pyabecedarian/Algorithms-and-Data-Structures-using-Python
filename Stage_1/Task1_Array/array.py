"""
★ Task: To implement an array, supporting dynamic storage expansion ★
Cause we have python's built-in list, the concept and implementation of array is invisible in daily use.
But understanding the idea of array, which is widely used in other languages, and the implementation can
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
An array in C/C++ is a linear structure allocated in a continuous space in memory, which performs O(1)
efficiency in indexing/assignment, but can only store fixed number of data with same data type.
An linked-list, however, can store any type and any number of data with O(1) efficiency in append/pop
in the end.
In practice, python list is a comprehensive of linked-list and array combined. To make life easy, we can
use ctypes module to simulate arrays in python
"""
from ctypes import *


class Array(object):
    _types_ = {int: c_int, bool: c_bool, float: c_float, bytes: c_char, None: c_wchar_p}
    _pytypes_ = {c: t for t, c in _types_.items()}

    def __init__(self, pytype=int, size=1):
        """
        To initiate an array, one must specify the data type and total length
        :param pyType: The fundamental data type of each element, must be one of {int, float, bool, None, str}
        :param size: Indicate how many elements being stored
        """
        self.type = pytype
        self._ctype = self._match_type(pytype)
        self._size = size
        self._A = self._generate_array(self._ctype, self._size)
        self._n = 0
        self._i = 0

    def __len__(self):
        return self._n

    def _match_type(self, pyType):
        """Return ctype correspond to given python type"""
        return self._types_[pyType]

    @staticmethod
    def _generate_array(ctype, size):
        """Create an array"""
        return (size * ctype)()

    def __str__(self):
        s = '[' + ' '.join([str(self._A[i]) for i in range(self._n)]) + ']'
        return f'Array(int, {s})'

    def _get_index(self, k):
        return k if k >= 0 else self._n + k

    def __getitem__(self, k):
        k = self._get_index(k)
        return self._A[k]

    def __setitem__(self, k, v):
        k = self._get_index(k)
        self._A[k] = v

    def _resize(self):
        """If try to add more elements in array, it'll automatically resize"""
        self._size, oldSize = 2 * self._size, self._size
        tmpA = self._generate_array(self._ctype, self._size)
        for i in range(self._n):
            tmpA[i] = self._A[i]
        self._A = tmpA

    def append(self, v):
        if self._n >= self._size:
            self._resize()
        self._A[self._n] = v
        self._n += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._n:
            self._i = 0
            raise StopIteration
        i, self._i = self._i, self._i + 1
        return self._A[i]

    def extend(self, iterable):
        it = iter(iterable)
        while True:
            try:
                self.append(next(it))
            except StopIteration:
                break