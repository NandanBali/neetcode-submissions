class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        # rebalance
        if len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) - len(self.left) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return 0.5 * (-self.left[0] + self.right[0])
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        