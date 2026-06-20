from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word if it ends here, else None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word # Store the word at the end node
            
        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, parent_node: TrieNode) -> None:
            char = board[r][c]
            curr_node = parent_node.children[char]

            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None # Avoid duplicate duplicates

            board[r][c] = '#'

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            board[r][c] = char

            if not curr_node.children:
                parent_node.children.pop(char)

        # 3. Kick off DFS from every cell matching a Trie root child
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result