class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        nums.reverse()
        sumnum = 0
        for i in nums:
            sumnum += i
        
        for i in nums:
            if i > sumnum // k:
                return False
        if sumnum % k != 0:
            return False

        def backtrack(current: List[int], remaining: List[int], processed: List[List[int]], cs: int, rs: int) -> bool:
            if len(processed) > k:
                return False
            
            if cs ==  sumnum // k:
                lst = []
                for n in current:
                    lst.append(n)
                processed.append(list(lst))
                if len(remaining) == 0:
                    return True
                if rs < sumnum // k:
                    return False
                return backtrack([], remaining, processed, 0, rs)
            elif cs < sumnum // k:
                for i, n in enumerate(remaining):
                        remaining.remove(n)
                        current.append(n)
                        res = backtrack(current, remaining, processed, cs+n, rs-n)
                        if res:
                            return True
                        current.pop()
                        remaining.insert(i,  n)
                return False
            else: return False

        return backtrack([], nums, [], 0, sumnum)