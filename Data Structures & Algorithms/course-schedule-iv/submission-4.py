class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj: dict[int, List[int]] = {}
        for prereq, course in prerequisites:
            if course not in adj:
                adj[course] = []
            adj[course].append(prereq)
        def bfs(course, prereq):
            queue = deque()
            if course not in adj:
                return False
            traverse = set()
            queue.append(course)
            while queue:
                c = queue.popleft()
                traverse.add(c)

                if c == prereq:
                    for pre in adj[course]:
                        traverse.add(pre)
                    adj[course] = list(traverse)
                    return True
                if c not in adj:
                    continue
                for p in adj[c]:
                    if p not in traverse:
                        queue.append(p)
            for pre in adj[course]:
                traverse.add(pre)
            adj[course] = list(traverse)
            return False
    
        res = []
        for a, b in queries:
            res.append(bfs(b, a))
        return res

                


