class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tr = set()
        for num in nums:
            if num in tr:
                return True
            tr.add(num)
        return False