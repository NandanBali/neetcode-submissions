class Solution:
    def reorganizeString(self, s: str) -> str:
        data: List[tuple[int, str]] = [(-freq, char) for (char, freq) in Counter(s).items()]
        heapq.heapify(data)
        c = deque()
        result: str = ""
        while len(data) > 0:
            f, char = heapq.heappop(data)
            result += char
            while len(c) > 0:
                res = c.popleft()
                if -res[0] > 0:
                    heapq.heappush(data, res)
            c.append((f+1, char))

        if len(c) > 1 or (len(c) == 1 and c[0][0] != 0):
            return ""
        else: return result