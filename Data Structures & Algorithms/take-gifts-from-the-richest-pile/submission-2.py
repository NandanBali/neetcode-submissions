class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(0, k):
            idx = gifts.index(max(gifts))
            gifts[idx] = floor(sqrt(gifts[idx]))
        
        s = 0
        for g in gifts:
            s += g

        return s 