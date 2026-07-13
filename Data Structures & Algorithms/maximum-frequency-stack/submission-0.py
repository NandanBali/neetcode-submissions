class FreqStack:

    def __init__(self):
        self.heap = []
        self.freq = {}

    def push(self, val: int) -> None:
            fr = self.freq.get(val, 0) + 1
            self.freq[val] = fr
            heapq.heappush(self.heap, (-fr, -len(self.heap), val))

    def pop(self) -> int:
        r = heapq.heappop(self.heap)
        self.freq[r[2]] -= 1
        return r[2]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()