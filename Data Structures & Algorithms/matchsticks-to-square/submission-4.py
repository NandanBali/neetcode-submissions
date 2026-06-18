class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        num_sum = 0
        matchsticks.sort()
        matchsticks.reverse()
        for i in matchsticks: num_sum += i
        m = [x for x in enumerate(matchsticks)]
        if num_sum % 4 != 0: return False
        for i in matchsticks:
            if i > num_sum // 4:
                return False
        self.used = [False] * len(matchsticks)
        self.count = 0
        def backtrack(current: List[tuple[int, int]], remaining: List[tuple[int, int]], cs, rs):
            if self.count == 4:
                return
            if cs == num_sum // 4:
                self.count += 1
                for idx, n in current:
                    self.used[idx] = True
                return
            elif cs < num_sum // 4:
                for i, (idx, n) in enumerate(remaining):
                    if not self.used[idx]:
                        del remaining[i]
                        current.append((idx, n))
                        backtrack(current, remaining, cs+n, rs-n)
                        current.pop()
                        remaining.insert(i, (idx,n))
            else: return
        backtrack([], m, 0, num_sum)
        return self.count == 4