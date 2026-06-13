class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = []
        for i in range(0, len(tasks)):
            t.append((tasks[i][0], tasks[i][1], i))
        
        order_of_processing = []
        heapq.heapify(t)
        while len(t) > 0:
            res = heapq.heappop(t)
            order_of_processing.append(res[2])

            t = [(max(0, a-(res[0]+res[1])), b, c) for (a, b, c) in t]
            heapq.heapify(t)
        return order_of_processing
        
        
