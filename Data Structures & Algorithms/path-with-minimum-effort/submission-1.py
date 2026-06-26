class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        adjlist = {}
        xl, yl = len(heights[0]), len(heights)

        min_heap = [(0, 0, 0)]
        effort_to = {}
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)

            if (x, y) in effort_to:
                continue

            effort_to[(x, y)] = effort

            if (x,y) == (xl-1, yl-1):
                break
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= x + dx < xl and 0 <= y + dy < yl and (x+dx, y+dy) not in effort_to:
                    htd = abs(heights[y+dy][x+dx] - heights[y][x])
                    heapq.heappush(min_heap, (max(effort, htd), x+dx, y+dy))

        return effort_to[(xl-1, yl-1)]