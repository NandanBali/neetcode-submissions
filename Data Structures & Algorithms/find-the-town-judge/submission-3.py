class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjmatrix = [[0] * n for _ in range(n)]
        for truster, trustee in trust:
            adjmatrix[trustee-1][truster-1] = 1
        for i in range(0, n):
            ita = True
            for j in range(0, n):
                if adjmatrix[i][j] == 0 and i != j:
                    ita = False
                    break
            if ita:
                tn = True
                for j in range(0, n):
                    if adjmatrix[j][i] == 1 and i != j:
                        tn = False
                        break
                if tn:
                    return i+1

        return -1