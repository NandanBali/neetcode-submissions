class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for _ in range(m-1, 0, -1):
            for x in range(n-2, -1, -1):
                prev_row[x] += prev_row[x+1]
        return prev_row[0]
