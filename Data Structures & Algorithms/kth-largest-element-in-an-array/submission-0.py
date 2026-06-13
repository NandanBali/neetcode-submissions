class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = [-x for x in nums]
        heapq.heapify(n)
        i = 0
        while i < k-1:
            heapq.heappop(n)
            i += 1
        return -heapq.heappop(n)