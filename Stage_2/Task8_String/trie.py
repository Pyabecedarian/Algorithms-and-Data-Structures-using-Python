"""
Trie Tree
    is a tree-like data structure whose nodes store the letters of an alphabet. By structuring the nodes in
    a particular way, words and strings can be retrieved from the structure by traversing down a branch path
    of the tree.
                                       *
                                     a - z  (each node has a flag)
                                     /   \
                                    *     *
                                a - z     a - z
                                            \
                                             *
                                            a - z

Node structure
                          ↓
                 a      b  ...   z
              (flag) (flag)    (flag)
                ↓      ↓   ...    ↓


link:  https://leetcode-cn.com/problems/implement-trie-prefix-tree
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
from datastruct.collections import List, HashTable


class TrieNode(object):
    def __init__(self):
        self.flag = False  # to indicate whether the traversal is a complete word
        self.child = List([None] * 26)  # 26 letters from a-z


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.convert = HashTable(53)  # `53` is set appropriately that neither not too large to waste memory nor
                                      # too small to increase the probability of hash collision

        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            self.convert[c] = i

    def insert(self, word: str):
        """Insert a word into the Trie"""
        currNode = self.root
        for c in word:
            idx = self.convert[c]
            if not currNode.child[idx]:
                tmpNode = TrieNode()
                currNode.child[idx] = tmpNode
                currNode = tmpNode
            else:
                currNode = currNode.child[idx]
        else:
            currNode.flag = True

    def search(self, word: str) -> bool:
        """Search if a word exists in the Trie"""
        found = False
        currNode = self.root
        for c in word:
            idx = self.convert[c]
            if not currNode.child[idx]:
                break
            currNode = currNode.child[idx]
        else:
            if currNode.flag:
                found = True

        return found

    def startsWith(self, prefix: str) -> bool:
        """Determine whether the input string is a prefix or not"""
        found = True
        currNode = self.root
        for c in prefix:
            idx = self.convert[c]
            if not currNode.child[idx]:
                found = False
                break
            currNode = currNode.child[idx]

        return found


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
