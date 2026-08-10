class MinStack:

    def __init__(self):
        self.st = []
        self.mst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.mst) == 0 or self.mst[-1][0] > val:
            self.mst.append((val, len(self.st)))

    def pop(self) -> None:
        self.st.pop()
        while len(self.mst) > 0 and self.mst[-1][1] > len(self.st):
            self.mst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1][0]