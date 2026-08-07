class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = []
        for start, end in intervals:
            if len(res) == 0:
                res.append([start, end])
                continue
            
            if res[-1][1] >= start:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
            else:
                res.append([start, end])
        
        return res