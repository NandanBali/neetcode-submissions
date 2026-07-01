class TrieNode:
    def __init__(self, depth=0):
        self.depth = depth
        self.children = {}
        self.word = False

    def add(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(depth=curr.depth + 1)
            curr = curr.children[char]
        curr.word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = TrieNode()
        for word in wordDict:
            words.add(word)

        arr: List[int] = [0] * len(s)
        def dfs(start) -> bool:
            if start == len(s):
                return True
            if arr[start] != 0:
                return arr[start] == 1
            depths = []
            idx = start
            curr = words
            while idx < len(s):
                if s[idx] in curr.children:
                    curr = curr.children[s[idx]]
                    idx += 1
                    if curr.word:
                        depths.append(curr.depth)
                else: break
            
            if len(depths) == 0:
                arr[start] = -1
                return False

            depths.reverse() 
            for depth in depths:
                if dfs(start+depth):
                    arr[start] = 1
                    return True
            arr[start] = -1
            return False
        return dfs(0)