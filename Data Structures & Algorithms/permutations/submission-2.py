class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def _helper(acc, index):
            if index == len(acc):
                self.result.append(list(acc))
                return
            for i in range(index, len(acc)):
                acc[i], acc[index] = acc[index], acc[i]
                _helper(acc, index+1)
                acc[i], acc[index] = acc[index], acc[i]
        
        _helper(nums, 0)
        return self.result