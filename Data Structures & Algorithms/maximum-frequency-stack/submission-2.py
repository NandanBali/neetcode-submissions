class FreqStack:

    def __init__(self):
        self.counts = {}
        self.freqstacks: dict[int, deque[int]] = {}        

    def push(self, val: int) -> None:
        count = self.counts.get(val, 0) + 1
        if count not in self.freqstacks:
            self.freqstacks[count] = deque()
        self.freqstacks[count].append(val)
        self.counts[val] = count

    def pop(self) -> int:
        max_freq = max(self.freqstacks)
        v = self.freqstacks[max_freq].pop()
        if len(self.freqstacks[max_freq]) == 0:
            del self.freqstacks[max_freq]
        self.counts[v] -= 1
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()