class MyQueue:

    def __init__(self):
        self.sa = []

    def push(self, x: int) -> None:
        self.sa.append(x)

    def pop(self) -> int:
        lst = []
        while self.sa:
            lst.append(self.sa.pop())
        v = lst.pop()
        while lst:
            self.sa.append(lst.pop())
        return v

    def peek(self) -> int:
        lst = []
        while self.sa:
            lst.append(self.sa.pop())
        v = lst[-1]
        while lst:
            self.sa.append(lst.pop())
        return v

    def empty(self) -> bool:
        return len(self.sa) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()