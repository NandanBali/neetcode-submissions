class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.x_len = len(board[0])
        self.y_len = len(board)
        self.found = False 

        def backtrack(acc: str, x: int, y: int, aci: int, collected: set[tuple[int, int]]):
            if acc == word:
                self.found = True
                return
            if len(acc) == len(word) or (x,y) in collected:
                return
            
            if word[aci] == board[y][x]:
                acc += board[y][x]
                if acc == word:
                    self.found = True
                    return
                collected.add((x,y))
                # up
                if y > 0:
                    backtrack(acc, x, y-1, aci+1, collected)
                if y < self.y_len - 1:
                    backtrack(acc, x, y+1, aci+1, collected)
                if x > 0:
                    backtrack(acc, x-1, y, aci+1, collected)
                if x < self.x_len-1:
                    backtrack(acc, x+1, y, aci+1, collected)
                collected.remove((x,y))
                acc = acc[:-1]        
            else:
                return

        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                backtrack("", x, y, 0, set())
                if self.found:
                    return True

        return self.found
