class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars: List[List[str]] = []
        for c in list(digits):
            r = []
            t = 0
            if int(c) < 8:
                t = 97 + 3 * (int(c)-2)
            else:
                t = 98 + 3 * (int(c)-2)
            for n in range(t, t+3):
                r.append(chr(n))
            if int(c) == 9 or int(c) == 7: r.append(chr(t+3))
            chars.append(r)

        self.result = []
        def backtrack(acc, index):
            if len(acc) == len(digits):
                self.result.append(acc)
                return
            
            for i in chars[index]:
                acc += i
                backtrack(acc, index+1)
                acc = acc[:-1]
        
        backtrack("", 0)
        return [a for a in self.result if a != ""]
        