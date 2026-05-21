class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = [0] * 1000
        n = 0
        for op in operations:
            match op:
                case "+":
                    s[n] = s[n-1] + s[n-2]
                    n += 1
                case "D":
                    s[n] = 2 * s[n-1]
                    n += 1
                case "C":
                    n -= 1
                case _:
                    s[n] = int(op)
                    n += 1
        f_s = 0
        for i in range(0, n):
            f_s += s[i]
        return f_s