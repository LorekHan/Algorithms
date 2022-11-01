# A solution to leetcode 720

class Trie:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.nodes:
                node.nodes[ch] = Trie()
            node = node.nodes[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            if node.nodes[ch] is None or not node.nodes[ch].isEnd:
                return False
            node = node.nodes[ch]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        longest = ""
        for word in words:
            if t.search(word) and (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                longest = word
        return longest
