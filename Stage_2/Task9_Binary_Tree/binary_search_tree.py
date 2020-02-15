"""
Binary Search Tree
    relies on the property (called bst property) that values less than the parent are found in the
    left subtree, and values larger than the parent are found in the right subtree.

                                             10
                                          8      20      -->  [10, 8, 20, 1, 9, 17, 39, 14]
                                        1   9  17  39
                                              14


We have already know two implementations of a `map abstract data structure`: binary search on a list and
Hash Table.
A Binary Search Tree is another important way to map from a key to value. We will focus on using the
binary tree structure to provide for efficient searching.

Possible methods are:
    > Map()          : constructor
    > put(key, value): Add a new key-value pair to the map. If key exists, replace the old value
    > get(key)       : Given a key, return the corresponding value in the map
    > in             : Return True for a statement of the form `key in map`, if the key is in the map.
    > del            : Delete the key-value pair in map using a statement of the form `del d[key]

"""


class BSTNode(object):
    """Tree node of binary search tree. """

    def __init__(self, key=None, value=None, parent=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __repr__(self):
        return str(self.key)

    def __iter__(self):
        if self.has_left():
            for item in self.left:
                yield item
        yield self.key
        if self.has_right():
            for item in self.right:
                yield item

    def replace(self, key, value):
        """Reset the node's key and value"""
        self.key = key
        self.value = value

    def has_left(self):
        """Whether the node has a left child"""
        return self.left is not None

    def has_right(self):
        """Whether the node has a right child"""
        return self.right is not None

    def is_leaf(self):
        """Whether the node is a leaf node"""
        return not self.left and not self.right

    def is_left_child(self):
        """Whether the node is the left child of its parent"""
        return self.parent.left is self

    def is_right_child(self):
        """Whether the node is the right child of its parent"""
        return self.parent.right is self

    def any_child(self):
        """Return the only one child if the node has one"""
        if self.left and not self.right:
            return self.left
        elif not self.left and self.right:
            return self.right

    def has_both_children(self):
        """Whether the node has both two children"""
        return self.left and self.right


class BSTMap(object):
    def __init__(self, func=None):
        self.root = None
        self.size = 0
        self.func = func if func else lambda x: x

    def __len__(self):
        return self.size

    def __repr__(self, node: BSTNode = None, i=0):
        node = node if node is not None else self.root
        s = ''
        if node is not None:
            gap = '\t' * i * bool(i)
            s += gap + ':-> ' * bool(i) + str(node.key) + ':' + str(node.value) + '\n'
            if node.has_left():
                s += self.__repr__(node.left, i + 1)
            else:
                if node.any_child():
                    s += '\t' + gap + ':-\n'
            if node.has_right():
                s += self.__repr__(node.right, i + 1)
            else:
                if node.any_child():
                    s += '\t' + gap + ':-\n'
        return s

    def __getitem__(self, key):
        """Given a key, get the value from the Map using a statement of the form d[key],
        if the key does not exist, raise a KeyError"""
        node = self._get(key, self.root)
        if node is not None:
            return node.value
        else:
            raise KeyError(f'Key not exists: `{key}`!')

    def __setitem__(self, key, value):
        """Put the key-value pair in Map using a statement of the form d[key]=value,
        if the key has existed, replace the old value with the new one."""
        self.put(key, value)

    def __contains__(self, key):
        """Magic method overloads `in` operator"""
        if self._get(key, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        return self.root.__iter__()

    def keys(self):
        return iter(self)

    def delete(self, key):
        """Delete the key-value pair in map. If the key does not exist, raise a KeyError.

        There are three cases need to consider:
            1. If the key is the leaf node of the tree, and is the left/right child of its parent,
            then replace the parent's left/right with None;
            2. If the key node has only one child (either left or right), then promote its
            left/right child to its position
            3. If the key has two children, find the successor.
        """
        f = self.func
        node = self._get(key, self.root)
        if node:
            # 1. The node is a leaf
            if node.is_leaf():
                if node is not self.root:  # make sure node isn't the root of the tree
                    if node.is_left_child():
                        node.parent.left = None
                    else:
                        node.parent.right = None
                else:
                    self.root = None

            # 2. The node only has a left/right child
            elif node.any_child():
                child = node.any_child()
                child.parent = node.parent
                if node is not self.root:
                    if child.is_left_child():
                        node.parent.left = child
                    else:
                        node.parent.right = child
                else:
                    self.root = child

            # 3. The node has both left and right child, find the successor.
            # Successor is the `next-largest` node in the tree, and it has no more than one child.
            # child at most. The node will preserve the bst relationship for both of the existing left and right
            # subtrees.
            elif node.has_both_children():
                successor = self.findMin(node.right)
                node.replace(successor.key, successor.value)

                if successor.is_leaf():
                    if successor.is_left_child():
                        successor.parent.left = None
                    else:
                        successor.parent.right = None

                elif successor.has_right():
                    if successor.is_left_child():
                        successor.parent.left = successor.right
                        successor.right.parent = successor.parent
                    else:
                        successor.parent.right = successor.right
                        successor.right.parent = successor.parent
        else:
            # the key not found, raise KeyError
            raise KeyError(f'{key}')

    def findMin(self, node: BSTNode):
        """Find the result node which contains the smallest key in the subtree started with input node.
        The recursive invocation makes sure that the minimum node is the left most child in the right subtree,
        it would be a leaf or a node only has a right child."""
        min_node = node
        if node.has_left():
            min_node = self.findMin(node.left)
        return min_node

    def _put(self, key, value, node: BSTNode):
        """Helper function put a key-value pair in map"""
        f = self.func
        if f(key) < f(node.key):
            if node.has_left():
                self._put(key, value, node.left)
            else:
                node.left = BSTNode(key, value, parent=node)
                self.size += 1

        elif f(key) > f(node.key):
            if node.has_right():
                self._put(key, value, node.right)
            else:
                node.right = BSTNode(key, value, parent=node)
                self.size += 1

        else:
            node.value = value

    def put(self, key, value):
        f = self.func
        """Add a key-value pair to the Map"""
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BSTNode(key, value)
            self.size += 1

    def _get(self, key, node: BSTNode):
        """Helper function that recursively search a key in Map, and return the node if key is found."""
        f = self.func
        if not node:
            return None

        elif node.key == key:
            return node

        elif f(key) < f(node.key):
            if node.has_left():
                return self._get(key, node.left)
            else:
                return None

        elif f(key) > f(node.key):
            if node.has_right():
                return self._get(key, node.right)
            else:
                return None

    def get(self, key, default=None):
        """Return the value of the given key, if the key does not exist, return `default` value"""
        node = self._get(key, self.root)
        if node is None:
            return default
        else:
            return node.value


if __name__ == '__main__':
    d = BSTMap()
    keys = [17, 5, 35, 2, 11, 29, 38, 26, 7, 8]
    for key in keys:
        value = str(key)
        d.put(key, value)

    for key in keys:
        print(d[key], end='\t')
    print()

    # print the structure of d
    print(d)

    # use d.keys() method to get the keys
    print(list(d.keys()))

    # delete some keys
    del d[5], d[17]
    print(list(d.keys()))

    # We can also iterate over Map() object to get the keys
    for key in d:
        print(key, end='\t')
    print()
