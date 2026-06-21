class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_lst = [0] * n
        for truster, trustee in trust:
            trust_lst[truster-1] = -1
            if trust_lst[trustee-1] != -1:
                trust_lst[trustee-1] += 1
        
        for idx, t in enumerate(trust_lst):
            if t == n - 1:
                return  idx + 1
        return -1