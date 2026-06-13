class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                heapq.heappushpop(h, num)
        
        return heapq.heappop(h)