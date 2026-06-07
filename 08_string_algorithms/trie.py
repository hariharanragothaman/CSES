"""
Reusable trie for lowercase a-z strings.

Common uses in CSES:
  - Word Combinations      : match words from a position in text
  - Finding Patterns       : store multiple patterns, scan text
  - Counting Patterns      : store patterns with frequency counts
  - Required Substring     : forbidden / required substring checks
"""


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def match_from(self, text: str, start: int) -> list[int]:
        """
        Return end indices (exclusive) of every dictionary word that matches
        text[start:]. Example: text='ababc', start=0 -> [2, 4] for 'ab', 'abab'.
        """
        ends: list[int] = []
        node = self.root
        for i in range(start, len(text)):
            ch = text[i]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_end:
                ends.append(i + 1)
        return ends

    def _walk(self, s: str) -> TrieNode | None:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
