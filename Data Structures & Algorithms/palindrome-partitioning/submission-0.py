class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result: List[List[str]] = []
        def _is_palindrome(a: str):
            i = 0
            t = len(a) - 1
            while i < t:
                if a[i] != a[t]: return False
                i += 1
                t -= 1
            return True

        def backtrack(acc: List[str], index: int):
            print(acc)
            if index == len(s):
                for t in acc:
                    if not _is_palindrome(t):
                        return
                self.result.append(list(acc))
                return
            # include in the last sec
            acc[-1] += s[index]
            backtrack(acc, index+1)
            acc[-1] = acc[-1][:-1] 
            
            if _is_palindrome(acc[-1]):
                acc.append(s[index])
                backtrack(acc, index+1)
                acc.pop()
        backtrack([str(s[0])], 1)
        return self.result