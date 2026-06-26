class Solution:
    def tribonacci(self, n: int) -> int:
        self.c0, self.c1, self.c2 = 0, 1, 1
        if n == 0: return 0
        elif n < 3: return 1

        def f():
            t0, t1 = self.c0, self.c1
            self.c0 = self.c1
            self.c1 = self.c2 
            self.c2 = self.c2 + t1 + t0
        
        for i in range(3, n+1):
            f()
        return self.c2
