class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = set()
        rotting_fruits = []

        xl = len(grid[0])
        yl = len(grid)

        for x in range(0, xl):
            for y in range(0, yl):
                if grid[y][x] == 2:
                    rotting_fruits.append((x, y))
                elif grid[y][x] == 1:
                    fresh_fruits.add((x, y))

        queue = deque()
        for rotten in rotting_fruits:
            queue.append((rotten, 0))

        count = 0
        while queue and fresh_fruits:
            (x, y), time = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + dx < xl and 0 <= y + dy < yl and (x+dx, y+dy) in fresh_fruits:
                    fresh_fruits.remove((x+dx, y+dy))
                    queue.append(((x+dx, y+dy), time+1))
                    count = max(count, time+1)

        if fresh_fruits: return -1
        return count
