"""
★ Task: Write an algorithm that can find whether a word is present in a sentence. ★
"""
import string
from datastruct import Trie


def math_word(word: str, sentence: str) -> bool:
    table = str.maketrans({key: None for key in string.punctuation})
    sentence = sentence.translate(table).lower()
    words = sentence.split()

    repertoire = Trie()
    for w in words:
        repertoire.insert(w)

    return repertoire.search(word)


if __name__ == '__main__':
    s = 'How to match a word in a string? Use Trie.'
    print(math_word('how', s))
