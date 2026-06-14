class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = [x for x in heap if x[0] != 0]
        res = ""
        heapq.heapify(heap)
        while heap:
            fcn, fcr = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == fcr:
                if not heap:
                    break
                scnt, scr = heapq.heappop(heap)
                cta = 1
                res += scr * cta
                scnt += cta
                if scnt < 0:
                    heapq.heappush(heap, (scnt, scr))
            else:
                cta = 1
                if (-fcn > 1 and len(res) == 0) or (len(res) > 0 and res[-1] != fcr and -fcn > 1):
                    cta = 2
                res += fcr * cta
                fcn += cta
            if fcn < 0:
                heapq.heappush(heap, (fcn, fcr))
        return res