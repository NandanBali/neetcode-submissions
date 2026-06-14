class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap:
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
    
    def findMedian(self) -> float:
        # rebalance
        while abs(len(self.maxHeap) - len(self.minHeap)) >= 2:
            if len(self.maxHeap) > len(self.minHeap):
                x = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -x)
            else:
                x = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -x)

        print(f"{self.minHeap} and {self.maxHeap}")

        if self.maxHeap and self.minHeap:
            if len(self.maxHeap) == len(self.minHeap):
                return 0.5 * (-self.maxHeap[0]+self.minHeap[0])
            elif len(self.maxHeap) - len(self.minHeap) == 1:
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]
        elif self.maxHeap and not self.minHeap:
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        