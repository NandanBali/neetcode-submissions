class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l, r = 0, 0
        n = len(heights)
        max_area = 0
        min_index = 0

        while r < n:
            if heights[r] <= heights[min_index]:
                min_index = r
            max_area = max(heights[min_index] * (r -  l + 1), max_area)
            if min_index < r:
                mtr = min_index + 1
                for i in range(mtr, r+1):
                    if heights[mtr] > heights[i]:
                        mtr = i
                if heights[min_index] * (r - l + 1) < (r - min_index) * heights[mtr]:
                    l = min_index + 1
                    min_index = mtr
                else:
                    r += 1
            else:
                r += 1
        return max_area