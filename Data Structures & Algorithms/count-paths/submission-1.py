class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n

        for y in range(m-1, 0, -1):
            curr_row = [1] * n
            for x in range(n-1, 0, -1):
                curr_row[x-1] = prev_row[x-1] + curr_row[x]
            prev_row = curr_row
        return prev_row[0]
