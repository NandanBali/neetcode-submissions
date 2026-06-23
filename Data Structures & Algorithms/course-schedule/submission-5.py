class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        sizes = [0 for _ in range(0, numCourses)]
        for course, prereq in prerequisites:
            if prereq not in adj:
                adj[prereq] = []
            adj[prereq].append(course)
            sizes[course] += 1
        
        queue = deque()
        traverse = set()
        
        for index, course in enumerate(sizes):
            if course == 0:
                queue.append(index)
        
        while queue and len(traverse) < numCourses:
            prereq = queue.popleft()
            traverse.add(prereq)
            if prereq not in adj:
                continue
            for course in adj[prereq]:
                if course not in traverse:
                    sizes[course] -= 1
                    if sizes[course] == 0:
                        queue.append(course)

        return len(traverse) == numCourses