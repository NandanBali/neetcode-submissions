class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [([], 0)]
        n = len(s)
        wd = set(wordDict)
        for right in range(1, n+1):
            new_dp = []
            for acc, left in dp:
                if s[left: right] in wd:
                    new_dp.append((acc + [s[left:right]], right))
            dp += new_dp
        res = []
        for lst, index in dp:
            if index != n:
                continue
            sentence = ""
            for word in lst:
                sentence += word + " "
            sentence = sentence[:-1]
            res.append(sentence)
        return res