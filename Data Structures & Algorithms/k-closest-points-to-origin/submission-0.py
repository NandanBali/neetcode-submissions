class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def _distance(a: List[int]) -> float:
            return math.sqrt(math.pow(a[0], 2) + math.pow(a[1], 2))
        self.pwd = [(_distance(x), x) for x in points]

        def _swap(a, b):
            t = self.pwd[a]
            self.pwd[a] = self.pwd[b]
            self.pwd[b] = t

        def _pop() -> list[int]:
            if len(self.pwd) == 2:
                return self.pwd.pop()[1]

            res = self.pwd[1]
            self.pwd[1] = self.pwd.pop()
            i = 1
            while 2*i < len(self.pwd):
                if 2 * i + 1 < len(self.pwd) and self.pwd[2*i+1][0] < self.pwd[2*i][0] and self.pwd[2*i+1][0] < self.pwd[i][0]:
                    _swap(2*i+1, i)
                    i = 2*i + 1
                elif self.pwd[2*i][0] < self.pwd[i][0]:
                    _swap(2*i, i)
                    i = 2*i
                else: break
            return res[1]
        
        def _heapify():
            self.pwd.append(self.pwd[0])
            self.pwd[0] = (0, [0, 0])
            index = len(self.pwd) // 2
            while index >= 1:
                i = index
                while 2 * i < len(self.pwd):
                    if 2 * i + 1 < len(self.pwd) and self.pwd[2*i+1][0] < self.pwd[2*i][0] and self.pwd[2*i+1][0] < self.pwd[i][0]:
                        _swap(2*i+1, i)
                        i = 2*i+1
                    elif self.pwd[2*i][0] < self.pwd[i][0]:
                        _swap(2*i, i)
                        i = 2*i
                    else: break
                index -= 1
        
        _heapify()
        print(self.pwd)
        lst = []
        for i in range(0, k):
            lst.append(_pop())
        return lst
