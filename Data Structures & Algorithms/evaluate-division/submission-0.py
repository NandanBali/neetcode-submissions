class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        
        for idx, eq in enumerate(equations):
            a, b = eq[0], eq[1]
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            adj[a].append((b, values[idx]))
            adj[b].append((a, 1/values[idx]))

        def query(a, b):
            queue = deque()
            traversed = set()
            if a not in adj:
                return -1
            queue.append((a, 1))
            while queue:
                node, acc = queue.popleft()
                if node == b:
                    return acc
                traversed.add(node)
                if node not in adj:
                    continue
                for child, multiplier in adj[node]:
                    if child not in traversed:
                        queue.append((child, acc * multiplier))
            return -1

        res = []
        for a, b in queries:
            res.append(query(a, b))
        return res