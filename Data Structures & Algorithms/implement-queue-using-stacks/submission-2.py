class MyQueue:

    def __init__(self):
       self.st = deque()

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        self.st.reverse()
        r = self.st.pop()
        self.st.reverse()
        return r

    def peek(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()