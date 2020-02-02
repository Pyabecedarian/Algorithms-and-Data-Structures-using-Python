"""
Hash Table
    is a collection of items which are stored in such a way as to make it easy to find them in O(1) time.

    Each position in hash table is a `slot`, which can hold an item and named by an integer (index).

        names:      0       1       2       3       4       5
        items:      None    None    None    None    None    None

    The mapping between an item and the slot where that item belongs in the hash table is called
    `hash function`. The hash function will take any item in the collection and return an integer
    in the range of slot names, between 0 and n - 1.

    The simplest hash function is a `remainder method`, takes an item and divide by the table size, n:

                              hash_value = hash(item) = item % n

    The hash_value is the slot name that the item will be stored in the hash table.

        names:      0       1       2       3       4       5
        items:      None    None    None    13      None    None         13 % 5 = 3, stored on slot 3


    Load Factor, λ:
                            λ = num_items / table_size

    Sometimes, there will be a `collision`, since 23 % 5 also equal 3. So we need a technique to solve
    this problem.


Hash Function:
    The hash function is the key to hash table. Several methods for creating a hash function:

        > folding method:
            item    :  436-555-4601
            hash    :  43+65+55+46+01 = 210
                           hash_value = 210 % n

        > mid-square method:  square the item then extract a portion
            item    :  44
            hash    :  44^2 = 1936,
                       extract middle 2 digits, get 93
                       hash_value = 93 % n

    For string items, ord() can get its ordinal value
        ord('c') = 99


Collision Resolution
    Here we use a LinkedList to store all the collided items in a slot.


Some possible operations are as follows:
    HashTable()     : the constructor
    put(key, value) : Add new k-v pair to hash table, same as indexing: t[k] = v
    get(key)        : Retrieve the value in the table if a key is given, or `None` is returned if key
                      is not in table
    del t[key]      : delete k-v pair from the table
    in              : return True if key in table, False other wise

Here we use `List` as container in order to understand basic data structures better. But also can use built-in
python list alternatively.
"""
from datastruct import List


class HashTable(object):
    def __init__(self, size=11):
        self._size = size  # default size
        self.keys = List([None] * size)
        self.values = List([None] * size)
        self._k = 0  # for iteration

    def __repr__(self):
        s = ''
        for ks, vs in zip(self.keys, self.values):
            if ks:
                for k, v in zip(ks, vs):
                    kv_pair = f'{str(k)}: {str(v)}, '
                    s += kv_pair
        return f"HashTable([ {s[:-2]} ])"

    def __delitem__(self, key):
        hash_value = self._hash(key)
        if not self.keys[hash_value]:
            raise KeyError(f'{key}')
        else:
            try:
                i = self.keys[hash_value].index(key)
            except ValueError:
                raise KeyError(f'{key}')
            else:
                self.keys[hash_value].pop(i)
                self.values[hash_value].pop(i)

    def __getitem__(self, key):
        v = self.get(key)
        if v is None:
            raise KeyError(f'{key}')
        else:
            return v

    def __setitem__(self, key, value):
        self.put(key, value)

    def _hash(self, key: int):
        """Very simple hash function that only support int and str type"""
        hashvalue = 0
        if isinstance(key, int):
            hashvalue = key
        elif isinstance(key, str):
            for i, c in enumerate(key):
                hashvalue += (i+1) * ord(c)

        hashvalue = hashvalue % self._size
        return hashvalue

    def put(self, key, value):
        hash_value = self._hash(key)

        if not self.keys[hash_value]:
            # the slot is empty, key does not exists
            self.keys[hash_value] = List([key])
            self.values[hash_value] = List([value])
        else:
            # Hash Collision, search the key in the list
            try:
                i = self.keys[hash_value].index(key)
            except ValueError:
                # key is not in List, append new key and value
                self.keys[hash_value].append(key)
                self.values[hash_value].append(value)
            else:
                # key is already in list, change value
                self.values[hash_value][i] = value

    def get(self, key, default=None):
        hash_value = self._hash(key)

        if not self.keys[hash_value]:
            return default
        else:
            try:
                i = self.keys[hash_value].index(key)
            except ValueError:
                return default
            else:
                return self.values[hash_value][i]


if __name__ == '__main__':
    t = HashTable(53)
    t['a'] = 0
    t[97] = 'a'

    print(t['a'])


