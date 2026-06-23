class Solution:
    def solve(self, board: List[List[str]]) -> None:
        xl = len(board[0])
        yl = len(board)
        
        parent = {}
        ranks = {}
        for x in range(0, xl):
            for y in range(0, yl):
                parent[(x,y)] = (x,y)
                if x == 0 or x == xl -1 or y == 0 or y == yl - 1:
                    ranks[(x,y)] = 2
                else:
                    ranks[(x,y)] = 1
        
        def find(a: tuple[int, int]):
            if parent[a] == a:
                return a
            return  find(parent[a])
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            if ranks[pb] > ranks[pa]:
                parent[pa] = pb
            else:
                parent[pb] = pa

        traversed = set()
        for x in range(0, xl):
            for y in range(0, yl):
                if board[y][x] == 'O':
                    for dx, dy in [(0,1), (1, 0)]:
                        if 0 <= x + dx < xl and 0 <= y + dy < yl and board[y+dy][x+dx] == 'O':
                            union((x, y), (x+dx, y+dy))
        
        for x in range(0, xl):
            for y in range(0, yl):
                if board[y][x] == 'O':
                    if ranks[find((x,y))] == 1:
                        board[y][x] = 'X'

