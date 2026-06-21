class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        traversed = set()
        
        count = 0
        for ir in range(0, rows):
            for ic in range(0, cols):
                if grid[ir][ic] == "0" or (ir, ic) in traversed:
                    continue
                queue.append((ir, ic))
                while queue:
                    r, c = queue.popleft()
                    traversed.add((r, c))
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if (r+dr, c+dc) in traversed or not (0 <= r+dr < rows and 0 <= c+dc < cols):
                            continue
                        if grid[r+dr][c+dc] == "1":
                            queue.append((r+dr, c+dc))
                count += 1
        return count


