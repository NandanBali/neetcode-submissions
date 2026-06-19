class WordDictionary:

    def __init__(self):
        self.children: dict[str, WordDictionary] = {}
        self.word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(node: WordDictionary, index: int) -> bool:
            if index == len(word):
                return node.word
            elif word[index] == ".":
                for n in node.children.values():
                    if dfs(n, index+1):
                        return True
                return False
            else:
                if word[index] in node.children:
                    return dfs(node.children[word[index]], index+1)
                return False

        return dfs(self, 0)