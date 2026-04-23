class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        hi = sum(weights)
        lo = max(weights)

        while lo < hi:
            mid = math.floor(lo + (hi - lo) / 2)
            if self.canShip(weights, days, mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
    
    def canShip(self, weights: List[int], target: int, max_cap: int) -> bool:
        t = 1          # start with 1 day
        wc = 0
        for w in weights:
            if wc + w > max_cap:
                t += 1  # need a new day
                wc = 0
            wc += w
        return t <= target
