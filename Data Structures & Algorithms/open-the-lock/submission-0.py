class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dset = set()
        for deadend in deadends:
            dset.add(deadend)

        queue = deque()
        traversed = set()
        queue.append((target, 0))
        traversed.add(target)
        while queue:
            string, distance = queue.popleft()
            if string == "0000":
                return distance
            for idx, c in enumerate(string):
                r = int(c)
                up = string[:idx] + str(r+1) + string[idx+1:]
                if r == 9:
                    up = string[:idx] + str(0) + string[idx+1:]
                down = string[:idx] + str(r-1) + string[idx+1:]
                if r == 0:
                    down = string[:idx] + str(9) + string[idx+1:]
                    
                if up not in traversed and up not in dset:
                    traversed.add(up)
                    queue.append((up, distance+1))
                if down not in traversed and down not in dset:
                    traversed.add(down)
                    queue.append((down, distance+1))
                
        return -1 