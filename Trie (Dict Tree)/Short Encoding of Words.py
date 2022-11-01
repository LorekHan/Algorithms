# A solution of leetcode 820

from collections import defaultdict
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        nodes = []
        DTree = lambda: defaultdict(DTree)
        dtree = DTree()

        newwords = list(set(words))

        for word in newwords:
            cur = dtree
            for ch in word[::-1]:
                cur = cur[ch]
            nodes.append(cur)
        
        return sum(len(word)+1 for i, word in enumerate(newwords) if len(nodes[i])==0)
