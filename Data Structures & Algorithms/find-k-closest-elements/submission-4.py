import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        idx = bisect.bisect_left(arr, x)
        if idx == n:
            return arr[n - k:]
        arr.insert(idx, x)
        res = []
        l, r = idx - 1, idx + 1
        while len(res) < k:
            if r == len(arr):
                t = k - len(res)
                res += arr[l - t + 1 : l + 1]
                print(f"here 1 {res}")
            elif l < 0:
                t = k - len(res)
                res += arr[r + 1 : r + t]
                print(f"here 2 {res}")

            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1 
        res.sort()
        return res