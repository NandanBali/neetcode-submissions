class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        result = []

        # load up window
        for r in range(0, k):
            while len(q) > 0:
                if nums[q[-1]] <= nums[r]:
                    q.pop()
                else:
                    break
            q.append(r)
        
        result.append(nums[q[0]])
        for r in range(0, n - k):
            while len(q) > 0:
                if nums[q[-1]] <= nums[r+k]: q.pop()
                else: break
            q.append(r+k)
            while q[0] < r + 1:
                q.popleft()
            result.append(nums[q[0]])
        return result
        
