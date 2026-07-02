class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrows, ncols = len(obstacleGrid), len(obstacleGrid[0])

        prev_row = [0] * ncols
        prev_row[ncols-1] = 1
        for y in range(nrows-1, -1, -1):
            curr_row = [0] * ncols
            if obstacleGrid[y][ncols-1] != 1:
                curr_row[ncols-1] = prev_row[ncols-1]

            for x in range(ncols-2, -1, -1):
                if obstacleGrid[y][x] == 1:
                    curr_row[x] = 0
                else:
                    curr_row[x] = prev_row[x] + curr_row[x+1]
            prev_row = curr_row
        return prev_row[0]