class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        yl = len(heights)
        xl = len(heights[0])
        for y in range(0, yl):
            for x in range(0, xl):
                if x == 0 or y == 0: pacific.add((x, y))
                if x == xl - 1 or y == yl - 1: atlantic.add((x, y))
        
        # pacific
        traverse = set()
        pq = deque()
        for x, y in pacific:
            pq.append((x,y))
            traverse.add((x,y))

        while pq:
            x, y = pq.popleft()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x + dx < xl and 0 <= y + dy < yl and heights[y][x] <= heights[y+dy][x+dx] and (x+dx, y+dy) not in traverse:
                    pq.append((x+dx, y+dy))
                    pacific.add((x+dx, y+dy))
                    traverse.add((x+dx, y+dy))
        
        traverse.clear()
        for x, y in atlantic:
            pq.append((x, y))
            traverse.add((x, y))
        while pq:
            x, y = pq.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= x - dx < xl and 0 <= y - dy < yl and heights[y][x] <= heights[y-dy][x-dx] and (x-dx, y-dy) not in traverse:
                    pq.append((x-dx, y-dy))
                    atlantic.add((x-dx, y-dy))
                    traverse.add((x-dx, y-dy))

        result = []
        for (x, y) in pacific:
            if (x, y) in atlantic:
                result.append([y, x])
        
        return result