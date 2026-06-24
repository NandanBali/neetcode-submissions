class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(0, n))
        size = [1] * n

        def find(a):
            if parent[a] == a:
                return parent[a]
            parent[a] = find(parent[a])
            return parent[a]

        def union(a, b) -> bool:
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            if size[pb] > pa:
                pa, pb = pb, pa
            
            parent[pb] = pa
            size[pa] += size[pb]
            return True

        result = []
        for a, b in edges:
            if not union(a-1, b-1):
                result.append([a, b])

        return result[-1]

            