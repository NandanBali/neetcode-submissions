class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [nums]

        a = nums[0]
        result = []
        for p in self.permute(nums[1:]):
            for i in range(0, len(p)+1):
                p.insert(i, a)
                result.append(list(p))
                del p[i]
        return result