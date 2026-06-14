class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # o(n)
        profit_with_capital = []
        for i in range(0, len(profits)):
            profit_with_capital.append((capital[i], -profits[i]))

        heapq.heapify(profit_with_capital)
        task_count = 0
        initial_capital = w
        process_heap = []
        while task_count < k:
            while profit_with_capital and  profit_with_capital[0][0] <= initial_capital:
                _, profit = heapq.heappop(profit_with_capital)
                heapq.heappush(process_heap, profit)
            
            if not process_heap:
                break
            
            profit = -heapq.heappop(process_heap)
            initial_capital += profit
            task_count += 1
        return initial_capital