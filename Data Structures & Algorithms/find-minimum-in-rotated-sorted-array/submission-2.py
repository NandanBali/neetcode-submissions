class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find pivot first
        lo = 0
        hi = len(nums) - 1
        piv = -1
        while lo < hi:
            mid = math.floor(lo + 0.5 * (hi - lo))
            print(nums[mid])
            if nums[mid] < nums[hi]:
                hi = mid
            elif nums[mid] == nums[lo]:
                piv = mid + 1
                break
            else:
                lo = mid + 1
        if piv < 0:
            piv = lo
        print(nums[piv])
        return nums[piv]
        
