class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, c in enumerate(order):
            order_map[c] = index
        for i in range(0, len(words)-1):
            for idx in range(0, max(len(words[i]), len(words[i+1]))):
                if idx >= len(words[i+1]):
                    return False
                if idx >= len(words[i]):
                    break
                if order_map[words[i][idx]] > order_map[words[i+1][idx]]:
                    return False
                elif order_map[words[i][idx]] < order_map[words[i+1][idx]]:
                    break
                else:
                    continue
        return True
