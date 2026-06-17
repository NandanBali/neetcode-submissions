class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def backtrack(open_bracket: int, closed: int, acc: str):
            if closed == n:
                self.result.append(str(acc))
                return
            if open_bracket < n:
                acc += "("
                backtrack(open_bracket+1, closed, acc)
                acc = acc[:-1]
            if closed < open_bracket:
                acc += ")"
                backtrack(open_bracket, closed+1, acc)
                acc = acc[:-1]
        backtrack(0, 0, "")
        return self.result
