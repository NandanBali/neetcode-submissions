class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        sizes = [0 for _ in range(0, numCourses)]
        for course, prereq in prerequisites:
            if prereq not in adj:
                adj[prereq] = []
            adj[prereq].append(course)
            sizes[course] += 1
        
        queue = deque()
        for idx, course in enumerate(sizes):
            if course == 0:
                queue.append(idx)

        courses_done = []
        while queue and len(courses_done) < numCourses:
            prereq = queue.popleft()
            courses_done.append(prereq)
            if prereq not in adj:
                continue
            for course in adj[prereq]:
                if course not in courses_done:
                    sizes[course] -= 1
                    if sizes[course] == 0:
                        queue.append(course)
        if len(courses_done) == numCourses:
            return courses_done 
        else:
            return []