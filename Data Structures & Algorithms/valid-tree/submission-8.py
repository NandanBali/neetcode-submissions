class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(0, n))
        size = [1 for _ in range(0, n)]
        self.comp = n
        def find(a):
            if parent[a] == a:
                return a
            res = find(parent[a])
            parent[a] = res
            return res

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            self.comp -= 1
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            size[pa] += size[pb]
            parent[pa] = pb
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return self.comp == 1