class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_lst = [(task[0], task[1], index) for index, task in enumerate(tasks)]
        tasks_lst.sort()
        task_queue = deque()
        for task in tasks_lst:
            task_queue.append((task[0], task[1], task[2]))
        exec_heap = []
        clock = 0
        execution_order = []
        print(task_queue)
        while len(exec_heap) > 0 or len(task_queue) > 0:
            while len(task_queue) > 0 and task_queue[0][0] <= clock:
                task = task_queue.popleft()
                print(f"{clock} {task}")
                heapq.heappush(exec_heap, (task[1], task[2]))

            if len(exec_heap) > 0:
                task = heapq.heappop(exec_heap)
                execution_order.append(task[1])
                clock += task[0]
            else:
                clock = task_queue[0][0] 

        return execution_order