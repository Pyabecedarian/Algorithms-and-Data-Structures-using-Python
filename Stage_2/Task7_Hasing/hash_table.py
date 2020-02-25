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
from datastruct.collections import List


class HashTable(object):
    def __init__(self, size=11):
        self._size = size  # default size
        self.slots = List([None] * size)
        self.payloads = List([None] * size)
        self._k = 0

    def __str__(self):
        s = List()
        for key, value in self.items():
            s.append(f'{str(key)}: {str(value)}')
        return f'Hashtable([ {", ".join(s)} ])'

    def __len__(self):
        return self._k

    def __iter__(self):
        return self.keys()

    def keys(self):
        for key, _ in self.items():
            yield key

    def values(self):
        for _, value in self.items():
            yield value

    def items(self):
        for slot_keys, payload in zip(self.slots, self.payloads):
            if slot_keys is not None:
                for key, value in zip(slot_keys, payload):
                    yield key, value

    def __delitem__(self, key):
        hash_value = self._hash(key)
        if not self.slots[hash_value]:
            raise KeyError(f'{key}')
        else:
            try:
                i = self.slots[hash_value].index(key)
            except ValueError:
                raise KeyError(f'{key}')
            else:
                self.slots[hash_value].pop(i)
                self.payloads[hash_value].pop(i)
                self._k -= 1

    def __getitem__(self, key):
        v = self.get(key)
        if v is None:
            raise KeyError(f'{key}')
        else:
            return v

    def __setitem__(self, key, value):
        self.put(key, value)

    def _hash(self, key):
        """Very simple hash function"""
        hashvalue = 0
        if isinstance(key, int):
            hashvalue = key
        elif isinstance(key, str):
            for i, c in enumerate(key):
                hashvalue += (i + 1) * ord(c)
        else:
            # the key would be any type or any object in python, we use id(key) for hashing
            return self._hash(id(key))

        return hashvalue % self._size

    def put(self, key, value):
        hash_value = self._hash(key)

        self._k += 1
        if self.slots[hash_value] is None:
            # the slot is empty, key does not exists
            self.slots[hash_value] = List([key])
            self.payloads[hash_value] = List([value])
        else:
            # Hash Collision, search the key in the list
            try:
                i = self.slots[hash_value].index(key)
            except ValueError:
                # key is not in List, append new key and value
                self.slots[hash_value].append(key)
                self.payloads[hash_value].append(value)
            else:
                # key is already in list, change value
                self.payloads[hash_value][i] = value
                self._k -= 1

    def get(self, key, default=None):
        hash_value = self._hash(key)

        if self.slots[hash_value] is None:
            return default
        else:
            try:
                i = self.slots[hash_value].index(key)
            except ValueError:
                return default
            else:
                return self.payloads[hash_value][i]


if __name__ == '__main__':
    t = HashTable(53)
    t['a'] = 0
    t['a'] = 123
    t[97] = 2

    print(len(t))

    print(list(t.keys()))
    print(list(t.values()))
    print(list(t.items()))

    del t['a']
    print(len(t))

    t[int] = 10
    print(t[int])
    print(list(t.keys()))
