class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        max_area = 0
        heights.append(0)

        for index, height in enumerate(heights):
            it = index
            while stack and stack[-1][1] > height:
                i, ht = stack.pop()
                max_area = max(max_area, (index - i) * ht)
                it = i
            stack.append((it, height))
        
        return max_area