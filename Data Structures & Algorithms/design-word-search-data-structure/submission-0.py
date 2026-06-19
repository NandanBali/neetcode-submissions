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
        self.found = False

        def dfs(node: WordDictionary, remaining: str):
            if not self.found:
                if len(remaining) == 0:
                    self.found = node.word
                elif remaining[0] == ".":
                    for key, val in node.children.items():
                        dfs(val, remaining[1:])
                        if self.found: break
                else:
                    if remaining[0] in node.children:
                        dfs(node.children[remaining[0]], remaining[1:])

        dfs(self, word)
        return self.found