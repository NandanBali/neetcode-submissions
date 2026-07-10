class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l1, l2 = 0, n - 1
        if len(height) < 2:
            return 0

        while l1 < n:
            if height[l1] > height[l1+1]:
                break
            l1 += 1
        
        while l2 > 0:
            if height[l2] > height[l2-1]:
                break
            l2 -= 1
        
        area = 0
        depths = []
        p1 = l1
        p2 = p1 + 1
        while p1 < l2:
            if p2 == l2:
                for d in depths:
                    area += max(min(height[p1], height[p2]) - d, 0)
                break
            
            if height[p2] >= height[p1]:
                for d in depths:
                    area += max(height[p1] - d,0)
                depths.clear()
                p1 = p2
                p2 = p1 + 1
            else:
                depths.append(height[p2])
                p2 += 1
        return area


                