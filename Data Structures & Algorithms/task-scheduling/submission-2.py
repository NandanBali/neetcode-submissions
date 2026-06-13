class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        with_freq = [(-freq, task) for (task, freq) in Counter(tasks).items()]
        heapq.heapify(with_freq)
        cooldown_queue: deque[tuple[int, int, str]] = deque()

        cycles  = 0
        while len(with_freq) > 0 or len(cooldown_queue) > 0:
            cycles += 1

            for _ in range(0, len(cooldown_queue)):
                res = cooldown_queue.popleft()
                res = (res[0]-1, res[1], res[2])
                if res[0] == 0 and res[1] > 0:
                    heapq.heappush(with_freq, (-res[1], res[2]))
                elif res[0] > 0:
                    cooldown_queue.append(res)
 
            if len(with_freq) != 0:
                freq, task = heapq.heappop(with_freq)
                remaining_freq = -freq - 1
                
                if remaining_freq > 0:
                    cooldown_queue.append((n + 1, remaining_freq, task))
                
        return cycles
