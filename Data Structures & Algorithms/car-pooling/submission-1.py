class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = [(b, c, a) for (a, b , c) in trips]
        heapq.heapify(trips)
        prefix_sums = [0]
        while trips:
            start, end, people = heapq.heappop(trips)
            for i in range(start, end):
                while len(prefix_sums) - 1 < i:
                    prefix_sums.append(0)
                prefix_sums[i] += people
                if prefix_sums[i] > capacity: return False
        return True

