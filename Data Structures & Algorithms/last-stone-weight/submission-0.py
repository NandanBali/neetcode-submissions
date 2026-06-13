class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        print(heap)
        if not heap:
            return 0
        while len(heap) > 1:
            x1 = -heapq.heappop(heap)
            x2 = -heapq.heappop(heap)
            if not x1 == x2:
                heapq.heappush(heap, -abs(x1-x2))
        if len(heap) == 1:
            return -heap[0]
        else: return 0 
