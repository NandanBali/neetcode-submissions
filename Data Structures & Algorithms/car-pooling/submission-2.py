class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap: List[tuple[int, int, int]] = [(a[1], a[2], a[0]) for a in trips]
        heapq.heapify(heap)
        traveling_queue: deque[tuple[int, int, int]] = deque()
        current_location = 0
        current_passengers = 0
        print(heap) 
        while heap:
            print(f"{current_passengers} {current_location}")
            while traveling_queue and traveling_queue[0][1] <= current_location:
                current_passengers -= traveling_queue.popleft()[2]

            print(f"{current_passengers} {current_location}")
            while heap and heap[0][0] <= current_location:
                res = heapq.heappop(heap)
                current_passengers += res[2]
                if current_passengers > capacity:
                    return False
                traveling_queue.append(res)
            if heap:
                current_location = heap[0][0]
        return True
