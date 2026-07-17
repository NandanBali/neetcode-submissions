class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        def valid(limit):
            curr, subsets = 0,1 

            for index, num in enumerate(nums):
                if curr + num > limit:
                    curr = num
                    subsets += 1
                    if subsets > k:
                        return False
                else:
                    curr += num
            return True

        res = r
        while l < r:
            mid = (l + r) // 2
            if valid(mid):
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1
        return res