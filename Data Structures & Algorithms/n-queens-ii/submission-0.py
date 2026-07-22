class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        at_risk = {"col": set(), "rd": set(), "ld": set()}

        def dfs(row):
            nonlocal count
            if row == n:
                count += 1
            
            for col in range(0, n):
                rd = col - row
                ld = col + row
                if rd not in at_risk["rd"] and ld not in at_risk["ld"] and col not in at_risk["col"]:
                    at_risk["col"].add(col)
                    at_risk["rd"].add(rd)
                    at_risk["ld"].add(ld)
                    dfs(row + 1)
                    at_risk["col"].remove(col)
                    at_risk["rd"].remove(rd)
                    at_risk["ld"].remove(ld)
            return count
        dfs(0)
        return count
