class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for i in nums:
            if i == l:
                return i
            l = i
        