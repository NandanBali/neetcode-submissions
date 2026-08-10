class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                _, d = st.pop()
                res[d] = i - d
            st.append((t, i))

        return res 