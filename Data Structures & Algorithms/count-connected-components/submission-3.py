class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(0, n))
        sizes = [1] * n
        self.components = n
        def find(a):
            if parent[a] == a:
                return a
            res = find(parent[a])
            parent[a] = res
            return res
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if sizes[pb] > sizes[pb]:
                pb, pa = pa, pb
            parent[pa] = pb
            sizes[pa] += pb
            self.components -= 1
        
        for a, b in edges:
            union(a, b)
        
        return self.components