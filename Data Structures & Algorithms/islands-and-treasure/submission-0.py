class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find treasure 
        xl = len(grid[0])
        yl = len(grid)

        treasure_map = []
        traverse = set()
        for y in range(0, yl):
            for x in range(0, xl):
                if grid[y][x] == 0:
                    treasure_map.append((x, y))
        
        queue = deque()
        for treasure in treasure_map:
            queue.append((treasure, 0))
            traverse.add(treasure)
        
        while queue:
            (x, y), distance = queue.popleft()
            grid[y][x] = distance
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + dx < xl and 0 <= y + dy < yl and (x+dx, y+dy) not in traverse and  grid[y+dy][x+dx] > 0:
                    queue.append(((x+dx, y+dy), distance+1))
                    traverse.add((x+dx, y+dy))
