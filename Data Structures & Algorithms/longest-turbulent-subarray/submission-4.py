class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        best = 1
        for r in range(1, n):

            if r + 1 < n and ((arr[r-1] < arr[r] and arr[r] > arr[r+1]) or (arr[r-1] > arr[r] and arr[r] < arr[r+1])):
                best = max(r - l + 2, best)
            elif r == n - 1:
                if arr[r-1] != arr[r]:
                    best = max(r - l + 1, best)
            else:
                l = r
        return best
